# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerovec
%global full_version 0.11.5
%global pkgname zerovec-0.11

Name:           rust-zerovec-0.11
Version:        0.11.5
Release:        %autorelease
Summary:        Rust crate "zerovec"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:6c28719294829477f525be0186d13efa9a3c602f7ec202ca9e353d310fb9a002
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zerofrom-0.1) >= 0.1.6
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "zerovec"

%package     -n %{name}+alloc
Summary:        Zero-copy vector backed by a byte array - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/alloc) >= 1.0.220
Requires:       crate(serde-1.0/derive) >= 1.0.220
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust zerovec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+databake
Summary:        Zero-copy vector backed by a byte array - feature "databake"
Requires:       crate(%{pkgname})
Requires:       crate(databake-0.2/derive) >= 0.2.0
Provides:       crate(%{pkgname}/databake)

%description -n %{name}+databake
This metapackage enables feature "databake" for the Rust zerovec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Zero-copy vector backed by a byte array - feature "derive"
Requires:       crate(%{pkgname})
Requires:       crate(zerovec-derive-0.11) >= 0.11.2
Provides:       crate(%{pkgname}/derive)

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust zerovec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashmap
Summary:        Zero-copy vector backed by a byte array - feature "hashmap"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(twox-hash-2.0/xxhash64) >= 2.0.0
Provides:       crate(%{pkgname}/hashmap)

%description -n %{name}+hashmap
This metapackage enables feature "hashmap" for the Rust zerovec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Zero-copy vector backed by a byte array - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/derive) >= 1.0.220
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust zerovec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+yoke
Summary:        Zero-copy vector backed by a byte array - feature "yoke"
Requires:       crate(%{pkgname})
Requires:       crate(yoke-0.8) >= 0.8.1
Provides:       crate(%{pkgname}/yoke)

%description -n %{name}+yoke
This metapackage enables feature "yoke" for the Rust zerovec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+alloc

%files -n %{name}+databake

%files -n %{name}+derive

%files -n %{name}+hashmap

%files -n %{name}+serde

%files -n %{name}+yoke

%changelog
%{?autochangelog}
