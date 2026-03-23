# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fxhash
%global full_version 0.2.1
%global pkgname fxhash-0.2

Name:           rust-fxhash-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "fxhash"
License:        Apache-2.0/MIT
URL:            https://github.com/cbreeden/fxhash
#!RemoteAsset:  sha256:c31b6d751ae2c7f11320402d34e41349dd1016f8d5d45e48c4312bc8625af50c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1.0/default) >= 1.5.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "fxhash"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
