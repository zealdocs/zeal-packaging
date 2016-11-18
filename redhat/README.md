# Zeal Packaging: RPM

This specfile can be used to build Zeal RPM package for Red Hat based distributions. Tested on Fedora 21.

## Updating version
1\. Update the specfile with the new version and reset release to 0
```Diff
diff --git a/redhat/zeal.spec b/redhat/zeal.spec
index 4b27fb9..74401bc 100644
--- a/redhat/zeal.spec
+++ b/redhat/zeal.spec
@@ -3,8 +3,8 @@
 
 Summary: Zeal: Simple offline API documentation browser
 Name: zeal
-Version: 0.3.1
-Release: 1%{?dist}
+Version: 0.3.2
+Release: 0%{?dist}
 License: GPLv3+
 Group: Development/Tools
 URL: https://zealdocs.org/
```
2\. Bump specfile using `rpmdev-bumpspec`
```sh
rpmdev-bumpspec \
    --comment="upgrade to v0.3.2" \
    --userstring="$(git config user.name) <$(git config user.email)>" \
    zeal.spec
```
3\. Commit your changes

## Local build

### Install build tools
```sh
yum -y install rpm-build rpmdevtools yum-utils
```

### Install dependencies
```sh
yum-builddep zeal.spec
```
Note: If using `dnf` the command is `dnf builddep`.

### Download source files
```sh
spectool --sourcedir --get-files zeal.spec
```

### Prepare the RPM Build Directories
*See the [CentOS Howto](https://wiki.centos.org/HowTos/SetupRpmBuildEnvironment) for more information*
```sh
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
```

### Build RPM
```sh
rpmbuild -bb zeal.spec
```
