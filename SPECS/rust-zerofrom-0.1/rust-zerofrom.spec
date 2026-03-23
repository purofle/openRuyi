# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerofrom
%global full_version 0.1.6
%global pkgname zerofrom-0.1

Name:           rust-zerofrom-0.1
Version:        0.1.6
Release:        %autorelease
Summary:        Rust crate "zerofrom"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:50cc42e0333e05660c3587f3bf9d0478688e15d870fab3346451ce7f8c9fbea5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "zerofrom"

%package     -n %{name}+derive
Summary:        ZeroFrom trait for constructing - feature "derive"
Requires:       crate(%{pkgname})
Requires:       crate(zerofrom-derive-0.1) >= 0.1.6
Provides:       crate(%{pkgname}/derive)

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust zerofrom crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+derive

%changelog
%{?autochangelog}
