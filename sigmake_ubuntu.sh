#!/usr/bin/env bash

PACKAGES=(
    'comerr-dev' 'heimdal-multidev' 'lib32z1-dev' 'libbrotli-dev' 'libc6-dev' 'libcap-dev' 'libcrypto-dev' 'libcrypto++-dev' 'libcurl4-gnutls-dev' 'libcurl4-nss-dev' 'libc++-7-dev' 'libc++-8-dev' 'libc++-9-dev' 'libc++-10-dev' 'libc++-11-dev' 'libc++-12-dev' 'libc++-13-dev' 'libc++-14-dev' 'libc++-15-dev' 'libc++-16-dev' 'libc++-17-dev' 'libc++-18-dev' 'libc++-19-dev' 'libstdc++-5-dev' 'libstdc++-6-dev' 'libstdc++-7-dev' 'libstdc++-8-dev' 'libstdc++-9-dev' 'libstdc++-10-dev' 'libstdc++-11-dev' 'libstdc++-12-dev' 'libstdc++-13-dev' 'libstdc++-14-dev' 'libstdc++-15-dev' 'libcurl4-openssl-dev' 'libffi-dev' 'libgcc-7-dev' 'libgcc-8-dev' 'libgcc-9-dev' 'libgcc-10-dev' 'libgcc-11-dev' 'libgcc-12-dev' 'libgcc-113-dev' 'libgcc-14-dev' 'libgcc-15-dev' 'libgmp-dev' 'libgnutls28-dev' 'libidn2-dev' 'libkeyutils-dev' 'libldap-dev' 'libnghttp2-dev' 'libpcre2-dev' 'libplib-dev' 'libprotobuf-dev' 'libpsl-dev' 'librtmp-dev' 'libsasl2-dev' 'libselinux1-dev' 'libsdl2-dev' 'libssh-dev' 'libssh-gcrypt-dev' 'libssl-dev' 'libtasn1-6-dev' 'libunistring-dev' 'libx32z1-dev' 'libzstd-dev' 'musl-dev' 'nettle-dev' 'uuid-dev' 'zlib1g-dev'
)


for package in "${PACKAGES[@]}"
do
    python3 generate-sig.py -a amd64 -p ${package}
    python3 generate-sig.py -a i386 -p ${package}
    python3 generate-sig.py -a arm64 -p ${package}
    python3 generate-sig.py -a armhf -p ${package}
done
