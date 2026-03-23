# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lopdf
%global full_version 0.38.0
%global pkgname lopdf-0.38

Name:           rust-lopdf-0.38
Version:        0.38.0
Release:        %autorelease
Summary:        Rust crate "lopdf"
License:        MIT
URL:            https://github.com/J-F-Liu/lopdf
#!RemoteAsset:  sha256:c7184fdea2bc3cd272a1acec4030c321a8f9875e877b3f92a53f2f6033fdc289
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aes-0.8/default) >= 0.8.4
Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(cbc-0.1/default) >= 0.1.2
Requires:       crate(ecb-0.1/default) >= 0.1.2
Requires:       crate(encoding-rs-0.8/default) >= 0.8.35
Requires:       crate(flate2-1.0/default) >= 1.1.9
Requires:       crate(getrandom-0.3/default) >= 0.3.4
Requires:       crate(indexmap-2.0/default) >= 2.13.0
Requires:       crate(itoa-1.0/default) >= 1.0.18
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(md-5-0.10/default) >= 0.10.6
Requires:       crate(nom-8.0/default) >= 8.0.0
Requires:       crate(nom-locate-5.0/default) >= 5.0.0
Requires:       crate(rand-0.9/default) >= 0.9.2
Requires:       crate(rangemap-1.0/default) >= 1.7.1
Requires:       crate(sha2-0.10/default) >= 0.10.9
Requires:       crate(stringprep-0.1/default) >= 0.1.5
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(ttf-parser-0.25/default) >= 0.25.1
Requires:       crate(weezl-0.1/default) >= 0.1.12
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "lopdf"

%package     -n %{name}+async
Summary:        PDF document manipulation - feature "async"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0/fs) >= 1.0.0
Requires:       crate(tokio-1.0/io-util) >= 1.0.0
Requires:       crate(tokio-1.0/macros) >= 1.0.0
Requires:       crate(tokio-1.0/rt-multi-thread) >= 1.0.0
Provides:       crate(%{pkgname}/async)

%description -n %{name}+async
This metapackage enables feature "async" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        PDF document manipulation - feature "chrono"
Requires:       crate(%{pkgname})
Requires:       crate(chrono-0.4/clock) >= 0.4.44
Requires:       crate(chrono-0.4/std) >= 0.4.44
Provides:       crate(%{pkgname}/chrono)

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        PDF document manipulation - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/chrono)
Requires:       crate(%{pkgname}/jiff)
Requires:       crate(%{pkgname}/rayon)
Requires:       crate(%{pkgname}/time)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+image
Summary:        PDF document manipulation - feature "image" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(image-0.25/default) >= 0.25.0
Provides:       crate(%{pkgname}/embed-image)
Provides:       crate(%{pkgname}/image)

%description -n %{name}+image
This metapackage enables feature "image" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "embed_image" feature.

%package     -n %{name}+jiff
Summary:        PDF document manipulation - feature "jiff"
Requires:       crate(%{pkgname})
Requires:       crate(jiff-0.2/default) >= 0.2.23
Provides:       crate(%{pkgname}/jiff)

%description -n %{name}+jiff
This metapackage enables feature "jiff" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        PDF document manipulation - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.11.0
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        PDF document manipulation - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        PDF document manipulation - feature "time"
Requires:       crate(%{pkgname})
Requires:       crate(time-0.3/default) >= 0.3.47
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/parsing) >= 0.3.47
Provides:       crate(%{pkgname}/time)

%description -n %{name}+time
This metapackage enables feature "time" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        PDF document manipulation - feature "tokio"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0/default) >= 1.0.0
Requires:       crate(tokio-1.0/fs) >= 1.0.0
Requires:       crate(tokio-1.0/io-util) >= 1.0.0
Provides:       crate(%{pkgname}/tokio)

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-js
Summary:        PDF document manipulation - feature "wasm_js"
Requires:       crate(%{pkgname})
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.4
Provides:       crate(%{pkgname}/wasm-js)

%description -n %{name}+wasm-js
This metapackage enables feature "wasm_js" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+async

%files -n %{name}+chrono

%files -n %{name}+default

%files -n %{name}+image

%files -n %{name}+jiff

%files -n %{name}+rayon

%files -n %{name}+serde

%files -n %{name}+time

%files -n %{name}+tokio

%files -n %{name}+wasm-js

%changelog
%{?autochangelog}
