# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerotrie
%global full_version 0.2.3
%global pkgname zerotrie-0.2

Name:           rust-zerotrie-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "zerotrie"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:2a59c17a5562d507e4b54960e8569ebee33bee890c70aa3fe7b97e85a9fd7851
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(displaydoc-0.2) >= 0.2.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "zerotrie"

%package     -n %{name}+databake
Summary:        Data structure that efficiently maps strings to integers - feature "databake"
Requires:       crate(%{pkgname})
Requires:       crate(databake-0.2/derive) >= 0.2.0
Requires:       crate(zerovec-0.11/databake) >= 0.11.3
Provides:       crate(%{pkgname}/databake)

%description -n %{name}+databake
This metapackage enables feature "databake" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+litemap
Summary:        Data structure that efficiently maps strings to integers - feature "litemap"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(litemap-0.8/alloc) >= 0.8.0
Provides:       crate(%{pkgname}/litemap)

%description -n %{name}+litemap
This metapackage enables feature "litemap" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Data structure that efficiently maps strings to integers - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(litemap-0.8/alloc) >= 0.8.0
Requires:       crate(litemap-0.8/serde) >= 0.8.0
Requires:       crate(serde-core-1.0) >= 1.0.220
Requires:       crate(zerovec-0.11/serde) >= 0.11.3
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+yoke
Summary:        Data structure that efficiently maps strings to integers - feature "yoke"
Requires:       crate(%{pkgname})
Requires:       crate(yoke-0.8/derive) >= 0.8.1
Provides:       crate(%{pkgname}/yoke)

%description -n %{name}+yoke
This metapackage enables feature "yoke" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerofrom
Summary:        Data structure that efficiently maps strings to integers - feature "zerofrom"
Requires:       crate(%{pkgname})
Requires:       crate(zerofrom-0.1) >= 0.1.6
Provides:       crate(%{pkgname}/zerofrom)

%description -n %{name}+zerofrom
This metapackage enables feature "zerofrom" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerovec
Summary:        Data structure that efficiently maps strings to integers - feature "zerovec"
Requires:       crate(%{pkgname})
Requires:       crate(zerovec-0.11) >= 0.11.3
Provides:       crate(%{pkgname}/zerovec)

%description -n %{name}+zerovec
This metapackage enables feature "zerovec" for the Rust zerotrie crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+databake

%files -n %{name}+litemap

%files -n %{name}+serde

%files -n %{name}+yoke

%files -n %{name}+zerofrom

%files -n %{name}+zerovec

%changelog
%{?autochangelog}
