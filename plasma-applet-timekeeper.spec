%define oname timekeeper
%define kdeid 159345

Summary:	Plasma applet that provides clock and calendar via steampunk interface
Name:		plasma-applet-%{oname}
Version:	0.5.1
Release:	1
License:	GPLv3+
Group:		Graphical desktop/KDE
Url:		http://kde-apps.org/content/show.php/Time+Keeper?content=%{kdeid}
Source0:	http://kde-apps.org/CONTENT/content-files/%{kdeid}-%{oname}-%{version}.plasmoid
BuildRequires:	imagemagick
BuildRequires:	kde4-macros
Requires:	kdebase4-runtime
Requires:	marble-common >= 4.10.5-2
Provides:	plasma-applet
BuildArch:	noarch

%description
Plasma applet that provides clock and calendar functions via steampunk
interface. It is written entirely in QML + JavaScript.

%files
%doc LICENSE.GPL3
%{_kde_appsdir}/plasma/plasmoids/%{oname}
%{_kde_iconsdir}/hicolor/*/apps/%{oname}.png
%{_kde_services}/%{oname}.desktop

#--------------------------------------------------------------------

%prep
%setup -q -c
find . -type f | xargs chmod 0644
sed -i 's;icon.png;%{oname};g' metadata.desktop

%build
# nothing

%install
mkdir -p %{buildroot}%{_kde_appsdir}/plasma/plasmoids/%{oname}
cp -r * %{buildroot}%{_kde_appsdir}/plasma/plasmoids/%{oname}/
install -D -m 644 metadata.desktop %{buildroot}%{_kde_services}/%{oname}.desktop

# install icons
for N in 16 32 48 64 96 128;
do
convert icon.png -resize ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_kde_iconsdir}/hicolor/${N}x${N}/apps/%{oname}.png
done
