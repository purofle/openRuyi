# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name simd-adler32
%global full_version 0.3.8
%global pkgname simd-adler32-0.3

Name:           rust-simd-adler32-0.3
Version:        0.3.8
Release:        %autorelease
Summary:        Rust crate "simd-adler32"
License:        MIT
URL:            https://github.com/mcountryman/simd-adler32
#!RemoteAsset:  sha256:e320a6c5ad31d271ad523dcf3ad13e2767ad8b1cb8f047f75a8aeaf8da139da2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/const-generics)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "simd-adler32"

%package     -n %{name}+default
Summary:        SIMD-accelerated Adler-32 hash algorithm implementation - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/const-generics)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust simd-adler32 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+default

%changelog
%{?autochangelog}
