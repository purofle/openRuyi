# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name litemap
%global full_version 0.8.1
%global pkgname litemap-0.8

Name:           rust-litemap-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "litemap"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:6373607a59f0be73a39b6fe456b8192fcc3585f602af20751600e974dd455e77
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/testing)

%description
Source code for takopackized Rust crate "litemap"

%package     -n %{name}+databake
Summary:        Key-value Map implementation based on a flat, sorted Vec - feature "databake"
Requires:       crate(%{pkgname})
Requires:       crate(databake-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/databake)

%description -n %{name}+databake
This metapackage enables feature "databake" for the Rust litemap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Key-value Map implementation based on a flat, sorted Vec - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(serde-core-1.0/alloc) >= 1.0.220
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust litemap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+yoke
Summary:        Key-value Map implementation based on a flat, sorted Vec - feature "yoke"
Requires:       crate(%{pkgname})
Requires:       crate(yoke-0.8/derive) >= 0.8.0
Provides:       crate(%{pkgname}/yoke)

%description -n %{name}+yoke
This metapackage enables feature "yoke" for the Rust litemap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+databake

%files -n %{name}+serde

%files -n %{name}+yoke

%changelog
%{?autochangelog}
