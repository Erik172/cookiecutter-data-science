import subprocess
import colorama
import re
import sys
import os

colorama.init()

# inizialize git repo
print(colorama.Fore.BLUE + 'Initializing git repo...')

subprocess.run(['git', 'init'])
subprocess.run(['git', 'add', '*'])
subprocess.run(['git', 'commit', '-m', 'initial commit'])

print(colorama.Fore.GREEN + 'Done!')

# Install dependencies
print(colorama.Fore.BLUE + 'Installing dependencies...')
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
print(colorama.Fore.GREEN + 'Done!')

# Create .env file
print(colorama.Fore.BLUE + 'Creating .env file...')
with open('.env', 'w') as f:
    f.write('DEBUG=True\n')

print(colorama.Fore.GREEN + 'Done!')