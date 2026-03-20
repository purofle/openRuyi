# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gimp
Version:        3.2.0
Release:        %autorelease
Summary:        GNU Image Manipulation Program
License:        LGPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND CC0-1.0
URL:            https://www.gimp.org
VCS:            git:https://gitlab.gnome.org/GNOME/gimp.git
#!RemoteAsset
Source0:        https://download.gimp.org/gimp/v3.2/gimp-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pkgconfig(atk) >= 2.4.0
BuildRequires:  pkgconfig(babl-0.1) >= 0.1.118
BuildRequires:  pkgconfig(cairo) >= 1.14.0
BuildRequires:  pkgconfig(fontconfig) >= 2.12.4
BuildRequires:  pkgconfig(freetype2) >= 2.1.7
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30.8
BuildRequires:  pkgconfig(gegl-0.4) >= 0.4.66
BuildRequires:  pkgconfig(exiv2) >= 0.27.4
BuildRequires:  pkgconfig(gexiv2) >= 0.14.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.70.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.70.0
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(harfbuzz) >= 2.8.2
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.6
BuildRequires:  pkgconfig(lcms2) >= 2.8
BuildRequires:  pkgconfig(libmypaint) >= 1.5.0
BuildRequires:  pkgconfig(mypaint-brushes-2.0)
BuildRequires:  pkgconfig(pango) >= 1.50.0
BuildRequires:  pkgconfig(pangocairo) >= 1.50.0
BuildRequires:  pkgconfig(pangoft2) >= 1.50.0
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.40.6
BuildRequires:  pkgconfig(appstream) >= 0.16.1
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(shared-mime-info)

%description
GIMP (GNU Image Manipulation Program) is a powerful image composition and
editing program, which can be extremely useful for creating logos and other
graphics for web pages. GIMP has many of the tools and filters you would expect
to find in similar commercial offerings, and some interesting extras as well.
GIMP provides a large image manipulation toolbox, including channel operations
and layers, effects, sub-pixel imaging and anti-aliasing, and conversions, all
with multi-level undo.

%changelog
%{?autochangelog}
