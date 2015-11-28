
%define 	module	pypar

Summary:	pypar - Parallel Programming in the spirit of Python!
Summary(pl.UTF-8):	pypar - programowanie równoległe w duchu Pythona
Name:		python-%{module}
Version:	1.9.3
Release:	7
License:	GPL
Group:		Libraries/Python
Source0:	http://datamining.anu.edu.au/~ole/pypar/%{module}_%{version}.tgz
# Source0-md5:	7039dc549acd1db9806e7510c8eb93dc
Patch0:		%{name}-build.patch
URL:		http://datamining.anu.edu.au/~ole/pypar/
BuildRequires:	mpi
BuildRequires:	python-Numeric-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-numarray-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pypar is an efficient but easy-to-use module that allows
programs/scripts written in the Python programming language to run in
parallel on multiple processors and communicate using message passing.
Pypar provides bindings to an important subset of the message passing
interface standard MPI.

%description -l pl.UTF-8
Pypar to sprawny, lecz łatwy w użyciu moduł pozwalający programom i
skrtyptom napisanym w języku programowania Python działać równolegle
na wielu procesorach i komunikować się przy użyciu przekazywania
komunikatów. Pypar udostępnia dowiązania do istotnego podzbioru
standardu interfejsu przekazywania komunikatów MPI.

%package examples
Summary:	Example programs for Python pypar module
Summary(pl.UTF-8):	Programy przykładowe do modułu Pythona pypar
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Python pypar module.

%description examples -l pl.UTF-8
Pakiet zawierający programy przykładowe dla modułu Pythona pypar.

%prep
%setup -q -n %{module}_%{version}
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

%py_install \
	--install-lib=%{py_sitedir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DOC FAQ README
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%{py_sitedir}/*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
