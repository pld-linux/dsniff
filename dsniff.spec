Summary:	Network audit tools.
Summary(pl):	Narzêdzia do kontroli sieci
Name:		dsniff
Version:	2.3
Release:	2
License:	BSD
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	http://www.monkey.org/~dugsong/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-slist.patch
Patch1:		%{name}-headers.patch
URL:		http://www.monkey.org/~dugsong/
BuildRequires:	XFree86-devel
BuildRequires:	libpcap-devel
BuildRequires:	libnids-devel
BuildRequires:	libnet-devel
BuildRequires:	XFree86-devel
BuildRequires:	glibc-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools to audit network and to demonstrate the insecurity of cleartext
network protocols. Please do not abuse this software.

%description -l -l
Narzêdzia do kontroli sieci oraz demonstracji braku zabezpieczeñ w
nieszyfrowanych protoko³ach sieciowych. Proszê nie nadu¿ywac tego
oprogramowania.

%package webspy
Summary:	Network audit tools.
Summary(pl):	Narzêdzia do kontroli sieci
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Requires:	%{name} = %{version}

%description webspy
webspy sends URLs sniffed from a client to your local Netscape browser
for display, updated in real-time (as the target surfs, your browser
surfs along with them, automag€ ically). Netscape must be running on
your local X display ahead of time.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoheader
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
%doc README*
%attr(755,root,root) %{_sbindir}/[a-u]*
%attr(755,root,root) %{_sbindir}/webmitm
%{_datadir}/%{name}/*
%{_mandir}/man8/[a-u]*
%{_mandir}/man8/webmitm*

%files webspy
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/webspy
%{_mandir}/man8/webspy*
