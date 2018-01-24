import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.encryptBtn = tk.Button(self)
        self.encryptBtn["text"] = "Encrypt"
        self.encryptBtn["command"] = self.say_hi
        self.encryptBtn['width'] = 30
        self.encryptBtn.pack(side="left")

        self.decryptBtn = tk.Button(self)
        self.decryptBtn["text"] = "Decrypt"
        self.decryptBtn["command"] = self.say_hi
        self.decryptBtn['width'] = 30
        self.decryptBtn.pack(side="left")

        self.plaintext = tk.Text(self)
        self.plaintext['width'] = 30
        self.plaintext['height'] = 7
        self.plaintext.pack(side='top')

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()

# def check_space(a):
#     if a == ' ':
#         return 0
#     return ord(a) - 64
#
# alph = defaultdict(int)
# alph[0] = ' '
# for i in range(65, 91):
#     alph[i - 64] = chr(i)
#
# # print(a)
# text = 'com'
# # text = 'FXBXZKDBYWSSO'
# text = str.upper(text)
# kword = 'CIPHER'
# ltx = len(text)
# lkw = len(kword)
#
#
# kwadapt = kword * (int(ltx/lkw)) + kword[:int(ltx%lkw)]
#
# asd = ''.join([ alph[(check_space(text[i]) + check_space(kwadapt[i])) % 27] for i in range(len(kwadapt))])
#
# cripted = ''
# for i in range(len(kwadapt)):
#     cripted += alph[(check_space(text[i]) + check_space(kwadapt[i])) % 27]
#
#
# decrypted = ''.join([ alph[(check_space(cripted[i]) - check_space(kwadapt[i])) % 27] for i in range(len(kwadapt))])
# import ipdb; ipdb.set_trace()
# for i in range(len(kwadapt)):
#     if check_space(cripted[i]):
#         decrypted += chr(alph[kwadapt[i]])
#     else:
#         decrypted += chr((check_space(cripted[i]) - alph[kwadapt[i]]) % 27 + 64)
#
#
# # cripted = ''.join([ chr((check_space(text[i]) + alph[kwadapt[i]] ) % 27 + 64) for i in range(len(kwadapt))])
# # decrypted = ''.join([ chr((check_space(cripted[i]) - alph[kwadapt[i]] ) % 27 + 64) for i in range(len(kwadapt))])
# # chr((ord(text[0]) + alph[kwadapt[0]] - 64) % 27 + 64)
# import ipdb; ipdb.set_trace()
#
# print()

