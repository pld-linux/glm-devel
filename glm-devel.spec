# NOTE: there used to be a different 'glm' package,
#	it has been moved to 'devernay-glm'

# Conditional build:
%bcond_without	tests		# build without tests

Summary:	OpenGL Mathematics library
Name:		glm-devel
Version:	0.9.7.3
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://github.com/g-truc/glm/releases/download/%{version}/glm-%{version}.7z
# Source0-md5:	7de0a61696cc25969fef84aa1ba627b8
URL:		http://glm.g-truc.net/
%if %{with tests}
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenGL Mathematics (GLM) is a header only C++ mathematics library for
graphics software based on the OpenGL Shading Language (GLSL)
specifications.

GLM provides classes and functions designed and implemented with the
same naming conventions and functionalities than GLSL so that anyone
who knows GLSL, can use GLM as well in C++.

This project isn't limited to GLSL features. An extension system,
based on the GLSL extension conventions, provides extended
capabilities: matrix transformations, quaternions, data packing,
random numbers, noise, etc...

%prep
%setup -qn glm

%build
%if %{with tests}
install -d build
cd build
%{__cmake} \
	-DGLM_TEST_ENABLE=ON \
	../

%{__make}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

cp -pR glm $RPM_BUILD_ROOT%{_includedir}/glm

find $RPM_BUILD_ROOT%{_includedir}/glm -name CMakeLists.txt | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.md copying.txt doc
%{_includedir}/glm
