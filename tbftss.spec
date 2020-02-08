Name:           tbftss
Version:        1.5.1
Release:        1
Summary:        The Battle for the Solar System: The Pandoran War
Group:          Games/Shooter
# Nonfree due to the NC clause on art assets
License:        GPLv2+ and CC-BY-NC-SA 3.0
URL:            https://www.battleforthesolarsystem.com/games/pw
Source0:        https://www.battleforthesolarsystem.com/downloads/%{name}-%{version}.src.tar.gz
#or mirror:	ttps://github.com/stephenjsweeney/tbftss/

BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)

%description
The Pandoran War is a 2D mission-based space shooter set in the universe
of the space opera novel trilogy 'The Battle for the Solar System'.
The game features many missions, with many different objectives and craft.

%prep
%setup -qn build
cd %{name}-%{version}

%build
%set_build_flags
%make_build \
    DATA_DIR=%{_gamesdatadir}/%{name}

%install
%make_install \
    BIN_DIR=%{_gamesbindir} \
    DATA_DIR=%{_gamesdatadir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc README.md README_DEV.md
%{_datadir}/applications/%{name}.desktop
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}/
%{_iconsdir}/hicolor/*/apps/%{name}.png 
