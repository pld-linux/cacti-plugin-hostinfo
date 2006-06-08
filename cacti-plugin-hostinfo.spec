%define		namesrc	 hostinfo
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti -  Host info
Summary(pl):	Wtyczka do Cacti -  Host info
Name:		cacti-plugin-hostinfo
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/WWW
Source0:	http://download.cactiusers.org/downloads/%{namesrc}-%{version}.tar.gz
# Source0-md5:	b586fd6dc334381013f25bd19a63197b
URL:		http://www.cactiusers.org/
#BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - This plugin will give you version information about
your Cacti server. It outputs everything from Web server information,
to PHP, MySQL, RRDtool, and SNMP versions. It will also give you the
information in BBCode format to easily allow you to post it to a
forum.

%description -l pl
Wtyczka do Cacti wy¶wietlaj±ca informacje o serwerze na którym
uruchomiono cacti. Podaje wszystkie informacje pocz±wszy od serwera
WWW, a koñcz±c na wersjach PHP, MySQL-a, RRDtoola i SNMP. Podaje tak¿e
informacje w formacie BBCode, umo¿liwiaj±c ³atwe wys³anie ich na
forum.

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{webcactipluginroot}
