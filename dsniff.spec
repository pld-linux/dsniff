Summary:	Network audit tools
Summary(pl):	Narzêdzia do kontroli sieci
Name:		dsniff
Version:	2.4
Release:	0.b1.7
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.monkey.org/~dugsong/dsniff/beta/%{name}-%{version}b1.tar.gz
# Source0-md5:	2f761fa3475682a7512b0b43568ee7d6
Patch0:		%{name}-ac.patch
Patch1:		%{name}-libnet1.patch
Patch2:		%{name}-clk_tck.patch
Patch3:		%{name}-openssl-0.9.8.patch
#ggsniff 1.2 from http://ggsniff.sourceforge.net/
#Patch3:		%{name}-gg.patch
URL:		http://www.monkey.org/~dugsong/dsniff/
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	glibc-static
BuildRequires:	libnet1-devel
BuildRequires:	libnids-devel
BuildRequires:	libpcap-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools to audit network and to demonstrate the insecurity of cleartext
network protocols. Please do not abuse this software.

%description -l pl
Narzêdzia do kontroli sieci oraz demonstracji braku zabezpieczeñ w
nieszyfrowanych protoko³ach sieciowych. Proszê nie nadu¿ywaæ tego
oprogramowania.

%package webspy
Summary:	Network audit tools
Summary(pl):	Narzêdzia do kontroli sieci
Group:		Networking/Utilities
Requires:	%{name} = %{version}-%{release}
Requires:	mozilla

%description webspy
webspy sends URLs sniffed from a client to your local Mozilla browser
for display, updated in real-time (as the target surfs, your browser
surfs along with them, automagically). Mozilla must be running on
your local X display ahead of time.

%description webspy -l pl
webspy przesy³a pods³uchane URL-e do wy¶wietlenia w lokalnie
uruchomionej przegl±darce Mozilla. Adresy s± uaktualniane na bie¿±co
(a wiêc przegl±da siê strony równolegle z pods³uchiwanym). Mozilla
musi byæ wcze¶niej uruchomiona na lokalnym serwerze X.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__autoheader}
%{__aclocal}
%{__autoconf}
CFLAGS="%{rpmcflags} -I./missing"
%configure \
	--libdir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	install_prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_sbindir}/[a-u]*
%attr(755,root,root) %{_sbindir}/webmitm
%{_datadir}/%{name}
%{_mandir}/man8/[a-u]*
%{_mandir}/man8/webmitm*

%files webspy
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/webspy
%{_mandir}/man8/webspy*
