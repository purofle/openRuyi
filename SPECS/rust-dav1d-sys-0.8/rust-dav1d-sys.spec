# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dav1d-sys
%global full_version 0.8.3
%global pkgname dav1d-sys-0.8

Name:           rust-dav1d-sys-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "dav1d-sys"
License:        MIT
URL:            https://github.com/rust-av/dav1d-rs
#!RemoteAsset:  sha256:c3c91aea6668645415331133ed6f8ddf0e7f40160cd97a12d59e68716a58704b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.183
Requires:       crate(system-deps-7.0/default) >= 7.0.7
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "dav1d-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
