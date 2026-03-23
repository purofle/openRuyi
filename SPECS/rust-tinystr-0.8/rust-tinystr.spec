# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tinystr
%global full_version 0.8.2
%global pkgname tinystr-0.8

Name:           rust-tinystr-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "tinystr"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:42d3e9c45c09de15d06dd8acf5f4e0e399e85927b7f00711024eb7ae10fa4869
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(displaydoc-0.2) >= 0.2.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "tinystr"

%package     -n %{name}+alloc
Summary:        Small ASCII-only bounded length string representation - feature "alloc" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0/alloc) >= 1.0.220
Requires:       crate(zerovec-0.11/alloc) >= 0.11.5
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust tinystr crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+databake
Summary:        Small ASCII-only bounded length string representation - feature "databake"
Requires:       crate(%{pkgname})
Requires:       crate(databake-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/databake)

%description -n %{name}+databake
This metapackage enables feature "databake" for the Rust tinystr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Small ASCII-only bounded length string representation - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0) >= 1.0.220
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust tinystr crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerovec
Summary:        Small ASCII-only bounded length string representation - feature "zerovec"
Requires:       crate(%{pkgname})
Requires:       crate(zerovec-0.11) >= 0.11.5
Provides:       crate(%{pkgname}/zerovec)

%description -n %{name}+zerovec
This metapackage enables feature "zerovec" for the Rust tinystr crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+alloc

%files -n %{name}+databake

%files -n %{name}+serde

%files -n %{name}+zerovec

%changelog
%{?autochangelog}
