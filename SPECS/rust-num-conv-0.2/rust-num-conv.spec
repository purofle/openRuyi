# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-conv
%global full_version 0.2.0
%global pkgname num-conv-0.2

Name:           rust-num-conv-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "num-conv"
License:        MIT OR Apache-2.0
URL:            https://github.com/jhpratt/num-conv
#!RemoteAsset:  sha256:cf97ec579c3c42f953ef76dbf8d55ac91fb219dde70e49aa4a6b7d74e9919050
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
This provides better certainty when refactoring, makes the exact behavior of code more explicit, and allows using turbofish syntax.
Source code for takopackized Rust crate "num-conv"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
