%define		zope_subname	TranslationService
Summary:	A placeful translation service for Zope
Summary(pl.UTF-8):	Środowisko dla tłumaczeń językowych dla Zope
Name:		Zope-%{zope_subname}
Version:	0.4
Release:	6
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.zope.org/Members/efge/%{zope_subname}/%{zope_subname}-%{version}.tgz
# Source0-md5:	b1399f80dc71ea8a54f4c6dc179c12dd
URL:		http://www.zope.org/Members/efge/TranslationService
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
Requires:	Zope-Localizer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TranslationService is a placeful translation service for Zope.

%description -l pl.UTF-8
TranslationService jest środowiskiem dla tłumaczeń językowych dla
Zope.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {zmi,*.py,*.gif,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc HISTORY.txt
%{_datadir}/%{name}
