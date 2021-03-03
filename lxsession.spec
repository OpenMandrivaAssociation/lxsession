%define git 20210129

Summary:	The default X11 session manager of LXDE
Name:		lxsession
Version:	0.5.5
Release:	1.%{git}.0
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://www.lxde.org
# Current stable rel is old, use latest master git instead https://github.com/lxde/lxsession/
Source0:  %{name}-master.zip
#Source0:	https://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
# Patch from https://sourceforge.net/p/lxde/bugs/760/#29fe/6196 to correct reload option behavior
Patch1:	%{name}-0.5.2-git9f8d6133-reload.patch
Patch2:	%{name}-0.5.2-notify-daemon-default.patch
Patch3:	lxpolkit-0.5.5-openmandriva-disable-lxpolkit-autostart-for-other-environments.patch
Patch4:	d8ff02363de5e7e8cd3bc51958104cfa81b4a9bc.patch

BuildRequires:  desktop-file-utils
BuildRequires:	docbook-to-man
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
#BuildRequires:  docbook-utils
BuildRequires:  gettext
BuildRequires:  intltool
#BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
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

#---------------------------------------------------------------------------

%prep
%setup -q -n %{name}-master
%autosetup -p1
sh ./autogen.sh

%build
%configure --enable-advanced-notifications --enable-gtk3

%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/app-install/desktop

# locales
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/lxlock
%{_bindir}/%{name}
%{_bindir}/%{name}-logout
%{_bindir}/lxclipboard
%{_bindir}/%{name}-default
%{_bindir}/%{name}-default-apps
%{_bindir}/%{name}-default-terminal
%{_bindir}/%{name}-edit
%{_bindir}/%{name}-db
%{_bindir}/%{name}-xdg-autostart
%{_bindir}/lxsettings-daemon
%{_datadir}/app-install/desktop
%{_datadir}/applications/%{name}-default-apps.desktop
%{_datadir}/applications/%{name}-edit.desktop
%{_datadir}/%{name}/images
%{_datadir}/%{name}/ui/%{name}-default-apps.ui
%{_datadir}/%{name}/ui/%{name}-edit.ui
%{_libexecdir}/%{name}/%{name}-xsettings
%{_mandir}/man1/*

%files -n lxpolkit
%{_bindir}/lxpolkit
%{_sysconfdir}/xdg/autostart/lxpolkit.desktop
%{_datadir}/%{name}/ui/lxpolkit.ui

%files edit
%{_bindir}/%{name}-edit
%{_datadir}/applications/lxsession-edit.desktop
%{_datadir}/%{name}/ui/lxsession-edit.ui
