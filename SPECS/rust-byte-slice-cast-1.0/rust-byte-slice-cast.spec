# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name byte-slice-cast
%global full_version 1.2.3
%global pkgname byte-slice-cast-1.0

Name:           rust-byte-slice-cast-1.0
Version:        1.2.3
Release:        %autorelease
Summary:        Rust crate "byte-slice-cast"
License:        MIT
URL:            https://github.com/sdroege/bytes-num-slice-cast
#!RemoteAsset:  sha256:7575182f7272186991736b70173b0ea045398f984bf5ebbb3804736ce1330c9d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "byte-slice-cast"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
