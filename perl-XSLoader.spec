%define	module XSLoader
%define	upstream_version 0.24

Name:		perl-%{module}
Version:	%{upstream_version}
Release:	2
Summary:	Dynamically load C libraries into Perl code
License:	GPLv1+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/module/XSLoader
Source0:	https://cpan.metacpan.org/authors/id/S/SA/SAPER/XSLoader-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More) >= 0.470.0
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Test::Portability::Files)
BuildRequires:	perl(Test::Distribution)
BuildRequires:	perl-devel

%description
This module defines a standard simplified interface to the dynamic
linking mechanisms available on many platforms. Its primary purpose is
to implement cheap automatic dynamic loading of Perl modules.

For a more complicated interface, see DynaLoader. Many (most) features
of DynaLoader are not implemented in XSLoader, like for example the
dl_load_flags, not honored by XSLoader.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{_mandir}/man3/*
%{perl_vendorlib}/*
