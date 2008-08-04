#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Searcher for Man pages
Summary(pl.UTF-8):	Wyszukiwarka stron Man
Name:		Sman
Version:	1.03
Release:	0.1
# "same as perl"
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://joshr.com/src/sman/%{name}-%{version}.tar.gz
# Source0-md5:	41fe1c4eaa94d24f1f906ef1f967ea72
URL:		http://joshr.com/src/sman/
BuildRequires:	perl-Cache-Cache
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	swish-e-perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sman is the Searcher for Man pages. Based on the example of the same
name in Josh Rabinowitz's article "How To Index Anything" in the July,
2003 issue of Linux Journal
<http://www.linuxjournal.com/article.php?sid=6652>, sman is an
enhanced version of 'apropos' and 'man -k'. Sman adds several key
abilities over its predecessors:

- Supports complex natural language text searches such as "(linux and
  kernel) or (mach and microkernel)"

- Shows results in a ranked order, and optionally an extract (using
  -e) of the manpage showing the searched text highlighted

- Allows for searches by manpage section, title, body, or filename
  (use 'metaname=searchword')

- Indexes the complete contents of the man page, not just the title
  and description

- Uses a prebuilt index to perform fast searches

- Performs 'stemming' so that a search for "searches" will match a
  document with the word "searching"

%description -l pl.UTF-8
Sman to wyszukiwarka stron Man. Jest to rozszerzona wersja 'apropos' i
'man -k' oparta na przykładzie o tej samej nazwie z artykułu Josha
Rabinowitza "How To Index Anything" ("Jak indeksować cokolwiek") w
numerze Linux Journal z czerwca 2003
<http://www.linuxjournal.com/article.php?sid=6652>. Sman dodaje kilka
kluczowych możliwości, których nie mają poprzednicy:

- obsługuje złożone wyszukiwania tekstu w języku naturalnym, takie jak
  "(linux and kernel) or (mach and microkernel)"

- pokazuje wyniki w kolejności punktacji i opcjonalnie wyciąg ze
  strony (przy użyciu -e) z podświetleniem wyszukiwanego tekstu

- pozwala na wyszukiwanie po sekcji, tytule, ciele i nazwie pliku
  strony (przy użyciu 'nazwa-meta=szukane-słowo')

- indeksuje całą zawartość stron man, a nie tylko tytuł i opis

- używa wcześniej zbudowanego indeksu w celu szybszego wyszukiwania

- wykonuje "stemming", przez co np. wyszukiwanie słowa "searches"
  znajdzie dokument ze słowem "searching"

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%attr(755,root,root) %{_bindir}/sman
%attr(755,root,root) %{_bindir}/sman-update
%{perl_vendorlib}/Sman.pm
%dir %{perl_vendorlib}/Sman
%{perl_vendorlib}/Sman/Autoconfig.pm
%{perl_vendorlib}/Sman/Config.pm
%dir %{perl_vendorlib}/Sman/Man
%{perl_vendorlib}/Sman/Man/Cache.pm
%dir %{perl_vendorlib}/Sman/Man/Cache
%{perl_vendorlib}/Sman/Man/Cache/DB_File.pm
%{perl_vendorlib}/Sman/Man/Cache/FileCache.pm
%{perl_vendorlib}/Sman/Man/Convert.pm
%{perl_vendorlib}/Sman/Man/Find.pm
%{perl_vendorlib}/Sman/Swishe.pm
%{perl_vendorlib}/Sman/Util.pm
%{perl_vendorlib}/Sman/IndexVersion.pm
%{perl_vendorlib}/Sman/sman.conf.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
