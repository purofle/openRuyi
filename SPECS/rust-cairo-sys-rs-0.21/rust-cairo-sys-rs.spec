# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cairo-sys-rs
%global full_version 0.21.5
%global pkgname cairo-sys-rs-0.21

Name:           rust-cairo-sys-rs-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "cairo-sys-rs"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:06c28280c6b12055b5e39e4554271ae4e6630b27c0da9148c4cf6485fc6d245c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.183
Requires:       crate(system-deps-7.0/default) >= 7.0.7
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/freetype)
Provides:       crate(%{pkgname}/pdf)
Provides:       crate(%{pkgname}/png)
Provides:       crate(%{pkgname}/ps)
Provides:       crate(%{pkgname}/quartz-surface)
Provides:       crate(%{pkgname}/script)
Provides:       crate(%{pkgname}/svg)
Provides:       crate(%{pkgname}/v1-16)
Provides:       crate(%{pkgname}/v1-18)
Provides:       crate(%{pkgname}/xcb)

%description
Source code for takopackized Rust crate "cairo-sys-rs"

%package     -n %{name}+glib-sys
Summary:        FFI bindings to libcairo - feature "glib-sys" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(glib-sys-0.21/default) >= 0.21.5
Provides:       crate(%{pkgname}/glib-sys)
Provides:       crate(%{pkgname}/use-glib)

%description -n %{name}+glib-sys
This metapackage enables feature "glib-sys" for the Rust cairo-sys-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use_glib" feature.

%package     -n %{name}+windows-sys
Summary:        FFI bindings to libcairo - feature "windows-sys" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(windows-sys-0.52/default) >= 0.52
Requires:       crate(windows-sys-0.52/win32-graphics-gdi) >= 0.52
Provides:       crate(%{pkgname}/win32-surface)
Provides:       crate(%{pkgname}/windows-sys)

%description -n %{name}+windows-sys
This metapackage enables feature "windows-sys" for the Rust cairo-sys-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "win32-surface" feature.

%package     -n %{name}+x11
Summary:        FFI bindings to libcairo - feature "x11" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(x11-2.0/default) >= 2.16
Requires:       crate(x11-2.0/xlib) >= 2.16
Provides:       crate(%{pkgname}/x11)
Provides:       crate(%{pkgname}/xlib)

%description -n %{name}+x11
This metapackage enables feature "x11" for the Rust cairo-sys-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "xlib" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+glib-sys

%files -n %{name}+windows-sys

%files -n %{name}+x11

%changelog
%{?autochangelog}
