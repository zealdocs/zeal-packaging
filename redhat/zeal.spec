%global _hardened_build 1
%global debug_package %{nil}

Summary: Zeal: Simple offline API documentation browser
Name: zeal
Version: 0.5.0
Release: 1%{?dist}
License: GPLv3+
Group: Development/Tools
URL: https://zealdocs.org/
Source0: https://github.com/zealdocs/zeal/archive/v%{version}.tar.gz
BuildRequires: make gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: libarchive-devel
BuildRequires: qt5-qtbase qt5-qtbase-devel qt5-qtwebkit-devel qt5-qtx11extras-devel
BuildRequires: xcb-util-keysyms-devel sqlite-devel
Requires: hicolor-icon-theme

%description
Zeal is a simple offline documentation browser inspired by Dash.

%prep
%autosetup

%build
%{qmake_qt5} zeal.pro
make %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/zeal.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license COPYING
%doc README.md
%{_bindir}/zeal
%{_datadir}/applications/zeal.desktop
%{_datadir}/icons/hicolor/*/apps/zeal.png

%changelog
* Tue Dec 19 2017 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.5.0-1
- update to v0.5.0
- align to fedora project maintained rpm specfile (use qmake_qt5 macro)

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

