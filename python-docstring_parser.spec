# Created by pyp2rpm-3.3.5
%global pypi_name docstring_parser

Name:           python-%{pypi_name}
Version:        0.7.3
Release:        1
Summary:        Parse Python docstrings
Group:          Development/Python
License:        MIT
URL:            https://github.com/rr-/docstring_parser
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Parse Python docstrings. Currently support ReST, Google, and
Numpydoc-style docstrings.Example usage:python >>> from docstring_parser import
parse>>> >>> docstring parse( ... ''' ... Short description... Long description
spanning multiple lines ... - First line ... - Second line ... - Third line...
:param name: description 1 ... :param int priority: description 2 ... :param...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
