Summary:	The default X11 session manager of LXDE
Name:		lxsession
Version:	0.4.6.2
Release:	3
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://www.lxde.org
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
# Our docbook tools work... The configure script just detects them incorrectly
# because of /etc/sgml vs. /etc/xml confusion
Patch0:		lxsession-0.4.6.2-disable-broken-docbook-sanity-check.patch
BuildRequires:	docbook-to-man
BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	xsltproc
BuildRequires:	docbook-dtd412-xml
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(glib-2.0)
Requires:	desktop-common-data
%rename		lxsession-lite
Provides:	lxde-session-manager
Obsoletes:	lxde-settings-daemon

%description
LXSession is lightweiht session manager, and it's not tighted to "any" desktop
environment. It's desktop-independent and can be used with any window manager.
With proper configuration, you can make your own desktop environment with
LXSession. This is very useful to the users and developers of non-mainstream
window managers and desktop environemts.

%prep
%setup -q
%apply_patches
[ -e autogen.sh ] && ./autogen.sh

%build
%configure2_5x --disable-gtk --disable-gtk3
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/lxsession
%{_bindir}/lxsession-default
%{_bindir}/lxsession-default-terminal
%{_bindir}/lxsession-xsettings
%{_bindir}/lxsettings-daemon
%{_bindir}/lxlock
%{_datadir}/lxsession
%{_datadir}/applications/lxsession-edit.desktop
%{_datadir}/applications/lxsession-default-apps.desktop
%{_mandir}/man1/*

