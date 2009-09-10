# has major internal linking issues - AdamW 2008/12
%define _disable_ld_no_undefined	1

%define major		2
%define libname		%mklibname %{fname} %{major}
%define develname	%mklibname %{fname} %{major} -d

%define fname	fltk
%define fver	2.0.x
%define svn	6525
%define rel	3

%if %svn
%define release		%mkrel 0.%{svn}.%{rel}
%define distname	%{fname}-%{fver}-r%{svn}.tar.bz2
%define dirname		%{fname}-%{fver}-r%{svn}
%else
%define release		%mkrel %{rel}
%define distname	%{fname}-%{version}.tar.bz2
%define dirname		%{fname}-%{version}
%endif

Name:		fltk2
Version:	2.0.0
Release:	%{release}
Group:		System/Libraries
Summary:	Fast Light Tool Kit (FLTK) version 2
License:	LGPLv2+ with exceptions
Source0:	http://ftp.easysw.com/pub/fltk/snapshots/%{distname}
# Tries to run fltk2-config as simply bindir/fltk2-config: patch makes
# it run as destdir/bindir/fltk2-config - AdamW 2008/12
Patch0:		fltk2-6525-fluid_config_run.patch
# Fix underlinking - AdamW 2008/12
Patch1:		fltk2-6525-underlink.patch
URL:		http://www.fltk.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	X11-devel
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	zlib-devel
BuildRequires:	mesaglu-devel
BuildRequires:	GL-devel
BuildRequires:	makedepend
BuildRequires:	man

%description
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r),
and Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally
developed by Mr. Bill Spitzak and is currently maintained by a
small group of developers across the world with a central
repository in the US.

%package -n %{libname}
Summary:	Fast Light Tool Kit (FLTK) 2 - main library
Group:		System/Libraries

%description -n	%{libname}
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r),
and Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally
developed by Mr. Bill Spitzak and is currently maintained by a
small group of developers across the world with a central
repository in the US.

%package -n %{develname}
Summary:	Fast Light Tool Kit (FLTK) - development environment
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a LGPL'd
C++ graphical user interface toolkit for X (UNIX(r)), OpenGL(r),
and Microsoft(r) Windows(r) NT 4.0, 95, or 98. It was originally
developed by Mr. Bill Spitzak and is currently maintained by a
small group of developers across the world with a central
repository in the US. This package contains development libraries
and headers.

%prep
%setup -q -n %{dirname}
%patch0 -p1 -b .config
%patch1 -p1 -b .underlink

%build
%configure2_5x --enable-shared
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libfltk*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README README_fltk1_to_fltk2.txt CREDITS CHANGES COPYING TODO
%{_bindir}/%{name}-config
%{_bindir}/fluid2
%{_includedir}/%{fname}
%{_libdir}/libfltk*.so
%{_libdir}/libfltk*.a
