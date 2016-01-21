# Zeal Packaging: RPM

This specfile can be used to build Zeal RPM package for Red Hat based distributions. Tested on Fedora 21.

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
*See the [CentOS Howto](https://wiki.centos.org/HowTos/SetupRpmBuildEnvironment) for more information)*
```sh
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros
```

### Build RPM
```sh
rpmbuild -bb zeal.spec
```
