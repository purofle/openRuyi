# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name string_cache_codegen
%global full_version 0.5.4
%global pkgname string-cache-codegen-0.5

Name:           rust-string-cache-codegen-0.5
Version:        0.5.4
Release:        %autorelease
Summary:        Rust crate "string_cache_codegen"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/string-cache
#!RemoteAsset:  sha256:c711928715f1fe0fe509c53b43e993a9a557babc2d0a3567d0a3006f1ac931a0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-generator-0.11/default) >= 0.11.3
Requires:       crate(phf-shared-0.11/default) >= 0.11.3
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "string_cache_codegen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
