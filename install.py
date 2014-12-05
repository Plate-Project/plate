# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''


import os
import shutil

import platform
is_windows = False
if str.lower(platform.uname()[0]) == "windows":
    is_windows = True


def yellow(msg):
    if is_windows:
        return msg
    else:
        return "\033[1;33m" + msg + "\033[1;m"


def red(msg):
    if is_windows:
        return msg
    else:
        return "\033[1;41m" + msg + "\033[1;m"

print yellow("\nWelcome slate-flask v0.1.")
print yellow("Let's start your API Document system.")

project_name = str(raw_input(yellow('\nTyping API document name :')))
print "what is API document name? is" + red("\"" + project_name + "\"") + "."

project_path = "../" + project_name

print "Rename slate-flask to  " + red("\"" + project_name + "\"") + "..."
current_dir = os.path.abspath("./")
dest_dir = os.path.join(os.path.dirname(current_dir), project_name)
shutil.move(current_dir, dest_dir)

from pip.req import parse_requirements
import pip
print yellow("Install requirements.txt")

install_reqs = parse_requirements("./requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]
for req in reqs:
    pip.main(["install", req])
    pip.logger.consumers = []


print yellow("Complete. Enjoy Developing.")
