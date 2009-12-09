Summary:	The default X11 session manager of LXDE
Name:     	lxsession
Version:	0.4.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://www.lxde.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-to-man
BuildRequires:	intltool
Requires:	desktop-common-data
Obsoletes:	lxsession-lite < %version
Provides:	lxsession-lite = %version
Provides:	lxde-session-manager

%description
LXSession is lightweiht session manager, and it's not tighted to "any" desktop
environment. It's desktop-independent and can be used with any window manager.
With proper configuration, you can make your own desktop environment with
LXSession. This is very useful to the users and developers of non-mainstream
window managers and desktop environemts.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/lxsession
%{_bindir}/lxsession-logout
%{_datadir}/lxsession
%{_mandir}/man1/*
