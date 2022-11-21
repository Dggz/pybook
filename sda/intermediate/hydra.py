regrowth = 3
heads = int(input("How many heads does the Hydra have? "))
to_cut = int(input("How many heads do you want to cut? "))
remaining = 0 if to_cut >= heads else heads - to_cut + to_cut * regrowth
if remaining:
    print(f"The Hydra now has {remaining} heads!")
    exit(0)

print(f"The Hydra is dead!")
exit(0)
