%global pkgname dm.xmlsec.binding

Name:           python-dm-xmlsec-binding
Version:        1.3.7
Release:        1%{?dist}
Summary:        xmlsec binding

License:        MIT
URL:            https://pypi.org/project/dm.xmlsec.binding

Source0:        https://files.pythonhosted.org/packages/source/d/%{pkgname}/%{pkgname}-%{version}.tar.gz

BuildRequires:  python-lxml
BuildRequires:  python-setuptools
BuildRequires:  libxml2-devel
BuildRequires:  xmlsec1-devel
BuildRequires:  xmlsec1-openssl-devel
BuildRequires:  python2-devel
BuildRequires:  libtool-ltdl-devel

%description
This package contains a Cython-based binding to Aleksey Sanin's XML security
library to be used together with lxml, the most popular Python binding to the
Gnome XML library libxml2.

%prep
%autosetup -p1 -n %{pkgname}-%{version}

%build
export CFLAGS=-DXMLSEC_NO_SIZE_T
cp /usr/lib64/python2.7/site-packages/lxml/lxml.etree_api.h src/etree_api.h
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%check
export PYTHONPATH=$(pwd)
# %%{__python2} setup.py test
%{__python2} dm/xmlsec/binding/tests.py -v

%files
%doc dm/xmlsec/binding/README.txt
%license dm/xmlsec/binding/LICENSE.txt
%{python2_sitearch}/*

%changelog
* Tue Jan 15 2019 Ken Dreyer <kdreyer@redhat.com> - 1.3.7-1
- intial package
