# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gobject-sys
%global full_version 0.21.5
%global pkgname gobject-sys-0.21

Name:           rust-gobject-sys-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "gobject-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:2dca35da0d19a18f4575f3cb99fe1c9e029a2941af5662f326f738a21edaf294
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glib-sys-0.21/default) >= 0.21.5
Requires:       crate(libc-0.2/default) >= 0.2.183
Requires:       crate(system-deps-7.0/default) >= 7.0.7
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/v2-58)
Provides:       crate(%{pkgname}/v2-62)
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
Source code for takopackized Rust crate "gobject-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
