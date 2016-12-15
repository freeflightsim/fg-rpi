#!/bin/sh

echo "############################"
echo "fg-rpi - Initial Setup"
echo "############################"
echo ""
echo "=== Install python headers ==="
sudo apt-get install libpython-all-dev

echo ""
echo "=== Install Fabric ==="
sudo pip install -I fabric

echo ""
echo "Looks like install worked.. done.. now run `fab -l` "


