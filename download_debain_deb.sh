#!/usr/bin/env bash

PACKAGES=(
    'comerr-dev' 'heimdal-multidev' 'lib32z1-dev' 'libbrotli-dev' 'libc6-dev' 'libcap-dev' 'libcrypto++-dev' 'libcurl4-gnutls-dev' 'libcurl4-openssl-dev' 'libffi-dev' 'libgmp-dev' 'libgnutls28-dev' 'libidn2-dev' 'libkeyutils-dev' 'libldap-dev' 'libnghttp2-dev' 'libpcre2-dev' 'libplib-dev' 'libprotobuf-dev' 'libpsl-dev' 'librtmp-dev' 'libsasl2-dev' 'libselinux1-dev' 'libsdl2-dev' 'libssh-dev' 'libssl-dev' 'libtasn1-6-dev' 'libunistring-dev' 'libx32z1-dev' 'libzstd-dev' 'musl-dev' 'nettle-dev' 'uuid-dev' 'zlib1g-dev'
)


for package in "${PACKAGES[@]}"
do
    python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p ${package} -m "https://mirror.sg.gs"
done

python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libcurl4-nss-dev" -s "curl" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libssh-gcrypt-dev" -s "libssh" -m "https://mirror.sg.gs"

python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libc++-9-dev" -s "llvm-toolchain-9" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libc++-11-dev" -s "llvm-toolchain-11" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libc++-13-dev" -s "llvm-toolchain-13" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libc++-14-dev" -s "llvm-toolchain-14" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libc++-15-dev" -s "llvm-toolchain-15" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libc++-16-dev" -s "llvm-toolchain-16" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libc++-17-dev" -s "llvm-toolchain-17" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libc++-18-dev" -s "llvm-toolchain-18" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libc++-19-dev" -s "llvm-toolchain-19" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libc++-20-dev" -s "llvm-toolchain-20" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libc++-21-dev" -s "llvm-toolchain-21" -m "https://mirror.sg.gs"

python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libstdc++-9-dev" -s "gcc-9" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libstdc++-10-dev" -s "gcc-10" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libstdc++-11-dev" -s "gcc-11" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libstdc++-12-dev" -s "gcc-12" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libstdc++-13-dev" -s "gcc-13" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libstdc++-14-dev" -s "gcc-14" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libstdc++-15-dev" -s "gcc-15" -m "https://mirror.sg.gs"

python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libgcc-9-dev" -s "gcc-9" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libgcc-10-dev" -s "gcc-10" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libgcc-11-dev" -s "gcc-11" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libgcc-12-dev" -s "gcc-12" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libgcc-13-dev" -s "gcc-13" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libgcc-14-dev" -s "gcc-14" -m "https://mirror.sg.gs"
python3 debian-deb-scraper.py -a "amd64,i386,arm64,armhf" -p "libgcc-15-dev" -s "gcc-15" -m "https://mirror.sg.gs"
