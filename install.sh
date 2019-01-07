#!/bin/bash

RED='\033[0;31m'
NC='\033[0m' # No Color

mkdir /tmp/qtracker-extension
cd /tmp/qtracker-extension
echo "Installing gnome tweak tool"
sudo apt install gnome-tweak-tool
echo "Creating extensions directory if not exists"
mkdir -p ~/.local/share/gnome-shell/extensions/  #create extension directory if doesnt exists.
git clone https://github.com/Shihadt/qtracker-extension.git

echo "Enter authentication from http://qtracker.qburst.com/home/userattendancetracker/attendance"
read auth

sed -e "s/AUTH_KEY = ''/AUTH_KEY = '${auth}'/g" qtracker-extension/argos/qtracker.100s.py > qtracker-extension/argos/qtracker.100s.py_tmp
rm qtracker-extension/argos/qtracker.100s.py
mv qtracker-extension/argos/qtracker.100s.py_tmp qtracker-extension/argos/qtracker.100s.py

echo "Moving config files and removing downloaded files"

mv qtracker-extension/argos ~/.config/
mv qtracker-extension/qtracker@qburst.com/ ~/.local/share/gnome-shell/extensions/
rm -rf ../qtracker-extension

echo "Restart gnome."
echo "${RED} Press alt+f2 and run command 'r'  ${NC} "

# enable qtracker extension in gnome tweak tool

echo "${RED}\nAlso, Please Enable extensions and qtracker extension in tweaks->extensions.\n${NC}"
