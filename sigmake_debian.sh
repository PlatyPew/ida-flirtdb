#!/usr/bin/env bash

PACKAGES=(
    comerr-dev heimdal-multidev lib32z1-dev libbrotli-dev libc++ libc6-dev libcap-dev libcrypto++-dev libcurl4-gnutls-dev libcurl4-nss-dev libcurl4-openssl-dev libffi-dev libgcc libgmp-dev libgnutls28-dev libidn2-dev libkeyutils-dev libldap-dev libnghttp2-dev libpcre2-dev libplib-dev libprotobuf-dev libpsl-dev librtmp-dev libsasl2-dev libsdl2-dev libselinux1-dev libssh-dev libssh-gcrypt-dev libssl-dev libstdc++ libtasn1-6-dev libunistring-dev libx32z1-dev libzstd-dev musl-dev nettle-dev uuid-dev zlib1g-dev
)


for package in "${PACKAGES[@]}"
do
    python3 generate-sig.py -d debian -a amd64 -p ${package}
    python3 generate-sig.py -d debian -a i386 -p ${package}
    python3 generate-sig.py -d debian -a arm64 -p ${package}
    python3 generate-sig.py -d debian -a armhf -p ${package}
done
