Summary:	setxkbmap application - set the keyboard using the X Keyboard Extension
Summary(pl.UTF-8):	Aplikacja setxkbmap - konfiguracja klawiatury przy użyciu rozszerzenia X Keyboard
Name:		xorg-app-setxkbmap
Version:	1.3.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/setxkbmap-%{version}.tar.xz
# Source0-md5:	2f72c7170cdbadc8ef786b2f9cfd4a69
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The setxkbmap command maps the keyboard to use the layout determined
by the options specified on the command line.

An XKB keymap is constructed from a number of components which are
compiled only as needed.

%description -l pl.UTF-8
Polecenie setxkbmap odwzorowuje klawiaturę zgodnie z układem
określonym opcjami podanymi z linii poleceń.

Mapa klawiatury XKB jest konstruowana z wielu składników, które są
kompilowane tylko w razie potrzeby.

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
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/setxkbmap
%{_mandir}/man1/setxkbmap.1*
