# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proptest
%global full_version 1.10.0
%global pkgname proptest-1.0

Name:           rust-proptest-1.0
Version:        1.10.0
Release:        %autorelease
Summary:        Rust crate "proptest"
License:        MIT OR Apache-2.0
URL:            https://proptest-rs.github.io/proptest/proptest/index.html
#!RemoteAsset:  sha256:37566cb3fdacef14c0737f9546df7cfeadbfbc9fef10991038bf5015d0c80532
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(num-traits-0.2) >= 0.2.19
Requires:       crate(rand-0.9/alloc) >= 0.9.2
Requires:       crate(rand-chacha-0.9) >= 0.9.0
Requires:       crate(rand-xorshift-0.4/default) >= 0.4.0
Requires:       crate(unarray-0.1/default) >= 0.1.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/atomic64bit)
Provides:       crate(%{pkgname}/unstable)

%description
Source code for takopackized Rust crate "proptest"

%package     -n %{name}+bit-set
Summary:        Hypothesis-like property-based testing and shrinking - feature "bit-set"
Requires:       crate(%{pkgname})
Requires:       crate(bit-set-0.8/default) >= 0.8.0
Requires:       crate(bit-vec-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/bit-set)

%description -n %{name}+bit-set
This metapackage enables feature "bit-set" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Hypothesis-like property-based testing and shrinking - feature "default" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bit-set)
Requires:       crate(%{pkgname}/fork)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/timeout)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/default-code-coverage)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default-code-coverage" feature.

%package     -n %{name}+fork
Summary:        Hypothesis-like property-based testing and shrinking - feature "fork"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rusty-fork)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/tempfile)
Provides:       crate(%{pkgname}/fork)

%description -n %{name}+fork
This metapackage enables feature "fork" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-std
Summary:        Hypothesis-like property-based testing and shrinking - feature "no_std"
Requires:       crate(%{pkgname})
Requires:       crate(num-traits-0.2/libm) >= 0.2.19
Provides:       crate(%{pkgname}/no-std)

%description -n %{name}+no-std
This metapackage enables feature "no_std" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest-macro
Summary:        Hypothesis-like property-based testing and shrinking - feature "proptest-macro" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(proptest-macro-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/attr-macro)
Provides:       crate(%{pkgname}/proptest-macro)

%description -n %{name}+proptest-macro
This metapackage enables feature "proptest-macro" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "attr-macro" feature.

%package     -n %{name}+regex-syntax
Summary:        Hypothesis-like property-based testing and shrinking - feature "regex-syntax"
Requires:       crate(%{pkgname})
Requires:       crate(regex-syntax-0.8/default) >= 0.8.10
Provides:       crate(%{pkgname}/regex-syntax)

%description -n %{name}+regex-syntax
This metapackage enables feature "regex-syntax" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rusty-fork
Summary:        Hypothesis-like property-based testing and shrinking - feature "rusty-fork"
Requires:       crate(%{pkgname})
Requires:       crate(rusty-fork-0.3) >= 0.3.1
Provides:       crate(%{pkgname}/rusty-fork)

%description -n %{name}+rusty-fork
This metapackage enables feature "rusty-fork" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Hypothesis-like property-based testing and shrinking - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/regex-syntax)
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(rand-0.9/alloc) >= 0.9.2
Requires:       crate(rand-0.9/os-rng) >= 0.9.2
Requires:       crate(rand-0.9/std) >= 0.9.2
Provides:       crate(%{pkgname}/handle-panics)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "handle-panics" feature.

%package     -n %{name}+tempfile
Summary:        Hypothesis-like property-based testing and shrinking - feature "tempfile"
Requires:       crate(%{pkgname})
Requires:       crate(tempfile-3.0/default) >= 3.27.0
Provides:       crate(%{pkgname}/tempfile)

%description -n %{name}+tempfile
This metapackage enables feature "tempfile" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+timeout
Summary:        Hypothesis-like property-based testing and shrinking - feature "timeout"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/fork)
Requires:       crate(rusty-fork-0.3/timeout) >= 0.3.1
Provides:       crate(%{pkgname}/timeout)

%description -n %{name}+timeout
This metapackage enables feature "timeout" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+x86
Summary:        Hypothesis-like property-based testing and shrinking - feature "x86" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(x86-0.52/default) >= 0.52.0
Provides:       crate(%{pkgname}/hardware-rng)
Provides:       crate(%{pkgname}/x86)

%description -n %{name}+x86
This metapackage enables feature "x86" for the Rust proptest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "hardware-rng" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+bit-set

%files -n %{name}+default

%files -n %{name}+fork

%files -n %{name}+no-std

%files -n %{name}+proptest-macro

%files -n %{name}+regex-syntax

%files -n %{name}+rusty-fork

%files -n %{name}+std

%files -n %{name}+tempfile

%files -n %{name}+timeout

%files -n %{name}+x86

%changelog
%{?autochangelog}
