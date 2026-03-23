# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name safe_arch
%global full_version 0.7.4
%global pkgname safe-arch-0.7

Name:           rust-safe-arch-0.7
Version:        0.7.4
Release:        %autorelease
Summary:        Rust crate "safe_arch"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/Lokathor/safe_arch
#!RemoteAsset:  sha256:96b02de82ddbe1b636e6170c21be622223aea188ef2e139be0a5b219ec215323
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "safe_arch"

%package     -n %{name}+bytemuck
Summary:        Crate that exposes `core::arch` safely via `#[cfg()]` - feature "bytemuck"
Requires:       crate(%{pkgname})
Requires:       crate(bytemuck-1.0/default) >= 1.25.0
Provides:       crate(%{pkgname}/bytemuck)

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust safe_arch crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+bytemuck

%changelog
%{?autochangelog}
