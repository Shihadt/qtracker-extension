# Overview

Qtracker extension will show hours clocked, burned, break duration etc in top bar.

## Requirments
Qtracker extension only works on Gnome-3 (ubuntu 18). Also it needs gnome-tweak tool to activate.

## Installation

- Install gnome tweak tool
``` sudo apt install gnome-tweak-tool```
- clone the repo
```
git clone https://github.com/Shihadt/qtracker-extension.git
cd qtracker-extension
```

- Change ```AUTH=''``` in argos/qtracker.100s.py to your authentication header. Example ```AUTH = '0e891e9d2ed5aedgg3410b22ddad4368d6117f23dff0ee7d389cacedee2fcd591539229015200.950e0c0fee5b9b48e83f7a477c7de1e4e02815bf'``` which should be obtained from <http://qtracker.qburst.com/home/userattendancetracker/attendance>
	```
	auth = your qtracker authentication
	sed -e "s/AUTH_KEY = ''/AUTH_KEY = '${auth}'/g" argos/qtracker.100s.py > qtracker.100s.py_tmp
	mv qtracker.100s.py_tmp argos/qtracker.100s.py
	rm qtracker.100s.py_tmp
	```
	- For getting authentication header in chrome <https://www.mkyong.com/computer-tips/how-to-view-http-headers-in-google-chrome/>
	- For getting authentication header in Firefox <https://o7planning.org/en/11637/how-to-view-http-headers-in-firefox>
- Move argos folder into ~/.config
```
mv argos ~/.config/
```
- create folder extensions in  ~/.local/share/gnome-shell
```
mkdir -p  ~/.local/share/gnome-shell/extensions
```
- Move qtracker@qburst folder to ~/.local/share/gnome-shell/extensions/
```
mv qtracker@qburst.com ~/.local/share/gnome-shell/extensions/
```
- Restart gnome-shell. (Press alt+f2, then 'r' and enter)
- Enable qtracker extension in gnome tweak tool. (From gnome tweak tool -> extension-> Qtracker)



## Reference
This extension is made up with the help of https://github.com/p-e-w/argos
