Summary:	Network audit tools
Summary(pl):	Narz�dzia do kontroli sieci
Name:		dsniff
Version:	2.3
Release:	8
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.monkey.org/~dugsong/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-slist.patch
Patch1:		%{name}-headers.patch
Patch2:		%{name}-ac.patch
#ggsniff 1.2 from http://ggsniff.sourceforge.net/
Patch3:		%{name}-gg.patch
URL:		http://www.monkey.org/~dugsong/
BuildRequires:	XFree86-devel
BuildRequires:	libpcap-devel
BuildRequires:	libnids-devel
BuildRequires:	libnet-devel
BuildRequires:	glibc-static
BuildRequires:	openssl-devel >= 0.9.7a
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools to audit network and to demonstrate the insecurity of cleartext
network protocols. Please do not abuse this software.

%description -l pl
Narz�dzia do kontroli sieci oraz demonstracji braku zabezpiecze� w
nieszyfrowanych protoko�ach sieciowych. Prosz� nie nadu�ywa� tego
oprogramowania.

%package webspy
Summary:	Network audit tools
Summary(pl):	Narz�dzia do kontroli sieci
Group:		Networking/Utilities
Requires:	%{name} = %{version}
Requires:	netscape-navigator

%description webspy
webspy sends URLs sniffed from a client to your local Netscape browser
for display, updated in real-time (as the target surfs, your browser
surfs along with them, automagically). Netscape must be running on
your local X display ahead of time.

%description webspy -l pl
webspy przesy�a pods�uchane URLe do wy�wietlenia w lokalnie
uruchomionej przegl�darce Netscape Navigator. Adresy s� uaktualniane
na bie��co (a wi�c przegl�dasz strony r�wnolegle z pods�uchiwanym).
Netscape musi by� wcze�niej uruchomiony na lokalnym serwerze X.

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
