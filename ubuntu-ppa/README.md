Guide for Ubuntu packaging
==========================
General info: http://packaging.ubuntu.com/html/packaging-new-software.html
Debian guide (doesn't use bazaar, so command parameters are more correct): https://www.debian.org/doc/manuals/maint-guide/

Supporting new ubuntu version
=============================
http://packaging.ubuntu.com/html/getting-set-up.html#set-up-pbuilder
$ pbuilder-dist <release> create
    
Compiling locally to check it works before uploading
====================================================
http://packaging.ubuntu.com/html/packaging-new-software.html#building-the-package
Comment out debuild, uploading etc in ppa-upload.sh
Enter source directory.
$ debuild -us -uc

Clean compile to check it works
===============================
Follow steps for local compile above first.
Then: https://blog.packagecloud.io/eng/2015/05/18/building-deb-packages-with-pbuilder/

    sudo pbuilder --build                                                   \
                    --distribution trusty                                   \
                    --architecture amd64                                    \
                    --basetgz /var/cache/pbuilder/trusty-amd64-base.tgz     \
                    /path/to/package.dsc

Once the build has concluded, you will find the resulting files in $BUILDRESULT. The default value for this is: /var/cache/pbuilder/result/.


Troubleshooting
===============
If you have problems, take a look at the official ubuntu/debian build files:
https://packages.ubuntu.com/search?keywords=zeal&searchon=names


You can also try regenerating the debian directory yourself:
https://blog.packagecloud.io/eng/2015/07/14/using-dh-make-to-prepare-debian-packages/
