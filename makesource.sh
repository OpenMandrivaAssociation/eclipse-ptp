#!/bin/sh
# Build the ptp and photran source tarballs.
#
# Get some variables from the specfile
eval `awk '$1 == "%global" { print $2 "=" $3 }' eclipse-ptp.spec`

# Checkout and create ptp tarball
[ ! -d org.eclipse.ptp ] && git clone git://git.eclipse.org/gitroot/ptp/org.eclipse.ptp.git
pushd org.eclipse.ptp
git pull
git archive --prefix org.eclipse.ptp-$ptp_git_tag/ $ptp_git_tag | xz -c > ../org.eclipse.ptp-${ptp_git_tag}.tar.xz
popd

# Checkout and create photran tarball
[ ! -d org.eclipse.photran ] && git clone git://git.eclipse.org/gitroot/ptp/org.eclipse.photran.git
pushd org.eclipse.photran
git pull
git archive --prefix org.eclipse.photran-$photran_git_tag/ $photran_git_tag | xz -c > ../org.eclipse.photran-${photran_git_tag}.tar.xz
popd
