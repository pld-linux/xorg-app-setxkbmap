# $Rev: 3364 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	setxkbmap application
Summary(pl):	Aplikacja setxkbmap
Name:		xorg-app-setxkbmap
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/setxkbmap-%{version}.tar.bz2
# Source0-md5:	8c9d85deb35263dee2dd539ec7b5afc5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/setxkbmap-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
setxkbmap application.

%description -l pl
Aplikacja setxkbmap.


%prep
%setup -q -n setxkbmap-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
