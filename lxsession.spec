#FIMXE: workaround for clang 16
%global optflags %{optflags} -Wno-incompatible-function-pointer-types

# git snapshot
%global snapshot 1
%if 0%{?snapshot}
	%global commit		f68f4779a6ba4edd4f4e3e7641a8ab1e0486c8d6
	%global commitdate	20240416
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif


Summary:	The default X11 session manager of LXDE
Name:		lxsession
Version:	0.5.5
Release:	6
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://www.lxde.org
#Source0:	https://downloads.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
Source0:	https://github.com/lxde/lxsession/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz

# Patch from https://sourceforge.net/p/lxde/bugs/760/#29fe/6196 to correct reload option behavior
Patch1:		lxsession-0.5.2-git9f8d6133-reload.patch
Patch2:		lxsession-0.5.2-notify-daemon-default.patch
Patch3:		lxsession-0.5.4-load-settings-nullcheck.patch
Patch5:		lxsession-0.5.5-use_ayatana_indicators.patch
Patch6:		lxsession-0.5.5-add-custom-xdg-config-dir.patch
Patch100:	lxpolkit-0.5.5-openmandriva-disable-lxpolkit-autostart-for-other-environments.patch

BuildRequires:	desktop-file-utils
BuildRequires:	docbook-to-man
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
#BuildRequires:	docbook-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:	pkgconfig(ayatana-indicator3-0.4)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(unique-3.0)
BuildRequires:	pkgconfig(polkit-agent-1)
BuildRequires:	pkgconfig(x11)
BuildRequires:	xsltproc
BuildRequires:	vala

Requires:	notification-daemon
Requires:	polkit-agent
# required for suspend and hibernate
Requires:	upower

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

#---------------------------------------------------------------------------

%package -n lxpolkit
Summary:	Simple PolicyKit authentication agent
Requires:	polkit >= 0.95

%description -n lxpolkit
LXDE, which stands for Lightweight X11 Desktop Environment, is a desktop
environment which is lightweight and fast. It is designed to be user friendly
and slim, while keeping the resource usage low. LXDE uses less RAM and less CPU
while being a feature rich desktop environment.

LXPolKit is a simple PolicyKit authentication agent developed for LXDE, the
Lightweight X11 Desktop Environment.

%files -n lxpolkit
%{_bindir}/lxpolkit
%{_sysconfdir}/xdg/autostart/lxpolkit.desktop
%{_datadir}/%{name}/ui/lxpolkit.ui

#---------------------------------------------------------------------------

%package edit
Summary:	The standard session edit manager used by LXDE

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
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}


%build
sh ./autogen.sh
%configure \
	--enable-advanced-notifications \
	--enable-buildin-clipboard \
	--enable-gtk3 \
	--enable-man \
	--disable-silent-rules \
	--enable-debug \
	%{nil}

%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/app-install/desktop

# locales
%find_lang %{name}

