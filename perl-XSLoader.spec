%define	module	XSLoader
%define	upstream_version 0.15

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Dynamically load C libraries into Perl code
License:	GPLv1+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module//%{module}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
