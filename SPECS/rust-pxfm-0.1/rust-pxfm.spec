# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pxfm
%global full_version 0.1.28
%global pkgname pxfm-0.1

Name:           rust-pxfm-0.1
Version:        0.1.28
Release:        %autorelease
Summary:        Rust crate "pxfm"
License:        BSD-3-Clause OR Apache-2.0
URL:            https://github.com/awxkee/pxfm
#!RemoteAsset:  sha256:b5a041e753da8b807c9255f28de81879c78c876392ff2469cde94799b2896b9d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "pxfm"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
