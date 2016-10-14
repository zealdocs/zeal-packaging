%global _hardened_build 1
%global debug_package %{nil}

Summary: Zeal: Simple offline API documentation browser
Name: zeal
Version: 0.3.1
Release: 1%{?dist}
License: GPLv3+
Group: Development/Tools
URL: https://zealdocs.org/
Source0: https://github.com/zealdocs/zeal/archive/v%{version}.tar.gz
BuildRequires: make gcc-c++
BuildRequires: qt5-qtwebkit-devel libarchive-devel qt5-qtx11extras-devel xcb-util-keysyms-devel
Requires: qt5-qtbase qt5-qtwebkit libarchive qt5-qtx11extras xcb-util-keysyms

%description
Zeal is a simple offline documentation browser inspired by Dash.

%prep
%autosetup

%build
qmake-qt5
make %{?_smp_mflags}

%install
export INSTALL_ROOT=%{buildroot}
make install

%files
/usr/bin/zeal
/usr/share/applications/zeal.desktop
/usr/share/icons/hicolor/*/apps/zeal.png

%changelog
* Sun Oct 02 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.3.0-2
- update build requirements and disable debug package

* Sat Oct 01 2016 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.3.0-1
- update to v0.3.0

