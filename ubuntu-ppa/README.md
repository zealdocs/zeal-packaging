Guide for Ubuntu packaging
==========================
General info: http://packaging.ubuntu.com/html/packaging-new-software.html

Supporting new ubuntu version
=============================
http://packaging.ubuntu.com/html/getting-set-up.html#set-up-pbuilder
$ pbuilder-dist <release> create
    
Compiling to check it works before uploading
============================================
http://packaging.ubuntu.com/html/packaging-new-software.html#building-the-package
Comment out debuild, uploading etc in ppa-upload.sh
Enter source directory.
$ debuild -us -uc
