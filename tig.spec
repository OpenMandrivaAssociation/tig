%define name    tig
%define version 0.17
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Text-mode interface for the git revision control system

Group:          Development/Other
License:        GPLv2+
URL:            http://jonas.nitro.dk/tig
Source0:        http://jonas.nitro.dk/tig/releases/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  git-core
BuildRequires:  ncurses-devel
BuildRequires:  xmlto
BuildRequires:  asciidoc
Requires:       git-core

%description
Tig is a repository browser for the git revision control system that
additionally can act as a pager for output from various git commands.

When browsing repositories, it uses the underlying git commands to present the
user with various views, such as summarized revision log and showing the commit
with the log message, diffstat, and the diff.

Using it as a pager, it will display input from stdin and colorize it.

%prep
%setup -q

%build
%configure2_5x
%make all doc-man doc-html

#Convert to unix line endings
sed -i -e 's/\r//' *.html


%install
rm -rf %{buildroot}
%makeinstall_std install-doc-man

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING README SITES BUGS manual.txt *.html
%{_bindir}/tig
%{_bindir}/test-graph
%{_mandir}/man1/tig.1*
%{_mandir}/man5/tigrc.5*
%{_mandir}/man7/tigmanual.7.*


%changelog
* Wed Apr 20 2011 Michael Scherer <misc@mandriva.org> 0.17-1mdv2011.0
+ Revision: 656138
- update to 0.17

* Sun Jan 16 2011 Michael Scherer <misc@mandriva.org> 0.16.2-1
+ Revision: 631157
- update to 0.16.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Tue Mar 02 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.15-1mdv2010.1
+ Revision: 513699
- update to 0.15
- use %%configure2_5x
- fix file list, %%{_mandir}/man7/tigmanual.7.lzma was missing.

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.14.1-2mdv2010.0
+ Revision: 445433
- rebuild

* Wed Mar 04 2009 Michael Scherer <misc@mandriva.org> 0.14.1-1mdv2009.1
+ Revision: 348618
- update to new version 0.14.1

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0.13-1mdv2009.1
+ Revision: 332894
- New upstream release

* Mon Jan 05 2009 Jérôme Soyer <saispo@mandriva.org> 0.12.1-1mdv2009.1
+ Revision: 325062
- New upstream release

* Sat Aug 02 2008 Michael Scherer <misc@mandriva.org> 0.11-1mdv2009.0
+ Revision: 260695
- upload to contrib, based on fedora package, adapted by roudoudou
- various cleaning, as explained on bug #42431
- import tig


* Sun Aug 01 2008 roudoudou <roudoudou7@gmail.com> 0.11-1mdv2009.0
- Initial Mandriva rpm package (based on fedora package)

* Sun Apr 06 2008 James Bowes <jbowes@redhat.com> 0.11-1
- tig-0.11

* Tue Mar 25 2008 Todd Zullinger <tmz@pobox.com> 0.10.1-2
- use %%configure so ncursesw is picked up for utf-8 support
- BuildRequire git so configure finds git-config and git-repo-config
- change Requires: git-core to git

* Wed Mar 19 2008 James Bowes <jbowes@redhat.com> 0.10.1-1
- tig-0.10.1

* Mon Mar 17 2008 James Bowes <jbowes@redhat.com> 0.10-1
- tig-0.10

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.1-2
- Autorebuild for GCC 4.3

* Sun Sep 30 2007 James Bowes <jbowes@redhat.com> - 0.9.1-1
- tig-0.9.1

* Thu Sep 20 2007 James Bowes <jbowes@redhat.com> - 0.9-1
- tig-0.9

* Thu Aug 23 2007 James Bowes <jbowes@redhat.com> - 0.8-2
- Mark license as GPLv2+

* Tue Jun 19 2007 James Bowes <jbowes@redhat.com> - 0.8-1
- tig-0.8

* Sat Jun 02 2007 James Bowes <jbowes@redhat.com> - 0.7-4
- Ensure that the version string is set in the binary.

* Fri Jun 01 2007 James Bowes <jbowes@redhat.com> - 0.7-3
- Incorporate differences from jcollie's tig spec.

* Fri Jun 01 2007 James Bowes <jbowes@redhat.com> - 0.7-2
- Update spec file after review feedback.

* Thu May 31 2007 James Bowes <jbowes@redhat.com> - 0.7-1
- Initial packaging.
