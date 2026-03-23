# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rusty-fork
%global full_version 0.3.1
%global pkgname rusty-fork-0.3

Name:           rust-rusty-fork-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "rusty-fork"
License:        MIT/Apache-2.0
URL:            https://github.com/altsysrq/rusty-fork
#!RemoteAsset:  sha256:cc6bf79ff24e648f6da1f8d1f011e9cac26491b619e6b9280f2b47f1774e6ee2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fnv-1.0/default) >= 1.0.7
Requires:       crate(quick-error-1.0/default) >= 1.2.3
Requires:       crate(tempfile-3.0/default) >= 3.27.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "rusty-fork"

%package     -n %{name}+wait-timeout
Summary:        Cross-platform library for running Rust tests in sub-processes using a fork-like interface - feature "wait-timeout" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(wait-timeout-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/timeout)
Provides:       crate(%{pkgname}/wait-timeout)

%description -n %{name}+wait-timeout
This metapackage enables feature "wait-timeout" for the Rust rusty-fork crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "timeout" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+wait-timeout

%changelog
%{?autochangelog}
