%include	/usr/lib/rpm/macros.python

%define		zope_subname	TranslationService

Summary:	TranslationService is a placeful translation service for Zope
Summary(pl):	TranslationService jest ¶rodowiskiem dla translacji jêzykowych dla Zope
Name:		Zope-%{zope_subname}
Version:	0.4
Release:	1
License:	GNU
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
TranslationService is a placeful translation service for Zope

%description -l pl
TranslationService jest ¶rodowiskiem dla translacji jêzykowych dla
Zope

%prep
%setup -q -c %{zope_subname}-%{version}

%build
cd %{zope_subname}
mkdir docs
mv -f HISTORY.txt docs/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}
cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%preun

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/docs/*
%{product_dir}/%{zope_subname}
