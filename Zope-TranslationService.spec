%include	/usr/lib/rpm/macros.python
%define		zope_subname	TranslationService
Summary:	TranslationService - a placeful translation service for Zope
Summary(pl):	TranslationService - ¶rodowisko dla t³umaczeñ jêzykowych dla Zope
Name:		Zope-%{zope_subname}
Version:	0.4
Release:	2
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.zope.org/Members/efge/%{zope_subname}/%{zope_subname}-%{version}.tgz
# Source0-md5:	b1399f80dc71ea8a54f4c6dc179c12dd
URL:		http://www.zope.org/Members/efge/TranslationService
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-Localizer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
TranslationService is a placeful translation service for Zope.

%description -l pl
TranslationService jest ¶rodowiskiem dla t³umaczeñ jêzykowych dla
Zope.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

cp -af {zmi,*.py,*.gif} $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc HISTORY.txt
%{product_dir}/%{zope_subname}
