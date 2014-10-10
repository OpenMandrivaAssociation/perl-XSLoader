%define	module	XSLoader
%define	upstream_version 0.15

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Dynamically load C libraries into Perl code
License:	GPLv1+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module//%{module}-%{upstream_version}.tar.gz
BuildArch:	noarch
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


%changelog
* Wed Feb 01 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.150.0-3
+ Revision: 770500
- package is noarch
- update version
- new version
- clean spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for perl 5.12

* Sun Jul 26 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 400260
- rebuild without noarch
- using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10-3mdv2010.0
+ Revision: 375885
- rebuild

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10-2mdv2010.0
+ Revision: 372459
- provide description / summary

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10-1mdv2010.0
+ Revision: 372424
- import perl-XSLoader


* Wed May 06 2009 cpan2dist 0.10-1mdv
- initial mdv release, generated with cpan2dist

