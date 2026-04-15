%define module docstring-parser
%define oname docstring_parser
%bcond tests 1

Name:		python-docstring-parser
Version:	0.18.0
Release:	1
Summary:	Parse Python docstrings
Group:		Development/Python
License:	MIT
URL:		https://github.com/rr-/docstring_parser
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:  python%{pyver}dist(pytest)
%endif

%description
Parse Python docstrings. Currently support ReST, Google, and
Numpydoc-style docstrings.Example usage:python >>> from docstring_parser import
parse>>> >>> docstring parse( ... ''' ... Short description... Long description
spanning multiple lines ... - First line ... - Second line ... - Third line...
:param name: description 1 ... :param int priority: description 2 ... :param...

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python3_sitelib}:${PWD}"
pytest
%endif

%files
%doc README.md
%license LICENSE.md
%{python3_sitelib}/%{oname}
%{python3_sitelib}/%{oname}-%{version}.dist-info
