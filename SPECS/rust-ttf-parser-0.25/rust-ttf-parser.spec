# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ttf-parser
%global full_version 0.25.1
%global pkgname ttf-parser-0.25

Name:           rust-ttf-parser-0.25
Version:        0.25.1
Release:        %autorelease
Summary:        Rust crate "ttf-parser"
License:        MIT OR Apache-2.0
URL:            https://github.com/harfbuzz/ttf-parser
#!RemoteAsset:  sha256:d2df906b07856748fa3f6e0ad0cbaa047052d4a7dd609e231c4f72cee8c36f31
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/apple-layout)
Provides:       crate(%{pkgname}/glyph-names)
Provides:       crate(%{pkgname}/gvar-alloc)
Provides:       crate(%{pkgname}/opentype-layout)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/variable-fonts)

%description
Source code for takopackized Rust crate "ttf-parser"

%package     -n %{name}+core-maths
Summary:        High-level, safe, zero-allocation font parser for TrueType, OpenType, and AAT - feature "core_maths" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(core-maths-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/core-maths)
Provides:       crate(%{pkgname}/no-std-float)

%description -n %{name}+core-maths
This metapackage enables feature "core_maths" for the Rust ttf-parser crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "no-std-float" feature.

%package     -n %{name}+default
Summary:        High-level, safe, zero-allocation font parser for TrueType, OpenType, and AAT - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/apple-layout)
Requires:       crate(%{pkgname}/glyph-names)
Requires:       crate(%{pkgname}/opentype-layout)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/variable-fonts)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ttf-parser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+core-maths

%files -n %{name}+default

%changelog
%{?autochangelog}
