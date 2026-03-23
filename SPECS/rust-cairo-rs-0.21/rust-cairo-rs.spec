# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cairo-rs
%global full_version 0.21.5
%global pkgname cairo-rs-0.21

Name:           rust-cairo-rs-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "cairo-rs"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:b01fe135c0bd16afe262b6dea349bd5ea30e6de50708cec639aae7c5c14cc7e4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(cairo-sys-rs-0.21/default) >= 0.21.5
Requires:       crate(libc-0.2/default) >= 0.2.183
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "cairo-rs"

%package     -n %{name}+freetype
Summary:        Rust bindings for the Cairo library - feature "freetype"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/freetype-rs)
Requires:       crate(cairo-sys-rs-0.21/freetype) >= 0.21.5
Provides:       crate(%{pkgname}/freetype)

%description -n %{name}+freetype
This metapackage enables feature "freetype" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+freetype-rs
Summary:        Rust bindings for the Cairo library - feature "freetype-rs"
Requires:       crate(%{pkgname})
Requires:       crate(freetype-rs-0.38/default) >= 0.38.0
Provides:       crate(%{pkgname}/freetype-rs)

%description -n %{name}+freetype-rs
This metapackage enables feature "freetype-rs" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+glib
Summary:        Rust bindings for the Cairo library - feature "glib"
Requires:       crate(%{pkgname})
Requires:       crate(glib-0.21/default) >= 0.21.5
Provides:       crate(%{pkgname}/glib)

%description -n %{name}+glib
This metapackage enables feature "glib" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pdf
Summary:        Rust bindings for the Cairo library - feature "pdf"
Requires:       crate(%{pkgname})
Requires:       crate(cairo-sys-rs-0.21/pdf) >= 0.21.5
Provides:       crate(%{pkgname}/pdf)

%description -n %{name}+pdf
This metapackage enables feature "pdf" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+png
Summary:        Rust bindings for the Cairo library - feature "png"
Requires:       crate(%{pkgname})
Requires:       crate(cairo-sys-rs-0.21/png) >= 0.21.5
Provides:       crate(%{pkgname}/png)

%description -n %{name}+png
This metapackage enables feature "png" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ps
Summary:        Rust bindings for the Cairo library - feature "ps"
Requires:       crate(%{pkgname})
Requires:       crate(cairo-sys-rs-0.21/ps) >= 0.21.5
Provides:       crate(%{pkgname}/ps)

%description -n %{name}+ps
This metapackage enables feature "ps" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quartz-surface
Summary:        Rust bindings for the Cairo library - feature "quartz-surface"
Requires:       crate(%{pkgname})
Requires:       crate(cairo-sys-rs-0.21/quartz-surface) >= 0.21.5
Provides:       crate(%{pkgname}/quartz-surface)

%description -n %{name}+quartz-surface
This metapackage enables feature "quartz-surface" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+script
Summary:        Rust bindings for the Cairo library - feature "script"
Requires:       crate(%{pkgname})
Requires:       crate(cairo-sys-rs-0.21/script) >= 0.21.5
Provides:       crate(%{pkgname}/script)

%description -n %{name}+script
This metapackage enables feature "script" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+svg
Summary:        Rust bindings for the Cairo library - feature "svg"
Requires:       crate(%{pkgname})
Requires:       crate(cairo-sys-rs-0.21/svg) >= 0.21.5
Provides:       crate(%{pkgname}/svg)

%description -n %{name}+svg
This metapackage enables feature "svg" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-glib
Summary:        Rust bindings for the Cairo library - feature "use_glib" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/glib)
Requires:       crate(cairo-sys-rs-0.21/use-glib) >= 0.21.5
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/use-glib)

%description -n %{name}+use-glib
This metapackage enables feature "use_glib" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+v1-16
Summary:        Rust bindings for the Cairo library - feature "v1_16"
Requires:       crate(%{pkgname})
Requires:       crate(cairo-sys-rs-0.21/v1-16) >= 0.21.5
Provides:       crate(%{pkgname}/v1-16)

%description -n %{name}+v1-16
This metapackage enables feature "v1_16" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-18
Summary:        Rust bindings for the Cairo library - feature "v1_18"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/v1-16)
Requires:       crate(cairo-sys-rs-0.21/v1-18) >= 0.21.5
Provides:       crate(%{pkgname}/v1-18)

%description -n %{name}+v1-18
This metapackage enables feature "v1_18" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+win32-surface
Summary:        Rust bindings for the Cairo library - feature "win32-surface"
Requires:       crate(%{pkgname})
Requires:       crate(cairo-sys-rs-0.21/win32-surface) >= 0.21.5
Provides:       crate(%{pkgname}/win32-surface)

%description -n %{name}+win32-surface
This metapackage enables feature "win32-surface" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xcb
Summary:        Rust bindings for the Cairo library - feature "xcb"
Requires:       crate(%{pkgname})
Requires:       crate(cairo-sys-rs-0.21/xcb) >= 0.21.5
Provides:       crate(%{pkgname}/xcb)

%description -n %{name}+xcb
This metapackage enables feature "xcb" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xlib
Summary:        Rust bindings for the Cairo library - feature "xlib"
Requires:       crate(%{pkgname})
Requires:       crate(cairo-sys-rs-0.21/xlib) >= 0.21.5
Provides:       crate(%{pkgname}/xlib)

%description -n %{name}+xlib
This metapackage enables feature "xlib" for the Rust cairo-rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+freetype

%files -n %{name}+freetype-rs

%files -n %{name}+glib

%files -n %{name}+pdf

%files -n %{name}+png

%files -n %{name}+ps

%files -n %{name}+quartz-surface

%files -n %{name}+script

%files -n %{name}+svg

%files -n %{name}+use-glib

%files -n %{name}+v1-16

%files -n %{name}+v1-18

%files -n %{name}+win32-surface

%files -n %{name}+xcb

%files -n %{name}+xlib

%changelog
%{?autochangelog}
