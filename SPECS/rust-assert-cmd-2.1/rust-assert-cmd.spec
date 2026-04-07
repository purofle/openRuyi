# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name assert_cmd
%global full_version 2.1.1
%global pkgname assert-cmd-2.1

Name:           rust-assert-cmd-2.1
Version:        2.1.1
Release:        %autorelease
Summary:        Rust crate "assert_cmd"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/assert_cmd
#!RemoteAsset:  sha256:bcbb6924530aa9e0432442af08bbcafdad182db80d2e560da42a6d442535bf85
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1.0/default) >= 1.0.0
Requires:       crate(bstr-1.0/default) >= 1.0.1
Requires:       crate(libc-0.2/default) >= 0.2.137
Requires:       crate(predicates-3.0/diff) >= 3.0.1
Requires:       crate(predicates-core-1.0/default) >= 1.0.6
Requires:       crate(predicates-tree-1.0/default) >= 1.0.1
Requires:       crate(wait-timeout-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "assert_cmd"

%package     -n %{name}+color
Summary:        Test CLI Applications - feature "color" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(anstream-0.6/default) >= 0.6.7
Requires:       crate(predicates-3.0/color) >= 3.0.1
Requires:       crate(predicates-3.0/diff) >= 3.0.1
Provides:       crate(%{pkgname}/color)
Provides:       crate(%{pkgname}/color-auto)

%description -n %{name}+color
This metapackage enables feature "color" for the Rust assert_cmd crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "color-auto" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
