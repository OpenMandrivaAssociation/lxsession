Summary:	The default X11 session manager of LXDE
Name:     	lxsession
Version:	0.3.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.bz2
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-to-man
Requires:	desktop-common-data

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

# add startup script
install -d %buildroot%_bindir
cat > %buildroot%_bindir/startlxde << EOF
#!/bin/sh
exec /usr/bin/lxsession -s LXDE
EOF
chmod +x %buildroot%_bindir/startlxde

# add wmsession.d
install -d %buildroot%_sysconfdir/X11/wmsession.d/
cat > %buildroot%_sysconfdir/X11/wmsession.d/26LXDE << EOF
NAME=LXDE
DESC=Lightweight X11 Desktops Environment
EXEC=/usr/bin/startlxde
SCRIPT:
exec /usr/bin/startlxde
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post  
%make_session

%postun
%make_session

%files -f %{name}.lang
%defattr(-, root, root)
%attr(644,root,root) %{_sysconfdir}/X11/wmsession.d/26LXDE
%{_bindir}/lxsession
%{_bindir}/lxsession-logout
%{_bindir}/startlxde
%{_datadir}/lxsession
%{_mandir}/man1/*
