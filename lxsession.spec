Summary:	The default X11 session manager of LXDE
Name:     	lxsession
Version:	0.4.6.1
Release:	%mkrel 3
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
Patch1:		lxsession-0.4.6.1-gdm3.patch
Patch2:		lxsession-0.4.6.1-ltsp.patch
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
Obsoletes:      lxde-settings-daemon

%description
LXSession is lightweiht session manager, and it's not tighted to "any" desktop
environment. It's desktop-independent and can be used with any window manager.
With proper configuration, you can make your own desktop environment with
LXSession. This is very useful to the users and developers of non-mainstream
window managers and desktop environemts.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/lxsession
%{_bindir}/lxlock
%{_bindir}/lxsession-logout
%{_datadir}/lxsession
%{_mandir}/man1/*


%changelog
* Wed Aug 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.4.6.1-1mdv2011.0
+ Revision: 692999
- update to 0.4.6.1

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.5-2
+ Revision: 666113
- mass rebuild

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 0.4.5-1mdv2011.0
+ Revision: 598571
- update to new version 0.4.5

* Mon Apr 05 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.4.4-1mdv2010.1
+ Revision: 531752
- new upstream release 0.4.4

* Thu Mar 18 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.4.3-1mdv2010.1
+ Revision: 525018
- new upstream release 0.4.3

* Mon Mar 08 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.4.2-2mdv2010.1
+ Revision: 516567
- New upstream release 0.4.2
- Clean spec

* Tue Jan 26 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.4.1-2mdv2010.1
+ Revision: 496500
- Obsolete lxde-settings-daemon as it's been merged in
  lxsession upstream some time ago

* Fri Dec 11 2009 Funda Wang <fwang@mandriva.org> 0.4.1-1mdv2010.1
+ Revision: 476259
- new version 0.4.1

* Wed Dec 09 2009 Funda Wang <fwang@mandriva.org> 0.4.0-1mdv2010.1
+ Revision: 475337
- new version 0.4.0

* Tue May 26 2009 Funda Wang <fwang@mandriva.org> 0.3.8-1mdv2010.0
+ Revision: 379765
- BR intltool
- New version 0.3.8

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.3.2-3mdv2009.0
+ Revision: 268131
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Funda Wang <fwang@mandriva.org> 0.3.2-2mdv2009.0
+ Revision: 217330
- conflicts with lxsession-lite
- provides lxde-session-manager

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 0.3.2-1mdv2009.0
+ Revision: 200889
- session files will go lxde-common
- adopt to wmsession
- add source and spec
- Created package structure for lxsession.

