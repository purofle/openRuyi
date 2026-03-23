# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fallible_collections
%global full_version 0.4.9
%global pkgname fallible-collections-0.4

Name:           rust-fallible-collections-0.4
Version:        0.4.9
Release:        %autorelease
Summary:        Rust crate "fallible_collections"
License:        MIT/Apache-2.0
URL:            https://github.com/vcombey/fallible_collections.git
#!RemoteAsset:  sha256:a88c69768c0a15262df21899142bc6df9b9b823546d4b4b9a7bc2d6c448ec6fd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/rust-1-57)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/std-io)
Provides:       crate(%{pkgname}/unstable)

%description
Source code for takopackized Rust crate "fallible_collections"

%package     -n %{name}+hashbrown
Summary:        Crate which adds fallible allocation api to std collections - feature "hashbrown" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(hashbrown-0.13/default) >= 0.13.2
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/hashbrown)
Provides:       crate(%{pkgname}/hashmap)

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust fallible_collections crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "hashmap" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+hashbrown

%changelog
%{?autochangelog}
