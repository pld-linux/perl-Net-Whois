%define	pdir	Net
%define	pnam	Whois
%include	/usr/lib/rpm/macros.perl
Summary:	Net-Whois perl module
Summary(pl):	Modu� perla Net-Whois
Name:		perl-Net-Whois
Version:	1.9
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Whois - Get and parse "whois" data from InterNIC.

%description -l pl
Net-Whois - wsparcie dla us�ugi "whois".

%prep
%setup -q -n Net-Whois-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Net/Whois.pm
%{_mandir}/man3/*
