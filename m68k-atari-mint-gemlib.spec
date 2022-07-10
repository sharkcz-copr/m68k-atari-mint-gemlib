# we are cross-compiled libraries
%global debug_package %{nil}
%global __strip /bin/true

%global cvsdate 20130415

Name:           m68k-atari-mint-gemlib
Summary:        The GEM library for Atari MiNT
Version:        0.43.6
Release:        2.%{cvsdate}cvs%{?dist}
License:        Public Domain
Group:          Development/Libraries
URL:            http://arnaud.bercegeay.free.fr/gemlib/
Source0:        http://vincent.riviere.free.fr/soft/m68k-atari-mint/archives/gemlib-CVS-%{cvsdate}.tar.bz2
BuildArch:      noarch
BuildRequires:  m68k-atari-mint-gcc
Requires:       m68k-atari-mint-gcc


%description
GEMlib is a C library for Atari MiNT that allow your software to access AES
and VDI layers.


%prep
%setup -q -n gemlib-CVS-%{cvsdate}

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
* Wed May 14 2014 Dan Horák <dan[at]danny.cz> - 0.43.6-2.20130415
- updated to 20130415 snapshot

* Tue Mar 27 2012 Dan Horák <dan[at]danny.cz> - 0.43.6-1.20100223
- initial Fedora release
