import useful_tools   # imports functions written in outher python files


print(useful_tools.get_file_txt("test.txt"))

print(useful_tools.roll_dice(1))

# in this example the module file was in the same directory as the python program
#  two types of modules exist built in and external,
#  external modules are stored in the same folder that the python is installed

# external modules is stored in the lib/ folder with a name module_name.py when present there pycharm ide will be able to autocomplete functions


# pip unstall is used to install external modules
# pip uninstall is used to remove a module

# modules not handeled by pip should have installation instructions


# CAUTION of manually installing stuff that other people wrote