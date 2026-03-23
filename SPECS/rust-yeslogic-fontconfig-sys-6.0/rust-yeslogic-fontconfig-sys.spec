# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yeslogic-fontconfig-sys
%global full_version 6.0.0
%global pkgname yeslogic-fontconfig-sys-6.0

Name:           rust-yeslogic-fontconfig-sys-6.0
Version:        6.0.0
Release:        %autorelease
Summary:        Rust crate "yeslogic-fontconfig-sys"
License:        MIT
URL:            https://github.com/yeslogic/fontconfig-rs
#!RemoteAsset:  sha256:503a066b4c037c440169d995b869046827dbc71263f6e8f3be6d77d4f3229dbd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dlib-0.5/default) >= 0.5.3
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Requires:       crate(pkg-config-0.3/default) >= 0.3.32
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/dlopen)

%description
Source code for takopackized Rust crate "yeslogic-fontconfig-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
