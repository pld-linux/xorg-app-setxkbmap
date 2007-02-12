Summary:	setxkbmap application
Summary(pl.UTF-8):   Aplikacja setxkbmap
Name:		xorg-app-setxkbmap
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/setxkbmap-%{version}.tar.bz2
# Source0-md5:	2b53542095a35a8a5731164118643883
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
setxkbmap application.

%description -l pl.UTF-8
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/setxkbmap
%{_mandir}/man1/setxkbmap.1x*
