#!/bin/bash

# Ubuntu distributions
DISTRS=(bionic cosmic)
PPA="zeal-developers/ppa"

function failure {
    echo -e "\033[1mERROR:\033[0m \E[31m$1\033[0m"
    exit 1
}

if [ "$#" -ne 1 ]; then
    echo "Version required"
    exit 1
fi

ZEAL_VER=$1

SRC_TARBALL="zeal_$ZEAL_VER.orig.tar.gz"
SRC_DIR="zeal-$ZEAL_VER"

curl -L -o "$SRC_TARBALL" https://github.com/zealdocs/zeal/archive/v$ZEAL_VER.tar.gz
[ ! -f "$SRC_TARBALL" ] && failure "Cannot download tarball"

# TODO: dch -v

upload_tarball=true

for DISTR in ${DISTRS[@]}
do
    echo "Preparing $DISTR package..."

    tar xzf "$SRC_TARBALL"
    cp -r debian "$SRC_DIR"

    sed -i -- "s/#DISTR#/$DISTR/g" "$SRC_DIR"/debian/changelog

    cd "$SRC_DIR"
    if [ "$upload_tarball" = true ] ; then
        upload_tarball=false
        debuild -S -sa
    else
        debuild -S -sd
    fi
    cd ..

    dput "ppa:$PPA" "zeal_$ZEAL_VER-1ppa1~${DISTR}1_source.changes"

    rm -rf "$SRC_DIR"

    read -p "Press any key to continue... "
done
