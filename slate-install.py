# -*- coding:utf-8 -*-
'''
Created on 2014. 8. 20.
@author: seonghyunan
'''


import os 
import shutil
import json 
import pip


print "\nWelcome Slate-Flask. Let's start your API Document system."

project_name = str(raw_input('\nTyping project name :'))
print "Your project is \"" + project_name +"\"."
project_path = "../" + project_name


print "\nStart Copy Slate-Flask to "+ project_name +" ..."
# copy slate-flask => projectname 
if not os.path.isdir(project_path):
    shutil.copytree("../slate-flask", project_path)
else:
    print "Already exist " +  project_path
    os._exit(1)



print "\nRemove installer."
# remove projectname\slate-install.py
os.remove(os.path.join(project_path, "slate-install.py"))
shutil.rmtree(os.path.join(project_path, ".git"))
 
print "\nSet LOGO_TITLE and TITLE in config.json ..."
f = open(os.path.join(project_path, "config.json"), 'r')
config = json.loads(f.read())
config['LOGO_TITLE'] = project_name
config['TITLE'] = project_name
f.close()

f = open(os.path.join(project_path, "config.json"), 'w')
f.write(json.dumps(config))
f.close()



print "\n\nChecking Library ..."

need_library = ["tornado", "flask", "pygments", "markdown", "watchdog", "beautifulsoup4"]

installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])

for lib in need_library:
    is_exist = False
    for pkg in installed_packages_list:
        if lib in pkg:
            is_exist = True
            break

    if not is_exist:
        e = os.system('sudo pip install ' + lib)

        if not e == 0:
            print " ... "+lib + " not installed."

    else:
        print " ... "+lib + " is already installed."

print "Complete Library Checking "


print "\n\nEnd Go to " + os.path.abspath(project_path) + "\n"
