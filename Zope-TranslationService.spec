%define		zope_subname	TranslationService
Summary:	A placeful translation service for Zope
Summary(pl):	¦rodowisko dla t³umaczeñ jêzykowych dla Zope
Name:		Zope-%{zope_subname}
Version:	0.4
Release:	5
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.zope.org/Members/efge/%{zope_subname}/%{zope_subname}-%{version}.tgz
# Source0-md5:	b1399f80dc71ea8a54f4c6dc179c12dd
URL:		http://www.zope.org/Members/efge/TranslationService
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-Localizer
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TranslationService is a placeful translation service for Zope.

%description -l pl
TranslationService jest ¶rodowiskiem dla t³umaczeñ jêzykowych dla
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
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc HISTORY.txt
%{_datadir}/%{name}
