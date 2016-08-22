# -*- coding:utf-8 -*-

import os
import shutil

'''
 ____   _       _
 |  _ \| | __ _| |_ ___
 | |_) | |/ _` | __/ _ \
 |  __/| | (_| | ||  __/
 |_|   |_|\__,_|\__\___|

'''


def copy_dir(src, dst):
    for item in os.listdir(src):
        if item in ['tests', '.idea', 'doc', 'quick-start.py', '.git', 'requirements.txt']:
            continue
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

print("\nWelcome Plate v0.2.5")

print("Start your API Document system.")

project_name = None

try:
    project_name = str(raw_input('\nTyping API document name :'))
except NameError:
    project_name = str(input('\nTyping API document name :'))

# rename project
print("what is API document name? is" + "\"" + project_name + "\"" + ".")
project_path = "../" + project_name

print("Rename Plate to  " + "\"" + project_name + "\"" + "...")
current_dir = os.path.abspath("./")
dest_dir = os.path.join(os.path.dirname(current_dir), project_name)
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

copy_dir(src=current_dir, dst=dest_dir)


# setup requirements.txt
print("Install requirements.txt")
os.system('sudo pip install -r ./requirements.txt')

from builtins import input
is_delete_plate = str(input('Delete plate directory? (Y|N):'))
if is_delete_plate.upper() == 'Y':
    shutil.rmtree(current_dir)

print("Complete. Enjoy Developing.")
