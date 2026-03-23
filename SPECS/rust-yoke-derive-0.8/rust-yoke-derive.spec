# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name yoke-derive
%global full_version 0.8.1
%global pkgname yoke-derive-0.8

Name:           rust-yoke-derive-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "yoke-derive"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:b659052874eb698efe5b9e8cf382204678a0086ebf46982b79d6ca3182927e5d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/fold) >= 2.0.117
Requires:       crate(synstructure-0.13/default) >= 0.13.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "yoke-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
