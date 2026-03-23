# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name selectors
%global full_version 0.31.0
%global pkgname selectors-0.31

Name:           rust-selectors-0.31
Version:        0.31.0
Release:        %autorelease
Summary:        Rust crate "selectors"
License:        MPL-2.0
URL:            https://github.com/servo/stylo
#!RemoteAsset:  sha256:5685b6ae43bfcf7d2e7dfcfb5d8e8f61b46442c902531e41a32a9a8bf0ee0fb6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(cssparser-0.35/default) >= 0.35.0
Requires:       crate(derive-more-2.0/add) >= 2.1.1
Requires:       crate(derive-more-2.0/add-assign) >= 2.1.1
Requires:       crate(derive-more-2.0/default) >= 2.1.1
Requires:       crate(fxhash-0.2/default) >= 0.2.1
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(new-debug-unreachable-1.0/default) >= 1.0.6
Requires:       crate(phf-0.11/default) >= 0.11.3
Requires:       crate(phf-codegen-0.11/default) >= 0.11.3
Requires:       crate(precomputed-hash-0.1/default) >= 0.1.1
Requires:       crate(servo-arc-0.4/default) >= 0.4.3
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/bench)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "selectors"

%package     -n %{name}+to-shmem
Summary:        CSS Selectors matching for Rust - feature "to_shmem"
Requires:       crate(%{pkgname})
Requires:       crate(to-shmem-0.2/default) >= 0.2.0
Requires:       crate(to-shmem-0.2/servo-arc) >= 0.2.0
Requires:       crate(to-shmem-derive-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/to-shmem)

%description -n %{name}+to-shmem
This metapackage enables feature "to_shmem" for the Rust selectors crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+to-shmem

%changelog
%{?autochangelog}
