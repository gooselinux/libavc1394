Summary:        Audio/Video Control library for IEEE-1394 devices
Name:           libavc1394
Version:        0.5.3
Release:        9.1%{?dist}
License:        GPLv2+ and LGPLv2+
Group:          System Environment/Libraries
URL:            http://sourceforge.net/projects/libavc1394/
Source:         http://downloads.sourceforge.net/libavc1394/libavc1394-%{version}.tar.gz
Patch1:         libavc1394-0.5.3-librom.patch
BuildRequires:  libraw1394-devel
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
ExcludeArch:    s390 s390x

%description
The libavc1394 library allows utilities to control IEEE-1394 devices
using the AV/C specification.  Audio/Video Control allows applications
to control devices like the tape on a VCR or camcorder.

%package devel
Summary: Development libs for libavc1394
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libraw1394-devel, pkgconfig

%description devel
Development libraries required to build applications using libavc1394.

%prep
%setup -q
%patch1 -p1 -b .librom
chmod -x test/dvcont.c

%build
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT
# sigh, --disable-static doesn't work
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README ChangeLog TODO
# binaries are GPLv2+
%{_bindir}/dvcont
%{_bindir}/mkrfc2734
%{_bindir}/panelctl
%{_mandir}/man1/dvcont.1.gz
%{_mandir}/man1/panelctl.1.gz
%{_mandir}/man1/mkrfc2734.1*
# libs are LGPLv2+
%{_libdir}/libavc1394.so.*
%{_libdir}/librom1394.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/libavc1394/
%{_libdir}/pkgconfig/libavc1394.pc
%{_libdir}/libavc1394.so
%{_libdir}/librom1394.so


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.5.3-9.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Jarod Wilson <jarod@redhat.com> 0.5.3-8
- Fix duplicate global symbols in libavc1394 vs. librom1394 (#216143)

* Mon May 18 2009 Jarod Wilson <jarod@redhat.com> 0.5.3-7
- Use included libtool, kill rpath a different way (#225988)

* Mon May 18 2009 Jarod Wilson <jarod@redhat.com> 0.5.3-6
- Fix up merge review issues (#225988)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.5.3-4
- fix license tag

* Tue Jul 22 2008 Jarod Wilson <jwilson@redhat.com> 0.5.3-3
- Bump and rebuild for libraw1394 v2.0.0

* Thu Feb 14 2008 Jarod Wilson <jwilson@redhat.com> - 0.5.3-2
- Bump and rebuild with gcc 4.3

* Sun Sep 10 2006 Jarod Wilson <jwilson@redhat.com> - 0.5.3-1
- Upstream release 0.5.3

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.5.1-2.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.5.1-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.5.1-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Dec 22 2005 Warren Togami <wtogami@redhat.com> 0.5.1-2
- remove .a and .la (#172641)
- GPL -> LGPL (#165908)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 10 2005 Matthias Saou <http://freshrpms.net/> 0.5.1-1
- Update to 0.5.1.
- Update librom patch to still apply cleanly.

* Sat Oct 15 2005 Florian La Roche <laroche@redhat.com>
- make sure librom1394 is linked to libraw1394 and also
  libavc1394 is linked to librom1394 (also bz 156938)

* Wed Mar 16 2005 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 28 2005 Warren Togami <wtogami@redhat.com> 0.4.1-7
- gcc4 rebuild

* Sun Feb 06 2005 Warren Togami <wtogami@redhat.com> 0.4.1-6
- rebuild against new libraw1394

* Mon Jan 03 2005 Colin Walters <walters@redhat.com> 0.4.1-5
- Rerun autotools in attempt to get package to link to -lm
- Add patch libavc1394-0.4.1-kill-configure-insanity.patch

* Mon Nov 22 2004 Karsten Hopp <karsten@redhat.de> 0.4.1-4 
- remove bogus ldconfig after makeinstall

* Fri Jul 30 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- add symlinks for ldconfig

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 12 2004 Warren Togami <wtogami@redhat.com> 0.4.1-1
- upgrade to 0.4.1
- Spec cleanups
- License -> Copyright
- Remove INSTALL; Add News, ChangeLog
- Applications/Multimedia -> System Environment/Libraries

* Mon Aug 25 2003 Bill Nottingham <notting@redhat.com> 0.3.1-7
- fix buildreqs (#102204)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 0.3.1-4
- rebuild on all arches

* Wed Nov 20 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- exclude mainframe
- allow lib64

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 09 2002 Michael Fulbright <msf@redhat.com>
- First RPM build

