Summary:	An OpenGL and SDL based action flight simulator
Summary(de.UTF-8):   Ein OpenGL- und SDL-basierter Flugsimulator
Summary(pl.UTF-8):   Zręcznościowy symulator lotu używający OpenGL i SDL
Name:		gl-117
Version:	1.3.2
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-src.tar.bz2
# Source0-md5:	aad53c5531943529fd769fae4efeae02
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://home.t-online.de/home/Primetime./gl-117/gl-117.htm
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	glut-devel
BuildRequires:	libstdc++-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
GL-117 is an OpenGL and SDL-based action flight simulator written in
C++. It provides a random terrain generator, lighting effects, sounds,
and joystick support. Predefined levels of video quality and an amount
of viewing ranges let you perfectly adjust the game to the performance
of your system.

%description -l de.UTF-8
GL-117 ist ein in C++ entwickelter, OpenGL- und SDL-basierter
Action-Flugsimulator. Neben per Zufall erzeugten Landschaften besticht
das Spiel durch Lichteffekte, Sound und Joystickunterstützung. Anhand
vordefinierter Qualitätsstufen lässt sich die Grafik optimal an die
Leistung des eigenen Systems anpassen.

%description -l pl.UTF-8
GL-117 jest zręcznościowym symulatorem lotu napisanym w C++,
wykorzystującym biblioteki OpenGL i SDL. Posiada obsługę joysticka,
dźwięk, losowo generowany teren, efekty świetlne. Predefiniowane
poziomy jakości obrazu oraz szeroki zakres ustawień widoczności
pozwalają idealnie dopasować grę do wydajności systemu.

%prep
%setup -q -n %{name}-%{version}-src

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man6,%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install doc/*.6 $RPM_BUILD_ROOT%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README doc/gl-117.pdf
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
