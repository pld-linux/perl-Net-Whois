%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Whois
Summary:	Net::Whois perl module
Summary(pl):	Modu³ perla Net::Whois
Name:		perl-Net-Whois
Version:	1.9
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Whois - Get and parse "whois" data from InterNIC.

%description -l pl
Net::Whois - wsparcie dla us³ugi "whois".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Net/Whois.pm
%{_mandir}/man3/*
