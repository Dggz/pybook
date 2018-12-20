
# Old % way
print('\n%\n')

age = 74
name = "Eric"
print("Hello, %s. You are %s." % (name, age))

age = 74
first_name = "Eric"
last_name = "Idle"
profession = "comedian"
affiliation = "Monty Python"
print("Hello, %s %s. You are %s. You are a %s. You were a member of %s." % (
    first_name, last_name, age, profession, affiliation
))


# New-ish str.format()

print('\nstr.format()\n')

print("Hello, {}. You are {}.".format(name, age))

print("Hello, {1}. You are {0}.".format(age, name))

person = {'name': 'Eric', 'age': 74}
print("Hello, {name}. You are {age}.".format(name=person['name'], age=person['age']))

first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
print("Hello, {first_name} {last_name}. You are {age}. You are a {profession}."
      "You were a member of {affiliation}."
      .format(first_name=first_name, last_name=last_name, age=age,
              profession=profession, affiliation=affiliation))

# f-strings

print('\nf-strings\n')
age = 74
name = "Eric"
print(f"Hello, {name}. You are {age}.")

# Quote escape
print(f"The \"comedian\" is {name}, aged {age}.")

age = 74
first_name = "Eric"
last_name = "Idle"
profession = "comedian"
affiliation = "Monty Python"
print(f"Hello, {first_name} {last_name}. You are {age}. You are a {profession}."
      f" You were a member of {affiliation}.")

print(f"{name.lower()} is funny.")

print(f"{2 * 37}")


class Comedian:
    def __init__(self, com_fn, com_ln, com_age):
        self.first_name = com_fn
        self.last_name = com_ln
        self.age = com_age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"


new_comedian = Comedian("Eric", "Idle", "74")
print(f"{new_comedian}")
