# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dlib
%global full_version 0.5.3
%global pkgname dlib-0.5

Name:           rust-dlib-0.5
Version:        0.5.3
Release:        %autorelease
Summary:        Rust crate "dlib"
License:        MIT
URL:            https://github.com/elinorbgr/dlib
#!RemoteAsset:  sha256:ab8ecd87370524b461f8557c119c405552c396ed91fc0a8eec68679eab26f94a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libloading-0.8/default) >= 0.8.9
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "dlib"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%{?autochangelog}
