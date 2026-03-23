# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nom_locate
%global full_version 5.0.0
%global pkgname nom-locate-5.0

Name:           rust-nom-locate-5.0
Version:        5.0.0
Release:        %autorelease
Summary:        Rust crate "nom_locate"
License:        MIT
URL:            https://github.com/fflorent/nom_locate
#!RemoteAsset:  sha256:0b577e2d69827c4740cba2b52efaad1c4cc7c73042860b199710b3575c68438d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytecount-0.6/default) >= 0.6.9
Requires:       crate(memchr-2.0) >= 2.8.0
Requires:       crate(nom-8.0) >= 8.0.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "nom_locate"

%package     -n %{name}+alloc
Summary:        Special input type for nom to locate tokens - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(nom-8.0/alloc) >= 8.0.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust nom_locate crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+generic-simd
Summary:        Special input type for nom to locate tokens - feature "generic-simd"
Requires:       crate(%{pkgname})
Requires:       crate(bytecount-0.6/generic-simd) >= 0.6.9
Provides:       crate(%{pkgname}/generic-simd)

%description -n %{name}+generic-simd
This metapackage enables feature "generic-simd" for the Rust nom_locate crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime-dispatch-simd
Summary:        Special input type for nom to locate tokens - feature "runtime-dispatch-simd"
Requires:       crate(%{pkgname})
Requires:       crate(bytecount-0.6/runtime-dispatch-simd) >= 0.6.9
Provides:       crate(%{pkgname}/runtime-dispatch-simd)

%description -n %{name}+runtime-dispatch-simd
This metapackage enables feature "runtime-dispatch-simd" for the Rust nom_locate crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stable-deref-trait
Summary:        Special input type for nom to locate tokens - feature "stable_deref_trait"
Requires:       crate(%{pkgname})
Requires:       crate(stable-deref-trait-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/stable-deref-trait)

%description -n %{name}+stable-deref-trait
This metapackage enables feature "stable_deref_trait" for the Rust nom_locate crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Special input type for nom to locate tokens - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(memchr-2.0/use-std) >= 2.8.0
Requires:       crate(nom-8.0/std) >= 8.0.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust nom_locate crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+alloc

%files -n %{name}+generic-simd

%files -n %{name}+runtime-dispatch-simd

%files -n %{name}+stable-deref-trait

%files -n %{name}+std

%changelog
%{?autochangelog}
