import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_txt(ext):
    return ext[ext.index(".") + 1:]

def roll_dice(num):
    return random.randint(156, num)
