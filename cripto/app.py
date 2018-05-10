import rsa
from appJar import gui


def exit_f(button):
    app.stop()


def encrypt(button):
    plain = app.getEntry("Plaintext")
    public_key = app.getEntry("Key")
    app.setEntry("Result", rsa.encrypt(plain, public_key.split()))
    print(rsa.encrypt(plain, public_key))


def decrypt(button):
    plain = app.getEntry("Plaintext")
    private_key = app.getEntry("Key")
    app.setEntry("Result", rsa.decrypt(plain, private_key.split()))
    print(rsa.decrypt(plain, private_key))


def generate_keys(button):
    public_key, private_key = rsa.generate_keys()
    app.setEntry("Public Key", public_key)
    app.setEntry("Private Key", private_key)


app = gui("Login Window", "500x300")
app.setFont(18)

app.addLabelEntry("Plaintext")
app.addLabelEntry("Key")
app.addLabelEntry("Private Key")
app.addLabelEntry("Public Key")
app.addLabelEntry("Result")

app.addButton("Encrypt", encrypt)
app.addButton("Decrypt", decrypt)
app.addButton("Generate keys", generate_keys)
app.addButton("Exit", exit_f)

app.setFocus("Plaintext")

app.go()
