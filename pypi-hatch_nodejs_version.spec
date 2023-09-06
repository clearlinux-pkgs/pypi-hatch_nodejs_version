#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-hatch_nodejs_version
Version  : 0.3.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/af/b6/c9406cfa9edf740c6b3de6173408a159228eac0cee80eead4a5b9cc88848/hatch_nodejs_version-0.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/af/b6/c9406cfa9edf740c6b3de6173408a159228eac0cee80eead4a5b9cc88848/hatch_nodejs_version-0.3.2.tar.gz
Summary  : Hatch plugin for versioning from a package.json file
Group    : Development/Tools
License  : MIT
Requires: pypi-hatch_nodejs_version-license = %{version}-%{release}
Requires: pypi-hatch_nodejs_version-python = %{version}-%{release}
Requires: pypi-hatch_nodejs_version-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# hatch-nodejs-version
[![PyPI - Version](https://img.shields.io/pypi/v/hatch-nodejs-version.svg)](https://pypi.org/project/hatch-nodejs-version)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hatch-nodejs-version.svg)](https://pypi.org/project/hatch-nodejs-version)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

%package license
Summary: license components for the pypi-hatch_nodejs_version package.
Group: Default

%description license
license components for the pypi-hatch_nodejs_version package.


%package python
Summary: python components for the pypi-hatch_nodejs_version package.
Group: Default
Requires: pypi-hatch_nodejs_version-python3 = %{version}-%{release}

%description python
python components for the pypi-hatch_nodejs_version package.


%package python3
Summary: python3 components for the pypi-hatch_nodejs_version package.
Group: Default
Requires: python3-core
Provides: pypi(hatch_nodejs_version)
Requires: pypi(hatchling)

%description python3
python3 components for the pypi-hatch_nodejs_version package.


%prep
%setup -q -n hatch_nodejs_version-0.3.2
cd %{_builddir}/hatch_nodejs_version-0.3.2
pushd ..
cp -a hatch_nodejs_version-0.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694011297
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-hatch_nodejs_version
cp %{_builddir}/hatch_nodejs_version-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-hatch_nodejs_version/53a354d580da90aae965cade415b998ffd6612e4 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-hatch_nodejs_version/53a354d580da90aae965cade415b998ffd6612e4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
