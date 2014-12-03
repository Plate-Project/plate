# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''


import os 
import shutil

print "\nWelcome slate-flask v0.1. Let's start your API Document system."

project_name = str(raw_input('\nTyping API document name :'))
print "what is API document name? is \"" + project_name +"\"."
project_path = "../" + project_name


print "\nRename slate-flask to \""+ project_name +"\" ..."
current_dir = os.path.abspath("./")
shutil.move(current_dir, os.path.join(os.path.dirname(current_dir), project_name))

print "Complete. Enjoy developing."

