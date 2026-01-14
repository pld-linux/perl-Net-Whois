#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)

%define		pdir	Net
%define		pnam	Whois
Summary:	Net::Whois perl module
Summary(pl.UTF-8):	Moduł perla Net::Whois
Name:		perl-Net-Whois
Version:	1.9
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c461a0f8991d9df848f66c4189971af7
URL:		http://search.cpan.org/dist/Net-Whois/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Whois - Get and parse "whois" data from InterNIC.

%description -l pl.UTF-8
Net::Whois - wsparcie dla usługi "whois".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Net/Whois.pm
%{_mandir}/man3/*
