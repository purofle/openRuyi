# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name simba
%global full_version 0.9.1
%global pkgname simba-0.9

Name:           rust-simba-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "simba"
License:        Apache-2.0
URL:            https://github.com/dimforge/simba
#!RemoteAsset:  sha256:c99284beb21666094ba2b75bbceda012e610f5479dfcc2d6e2426f53197ffd95
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(approx-0.5) >= 0.5.1
Requires:       crate(num-complex-0.4) >= 0.4.6
Requires:       crate(num-traits-0.2) >= 0.2.19
Requires:       crate(paste-1.0/default) >= 1.0.15
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "simba"

%package     -n %{name}+cordic
Summary:        SIMD algebra for Rust - feature "cordic"
Requires:       crate(%{pkgname})
Requires:       crate(cordic-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/cordic)

%description -n %{name}+cordic
This metapackage enables feature "cordic" for the Rust simba crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+decimal
Summary:        SIMD algebra for Rust - feature "decimal"
Requires:       crate(%{pkgname})
Requires:       crate(decimal-2.0) >= 2.0.0
Provides:       crate(%{pkgname}/decimal)

%description -n %{name}+decimal
This metapackage enables feature "decimal" for the Rust simba crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fixed
Summary:        SIMD algebra for Rust - feature "fixed"
Requires:       crate(%{pkgname})
Requires:       crate(fixed-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/fixed)

%description -n %{name}+fixed
This metapackage enables feature "fixed" for the Rust simba crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        SIMD algebra for Rust - feature "libm"
Requires:       crate(%{pkgname})
Requires:       crate(num-traits-0.2/libm) >= 0.2.19
Provides:       crate(%{pkgname}/libm)

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust simba crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm-force
Summary:        SIMD algebra for Rust - feature "libm_force"
Requires:       crate(%{pkgname})
Requires:       crate(libm-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/libm-force)

%description -n %{name}+libm-force
This metapackage enables feature "libm_force" for the Rust simba crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+partial-fixed-point-support
Summary:        SIMD algebra for Rust - feature "partial_fixed_point_support"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cordic)
Requires:       crate(%{pkgname}/fixed)
Provides:       crate(%{pkgname}/partial-fixed-point-support)

%description -n %{name}+partial-fixed-point-support
This metapackage enables feature "partial_fixed_point_support" for the Rust simba crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        SIMD algebra for Rust - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust simba crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv
Summary:        SIMD algebra for Rust - feature "rkyv" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/rkyv)
Provides:       crate(%{pkgname}/rkyv-serialize)

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust simba crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rkyv-serialize" feature.

%package     -n %{name}+serde
Summary:        SIMD algebra for Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust simba crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-serialize
Summary:        SIMD algebra for Rust - feature "serde_serialize"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(fixed-1.0/serde) >= 1.0.0
Provides:       crate(%{pkgname}/serde-serialize)

%description -n %{name}+serde-serialize
This metapackage enables feature "serde_serialize" for the Rust simba crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        SIMD algebra for Rust - feature "std" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(wide-0.7/std) >= 0.7.33
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/portable-simd)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust simba crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "portable_simd" features.

%package     -n %{name}+wide
Summary:        SIMD algebra for Rust - feature "wide"
Requires:       crate(%{pkgname})
Requires:       crate(wide-0.7) >= 0.7.33
Provides:       crate(%{pkgname}/wide)

%description -n %{name}+wide
This metapackage enables feature "wide" for the Rust simba crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+cordic

%files -n %{name}+decimal

%files -n %{name}+fixed

%files -n %{name}+libm

%files -n %{name}+libm-force

%files -n %{name}+partial-fixed-point-support

%files -n %{name}+rand

%files -n %{name}+rkyv

%files -n %{name}+serde

%files -n %{name}+serde-serialize

%files -n %{name}+std

%files -n %{name}+wide

%changelog
%{?autochangelog}
