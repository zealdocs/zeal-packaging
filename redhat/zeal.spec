%global _hardened_build 1
%global debug_package %{nil}

Summary: Zeal: Simple offline API documentation browser
Name: zeal
Version: 0.4.0
Release: 3%{?dist}
License: GPLv3+
Group: Development/Tools
URL: https://zealdocs.org/
Source0: https://github.com/zealdocs/zeal/archive/v%{version}.tar.gz
%{?fedora:BuildRequires: cmake}
%{?rhel:BuildRequires: cmake3 cmake3-data}
BuildRequires: make gcc-c++ extra-cmake-modules
BuildRequires: qt5-qtwebkit-devel libarchive-devel qt5-qtx11extras-devel
BuildRequires: xcb-util-keysyms-devel sqlite-devel
Requires: qt5-qtbase qt5-qtwebkit libarchive qt5-qtx11extras
Requires: xcb-util-keysyms sqlite-libs

%description
Zeal is a simple offline documentation browser inspired by Dash.

%prep
%autosetup

%build
%{?fedora:%cmake .}
%{?rhel:%cmake3 .}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
ctest -V %{?_smp_mflags}

%files
/usr/bin/zeal
/usr/share/applications/zeal.desktop
/usr/share/icons/hicolor/*/apps/zeal.png

%changelog
* Mon Dec 18 2017 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.4.0-3
- Support CMake 3 builds for CentOS/RHEL distros

* Wed Sep 06 2017 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.4.0-2
- move to using cmake and checks

* Mon Sep 04 2017 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.4.0-1
- update to v0.4.0 and add sqlite dependency

* Sun Oct 02 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.3.0-2
- update build requirements and disable debug package

* Sat Oct 01 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.3.0-1
- update to v0.3.0

