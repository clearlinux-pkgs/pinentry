#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6
#
Name     : pinentry
Version  : 1.1.0
Release  : 26
URL      : https://gnupg.org/ftp/gcrypt/pinentry/pinentry-1.1.0.tar.bz2
Source0  : https://gnupg.org/ftp/gcrypt/pinentry/pinentry-1.1.0.tar.bz2
Source1 : https://gnupg.org/ftp/gcrypt/pinentry/pinentry-1.1.0.tar.bz2.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: pinentry-bin = %{version}-%{release}
Requires: pinentry-info = %{version}-%{release}
Requires: pinentry-license = %{version}-%{release}
BuildRequires : fltk-dev
BuildRequires : gcr-dev
BuildRequires : gtk3-dev
BuildRequires : libXcursor-dev
BuildRequires : libassuan-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libgpg-error-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(gcr-3)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libsecret-1)
Patch1: 0001-add-pinentry-wrapper.patch

%description
PINEntry
---------
This is a collection of PIN or passphrase entry dialogs which
utilize the Assuan protocol as specified in the Libassuan manual.

%package bin
Summary: bin components for the pinentry package.
Group: Binaries
Requires: pinentry-license = %{version}-%{release}

%description bin
bin components for the pinentry package.


%package extras
Summary: extras components for the pinentry package.
Group: Default

%description extras
extras components for the pinentry package.


%package info
Summary: info components for the pinentry package.
Group: Default

%description info
info components for the pinentry package.


%package license
Summary: license components for the pinentry package.
Group: Default

%description license
license components for the pinentry package.


%prep
%setup -q -n pinentry-1.1.0
cd %{_builddir}/pinentry-1.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573790232
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --disable-pinentry-gtk2 --disable-pinentry-qt5 --enable-pinentry-gnome3 --enable-pinentry-curses
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1573790232
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pinentry
cp %{_builddir}/pinentry-1.1.0/COPYING %{buildroot}/usr/share/package-licenses/pinentry/2d29c273fda30310211bbf6a24127d589be09b6c
%make_install
## install_append content
install -m 0755 pinentry-wrapper %{buildroot}/usr/bin/pinentry
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pinentry
/usr/bin/pinentry-curses

%files extras
%defattr(-,root,root,-)
/usr/bin/pinentry-fltk
/usr/bin/pinentry-gnome3

%files info
%defattr(0644,root,root,0755)
/usr/share/info/pinentry.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pinentry/2d29c273fda30310211bbf6a24127d589be09b6c
