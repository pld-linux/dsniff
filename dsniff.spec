# TODO
# - make R: firefox something generic (it uses X11 and remote.c to find
#   browser window to send openURL(%s, %s) command there)
%define		rel	31
Summary:	Network audit tools
Summary(pl.UTF-8):	Narzędzia do kontroli sieci
Name:		dsniff
Version:	2.4
Release:	0.b1.%{rel}
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.monkey.org/~dugsong/dsniff/beta/%{name}-%{version}b1.tar.gz
# Source0-md5:	2f761fa3475682a7512b0b43568ee7d6
Patch0:		debian.patch
Patch1:		%{name}-libdir.patch
Patch2:		%{name}-nolibs.patch
Patch3:		pcap.patch
Patch4:		rpc.patch
# ggsniff 1.2 from http://ggsniff.sourceforge.net/
#Patch3:	%{name}-gg.patch
URL:		http://www.monkey.org/~dugsong/dsniff/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	db-devel
BuildRequires:	glibc-static
BuildRequires:	libnet-devel >= 1:1.1
BuildRequires:	libnids-devel
BuildRequires:	libnsl-devel
BuildRequires:	libpcap-devel
BuildRequires:	libtirpc-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpcsvc-proto
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools to audit network and to demonstrate the insecurity of cleartext
network protocols. Please do not abuse this software.

%description -l pl.UTF-8
Narzędzia do kontroli sieci oraz demonstracji braku zabezpieczeń w
nieszyfrowanych protokołach sieciowych. Proszę nie nadużywać tego
oprogramowania.

%package webspy
Summary:	Network audit tools
Summary(pl.UTF-8):	Narzędzia do kontroli sieci
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Requires:	firefox

%description webspy
webspy sends URLs sniffed from a client to your local Firefox browser
for display, updated in real-time (as the target surfs, your browser
surfs along with them, automagically). Firefox must be running on your
local X display ahead of time.

%description webspy -l pl.UTF-8
webspy przesyła podsłuchane URL-e do wyświetlenia w lokalnie
uruchomionej przeglądarce Firefox. Adresy są uaktualniane na bieżąco
(a więc przegląda się strony równolegle z podsłuchiwanym). Firefox
musi być wcześniej uruchomiony na lokalnym serwerze X.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%{__rm} configure

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--libdir=%{_datadir}/%{name}

# don't build libmissing.a with progs in parallel 
%{__make} libmissing.a
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	install_prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README TODO
%attr(755,root,root) %{_sbindir}/arpspoof
%attr(755,root,root) %{_sbindir}/dnsspoof
%attr(755,root,root) %{_sbindir}/dsniff
%attr(755,root,root) %{_sbindir}/filesnarf
%attr(755,root,root) %{_sbindir}/macof
%attr(755,root,root) %{_sbindir}/mailsnarf
%attr(755,root,root) %{_sbindir}/msgsnarf
%attr(755,root,root) %{_sbindir}/sshmitm
%attr(755,root,root) %{_sbindir}/sshow
%attr(755,root,root) %{_sbindir}/tcpkill
%attr(755,root,root) %{_sbindir}/tcpnice
%attr(755,root,root) %{_sbindir}/urlsnarf
%attr(755,root,root) %{_sbindir}/webmitm
%{_datadir}/%{name}
%{_mandir}/man8/arpspoof.8*
%{_mandir}/man8/dnsspoof.8*
%{_mandir}/man8/dsniff.8*
%{_mandir}/man8/filesnarf.8*
%{_mandir}/man8/macof.8*
%{_mandir}/man8/mailsnarf.8*
%{_mandir}/man8/msgsnarf.8*
%{_mandir}/man8/sshmitm.8*
%{_mandir}/man8/sshow.8*
%{_mandir}/man8/tcpkill.8*
%{_mandir}/man8/tcpnice.8*
%{_mandir}/man8/urlsnarf.8*
%{_mandir}/man8/webmitm.8*

%files webspy
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/webspy
%{_mandir}/man8/webspy.8*
