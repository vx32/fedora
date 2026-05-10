Name:           autosub
Version:        0.1.1
Release:        1%{?dist}
Summary:        autosub
License:        Unlicense
URL:            https://github.com/vx32/autosub
Source0:        https://github.com/vx32/autosub/archive/refs/heads/main.tar.gz#/autosub-main.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  libcurl-devel

Requires:       libcurl

%description
autosub

%prep
%setup -q -n autosub-main

%conf
%cmake  \
  -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
  -DCMAKE_INSTALL_BINDIR=%{_bindir} 

%build
%cmake_build

%install
%cmake_install

%files
%{_bindir}/autosub
%config(noreplace) %{_sysconfdir}/autosub/

%changelog
* Sun May 10 2026 vx32 <x64wall@proton.me> - 0.1.1
- first
