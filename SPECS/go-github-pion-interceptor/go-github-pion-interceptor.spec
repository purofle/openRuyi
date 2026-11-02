# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           interceptor
%define go_import_path  github.com/pion/interceptor
%define go_test_exclude %{go_import_path}

Name:           go-github-pion-interceptor
Version:        0.1.51
Release:        %autorelease
Summary:        RTCP and RTCP processors for building real time communications
License:        MIT
URL:            https://github.com/pion/interceptor
#!RemoteAsset:  sha256:a721be3f44d0ff9e258f0817e4bc3f03f3ace3fc45942622df185f8bbadff629
Source0:        https://github.com/pion/interceptor/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pion/logging)
BuildRequires:  go(github.com/pion/rtcp)
BuildRequires:  go(github.com/pion/rtp)
BuildRequires:  go(github.com/pion/transport/v3)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/pion/interceptor) = %{version}

Requires:       go(github.com/pion/logging)
Requires:       go(github.com/pion/rtcp)
Requires:       go(github.com/pion/rtp)

%description
Interceptor is a framework for building RTP/RTCP communication software. This
framework defines a interface that each interceptor must satisfy. These
interceptors are then run sequentially. We also then provide common
interceptors that will be useful for building RTC software.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
