
from pprint import pprint

var = "/root/folder/"

target_folder = "/root/folder/"


CONFIG_FILES = {

  "pe1":target_folder + "pe1.conf",
  "pe2":target_folder + "pe2.conf",
  "pe3":target_folder + "pe3.conf",
  "pe4":target_folder + "pe4.conf",
  "p1":target_folder + "p1.conf",
  "p2rr":target_folder + "p2rr.conf",
  "p3":target_folder + "p3.conf",

}


config_file = CONFIG_FILES["pe1"]


with open("device.txt", "r") as f:
    devices = f.readlines()
    devices = [x.strip() for x in devices]

    for device in devices:
        dev = Device(host=device).open()
        with Config(dev) as cu:
            cu.load(path=CONFIG_FILES[device], )




print(devices)








#pprint(CONFIG_FILES)