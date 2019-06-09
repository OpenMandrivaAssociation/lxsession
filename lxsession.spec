Summary:	The default X11 session manager of LXDE
Name:		lxsession
Version:	0.5.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://www.lxde.org
Source0:	https://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
# Our docbook tools work... The configure script just detects them incorrectly
# because of /etc/sgml vs. /etc/xml confusion
#Patch0:		lxsession-0.4.6.2-disable-broken-docbook-sanity-check.patch

BuildRequires:  desktop-file-utils
BuildRequires:	docbook-to-man
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
#BuildRequires:  docbook-utils
BuildRequires:  gettext
BuildRequires:  intltool
#BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(indicator-0.4)
BuildRequires:  pkgconfig(appindicator-0.1)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:  pkgconfig(unique-1.0)
BuildRequires:  pkgconfig(polkit-agent-1)
#BuildRequires:	pkgconfig(x11)
BuildRequires:	xsltproc
BuildRequires:  vala

Provides:	lxde-session-manager

%description
LXDE, which stands for Lightweight X11 Desktop Environment, is a desktop
environment which is lightweight and fast. It is designed to be user friendly
and slim, while keeping the resource usage low. LXDE uses less RAM and less CPU
while being a feature rich desktop environment.

LXSession is a lightweiht session manager, is used to automatically start a set
of applications and set up a working desktop environment. Moreover, the session
manager is able to remember the applications in use when a user logs out and to
restart them the next time the user logs in.

LXSession is the standard session manager used by LXDE but it's
desktop-independent and can be used with any window manager.

%files -f %{name}.lang
%{_bindir}/lxsettings-daemon
%{_bindir}/lxlock
%{_bindir}/lxclipboard
%{_bindir}/%{name}
%{_bindir}/%{name}-logout
%{_bindir}/%{name}-db
%{_bindir}/%{name}-default
%{_bindir}/%{name}-default-apps
%{_bindir}/%{name}-default-terminal
%{_bindir}/%{name}-xdg-autostart
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}-xsettings
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/ui/lxpolkit.ui
%exclude %{_datadir}/%{name}/ui/lxsession-edit.ui
%{_datadir}/applications/lxsession-default-apps.desktop
%{_mandir}/man1/%{name}*.*
%{_mandir}/man1/lxlock.1*
%{_mandir}/man1/lxpolkit.1*
%{_mandir}/man1/lxclipboard.1*
%{_mandir}/man1/lxsettings-daemon.1*
%dir %{_sysconfdir}/xdg/%{name}

#---------------------------------------------------------------------------

%package -n lxpolkit
Summary:        Simple PolicyKit authentication agent
Requires:       polkit >= 0.95
# required to replace polkit-gnome and polkit-kde
Provides:       PolicyKit-authentication-agent


%description -n lxpolkit
LXDE, which stands for Lightweight X11 Desktop Environment, is a desktop
environment which is lightweight and fast. It is designed to be user friendly
and slim, while keeping the resource usage low. LXDE uses less RAM and less CPU
while being a feature rich desktop environment.

LXPolKit is a simple PolicyKit authentication agent developed for LXDE, the
Lightweight X11 Desktop Environment.

%files
%{_bindir}/lxpolkit
%config %{_sysconfdir}/xdg/autostart/lxpolkit.desktop
%{_datadir}/%{name}/ui/lxpolkit.ui

#---------------------------------------------------------------------------

%package edit
Summary:        The standard session edit manager used by LXDE

%description edit
LXDE, which stands for Lightweight X11 Desktop Environment, is a desktop
environment which is lightweight and fast. It is designed to be user friendly
and slim, while keeping the resource usage low. LXDE uses less RAM and less CPU
while being a feature rich desktop environment.

LXSession-edit is a tool used to manage freedesktop.org compliant desktop
session autostarts, especially for LXSession.

%files edit
%{_bindir}/%{name}-edit
%{_datadir}/applications/lxsession-edit.desktop
%{_datadir}/%{name}/ui/lxsession-edit.ui

#---------------------------------------------------------------------------

%prep
%setup -q
sh ./autogen.sh

%build
%configure \
	--disable-gtk  \
	--disable-gtk3 \
	%{nil}
%make

%install
%makeinstall_std

# locales
%find_lang %{name}
