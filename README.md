fg-rpi
=====================

The journet of a  FlightGear pilot

- landing a huge FlightGear aircraft 
- with a CAT3 landing 
- and some CAT5 cable
- connected to a Raspberry Pie
- via wifi.. and... 
- landing .. 

FlightGear RaspberryPi 
=================================

This repos contains some scripts and utils to setup an RPI.
by getting rid of crap, installing essentials,
and minor configuration, for a first time install.

The First time install is condidered to be a Noobs image or raspian alike..

IMPORTANT Note: The "default" 
 - user =  `pi` 
 - password is `raspberry`


1: Install git and clone this repos
=======================================

Kick up a terminal and tap in

    sudo apt-get install git
    
2: clone the fg-rpi stuff
=============================

    git clone https://github.com/freeflightsim/fg-rpi.git


3: Run the bootstrap essentials
===========================================

Enter the fg-rpi dir and run the script "initial-setup.sh"
which install some python headers and fabric

    cd fg-rpi
    ./initial-setup.sh


4: Run `fab` commands
===============================

To complete tap in `fab all` which executes a series of commands
and could take a while. When complete it will reboot.

    fab all

For more "fab commands" exec `fab -l`

5: Bonus
==============================

SSH in from remote machine with

    ssh pi@<ip>
    > pass = raspberry

To set passwordless login

    ssh-copy-id pi@<ip>

then below should work with no pass

    ssh pi@<ip>

