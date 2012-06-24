#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	chdir
Summary:	File::chdir - a more sensible way to change directories
Summary(pl):	File::chdir - rozs�dniejszy spos�b zmiany katalog�w
Name:		perl-File-chdir
Version:	0.06
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	41a4661789f6de97fb632e4560d37864
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::chdir module - a more sensible way to change directories.

Perl's chdir() has the unfortunate problem of being very, very, very
global. If any part of your program calls chdir() or if any library
you use calls chdir(), it changes the current working directory for
the whole program.

File::chdir gives you an alternative, $CWD and @CWD. These two
variables combine all the power of chdir(), File::Spec and Cwd.

%description -l pl
Modu� File::chdir - rozs�dniejszy spos�b zmiany katalog�w.

Perlowa funkcja chdir() jest problematyczna, poniewa� dzia�a bardzo,
bardzo, bardzo globalnie. Je�li dowolna cz�� programu lub dowolna
u�ywana biblioteka wywo�a chdir(), zmienia si� bie��cy katalog dla
ca�ego programu.

File::chdir daje alternatyw� - $CWD i @CWD. Te dwie zmienne ��cz� ca��
pot�g� chdir(), File::Spec i Cwd.

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
%doc Changes
%{perl_vendorlib}/File/chdir.pm
%{_mandir}/man3/*
