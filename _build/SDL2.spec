Summary: Simple DirectMedia Layer
Name: SDL2
Version: 2.32.8
Release: 2
Source: http://www.libsdl.org/release/%{name}-%{version}.tar.gz
URL: http://www.libsdl.org/
License: zlib
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Prefix: %{_prefix}
%ifos linux
Provides: libSDL2-2.0.so.0
%endif

%define __defattr %defattr(-,root,root)
%define __soext so

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

This is the libraries, include files and other resources you can use
to develop SDL applications.


%prep
%setup -q 

%build
%ifos linux
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix} --disable-video-directfb
%else
%configure
%endif
make

%install
rm -rf $RPM_BUILD_ROOT
%ifos linux
make install prefix=$RPM_BUILD_ROOT%{prefix} \
             bindir=$RPM_BUILD_ROOT%{_bindir} \
             libdir=$RPM_BUILD_ROOT%{_libdir} \
             includedir=$RPM_BUILD_ROOT%{_includedir} \
             datadir=$RPM_BUILD_ROOT%{_datadir} \
             mandir=$RPM_BUILD_ROOT%{_mandir}
%else
%makeinstall
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{__defattr}
%doc README*.txt LICENSE.txt CREDITS.txt BUGS.txt
%{_libdir}/lib*.%{__soext}.*

%files devel
%{__defattr}
%doc docs/README*.md
%{_bindir}/*-config
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.%{__soext}
%{_includedir}/*/*.h
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/SDL2/*
%{_datadir}/aclocal/*

%changelog
* Thu Jun 04 2015 Ryan C. Gordon <icculus@icculus.org>
- Fixed README paths.

* Sun Dec 07 2014 Simone Contini <s.contini@oltrelinux.com>
- Fixed changelog date issue and docs filenames

* Sun Jan 22 2012 Sam Lantinga <slouken@libsdl.org>
- Updated for SDL 2.0

* Tue May 16 2006 Sam Lantinga <slouken@libsdl.org>
- Removed support for Darwin, due to build problems on ps2linux

* Sat Jan 03 2004 Anders Bjorklund <afb@algonet.se>
- Added support for Darwin, updated spec file

* Wed Jan 19 2000 Sam Lantinga <slouken@libsdl.org>
- Re-integrated spec file into SDL distribution
- 'name' and 'version' come from configure 
- Some of the documentation is devel specific
- Removed SMP support from %build - it doesn't work with libtool anyway

* Tue Jan 18 2000 Hakan Tandogan <hakan@iconsult.com>
- Hacked Mandrake sdl spec to build 1.1

* Sun Dec 19 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Sat Dec 18 1999 John Buswell <johnb@mandrakesoft.com>
- Add symlink for libSDL-1.0.so.0 required by sdlbomber
- Added docs

* Thu Dec 09 1999 Lenny Cartier <lenny@mandrakesoft.com>
- v 1.0.0

* Mon Nov  1 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- First spec file for Mandrake distribution.

# end of file
