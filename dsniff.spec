Summary:	Network audit tools.
Name:		dsniff
Version:	2.2
Release:	1
License:	BSD
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
URL:		http://www.monkey.org/~dugsong/
Source0:	http://www.monkey.org/~dugsong/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	XFree86-devel
BuildRequires:	libpcap-devel
BuildRequires:	libnids-devel
BuildRequires:	libnet-devel
BuildConflicts:	cyrus-sasl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools to audit network and to demonstrate the insecurity of cleartext
network protocols.
please do not abuse this software.

%prep
%setup -q

%build
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
