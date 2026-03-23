# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pango-sys
%global full_version 0.21.5
%global pkgname pango-sys-0.21

Name:           rust-pango-sys-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "pango-sys"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:b4f06627d36ed5ff303d2df65211fc2e52ba5b17bf18dd80ff3d9628d6e06cfd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glib-sys-0.21/default) >= 0.21.5
Requires:       crate(gobject-sys-0.21/default) >= 0.21.5
Requires:       crate(libc-0.2/default) >= 0.2.183
Requires:       crate(system-deps-7.0/default) >= 7.0.7
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/v1-42)
Provides:       crate(%{pkgname}/v1-44)
Provides:       crate(%{pkgname}/v1-46)
Provides:       crate(%{pkgname}/v1-48)
Provides:       crate(%{pkgname}/v1-50)
Provides:       crate(%{pkgname}/v1-52)
Provides:       crate(%{pkgname}/v1-54)
Provides:       crate(%{pkgname}/v1-56)
Provides:       crate(%{pkgname}/v1-57)

%description
Source code for takopackized Rust crate "pango-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
