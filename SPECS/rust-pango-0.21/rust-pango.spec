# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pango
%global full_version 0.21.5
%global pkgname pango-0.21

Name:           rust-pango-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "pango"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:52d1d85e2078077a065bb7fc072783d5bcd4e51b379f22d67107d0a16937eb69
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gio-0.21/default) >= 0.21.5
Requires:       crate(glib-0.21/default) >= 0.21.5
Requires:       crate(libc-0.2/default) >= 0.2.183
Requires:       crate(pango-sys-0.21/default) >= 0.21.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "pango"

%package     -n %{name}+v1-42
Summary:        Rust bindings for the Pango library - feature "v1_42"
Requires:       crate(%{pkgname})
Requires:       crate(pango-sys-0.21/v1-42) >= 0.21.5
Provides:       crate(%{pkgname}/v1-42)

%description -n %{name}+v1-42
This metapackage enables feature "v1_42" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-44
Summary:        Rust bindings for the Pango library - feature "v1_44"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/v1-42)
Requires:       crate(pango-sys-0.21/v1-44) >= 0.21.5
Provides:       crate(%{pkgname}/v1-44)

%description -n %{name}+v1-44
This metapackage enables feature "v1_44" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-46
Summary:        Rust bindings for the Pango library - feature "v1_46"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/v1-44)
Requires:       crate(pango-sys-0.21/v1-46) >= 0.21.5
Provides:       crate(%{pkgname}/v1-46)

%description -n %{name}+v1-46
This metapackage enables feature "v1_46" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-48
Summary:        Rust bindings for the Pango library - feature "v1_48"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/v1-46)
Requires:       crate(pango-sys-0.21/v1-48) >= 0.21.5
Provides:       crate(%{pkgname}/v1-48)

%description -n %{name}+v1-48
This metapackage enables feature "v1_48" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-50
Summary:        Rust bindings for the Pango library - feature "v1_50"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/v1-48)
Requires:       crate(pango-sys-0.21/v1-50) >= 0.21.5
Provides:       crate(%{pkgname}/v1-50)

%description -n %{name}+v1-50
This metapackage enables feature "v1_50" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-52
Summary:        Rust bindings for the Pango library - feature "v1_52"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/v1-50)
Requires:       crate(pango-sys-0.21/v1-52) >= 0.21.5
Provides:       crate(%{pkgname}/v1-52)

%description -n %{name}+v1-52
This metapackage enables feature "v1_52" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-54
Summary:        Rust bindings for the Pango library - feature "v1_54"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/v1-52)
Requires:       crate(pango-sys-0.21/v1-54) >= 0.21.5
Provides:       crate(%{pkgname}/v1-54)

%description -n %{name}+v1-54
This metapackage enables feature "v1_54" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-56
Summary:        Rust bindings for the Pango library - feature "v1_56"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/v1-54)
Requires:       crate(pango-sys-0.21/v1-56) >= 0.21.5
Provides:       crate(%{pkgname}/v1-56)

%description -n %{name}+v1-56
This metapackage enables feature "v1_56" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-57
Summary:        Rust bindings for the Pango library - feature "v1_57"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/v1-56)
Requires:       crate(pango-sys-0.21/v1-57) >= 0.21.5
Provides:       crate(%{pkgname}/v1-57)

%description -n %{name}+v1-57
This metapackage enables feature "v1_57" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%files -n %{name}+v1-42

%files -n %{name}+v1-44

%files -n %{name}+v1-46

%files -n %{name}+v1-48

%files -n %{name}+v1-50

%files -n %{name}+v1-52

%files -n %{name}+v1-54

%files -n %{name}+v1-56

%files -n %{name}+v1-57

%changelog
%{?autochangelog}
