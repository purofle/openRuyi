# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gio-sys
%global full_version 0.21.5
%global pkgname gio-sys-0.21

Name:           rust-gio-sys-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "gio-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:0071fe88dba8e40086c8ff9bbb62622999f49628344b1d1bf490a48a29d80f22
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glib-sys-0.21/default) >= 0.21.5
Requires:       crate(gobject-sys-0.21/default) >= 0.21.5
Requires:       crate(libc-0.2/default) >= 0.2.183
Requires:       crate(system-deps-7.0/default) >= 7.0.7
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.2
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
Source code for takopackized Rust crate "gio-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
