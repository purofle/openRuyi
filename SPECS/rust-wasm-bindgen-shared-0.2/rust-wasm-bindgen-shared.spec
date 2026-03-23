# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen-shared
%global full_version 0.2.114
%global pkgname wasm-bindgen-shared-0.2

Name:           rust-wasm-bindgen-shared-0.2
Version:        0.2.114
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen-shared"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen/
#!RemoteAsset:  sha256:75a326b8c223ee17883a4251907455a2431acc2791c98c26279376490c378c16
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-ident-1.0/default) >= 1.0.24
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wasm-bindgen-shared"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
