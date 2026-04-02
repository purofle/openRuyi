# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-c
%global full_version 0.10.16+cargo-0.91.0

Name:           cargo-c
Version:        0.10.16
Release:        %autorelease
Summary:        Helper program to build and install c-like libraries
License:        MIT
URL:            https://github.com/lu-zero/cargo-c
#!RemoteAsset:  sha256:17d431789b050b0fcf678455dfd5ceb7e5b45cd806140f8fe03b16b995d6cbff
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1.0/default) >= 1.0.0
Requires:       crate(cargo-0.91/default) >= 0.91.0
Requires:       crate(cargo-util-0.2/default) >= 0.2.0
Requires:       crate(cbindgen-0.29) >= 0.29.0
Requires:       crate(cc-1.0/default) >= 1.0.0
Requires:       crate(clap-4.0/cargo) >= 4.5.18
Requires:       crate(clap-4.0/color) >= 4.5.18
Requires:       crate(clap-4.0/default) >= 4.5.18
Requires:       crate(clap-4.0/derive) >= 4.5.18
Requires:       crate(clap-4.0/string) >= 4.5.18
Requires:       crate(clap-4.0/wrap-help) >= 4.5.18
Requires:       crate(glob-0.3/default) >= 0.3.0
Requires:       crate(implib-0.4/default) >= 0.4.0
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(object-0.37/pe) >= 0.37.1
Requires:       crate(object-0.37/read-core) >= 0.37.1
Requires:       crate(object-0.37/std) >= 0.37.1
Requires:       crate(regex-1.0/default) >= 1.5.6
Requires:       crate(semver-1.0/default) >= 1.0.3
Requires:       crate(serde-1.0/default) >= 1.0.123
Requires:       crate(serde-derive-1.0/default) >= 1.0.0
Requires:       crate(serde-json-1.0/default) >= 1.0.62
Requires:       crate(toml-0.9/default) >= 0.9.0

%prep -a
mkdir -p ~/.cargo
cat > ~/.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF

rm -rf Cargo.lock

%build
cargo build --release

%install -a
install -Dm0755 target/release/cargo-capi %{buildroot}%{_bindir}/cargo-capi
install -Dm0755 target/release/cargo-cbuild %{buildroot}%{_bindir}/cargo-cbuild
install -Dm0755 target/release/cargo-cinstall %{buildroot}%{_bindir}/cargo-cinstall
install -Dm0755 target/release/cargo-ctest %{buildroot}%{_bindir}/cargo-ctest

%files
%{_bindir}/cargo-capi
%{_bindir}/cargo-cbuild
%{_bindir}/cargo-cinstall
%{_bindir}/cargo-ctest
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
