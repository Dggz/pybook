import multiprocessing
from collections import deque
from contextlib import suppress
from math import sqrt

import numpy as np


# noinspection PyShadowingNames
class Block:

    def __init__(self, values, x_pos, y_pos, block_type):
        self.values = values
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.block_type = block_type

    def compress(self):
        new_vals = []
        for i in range(0, 8, 2):
            for j in range(0, 8, 2):
                new_vals.append(sum(
                    self.values[i][j:j + 2] + self.values[i + 1][j:j + 2]) // 4)
        self.values = np.array(new_vals)

    def decompress(self):
        new_vals = np.zeros((8, 8))
        for i in range(0, 8, 2):
            vals = self.values[2 * i:2 * i + 4]
            for j, val in zip(range(0, 8, 2), vals):
                new_vals[i][j:j+2], new_vals[i+1][j:j+2] = val, val
        self.values = np.array(new_vals)

    def fdct(self):
        pi = 3.141592653589793238463
        new_vals = np.zeros((8, 8))
        self.values -= 128
        for u in range(8):
            for v in range(8):
                summ = sum([self.values[x][y]
                    * np.cos(((2 * x + 1) * u * pi) / 16)
                    * np.cos(((2 * y + 1) * v * pi) / 16)
                    for y in range(8) for x in range(8)])
                alpha_u = 1 / sqrt(2) if u == 0 else 1
                alpha_v = 1 / sqrt(2) if v == 0 else 1
                new_vals[u][v] = 1 / 4 * alpha_u * alpha_v * summ
        self.values = new_vals

    def idct(self):
        pi = 3.141592653589793238463
        new_vals = np.zeros((8, 8))
        for x in range(8):
            for y in range(8):
                summ = 0
                for u in range(8):
                    for v in range(8):
                        alpha_u = 1 / sqrt(2) if u == 0 else 1
                        alpha_v = 1 / sqrt(2) if v == 0 else 1
                        cos_u = np.cos(((2 * x + 1) * u * pi) / 16)
                        cos_v = np.cos(((2 * y + 1) * v * pi) / 16)
                        summ += alpha_u * alpha_v * self.values[u][v] * cos_u * cos_v
                new_vals[x][y] = 1 / 4 * summ
        self.values = new_vals + 128

    def quantize(self):
        q_matrix = np.array([
            [6, 4, 4, 6, 10, 16, 20, 24],
            [5, 5, 6, 8, 10, 23, 24, 22],
            [6, 5, 6, 10, 16, 23, 28, 22],
            [6, 7, 9, 12, 20, 35, 32, 25],
            [7, 9, 15, 22, 27, 44, 41, 31],
            [10, 14, 22, 26, 32, 42, 45, 37],
            [20, 26, 31, 35, 41, 48, 48, 40],
            [29, 37, 38, 39, 45, 40, 41, 40]])
        self.values = self.values // q_matrix

    def dequantize(self):
        q_matrix = np.array([
            [6, 4, 4, 6, 10, 16, 20, 24],
            [5, 5, 6, 8, 10, 23, 24, 22],
            [6, 5, 6, 10, 16, 23, 28, 22],
            [6, 7, 9, 12, 20, 35, 32, 25],
            [7, 9, 15, 22, 27, 44, 41, 31],
            [10, 14, 22, 26, 32, 42, 45, 37],
            [20, 26, 31, 35, 41, 48, 48, 40],
            [29, 37, 38, 39, 45, 40, 41, 40]])
        self.values = self.values * q_matrix

    @staticmethod
    def zigzag(n=8):
        indexorder = sorted(
            ((x, y) for x in range(n) for y in range(n)),
            key=lambda x: (
                x[0] + x[1], -x[1] if (x[0] + x[1]) % 2 else x[1])
        )
        return indexorder

    def entropy_encode(self):
        new_vals, zeros = [], 0
        try:
            for idx, val in enumerate(
                    [self.values[x][y] for x, y in self.zigzag()]):
                if val == 0 and idx != 0:
                    zeros += 1
                    continue
                if idx != 0:
                    new_vals.append(zeros)
                    zeros = 0
                if val in range(-1, 2):
                    new_vals.append(1)
                elif val in [*range(-3, -1), *range(2, 4)]:
                    new_vals.append(2)
                elif val in [*range(-7, -3), *range(4, 8)]:
                    new_vals.append(3)
                elif val in [*range(-15, -7), *range(8, 16)]:
                    new_vals.append(4)
                elif val in [*range(-31, -15), *range(16, 32)]:
                    new_vals.append(5)
                elif val in [*range(-63, -31), *range(32, 64)]:
                    new_vals.append(6)
                elif val in [*range(-127, -63), *range(64, 128)]:
                    new_vals.append(7)
                elif val in [*range(-255, -127), *range(128, 256)]:
                    new_vals.append(8)
                elif val in [*range(-511, -255), *range(256, 512)]:
                    new_vals.append(9)
                elif val in [*range(-1023, -511), *range(512, 1024)]:
                    new_vals.append(10)
                new_vals.append(val)
            new_vals.append(0)
            new_vals.append(0)
        except IndexError:
            import ipdb; ipdb.set_trace()
            print()
        return new_vals

    @staticmethod
    def entropy_decode(e_bytes):
        vals, idx = [], 0
        vals.append(e_bytes[1])
        idx += 2
        while True:
            if (e_bytes[idx], e_bytes[idx + 1]) == (0, 0):
                break
            vals += [0 for i in range(e_bytes[idx])]
            vals.append(e_bytes[idx + 2])
            idx += 3
        idx += 2
        vals += [0 for i in range(64 - len(vals))]
        new_block = np.zeros((8, 8))
        for pos, val in zip(Block.zigzag(), vals):
            new_block[pos[0]][pos[1]] = val
        return idx, new_block



# inp_photo = 'test.ppm'
inp_photo = 'nt-P3.ppm'
# out_photo = 'encoded-test.ppm'
# out_photo = 'encoded3.ppm'
out_photo = 'encoded.ppm'


def pre_process_blocks(pos, step=4):
    for idx in range(pos, pos + step):
        y_blocks[idx].fdct()
        y_blocks[idx].quantize()

        cb_blocks[idx].fdct()
        cb_blocks[idx].quantize()

        cr_blocks[idx].fdct()
        cr_blocks[idx].quantize()


def post_process_blocks(pos, step=4):
    for idx in range(pos, pos + step):
        y_blocks[idx].dequantize()
        y_blocks[idx].idct()

        cb_blocks[idx].dequantize()
        cb_blocks[idx].idct()

        cr_blocks[idx].dequantize()
        cr_blocks[idx].idct()


# noinspection PyPep8Naming,PyShadowingNames
def rgb2Y(r_val, g_val, b_val):
    return int(0.299 * r_val + 0.587 * g_val + 0.114 * b_val)


# noinspection PyPep8Naming,PyShadowingNames
def rgb2Cb(r_val, g_val, b_val):
    return int(128 - 0.169 * r_val - 0.331 * g_val + 0.5 * b_val)


# noinspection PyPep8Naming,PyShadowingNames
def rgb2Cr(r_val, g_val, b_val):
    return int(128 + 0.5 * r_val - 0.419 * g_val - 0.081 * b_val)


# noinspection PyUnusedLocal,PyPep8Naming,PyShadowingNames
def yuv2R(y_val, cb_val, cr_val):
    return int(y_val + 1.402 * (cr_val - 128))


# noinspection PyPep8Naming,PyShadowingNames
def yuv2G(y_val, cb_val, cr_val):
    return int(y_val - 0.343 * (cb_val - 128) - 0.711 * (cr_val - 128))


# noinspection PyUnusedLocal,PyPep8Naming,PyShadowingNames
def yuv2B(y_val, cb_val, cr_val):
    return int(y_val + 1.765 * (cb_val - 128))

from time import time

start = time()

with open(inp_photo, 'r') as photo:
    photo_format = photo.readline().strip()
    x_res, y_res = None, None
    while not x_res and not y_res:
        with suppress(ValueError):
            x_res, y_res = photo.readline().strip().split()

    x_res, y_res = int(x_res), int(y_res)
    max_val = int(photo.readline().strip())
    values = deque([int(line.strip()) for line in photo.readlines() if line.strip().isdecimal()])

y_vals = np.zeros((y_res, x_res))
cb_vals = np.zeros((y_res, x_res))
cr_vals = np.zeros((y_res, x_res))
x_val, y_val = 0, 0
while values:
    r_val, g_val, b_val = values.popleft(), values.popleft(), values.popleft()
    y_vals[y_val][x_val] = int(rgb2Y(r_val, g_val, b_val))
    cb_vals[y_val][x_val] = int(rgb2Cb(r_val, g_val, b_val))
    cr_vals[y_val][x_val] = int(rgb2Cr(r_val, g_val, b_val))
    x_val += 1
    if x_val == int(x_res):
        x_val = 0
        y_val += 1

y_blocks, cb_blocks, cr_blocks = [], [], []
for y_pos in range(0, y_res, 8):
    for x_pos in range(0, x_res, 8):
        y = Block(np.array([
            yvl[x_pos:x_pos + 8] for yvl in y_vals[y_pos:y_pos + 8]]),
            x_pos, y_pos, 'Y')
        y_blocks.append(y)
        cb = Block(np.array([
            cbvl[x_pos:x_pos + 8] for cbvl in cb_vals[y_pos:y_pos + 8]]),
            x_pos, y_pos, 'Cb')
        cb.compress()
        cb.decompress()
        cb_blocks.append(cb)
        cr = Block(np.array([
            crvl[x_pos:x_pos + 8] for crvl in cr_vals[y_pos:y_pos + 8]]),
            x_pos, y_pos, 'Cr')
        cr.compress()
        cr.decompress()
        cr_blocks.append(cr)

del y_vals, cb_vals, cr_vals

tasks = x_res * y_res // 64
def pre():
    print("blana stuff")
    for i in range(0, tasks, tasks // 4):
    # for i in range(0, tasks, 4):
        p = multiprocessing.Process(target=pre_process_blocks, args=(i, tasks // 4))
        # p = multiprocessing.Process(target=process_blocks, args=(i, 4))
        p.start()
        p.join()
        # pre_process_blocks(i, 4)
        if i % 500 == 0:
            print(i)

pre()
e_counter = 0
def entr():
    print('entropy encode')
    e_bytes, e_counter = [], 0
    for y_block, cb_block, cr_block in zip(y_blocks, cb_blocks, cr_blocks):
        e_bytes += y_block.entropy_encode()
        e_bytes += cb_block.entropy_encode()
        e_bytes += cr_block.entropy_encode()
        if e_counter % 1000 == 0:
            print(e_counter)
        e_counter += 1
    return e_bytes

entropy_bytes = entr()
new_y_blocks = []
new_cb_blocks = []
new_cr_blocks = []
idx, x_pos, y_pos = 0, 0, 0
print('entropy decode')
while True:

    if idx >= len(entropy_bytes):
        break
    elif entropy_bytes[idx] == 0:
        break
    jmp, y_values = Block.entropy_decode(entropy_bytes[idx:])
    new_y_blocks.append(Block(y_values, x_pos, y_pos, 'Y'))
    idx += jmp
    jmp, cb_values = Block.entropy_decode(entropy_bytes[idx:])
    new_cb_blocks.append(Block(cb_values, x_pos, y_pos, 'Cb'))
    idx += jmp
    jmp, cr_values = Block.entropy_decode(entropy_bytes[idx:])
    new_cr_blocks.append(Block(cr_values, x_pos, y_pos, 'Cr'))
    idx += jmp
    x_pos += 8
    if x_pos >= x_res - 1:
        print(x_pos)
        y_pos += 8
        x_pos = 0

y_blocks = new_y_blocks
cb_blocks = new_cb_blocks
cr_blocks = new_cr_blocks

print('entropy done')
print('blana again')
for i in range(0, tasks, tasks // 4):
# for i in range(0, tasks, 4):
    p = multiprocessing.Process(target=post_process_blocks, args=(i, tasks // 4))
    # p = multiprocessing.Process(target=process_blocks, args=(i, 4))
    p.start()
    p.join()
    # post_process_blocks(i, 4)
    # if i % 500 == 0:
    #     print(i)

print("gata blana stuff")
###

new_y_vals = np.zeros((y_res, x_res))
new_cr_vals = np.zeros((y_res, x_res))
new_cb_vals = np.zeros((y_res, x_res))
for y_block, cb_block, cr_block in zip(y_blocks, cb_blocks, cr_blocks):
    for i in range(8):
        new_y_vals[y_block.y_pos + i][y_block.x_pos:y_block.x_pos + 8] = y_block.values[i]
        new_cb_vals[cb_block.y_pos + i][cb_block.x_pos:cb_block.x_pos + 8] = cb_block.values[i]
        new_cr_vals[cr_block.y_pos + i][cr_block.x_pos:cr_block.x_pos + 8] = cr_block.values[i]

with open(out_photo, 'w') as encoded:
    encoded.write(photo_format + '\n')
    print('writing')
    encoded.write('# Encoded by Dggz\n')
    encoded.write(str(x_res) + ' ' + str(y_res) + '\n')
    encoded.write(str(max_val) + '\n')
    for i in range(y_res):
        for j in range(x_res):
            r_val = yuv2R(new_y_vals[i][j], new_cb_vals[i][j], new_cr_vals[i][j])
            g_val = yuv2G(new_y_vals[i][j], new_cb_vals[i][j], new_cr_vals[i][j])
            b_val = yuv2B(new_y_vals[i][j], new_cb_vals[i][j], new_cr_vals[i][j])
            if r_val > max_val:
                r_val = max_val
            if g_val > max_val:
                g_val = max_val
            if b_val > max_val:
                b_val = max_val

            encoded.write(str(r_val) + '\n')
            encoded.write(str(g_val) + '\n')
            encoded.write(str(b_val) + '\n')

end = time()
print(str(end - start))