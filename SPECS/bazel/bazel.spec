# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bazel
Version:        9.1.1
Release:        %autorelease
Summary:        Fast, scalable, multi-language and extensible build system
License:        Apache-2.0
URL:            https://github.com/bazelbuild/bazel
#!RemoteAsset:  sha256:a6f66e26c8f4ca04fa83c796a404eff0544bd78336fbbcd122c9e10cbec4a5d7
Source:         https://github.com/bazelbuild/bazel/releases/download/%{version}/bazel-%{version}-dist.zip

BuildRequires:  java-21-openjdk
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  python3

%description
Build and test software of any size, quickly and reliably.

%prep
%autosetup -p0 -C -n %{name}-%{version}

%build
export EXTRA_BAZEL_ARGS="--tool_java_runtime_version=local_jdk"
bash ./compile.sh

%install
install -D --m 0755 output/bazel %{buildroot}%{_bindir}/bazel

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/bazel

%changelog
%autochangelog
