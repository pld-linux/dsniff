Summary:	Network audit tools.
Summary(pl):	Narz�dzia do kontroli sieci.
Name:		dsniff
Version:	2.3
Release:	1
License:	BSD
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narz�dzia
URL:		http://www.monkey.org/~dugsong/
Source0:	http://www.monkey.org/~dugsong/%{name}/%{name}-%{version}.tar.gz
Patch0:		dsniff-slist.patch
BuildRequires:	XFree86-devel
BuildRequires:	libpcap-devel
BuildRequires:	libnids-devel
BuildRequires:	libnet-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools to audit network and to demonstrate the insecurity of cleartext
network protocols. Please do not abuse this software.

%description -l -l
Narz�dzia do kontroli sieci oraz demonstracji braku zabezpiecze�
w nieszyfrowanych protoko�ach sieciowych. Prosz� nie nadu�ywac tego
oprogramowania.

%prep
%setup -q
%patch0 -p1

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
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/%{name}/*
%{_mandir}/man8/*
