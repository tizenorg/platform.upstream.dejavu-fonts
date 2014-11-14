%define _fontsdir               %{_datadir}/fonts
%define _ttffontsdir            %{_fontsdir}/truetype
%define _miscfontsdir           %{_fontsdir}/misc
%define _fontsconfdir           %{_sysconfdir}/fonts
%define _fontsconfddir          %{_fontsconfdir}/conf.d
%define _fontsconfavaildir      %{_datadir}/%{name}/conf.avail

Name:           dejavu-fonts
Version:        2.33
Release:        0
License:        Bitstream Vera and Public Domain
Summary:        DejaVu Truetype Fonts
Url:            http://dejavu.sourceforge.net/
Group:          Graphics & UI Framework/Fonts
Source:         dejavu-fonts-ttf-%{version}.tar.bz2
Source1001: 	dejavu-fonts.manifest
BuildArch:      noarch

%description
The DejaVu fonts are a font family based on the Vera Fonts.
Its purpose is to provide a wider range of characters while
maintaining the original look and feel through the process
of collaborative development (see authors), under a Free license.

%prep
%setup -n %{name}-ttf-%{version}
cp %{SOURCE1001} .

%build

%install
mkdir -p %{buildroot}%{_ttffontsdir}/
install -m 0644 ttf/*.ttf %{buildroot}%{_ttffontsdir}/


%post
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{_ttffontsdir} || :
fi

%postun
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{_ttffontsdir} || :
fi

%files
%manifest %{name}.manifest
%defattr(-,root,root,755)
%license LICENSE
%{_ttffontsdir}/

