# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name icu_normalizer
%global full_version 2.1.1
%global pkgname icu-normalizer-2.0

Name:           rust-icu-normalizer-2.0
Version:        2.1.1
Release:        %autorelease
Summary:        Rust crate "icu_normalizer"
License:        Unicode-3.0
URL:            https://icu4x.unicode.org
#!RemoteAsset:  sha256:5f6c8828b67bf8908d82127b2054ea1b4427ff0230ee9141c54251934ab1b599
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(icu-collections-2.0) >= 2.1.1
Requires:       crate(icu-provider-2.0) >= 2.1.1
Requires:       crate(smallvec-1.0) >= 1.15.1
Requires:       crate(zerovec-0.11) >= 0.11.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/experimental)
Provides:       crate(%{pkgname}/write16)

%description
Source code for takopackized Rust crate "icu_normalizer"

%package     -n %{name}+compiled-data
Summary:        API for normalizing text into Unicode Normalization Forms - feature "compiled_data"
Requires:       crate(%{pkgname})
Requires:       crate(icu-normalizer-data-2.0) >= 2.1.1
Requires:       crate(icu-properties-2.0/compiled-data) >= 2.1.2
Requires:       crate(icu-provider-2.0/baked) >= 2.1.1
Provides:       crate(%{pkgname}/compiled-data)

%description -n %{name}+compiled-data
This metapackage enables feature "compiled_data" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+datagen
Summary:        API for normalizing text into Unicode Normalization Forms - feature "datagen"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/icu-properties)
Requires:       crate(%{pkgname}/serde)
Requires:       crate(databake-0.2/derive) >= 0.2.0
Requires:       crate(icu-collections-2.0/databake) >= 2.1.1
Requires:       crate(icu-properties-2.0/datagen) >= 2.1.2
Requires:       crate(icu-provider-2.0/export) >= 2.1.1
Requires:       crate(zerovec-0.11/databake) >= 0.11.5
Provides:       crate(%{pkgname}/datagen)

%description -n %{name}+datagen
This metapackage enables feature "datagen" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        API for normalizing text into Unicode Normalization Forms - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/compiled-data)
Requires:       crate(%{pkgname}/utf16-iter)
Requires:       crate(%{pkgname}/utf8-iter)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+icu-properties
Summary:        API for normalizing text into Unicode Normalization Forms - feature "icu_properties"
Requires:       crate(%{pkgname})
Requires:       crate(icu-properties-2.0) >= 2.1.2
Provides:       crate(%{pkgname}/icu-properties)

%description -n %{name}+icu-properties
This metapackage enables feature "icu_properties" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        API for normalizing text into Unicode Normalization Forms - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(icu-collections-2.0/serde) >= 2.1.1
Requires:       crate(icu-properties-2.0/serde) >= 2.1.2
Requires:       crate(icu-provider-2.0/serde) >= 2.1.1
Requires:       crate(serde-1.0/alloc) >= 1.0.220
Requires:       crate(serde-1.0/derive) >= 1.0.220
Requires:       crate(zerovec-0.11/serde) >= 0.11.5
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+utf16-iter
Summary:        API for normalizing text into Unicode Normalization Forms - feature "utf16_iter"
Requires:       crate(%{pkgname})
Requires:       crate(utf16-iter-1.0) >= 1.0.2
Requires:       crate(write16-1.0/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/utf16-iter)

%description -n %{name}+utf16-iter
This metapackage enables feature "utf16_iter" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+utf8-iter
Summary:        API for normalizing text into Unicode Normalization Forms - feature "utf8_iter"
Requires:       crate(%{pkgname})
Requires:       crate(utf8-iter-1.0) >= 1.0.2
Provides:       crate(%{pkgname}/utf8-iter)

%description -n %{name}+utf8-iter
This metapackage enables feature "utf8_iter" for the Rust icu_normalizer crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+compiled-data

%files -n %{name}+datagen

%files -n %{name}+default

%files -n %{name}+icu-properties

%files -n %{name}+serde

%files -n %{name}+utf16-iter

%files -n %{name}+utf8-iter

%changelog
%{?autochangelog}
