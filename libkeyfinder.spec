# TODO: catch2 v3 for TESTING
Summary:	Library for estimating the musical key of digital audio
Summary(pl.UTF-8):	Biblioteka do określania klucza muzyczego dźwięku cyfrowego
Name:		libkeyfinder
Version:	2.2.8
Release:	1
License:	GPL v3+
Group:		Libraries
#Source0Download: https://github.com/mixxxdj/libkeyfinder/releases
Source0:	https://github.com/mixxxdj/libkeyfinder/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	249b537b91ad55c32459ba8624e51930
Patch0:		%{name}-fftw3.patch
URL:		https://github.com/mixxxdj/libkeyfinder
BuildRequires:	cmake >= 3.5
BuildRequires:	fftw3-devel >= 3
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libkeyfinder is a small C++11 library for estimating the musical key
of digital audio.

%description -l pl.UTF-8
libkeyfinder to mała biblioteka C++11 do określania klucza muzycznego
dźwięku cyfrowego.

%package devel
Summary:	Header files for libkeyfinder library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libkeyfinder
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fftw3-devel >= 3
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for libkeyfinder library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libkeyfinder.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	-DBUILD_TESTING=OFF

%{__make}
%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_libdir}/libkeyfinder.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkeyfinder.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkeyfinder.so
%{_includedir}/keyfinder
%{_pkgconfigdir}/libkeyfinder.pc
%{_libdir}/cmake/KeyFinder
