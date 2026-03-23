# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name locale_config
%global full_version 0.3.0
%global pkgname locale-config-0.3

Name:           rust-locale-config-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "locale_config"
License:        MIT
URL:            https://github.com/rust-locale/locale_config/
#!RemoteAsset:  sha256:08d2c35b16f4483f6c26f0e4e9550717a2f6575bcd6f12a53ff0c490a94a6934
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1.0/default) >= 1.5.0
Requires:       crate(objc-0.2/default) >= 0.2.7
Requires:       crate(objc-foundation-0.1/default) >= 0.1.1
Requires:       crate(regex-1.0/default) >= 1.12.3
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/winnls) >= 0.3.9
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "locale_config"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
