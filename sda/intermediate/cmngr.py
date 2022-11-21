from contextlib import contextmanager


@contextmanager
def file_manager(name, mode):
    f = open(name, mode)
    yield f
    print('closing')
    f.close()


if __name__ == "__main__":
    with file_manager("test.txt", 'w') as file:

        file.write("Test")
        print('asd')
        suma = 5 + 5
    file.read()
    print('file processing done')
