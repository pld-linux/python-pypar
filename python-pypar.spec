
%define 	module	pypar

%define		_vername %(echo %{version}|tr . _)
Summary:	pypar - Parallel Programming in the spirit of Python!
Summary(pl):	pypar - programowanie równoleg³e w duchu Pythona
Name:		python-%{module}
Version:	1.9.2
Release:	3
License:	GPL
Group:		Libraries/Python
Source0:	http://datamining.anu.edu.au/~ole/pypar/%{module}_%{_vername}.tgz
# Source0-md5:	a21bf293f64ae4531ebcdb7be74b5415
URL:		http://datamining.anu.edu.au/~ole/pypar/
BuildRequires:	mpi
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-libs
BuildRequires:	python-Numeric-devel
BuildRequires:	python-numarray-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pypar is an efficient but easy-to-use module that allows
programs/scripts written in the Python programming language to run in
parallel on multiple processors and communicate using message passing.
Pypar provides bindings to an important subset of the message passing
interface standard MPI.

%description -l pl
Pypar to sprawny, lecz ³atwy w u¿yciu modu³ pozwalaj±cy programom i
skrtyptom napisanym w jêzyku programowania Python dzia³aæ równolegle
na wielu procesorach i komunikowaæ siê przy u¿yciu przekazywania
komunikatów. Pypar udostêpnia dowi±zania do istotnego podzbioru
standardu interfejsu przekazywania komunikatów MPI.

%package examples
Summary:	Example programs for Python pypar module
Summary(pl):	Programy przyk³adowe do modu³u Pythona pypar
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Python pypar module.

%description examples -l pl
Pakiet zawieraj±cy programy przyk³adowe dla modu³u Pythona pypar.

%prep
%setup -q -n %{module}_%{_vername}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
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

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
