Summary:	setxkbmap application
Summary(pl):	Aplikacja setxkbmap
Name:		xorg-app-setxkbmap
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/setxkbmap-%{version}.tar.bz2
# Source0-md5:	0316b2ab6fea88ed76d231c3b47544d8
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-data-xkbdata
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/setxkbmap
%{_mandir}/man1/setxkbmap.1x*
