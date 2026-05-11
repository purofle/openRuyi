# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           librsvg
Version:        2.61.4
Release:        %autorelease
Summary:        SVG rendering library implemented in Rust
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/librsvg
VCS:            git:https://gitlab.gnome.org/GNOME/librsvg.git
#!RemoteAsset:  sha256:fca0ea28d1f28f95c8407d2579f4702dac085e7c758644daca8b40d1e072ca0c
Source0:        https://download.gnome.org/sources/librsvg/2.61/librsvg-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  python-docutils
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-png)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(cairo-svg)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  crate(cairo-rs-0.21/default) >= 0.21.0
BuildRequires:  crate(cairo-rs-0.21/pdf) >= 0.21.0
BuildRequires:  crate(cairo-rs-0.21/png) >= 0.21.0
BuildRequires:  crate(cairo-rs-0.21/ps) >= 0.21.0
BuildRequires:  crate(cairo-rs-0.21/svg) >= 0.21.0
BuildRequires:  crate(cairo-rs-0.21/v1-16) >= 0.21.0
BuildRequires:  crate(cast-0.3/default) >= 0.3.0
BuildRequires:  crate(clap-4.0/default) >= 4.0.17
BuildRequires:  crate(clap-complete-4.0/default) >= 4.0.5
BuildRequires:  crate(assert-cmd-2.1/default) >= 4.0.5
BuildRequires:  crate(chrono-0.4/default) >= 0.4.23
BuildRequires:  crate(cssparser-0.35/default) >= 0.35.0
BuildRequires:  crate(cssparser-color-0.3/default) >= 0.3.0
BuildRequires:  crate(data-url-0.3/default) >= 0.3.0
BuildRequires:  crate(encoding-rs-0.8/default) >= 0.8.32
BuildRequires:  crate(float-cmp-0.10/default) >= 0.10.0
BuildRequires:  crate(gio-0.21/default) >= 0.21.0
BuildRequires:  crate(glib-0.21/default) >= 0.21.0
BuildRequires:  crate(image-0.25/gif) >= 0.25.0
BuildRequires:  crate(image-0.25/jpeg) >= 0.25.0
BuildRequires:  crate(image-0.25/png) >= 0.25.0
BuildRequires:  crate(image-0.25/webp) >= 0.25.0
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(language-tags-0.3/default) >= 0.3.1
BuildRequires:  crate(libc-0.2/default) >= 0.2.0
BuildRequires:  crate(locale-config-0.3/default) >= 0.3.0
BuildRequires:  crate(markup5ever-0.35/default) >= 0.35.0
BuildRequires:  crate(nalgebra-0.33/default) >= 0.33.0
BuildRequires:  crate(num-traits-0.2/default) >= 0.2.0
BuildRequires:  crate(pango-0.21/default) >= 0.21.0
BuildRequires:  crate(pango-0.21/v1-46) >= 0.21.0
BuildRequires:  crate(pangocairo-0.21/default) >= 0.21.0
BuildRequires:  crate(precomputed-hash-0.1/default) >= 0.1.1
BuildRequires:  crate(rayon-1.0/default) >= 1.0.0
BuildRequires:  crate(rctree-0.6/default) >= 0.6.0
BuildRequires:  crate(regex-1.0/default) >= 1.7.1
BuildRequires:  crate(rgb-0.8/argb) >= 0.8.0
BuildRequires:  crate(rgb-0.8/default) >= 0.8.0
BuildRequires:  crate(selectors-0.31/default) >= 0.31.0
BuildRequires:  crate(string-cache-0.9/default) >= 0.9.0
BuildRequires:  crate(system-deps-7.0/default) >= 7.0.0
BuildRequires:  crate(tinyvec-1.0/alloc) >= 1.2.0
BuildRequires:  crate(tinyvec-1.0/default) >= 1.2.0
BuildRequires:  crate(tinyvec-1.0/rustc-1-55) >= 1.2.0
BuildRequires:  crate(url-2.0/default) >= 2.0.0
BuildRequires:  crate(xml5ever-0.35/default) >= 0.35.0

%description
Librsvg is a high-performance SVG rendering library written in Rust. It
provides a C API for rendering SVG documents to Cairo surfaces.

This package builds the shared librsvg library and exports the
`librsvg-2.0.pc` pkg-config file for consumers.

%package        devel
Summary:        Development files for librsvg
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers, linker symlink, and pkg-config metadata for librsvg.

%prep -a
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF

rm -rf Cargo.lock

%files
%license COPYING.LIB
%doc AUTHORS NEWS README.md
%{_libdir}/librsvg-2.so.*

%files devel
%{_includedir}/librsvg-2.0/
%{_libdir}/librsvg-2.so
%{_libdir}/pkgconfig/librsvg-2.0.pc

%changelog
%autochangelog
