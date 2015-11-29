%define 	module	burn
Summary:	simple and quick way to burn CDs or DVDs
Summary(pl.UTF-8):	prosty skrypt umożliwiający wypalanie CD/DVD
Name:		python-%{module}
Version:	0.4.4
Release:	4
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://www.bigpaul.org/burn/download/%{module}-%{version}.tar.gz
# Source0-md5:	89526cac818f216eb93407b47d05f971
Patch0:		%{name}-confdir.patch
URL:		http://www.bigpaul.org/burn/
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	cdrdao
Requires:	cdrecord
Requires:	mkisofs
Requires:	python-eyeD3
Requires:	python-mad
Requires:	python-modules
Requires:	python-pyao
Requires:	python-pyvorbis
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Burn is a simple program/script written in Python. It's aim is to make
it simple and quick to burn CDs or DVDs.

%description -l pl.UTF-8
Burn jest prostym skryptem napisanym w języku Python. Jego zadaniem
jest umożliwienie wypalenia płyt CD/DVD w możliwie prosty i szybki
sposób.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

install -d $RPM_BUILD_ROOT%{_sysconfdir}/burn
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp doc/{burn.1,burn-configure.1} $RPM_BUILD_ROOT%{_mandir}/man1
cp burn.conf $RPM_BUILD_ROOT%{_sysconfdir}/burn

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/AUTHORS doc/BUGS changelog doc/KNOWN_BUGS README doc/TODO doc/WISHLIST burn.conf-dist burn.conf
%dir %{_sysconfdir}/burn
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/burn/burn.conf
%attr(755,root,root) %{_bindir}/burn
%attr(755,root,root) %{_bindir}/burn-configure
%dir %{py_sitescriptdir}/burnlib
%{py_sitescriptdir}/burnlib/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info
%endif
%{_mandir}/man1/burn.1*
%{_mandir}/man1/burn-configure.1*
