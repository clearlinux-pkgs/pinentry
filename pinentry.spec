#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x528897B826403ADA
#
Name     : pinentry
Version  : 1.2.1
Release  : 31
URL      : https://gnupg.org/ftp/gcrypt/pinentry/pinentry-1.2.1.tar.bz2
Source0  : https://gnupg.org/ftp/gcrypt/pinentry/pinentry-1.2.1.tar.bz2
Source1  : https://gnupg.org/ftp/gcrypt/pinentry/pinentry-1.2.1.tar.bz2.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: pinentry-bin = %{version}-%{release}
Requires: pinentry-info = %{version}-%{release}
Requires: pinentry-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : fltk-dev
BuildRequires : gcr-dev
BuildRequires : gtk3-dev
BuildRequires : libassuan-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libgpg-error-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(gcr-3)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(x11)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
%setup -q -n pinentry-1.2.1
cd %{_builddir}/pinentry-1.2.1
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689782977
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --disable-pinentry-gtk2 \
--disable-pinentry-qt5 \
--enable-pinentry-gnome3 \
--enable-pinentry-curses
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1689782977
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pinentry
cp %{_builddir}/pinentry-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pinentry/2d29c273fda30310211bbf6a24127d589be09b6c || :
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
