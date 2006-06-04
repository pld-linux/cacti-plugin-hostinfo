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
Plugin for Cacti - This plugin displays information about your Host for
use in Bug Reports.

%description -l pl
Wtyczka do Cacti wy¶wietlaj±ca informacje o urz±dzeniu.

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
