import random
import string
import pyperclip
x = int(input('how long password you need? '))

def passGenerator(n):
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for i in range(n))


z = passGenerator(x)
pyperclip.copy(z)
print("Your password " + z)