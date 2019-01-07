# Overview

Qtracker extension will show hours clocked, burned, break duration etc in top bar.

## Requirments
Qtracker extension only works on Gnome-3 (ubuntu 18). Also it needs gnome-tweak tool to activate.

## Installation

Install extension by following command or do manual installation.

```
sh install.sh
```

### Manual installation

- Install gnome tweak tool
- Change ```AUTH=''``` in argos/qtracker.100s.py to your authentication header. Example ```AUTH = '0e891e9d2ed5aedgg3410b22ddad4368d6117f23dff0ee7d389cacedee2fcd591539229015200.950e0c0fee5b9b48e83f7a477c7de1e4e02815bf'```
	- For getting authentication header in chrome <https://www.mkyong.com/computer-tips/how-to-view-http-headers-in-google-chrome/>
	- For getting authentication header in Firefox <https://o7planning.org/en/11637/how-to-view-http-headers-in-firefox>
- Move argos folder into ~/.config
- Move qtracker@qburst folder to ~/.local/share/gnome-shell/extensions/
- Enable qtracker extension in gnome tweak tool. (From gnome tweak tool -> extension-> Qtracker)
- If extension doesnt appear on top bar restart gnome-shell. (Press alt+f2, then 'r' and enter)


## Reference
This extension is made up with the help of https://github.com/p-e-w/argos
