# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name system-deps
%global full_version 7.0.7
%global pkgname system-deps-7.0

Name:           rust-system-deps-7.0
Version:        7.0.7
Release:        %autorelease
Summary:        Rust crate "system-deps"
License:        MIT OR Apache-2.0
URL:            https://github.com/gdesmott/system-deps
#!RemoteAsset:  sha256:48c8f33736f986f16d69b6cb8b03f55ddcad5c41acc4ccc39dd88e84aa805e7f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-expr-0.20/default) >= 0.20.7
Requires:       crate(cfg-expr-0.20/targets) >= 0.20.7
Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(pkg-config-0.3/default) >= 0.3.32
Requires:       crate(toml-0.9/parse) >= 0.9.12
Requires:       crate(toml-0.9/std) >= 0.9.12
Requires:       crate(version-compare-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "system-deps"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
