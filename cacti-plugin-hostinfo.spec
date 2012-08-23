%define		plugin hostinfo
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Plugin for Cacti -  Host info
Summary(pl.UTF-8):	Wtyczka do Cacti -  Host info
Name:		cacti-plugin-%{plugin}
Version:	0.2
Release:	7
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{plugin}-%{version}.zip
# Source0-md5:	e06cda8197ed5677d918737321528394
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	unzip
Requires:	cacti
Requires:	php(core) >= %{php_min_version}
Requires:	php(mysql)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Plugin for Cacti - This plugin will give you version information about
your Cacti server. It outputs everything from Web server information,
to PHP, MySQL, RRDtool, and SNMP versions. It will also give you the
information in BBCode format to easily allow you to post it to a
forum.

%description -l pl.UTF-8
Wtyczka do Cacti wyświetlająca informacje o serwerze na którym
uruchomiono cacti. Podaje wszystkie informacje począwszy od serwera
WWW, a kończąc na wersjach PHP, MySQL-a, RRDtoola i SNMP. Podaje także
informacje w formacie BBCode, umożliwiając łatwe wysłanie ich na
forum.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -p *.php $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{plugindir}
