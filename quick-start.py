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

print("\nWelcome Plate v0.2")
print("Start your API Document system.")

project_name = None
try:
    #  python2.x
    project_name = str(raw_input('\nTyping API document name :'))
except NameError:
    #  python3.x
    project_name = str(input('\nTyping API document name :'))

# rename project 
print("what is API document name? is" + "\"" + project_name + "\"" + ".")
project_path = "../" + project_name

print("Rename slate-flask to  " + "\"" + project_name + "\"" + "...")
current_dir = os.path.abspath("./")
dest_dir = os.path.join(os.path.dirname(current_dir), project_name)
shutil.move(current_dir, dest_dir)

# setup requirements.txt 
from pip.req import parse_requirements
import pip
print("Install requirements.txt")

install_reqs = parse_requirements("./requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]
for req in reqs:
    pip.main(["install", req])
    pip.logger.consumers = []

print("Complete. Enjoy Developing.")
