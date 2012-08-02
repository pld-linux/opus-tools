Summary:	Command-line utilities to encode, inspect, and decode .opus files
Summary(pl.UTF-8):	Narzędzia linii poleceń do kodowania, badania i dekodowania plików .opus
Name:		opus-tools
Version:	0.1.4
Release:	1
License:	BSD
Group:		Applications/Sound
Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
# Source0-md5:	82dddc3482f066f2f84557fc643b2b09
URL:		http://opus-codec.org/
BuildRequires:	libogg-devel >= 2:1.3
BuildRequires:	opus-devel >= 0.9.10
BuildRequires:	pkgconfig
Requires:	libogg >= 2:1.3
Requires:	opus >= 0.9.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides command-line utilities to encode, inspect, and
decode .opus files.

%description -l pl.UTF-8
Ten pakiet zawiera działające z linii poleceń narzędzia do kodowania,
badania i dekodowania plików .opus.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/opusdec
%attr(755,root,root) %{_bindir}/opusenc
%attr(755,root,root) %{_bindir}/opusinfo
%{_mandir}/man1/opusdec.1*
%{_mandir}/man1/opusenc.1*
%{_mandir}/man1/opusinfo.1*
