Name:           autosubqt
Version:        0.1.1
Release:        1%{?dist}
Summary:        autosubqt
License:        Unlicense
URL:            https://github.com/vx32/autosubqt
Source0:        https://github.com/vx32/autosubqt/archive/refs/heads/main.tar.gz#/autosubqt-main.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel

Requires:       qt6-qtbase%{?_isa}

%description
autosubqt

%prep
%setup -q -n autosubqt-main

%conf
%cmake  \
  -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
  -DCMAKE_INSTALL_BINDIR=%{_bindir} \
  -DCMAKE_INSTALL_DATADIR=%{_datadir}

%build
%cmake_build

%install
%cmake_install

%files
%{_bindir}/autosubqt
%{_datadir}/applications/autosubqt.desktop

%changelog
* Sun May 10 2026 vx32 <x64wall@proton.me> - 0.1.1
- first
