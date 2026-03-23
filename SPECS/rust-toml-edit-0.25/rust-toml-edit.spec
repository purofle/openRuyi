# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml_edit
%global full_version 0.25.5+spec-1.1.0
%global pkgname toml-edit-0.25

Name:           rust-toml-edit-0.25
Version:        0.25.5
Release:        %autorelease
Summary:        Rust crate "toml_edit"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:8ca1a40644a28bce036923f6a431df0b34236949d111cc07cb6dca830c9ef2e1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indexmap-2.0/default) >= 2.13.0
Requires:       crate(indexmap-2.0/std) >= 2.13.0
Requires:       crate(toml-datetime-1.0/default) >= 1.0.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unbounded)

%description
Source code for takopackized Rust crate "toml_edit"

%package     -n %{name}+debug
Summary:        Yet another format-preserving TOML parser - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/display)
Requires:       crate(anstream-0.6/default) >= 0.6.20
Requires:       crate(anstyle-1.0/default) >= 1.0.11
Requires:       crate(toml-parser-1.0/debug) >= 1.0.10
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Yet another format-preserving TOML parser - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/display)
Requires:       crate(%{pkgname}/parse)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+display
Summary:        Yet another format-preserving TOML parser - feature "display"
Requires:       crate(%{pkgname})
Requires:       crate(toml-writer-1.0/default) >= 1.0.7
Provides:       crate(%{pkgname}/display)

%description -n %{name}+display
This metapackage enables feature "display" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parse
Summary:        Yet another format-preserving TOML parser - feature "parse"
Requires:       crate(%{pkgname})
Requires:       crate(toml-parser-1.0/default) >= 1.0.10
Requires:       crate(winnow-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/parse)

%description -n %{name}+parse
This metapackage enables feature "parse" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Yet another format-preserving TOML parser - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0/default) >= 1.0.225
Requires:       crate(serde-spanned-1.0/default) >= 1.0.4
Requires:       crate(serde-spanned-1.0/serde) >= 1.0.4
Requires:       crate(toml-datetime-1.0/serde) >= 1.0.1
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust toml_edit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+debug

%files -n %{name}+default

%files -n %{name}+display

%files -n %{name}+parse

%files -n %{name}+serde

%changelog
%{?autochangelog}
