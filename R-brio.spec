#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-brio
Version  : 1.1.0
Release  : 3
URL      : https://cran.r-project.org/src/contrib/brio_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/brio_1.1.0.tar.gz
Summary  : Basic R Input Output
Group    : Development/Tools
License  : MIT
Requires: R-brio-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
read and write UTF-8 (8-bit Unicode Transformation Format) files and provide
  more explicit control over line endings.

%package lib
Summary: lib components for the R-brio package.
Group: Libraries

%description lib
lib components for the R-brio package.


%prep
%setup -q -c -n brio
cd %{_builddir}/brio

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603306996

%install
export SOURCE_DATE_EPOCH=1603306996
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library brio
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library brio
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library brio
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc brio || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/brio/DESCRIPTION
/usr/lib64/R/library/brio/INDEX
/usr/lib64/R/library/brio/LICENSE
/usr/lib64/R/library/brio/Meta/Rd.rds
/usr/lib64/R/library/brio/Meta/features.rds
/usr/lib64/R/library/brio/Meta/hsearch.rds
/usr/lib64/R/library/brio/Meta/links.rds
/usr/lib64/R/library/brio/Meta/nsInfo.rds
/usr/lib64/R/library/brio/Meta/package.rds
/usr/lib64/R/library/brio/NAMESPACE
/usr/lib64/R/library/brio/NEWS.md
/usr/lib64/R/library/brio/R/brio
/usr/lib64/R/library/brio/R/brio.rdb
/usr/lib64/R/library/brio/R/brio.rdx
/usr/lib64/R/library/brio/help/AnIndex
/usr/lib64/R/library/brio/help/aliases.rds
/usr/lib64/R/library/brio/help/brio.rdb
/usr/lib64/R/library/brio/help/brio.rdx
/usr/lib64/R/library/brio/help/paths.rds
/usr/lib64/R/library/brio/html/00Index.html
/usr/lib64/R/library/brio/html/R.css
/usr/lib64/R/library/brio/tests/testthat.R
/usr/lib64/R/library/brio/tests/testthat/test-file_line_endings.R
/usr/lib64/R/library/brio/tests/testthat/test-readLines.R
/usr/lib64/R/library/brio/tests/testthat/test-read_file.R
/usr/lib64/R/library/brio/tests/testthat/test-read_file_raw.R
/usr/lib64/R/library/brio/tests/testthat/test-read_lines.R
/usr/lib64/R/library/brio/tests/testthat/test-writeLines.R
/usr/lib64/R/library/brio/tests/testthat/test-write_file.R
/usr/lib64/R/library/brio/tests/testthat/test-write_lines.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/brio/libs/brio.so
