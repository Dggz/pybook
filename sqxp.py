
def sq_mod_pow(n, p, md):
    bin_repr = bin(p)[2:][::-1] # take the binary repr of p, reverses it for better iteration

