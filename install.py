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



def decorate_yellow(msg):
    if is_windows:
        return msg
    else:
        return "\033[1;33m" + msg + "\033[1;m"

def decorate_red(msg):
    if is_windows:
        return msg
    else:
        return "\033[1;41m" + msg + "\033[1;m"





print decorate_yellow("\nWelcome slate-flask v0.1.")
print decorate_yellow("Let's start your API Document system.")

project_name = str(raw_input('\nTyping API document name :'))
print  "what is API document name? is" + decorate_red("\"" + project_name + "\"") + "."


project_path = "../" + project_name

print "Rename slate-flask to  " + decorate_red("\"" + project_name + "\"") +"..."
current_dir = os.path.abspath("./")
#shutil.move(current_dir, os.path.join(os.path.dirname(current_dir), project_name))


from pip.req import parse_requirements
import pip
print "Install requirements.txt"

install_reqs = parse_requirements("./requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]
for req in reqs:
    pip.main(["install", req])



print decorate_yellow( "Complete. Enjoy developing.")

