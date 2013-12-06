Summary:	Command-line utilities to encode, inspect, and decode .opus files
Summary(pl.UTF-8):	Narzędzia linii poleceń do kodowania, badania i dekodowania plików .opus
Name:		opus-tools
Version:	0.1.8
Release:	1
License:	BSD
Group:		Applications/Sound
Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
# Source0-md5:	b424790eda9357a4df394e2d7ca19eac
URL:		http://opus-codec.org/
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	libogg-devel >= 2:1.3
# for noinst opusrtc only
#BuildRequires:	libpcap-devel
BuildRequires:	opus-devel >= 1.0.3
BuildRequires:	pkgconfig
Requires:	flac >= 1.1.3
Requires:	libogg >= 2:1.3
Requires:	opus >= 1.0.3
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
