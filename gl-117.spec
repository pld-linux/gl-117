Summary:	An OpenGL and SDL based action flight simulator
Summary(de):	Ein OpenGL- und SDL-basierter Flugsimulator
Summary(pl):	Zrêczno¶ciowy symulator lotu u¿ywaj±cy OpenGL i SDL
Name:		gl-117
Version:	1.0.1
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
# Source0-md5:	95ac2ff4fc65070a28c670c67bb7a376
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://home.t-online.de/home/Primetime./gl-117/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
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

%description -l de
GL-117 ist ein in C++ entwickelter, OpenGL- und SDL-basierter
Action-Flugsimulator. Neben per Zufall erzeugten Landschaften besticht
das Spiel durch Lichteffekte, Sound und Joystickunterstützung. Anhand
vordefinierter Qualitätsstufen lässt sich die Grafik optimal an die
Leistung des eigenen Systems anpassen.

%description -l pl
GL-117 jest zrêczno¶ciowym symulatorem lotu napisanym w C++,
wykorzystuj±cym biblioteki OpenGL i SDL. Posiada obs³ugê joysticka,
d¼wiêk, losowo generowany teren, efekty ¶wietlne. Predefiniowane
poziomy jako¶ci obrazu oraz szeroki zakres ustawieñ widoczno¶ci
pozwalaj± idealnie dopasowaæ grê do wydajno¶ci systemu.

%prep
%setup -q -n %{name}-%{version}-src

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
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
%doc AUTHORS ChangeLog NEWS README doc/gl-117.pdf
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
