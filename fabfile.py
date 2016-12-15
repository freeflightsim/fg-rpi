
import os, sys

from fabric.api import env, local, run, cd, sudo, warn_only, prompt


HERE_PATH =  os.path.abspath( os.path.dirname( __file__ )	 ) 


def _read_apt_file(file_name):
    """retruns a list of files in apt/*.txt"""
	with open(HERE_PATH + "/apt/%s" % file_name, "r") as f:
		contents = f.read()
	items = contents.split("\n")
	lst = []
	for i in items:
		ii = i.strip()
		if ii == "" or ii[0] == "#":
			continue 
		lst.append(ii)
	return lst



def remove_crap():
	"""Remove crap packages - listed in `apt/remove.txt` """
	
	lst =_read_apt_file("remove.txt")
	cmd = "sudo apt-get -y remove %s" % " ".join(lst)
	#print cmd
	local(cmd)
	
	# NO local("sudo apt-get -y --auto-remove purge raspberrypi-artwork")

def upgrade():
	"""Update to latest patches"""
	local("sudo apt-get update")
	local("sudo apt-get -y upgrade")
	local("sudo apt-get -y autoremove")
	local("sudo apt-get clean")
	
	
def install_essentials():
	"""Install essentials  - listed in `apt/install.txt` """
	
	lst =_read_apt_file("install.txt")
	cmd = "sudo apt-get -y install %s" % " ".join(lst)
	#print cmd
	local(cmd)
	
def conky():
  """Install `conky` and sys info on background"""
  local("sudo cp %s/conky/conky.conf /etc/conky/conky.conf" % HERE_PATH)
  local("cp %s/conky/conky.desktop ~/.config/autostart/conky.desktop" % HERE_PATH)
	
	
def all():
  """## Runs all steps in sequence and recommended"""
  remove_crap()
  upgrade()
  install_essentials()
  upgrade()
  local("sudo reboot")
  
  