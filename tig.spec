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
