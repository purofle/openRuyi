# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nalgebra
%global full_version 0.33.2
%global pkgname nalgebra-0.33

Name:           rust-nalgebra-0.33
Version:        0.33.2
Release:        %autorelease
Summary:        Rust crate "nalgebra"
License:        Apache-2.0
URL:            https://nalgebra.org
#!RemoteAsset:  sha256:26aecdf64b707efd1310e3544d709c5c0ac61c13756046aaaba41be5c4f66a3b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(approx-0.5) >= 0.5.1
Requires:       crate(num-complex-0.4) >= 0.4.6
Requires:       crate(num-rational-0.4) >= 0.4.2
Requires:       crate(num-traits-0.2) >= 0.2.19
Requires:       crate(simba-0.9) >= 0.9.1
Requires:       crate(typenum-1.0/default) >= 1.19.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/slow-tests)
Provides:       crate(%{pkgname}/sparse)

%description
Source code for takopackized Rust crate "nalgebra"

%package     -n %{name}+alga
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "alga"
Requires:       crate(%{pkgname})
Requires:       crate(alga-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/alga)

%description -n %{name}+alga
This metapackage enables feature "alga" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "bytemuck"
Requires:       crate(%{pkgname})
Requires:       crate(bytemuck-1.0/default) >= 1.5
Provides:       crate(%{pkgname}/bytemuck)

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+convert-bytemuck
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "convert-bytemuck"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bytemuck)
Requires:       crate(num-complex-0.4/bytemuck) >= 0.4.6
Provides:       crate(%{pkgname}/convert-bytemuck)

%description -n %{name}+convert-bytemuck
This metapackage enables feature "convert-bytemuck" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rand)
Requires:       crate(approx-0.5/num-complex) >= 0.5.1
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/macros)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+glam014
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam014" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/convert-glam014)
Provides:       crate(%{pkgname}/glam014)

%description -n %{name}+glam014
This metapackage enables feature "glam014" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam014" feature.

%package     -n %{name}+glam015
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam015" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/convert-glam015)
Provides:       crate(%{pkgname}/glam015)

%description -n %{name}+glam015
This metapackage enables feature "glam015" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam015" feature.

%package     -n %{name}+glam016
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam016" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.16/default) >= 0.16.0
Provides:       crate(%{pkgname}/convert-glam016)
Provides:       crate(%{pkgname}/glam016)

%description -n %{name}+glam016
This metapackage enables feature "glam016" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam016" feature.

%package     -n %{name}+glam017
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam017" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.17/default) >= 0.17.0
Provides:       crate(%{pkgname}/convert-glam017)
Provides:       crate(%{pkgname}/glam017)

%description -n %{name}+glam017
This metapackage enables feature "glam017" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam017" feature.

%package     -n %{name}+glam018
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam018" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.18/default) >= 0.18.0
Provides:       crate(%{pkgname}/convert-glam018)
Provides:       crate(%{pkgname}/glam018)

%description -n %{name}+glam018
This metapackage enables feature "glam018" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam018" feature.

%package     -n %{name}+glam019
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam019" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.19/default) >= 0.19.0
Provides:       crate(%{pkgname}/convert-glam019)
Provides:       crate(%{pkgname}/glam019)

%description -n %{name}+glam019
This metapackage enables feature "glam019" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam019" feature.

%package     -n %{name}+glam020
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam020" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}/convert-glam020)
Provides:       crate(%{pkgname}/glam020)

%description -n %{name}+glam020
This metapackage enables feature "glam020" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam020" feature.

%package     -n %{name}+glam021
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam021" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.21/default) >= 0.21.0
Provides:       crate(%{pkgname}/convert-glam021)
Provides:       crate(%{pkgname}/glam021)

%description -n %{name}+glam021
This metapackage enables feature "glam021" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam021" feature.

%package     -n %{name}+glam022
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam022" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/convert-glam022)
Provides:       crate(%{pkgname}/glam022)

%description -n %{name}+glam022
This metapackage enables feature "glam022" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam022" feature.

%package     -n %{name}+glam023
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam023" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.23/default) >= 0.23.0
Provides:       crate(%{pkgname}/convert-glam023)
Provides:       crate(%{pkgname}/glam023)

%description -n %{name}+glam023
This metapackage enables feature "glam023" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam023" feature.

%package     -n %{name}+glam024
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam024" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.24/default) >= 0.24.0
Provides:       crate(%{pkgname}/convert-glam024)
Provides:       crate(%{pkgname}/glam024)

%description -n %{name}+glam024
This metapackage enables feature "glam024" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam024" feature.

%package     -n %{name}+glam025
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam025" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.25/default) >= 0.25.0
Provides:       crate(%{pkgname}/convert-glam025)
Provides:       crate(%{pkgname}/glam025)

%description -n %{name}+glam025
This metapackage enables feature "glam025" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam025" feature.

%package     -n %{name}+glam027
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam027" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.27/default) >= 0.27.0
Provides:       crate(%{pkgname}/convert-glam027)
Provides:       crate(%{pkgname}/glam027)

%description -n %{name}+glam027
This metapackage enables feature "glam027" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam027" feature.

%package     -n %{name}+glam028
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam028" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.28/default) >= 0.28.0
Provides:       crate(%{pkgname}/convert-glam028)
Provides:       crate(%{pkgname}/glam028)

%description -n %{name}+glam028
This metapackage enables feature "glam028" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam028" feature.

%package     -n %{name}+glam029
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "glam029" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glam-0.29/default) >= 0.29.0
Provides:       crate(%{pkgname}/convert-glam029)
Provides:       crate(%{pkgname}/glam029)

%description -n %{name}+glam029
This metapackage enables feature "glam029" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-glam029" feature.

%package     -n %{name}+io
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "io"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pest)
Requires:       crate(%{pkgname}/pest-derive)
Provides:       crate(%{pkgname}/io)

%description -n %{name}+io
This metapackage enables feature "io" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "libm"
Requires:       crate(%{pkgname})
Requires:       crate(simba-0.9/libm) >= 0.9.1
Provides:       crate(%{pkgname}/libm)

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm-force
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "libm-force"
Requires:       crate(%{pkgname})
Requires:       crate(simba-0.9/libm-force) >= 0.9.1
Provides:       crate(%{pkgname}/libm-force)

%description -n %{name}+libm-force
This metapackage enables feature "libm-force" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+matrixcompare-core
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "matrixcompare-core" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(matrixcompare-core-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/compare)
Provides:       crate(%{pkgname}/matrixcompare-core)

%description -n %{name}+matrixcompare-core
This metapackage enables feature "matrixcompare-core" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compare" feature.

%package     -n %{name}+matrixmultiply
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "matrixmultiply"
Requires:       crate(%{pkgname})
Requires:       crate(matrixmultiply-0.3/default) >= 0.3.10
Provides:       crate(%{pkgname}/matrixmultiply)

%description -n %{name}+matrixmultiply
This metapackage enables feature "matrixmultiply" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mint
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "mint" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(mint-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/convert-mint)
Provides:       crate(%{pkgname}/mint)

%description -n %{name}+mint
This metapackage enables feature "mint" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "convert-mint" feature.

%package     -n %{name}+nalgebra-macros
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "nalgebra-macros" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(nalgebra-macros-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/macros)
Provides:       crate(%{pkgname}/nalgebra-macros)

%description -n %{name}+nalgebra-macros
This metapackage enables feature "nalgebra-macros" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "macros" feature.

%package     -n %{name}+pest
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "pest"
Requires:       crate(%{pkgname})
Requires:       crate(pest-2.0/default) >= 2.0.0
Provides:       crate(%{pkgname}/pest)

%description -n %{name}+pest
This metapackage enables feature "pest" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pest-derive
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "pest_derive"
Requires:       crate(%{pkgname})
Requires:       crate(pest-derive-2.0/default) >= 2.0.0
Provides:       crate(%{pkgname}/pest-derive)

%description -n %{name}+pest-derive
This metapackage enables feature "pest_derive" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "proptest" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(proptest-1.0/std) >= 1.0.0
Provides:       crate(%{pkgname}/proptest)
Provides:       crate(%{pkgname}/proptest-support)

%description -n %{name}+proptest
This metapackage enables feature "proptest" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "proptest-support" feature.

%package     -n %{name}+quickcheck
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "quickcheck" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(quickcheck-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)
Provides:       crate(%{pkgname}/quickcheck)

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "arbitrary" feature.

%package     -n %{name}+rand
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rand-distr)
Requires:       crate(%{pkgname}/rand-no-std)
Requires:       crate(rand-0.8/std) >= 0.8.0
Requires:       crate(rand-0.8/std-rng) >= 0.8.0
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-package
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rand-package" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rand-no-std)
Provides:       crate(%{pkgname}/rand-package)

%description -n %{name}+rand-package
This metapackage enables feature "rand-package" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rand-no-std" feature.

%package     -n %{name}+rand-distr
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rand_distr"
Requires:       crate(%{pkgname})
Requires:       crate(rand-distr-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/rand-distr)

%description -n %{name}+rand-distr
This metapackage enables feature "rand_distr" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.6
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rkyv"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7) >= 0.7.41
Provides:       crate(%{pkgname}/rkyv)

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-safe-deser
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rkyv-safe-deser"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rkyv-serialize)
Requires:       crate(rkyv-0.7/validation) >= 0.7.41
Provides:       crate(%{pkgname}/rkyv-safe-deser)

%description -n %{name}+rkyv-safe-deser
This metapackage enables feature "rkyv-safe-deser" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-serialize
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rkyv-serialize"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rkyv-serialize-no-std)
Requires:       crate(rkyv-0.7/std) >= 0.7.41
Requires:       crate(rkyv-0.7/validation) >= 0.7.41
Provides:       crate(%{pkgname}/rkyv-serialize)

%description -n %{name}+rkyv-serialize
This metapackage enables feature "rkyv-serialize" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv-serialize-no-std
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "rkyv-serialize-no-std"
Requires:       crate(%{pkgname})
Requires:       crate(rkyv-0.7/size-32) >= 0.7.41
Provides:       crate(%{pkgname}/rkyv-serialize-no-std)

%description -n %{name}+rkyv-serialize-no-std
This metapackage enables feature "rkyv-serialize-no-std" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-serialize
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "serde-serialize"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde-serialize-no-std)
Requires:       crate(serde-1.0/derive) >= 1.0.0
Requires:       crate(serde-1.0/std) >= 1.0.0
Provides:       crate(%{pkgname}/serde-serialize)

%description -n %{name}+serde-serialize
This metapackage enables feature "serde-serialize" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-serialize-no-std
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "serde-serialize-no-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(num-complex-0.4/serde) >= 0.4.6
Provides:       crate(%{pkgname}/serde-serialize-no-std)

%description -n %{name}+serde-serialize-no-std
This metapackage enables feature "serde-serialize-no-std" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        General-purpose linear algebra library with transformations and statically-sized or dynamically-sized matrices - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/matrixmultiply)
Requires:       crate(approx-0.5/std) >= 0.5.1
Requires:       crate(num-complex-0.4/std) >= 0.4.6
Requires:       crate(num-rational-0.4/std) >= 0.4.2
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(simba-0.9/std) >= 0.9.1
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust nalgebra crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+alga

%files -n %{name}+bytemuck

%files -n %{name}+convert-bytemuck

%files -n %{name}+debug

%files -n %{name}+default

%files -n %{name}+glam014

%files -n %{name}+glam015

%files -n %{name}+glam016

%files -n %{name}+glam017

%files -n %{name}+glam018

%files -n %{name}+glam019

%files -n %{name}+glam020

%files -n %{name}+glam021

%files -n %{name}+glam022

%files -n %{name}+glam023

%files -n %{name}+glam024

%files -n %{name}+glam025

%files -n %{name}+glam027

%files -n %{name}+glam028

%files -n %{name}+glam029

%files -n %{name}+io

%files -n %{name}+libm

%files -n %{name}+libm-force

%files -n %{name}+matrixcompare-core

%files -n %{name}+matrixmultiply

%files -n %{name}+mint

%files -n %{name}+nalgebra-macros

%files -n %{name}+pest

%files -n %{name}+pest-derive

%files -n %{name}+proptest

%files -n %{name}+quickcheck

%files -n %{name}+rand

%files -n %{name}+rand-package

%files -n %{name}+rand-distr

%files -n %{name}+rayon

%files -n %{name}+rkyv

%files -n %{name}+rkyv-safe-deser

%files -n %{name}+rkyv-serialize

%files -n %{name}+rkyv-serialize-no-std

%files -n %{name}+serde

%files -n %{name}+serde-serialize

%files -n %{name}+serde-serialize-no-std

%files -n %{name}+std

%changelog
%{?autochangelog}
