#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libb64
Version  : 1.2
Release  : 4
URL      : http://download.draios.com/dependencies/libb64-1.2.src.zip
Source0  : http://download.draios.com/dependencies/libb64-1.2.src.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain
Patch1: build.patch

%description
b64: Base64 Encoding/Decoding Routines
======================================
Overview:
--------
libb64 is a library of ANSI C routines for fast encoding/decoding data into and
from a base64-encoded format. C++ wrappers are included, as well as the source
code for standalone encoding and decoding executables.

%package dev
Summary: dev components for the libb64 package.
Group: Development
Provides: libb64-devel

%description dev
dev components for the libb64 package.


%prep
%setup -q -n libb64-1.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506438066
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1506438066
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/b64/cdecode.h
/usr/include/b64/cencode.h
/usr/include/b64/decode.h
/usr/include/b64/encode.h
/usr/lib64/*.a
