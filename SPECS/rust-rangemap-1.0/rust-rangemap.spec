# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rangemap
%global full_version 1.7.1
%global pkgname rangemap-1.0

Name:           rust-rangemap-1.0
Version:        1.7.1
Release:        %autorelease
Summary:        Rust crate "rangemap"
License:        MIT/Apache-2.0
URL:            https://github.com/jeffparsons/rangemap
#!RemoteAsset:  sha256:973443cf09a9c8656b574a866ab68dfa19f0867d0340648c7d2f6a71b8a8ea68
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/const-fn)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)

%description
Contiguous and overlapping ranges that map to the same value are coalesced into a single range.
Source code for takopackized Rust crate "rangemap"

%package     -n %{name}+quickcheck
Summary:        Map and set data structures whose keys are stored as ranges - feature "quickcheck"
Requires:       crate(%{pkgname})
Requires:       crate(quickcheck-1.0/default) >= 1.0.3
Provides:       crate(%{pkgname}/quickcheck)

%description -n %{name}+quickcheck
Contiguous and overlapping ranges that map to the same value are coalesced into a single range.
This metapackage enables feature "quickcheck" for the Rust rangemap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Map and set data structures whose keys are stored as ranges - feature "serde" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/serde1)

%description -n %{name}+serde
Contiguous and overlapping ranges that map to the same value are coalesced into a single range.
This metapackage enables feature "serde" for the Rust rangemap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde1" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+quickcheck

%files -n %{name}+serde

%changelog
%{?autochangelog}
