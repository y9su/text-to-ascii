import pyfiglet
import time
import keyboard
import pyperclip


print("Find Fonts at http://www.figlet.org/examples.html\n")
time.sleep(1.5)

font = input("Font: ")
text = pyfiglet.figlet_format(input('Enter text: '), font=f"{font}")
print(text)

print("Copied to clipboard!")
pyperclip.copy(f"{text}")

time.sleep(5)
