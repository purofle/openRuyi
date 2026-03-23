# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc-foundation
%global full_version 0.1.1
%global pkgname objc-foundation-0.1

Name:           rust-objc-foundation-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "objc-foundation"
License:        MIT
URL:            http://github.com/SSheldon/rust-objc-foundation
#!RemoteAsset:  sha256:1add1b659e36c9607c7aab864a76c7a4c2760cd0cd2e120f3fb8b952c7e22bf9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(block-0.1/default) >= 0.1.6
Requires:       crate(objc-0.2/default) >= 0.2.7
Requires:       crate(objc-id-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "objc-foundation"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
