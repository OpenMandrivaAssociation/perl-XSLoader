%define upstream_name    XSLoader
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Dynamically load C libraries into Perl code
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: perl(Test::More)
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module defines a standard simplified interface to the dynamic
linking mechanisms available on many platforms. Its primary purpose is
to implement cheap automatic dynamic loading of Perl modules.

For a more complicated interface, see DynaLoader. Many (most) features
of DynaLoader are not implemented in XSLoader, like for example the
dl_load_flags, not honored by XSLoader.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

