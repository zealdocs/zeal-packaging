#!/bin/bash

# Ubuntu distributions
DISTRS=(trusty utopic vivid)
PPA="zeal-developers/ppa"

# TODO: Ask version
#if [ "$#" -ne 1 ]; then
#    echo "Version required"
#    exit 1
#fi

ZEAL_VER=0.1.0

SRC_TARBALL="zeal_$ZEAL_VER.orig.tar.gz"
SRC_DIR="zeal-$ZEAL_VER"

curl -L -o "$SRC_TARBALL" https://github.com/zealdocs/zeal/archive/v$ZEAL_VER.tar.gz

# TODO: dch -v

for DISTR in ${DISTRS[@]}
do
    echo "Preparing $DISTR package..."

    tar xzf "$SRC_TARBALL"
    cp -r debian "$SRC_DIR"

    sed -i -- "s/#DISTR#/$DISTR/g" "$SRC_DIR"/debian/changelog

    cd "$SRC_DIR"
    debuild -S -sa
    cd ..

    dput "ppa:$PPA" "zeal_$ZEAL_VER-1ppa1~${DISTR}1_source.changes"

    rm -rf "$SRC_DIR"

    read -p "Press any key to continue... "
done
