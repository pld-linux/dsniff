Summary:	Network audit tools
Summary(pl):	Narzêdzia do kontroli sieci
Name:		dsniff
Version:	2.3
Release:	5
License:	BSD
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	http://www.monkey.org/~dugsong/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-slist.patch
Patch1:		%{name}-headers.patch
URL:		http://www.monkey.org/~dugsong/
BuildRequires:	XFree86-devel
BuildRequires:	libpcap-devel
BuildRequires:	libnids-devel
BuildRequires:	libnet-devel
BuildRequires:	glibc-static
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools to audit network and to demonstrate the insecurity of cleartext
network protocols. Please do not abuse this software.

%description -l pl
Narzêdzia do kontroli sieci oraz demonstracji braku zabezpieczeñ w
nieszyfrowanych protoko³ach sieciowych. Proszê nie nadu¿ywac tego
oprogramowania.

%package webspy
Summary:	Network audit tools
Summary(pl):	Narzêdzia do kontroli sieci
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Requires:	%{name} = %{version}
Requires:	netscape-navigator

%description webspy
webspy sends URLs sniffed from a client to your local Netscape browser
for display, updated in real-time (as the target surfs, your browser
surfs along with them, automagically). Netscape must be running on
your local X display ahead of time.

%description -l pl webspy
webspy przesy³a pods³uchane URLe do wy¶wietlenia w lokalnie
uruchomionej przegl±darce Netscape Navigator. Adresy s± uaktualniane
na bierz±co (a wiêc przegl±dasz strony równolegle z pods³uchiwanym).
Netscape musi byæ wcze¶niej uruchomiony na lokalnym serwerze X.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoheader
aclocal
autoconf
CFLAGS="%{rpmcflags} -I./missing"
%configure \
	--libdir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	install_prefix=$RPM_BUILD_ROOT

gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/[a-u]*
%attr(755,root,root) %{_sbindir}/webmitm
%{_datadir}/%{name}
%{_mandir}/man8/[a-u]*
%{_mandir}/man8/webmitm*

%files webspy
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/webspy
%{_mandir}/man8/webspy*
