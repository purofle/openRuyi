# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cfg-expr
%global full_version 0.20.7
%global pkgname cfg-expr-0.20

Name:           rust-cfg-expr-0.20
Version:        0.20.7
Release:        %autorelease
Summary:        Rust crate "cfg-expr"
License:        MIT OR Apache-2.0
URL:            https://github.com/EmbarkStudios/cfg-expr
#!RemoteAsset:  sha256:3c6b04e07d8080154ed4ac03546d9a2b303cc2fe1901ba0b35b301516e289368
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(smallvec-1.0/default) >= 1.15.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cfg-expr"

%package     -n %{name}+target-lexicon
Summary:        Parser and evaluator for Rust `cfg()` expressions - feature "target-lexicon" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(target-lexicon-0.13/default) >= 0.13.3
Provides:       crate(%{pkgname}/target-lexicon)
Provides:       crate(%{pkgname}/targets)

%description -n %{name}+target-lexicon
This metapackage enables feature "target-lexicon" for the Rust cfg-expr crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "targets" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+target-lexicon

%changelog
%{?autochangelog}
