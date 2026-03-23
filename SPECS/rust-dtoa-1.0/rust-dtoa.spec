# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dtoa
%global full_version 1.0.11
%global pkgname dtoa-1.0

Name:           rust-dtoa-1.0
Version:        1.0.11
Release:        %autorelease
Summary:        Rust crate "dtoa"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/dtoa
#!RemoteAsset:  sha256:4c3cf4824e2d5f025c7b531afcb2325364084a16806f6d47fbc1f5fbd9960590
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "dtoa"

%package     -n %{name}+no-panic
Summary:        Fast floating point primitive to string conversion - feature "no-panic"
Requires:       crate(%{pkgname})
Requires:       crate(no-panic-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/no-panic)

%description -n %{name}+no-panic
This metapackage enables feature "no-panic" for the Rust dtoa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+no-panic

%changelog
%{?autochangelog}
