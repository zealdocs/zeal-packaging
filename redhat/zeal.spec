%global _hardened_build 1

Name:           zeal
Version:        0.6.0
Release:        1%{?dist}
Summary:        Offline documentation browser inspired by Dash

License:        GPLv3+
URL:            https://zealdocs.org/
Source0:        https://github.com/zealdocs/zeal/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%{?fedora:BuildRequires: cmake}
%{?rhel:BuildRequires: cmake3}
%{?rhel:BuildRequires: cmake3-data}
BuildRequires:  make
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libarchive-devel
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  sqlite-devel
BuildRequires:  xcb-util-keysyms-devel
Requires:       hicolor-icon-theme

%description
Zeal is a simple offline documentation browser inspired by Dash.

%prep
%autosetup

%build
# use rpm cmake macro but disable shared libraries and link libs statically
# as the zeal-libs are not currently expected to be consumed downstream
%{?fedora:%cmake -DBUILD_SHARED_LIBS:BOOL=OFF .}
%{?rhel:%cmake3 -DBUILD_SHARED_LIBS:BOOL=OFF .}
make %{?_smp_mflags}

%install
%make_install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/zeal.desktop

%check
%{?fedora:ctest}
%{?rhel:ctest3}

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
* Sun Feb 18 2018 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.6.0-1
- update to v0.6.0
- update specfile formatting
- support cmake builds
- drop qmake build support
- enable debug package

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
