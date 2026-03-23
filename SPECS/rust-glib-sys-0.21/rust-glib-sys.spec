# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name glib-sys
%global full_version 0.21.5
%global pkgname glib-sys-0.21

Name:           rust-glib-sys-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "glib-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:2d95e1a3a19ae464a7286e14af9a90683c64d70c02532d88d87ce95056af3e6c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.183
Requires:       crate(system-deps-7.0/default) >= 7.0.7
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/v2-58)
Provides:       crate(%{pkgname}/v2-60)
Provides:       crate(%{pkgname}/v2-62)
Provides:       crate(%{pkgname}/v2-64)
Provides:       crate(%{pkgname}/v2-66)
Provides:       crate(%{pkgname}/v2-68)
Provides:       crate(%{pkgname}/v2-70)
Provides:       crate(%{pkgname}/v2-72)
Provides:       crate(%{pkgname}/v2-74)
Provides:       crate(%{pkgname}/v2-76)
Provides:       crate(%{pkgname}/v2-78)
Provides:       crate(%{pkgname}/v2-80)
Provides:       crate(%{pkgname}/v2-82)
Provides:       crate(%{pkgname}/v2-84)
Provides:       crate(%{pkgname}/v2-86)

%description
Source code for takopackized Rust crate "glib-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
