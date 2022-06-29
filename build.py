import os

print("Installing Pyinstaller(Windows Compiler)") # Installs the compiler

os.system('python -m pip install pyinstaller')
print("Install Complete. Building!")
os.system('python -m pyinstaller --onefile main.py') # Creates Executable!
print("Install complete! Now go to dist and feel free to give copies to anyone else.")
print("As long as it complies with the MIT License")
# Script done!