# we are cross-compiled libraries
%global debug_package %{nil}
%global __strip /bin/true

%global gitdate 20170304
%global commit 533b3b231af3fb3f96a3bd4c40c6e6e0bdb2e521
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           m68k-atari-mint-gemlib
Summary:        The GEM library for Atari MiNT
Version:        0.44.0
Release:        1.%{gitdate}git%{?dist}
License:        Public Domain
URL:            https://github.com/freemint/gemlib
Source0:        https://github.com/freemint/gemlib/archive/%{commit}/gemlib-%{shortcommit}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  m68k-atari-mint-gcc
Requires:       m68k-atari-mint-gcc


%description
GEMlib is a C library for Atari MiNT that allow your software to access AES
and VDI layers.


%prep
%setup -q -n gemlib-%{commit}

find . -type f -exec chmod -x {} \;


%build
make -C gemlib PREFIX=%{mint_prefix} CROSS=yes \
	WITH_020_LIB=yes WITH_V4E_LIB=yes


%install
make -C gemlib install PREFIX=$RPM_BUILD_ROOT%{mint_prefix} \
	WITH_020_LIB=yes WITH_V4E_LIB=yes \
        CROSS=yes

# cleanup
rm -rf $RPM_BUILD_ROOT%{mint_libdir}/libgem16.a


%files
%doc
%{mint_includedir}/*
%{mint_libdir}/*


%changelog
* Sun Jul 10 2022 Dan Horák <dan[at]danny.cz> - 0.44.0-1.20170304
- updated to 20170304 snapshot

* Wed May 14 2014 Dan Horák <dan[at]danny.cz> - 0.43.6-2.20130415
- updated to 20130415 snapshot

* Tue Mar 27 2012 Dan Horák <dan[at]danny.cz> - 0.43.6-1.20100223
- initial Fedora release
