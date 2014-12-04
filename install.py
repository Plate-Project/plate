# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''


import os
import shutil


def output(msg):
    print "\033[1;33m" + msg + "\033[1;m"

output("\nWelcome slate-flask v0.1. ")
output( "Let's start your API Document system.")

project_name = str(raw_input('\nTyping API document name :'))
print  "what is API document name? is \033[1;41m\"" + project_name +"\"\033[1;m."
project_path = "../" + project_name

output( "\nRename slate-flask to \033[1;41m\""+ project_name +"\"\033[1;m ..." )
current_dir = os.path.abspath("./")
shutil.move(current_dir, os.path.join(os.path.dirname(current_dir), project_name))

output( "Complete. Enjoy developing." )

