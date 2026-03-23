# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mac
%global full_version 0.1.1
%global pkgname mac-0.1

Name:           rust-mac-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "mac"
License:        MIT/Apache-2.0
URL:            https://github.com/reem/rust-mac.git
#!RemoteAsset:  sha256:c41e0c4fef86961ac6d6f8a82609f55f31b05e4fce149ac5710e439df7619ba4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "mac"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
