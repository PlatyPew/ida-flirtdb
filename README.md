# IDA Flirt Database

Tool that converts Linux libraries into sig files for IDA

## Usage

This is only for ubuntu packages.
The packages of other operating systems have to be done manually.

```bash
python3 generate-sig
```

```text
usage: generate-sig.py [options]
generate-sig.py: error: the following arguments are required: -a/--arch, -p/--package
```

You need the flair directory to have these 3 commands

```
flair
├── pelf
├── sigmake
└── zipsig
```

### Misc

You may need to adjust the location of `ar` and `tar` to fit your needs

## Packages installed

### Ubuntu

| Architecture       | Package Name         | Pat |
| ------------------ | -------------------- | --- |
| amd64, i386, amd64 | comerr-dev           |     |
| amd64, i386, amd64 | heimdal-multidev     |     |
| amd64, i386        | lib32z1-dev          |     |
| amd64, i386        | libbrotli-dev        |     |
| amd64, i386, amd64 | libc6-dev            | ✅  |
| amd64, i386, amd64 | libcap-dev           |     |
| amd64, i386, amd64 | libcrypto++-dev      |     |
| amd64, i386, amd64 | libcurl4-gnutls-dev  |     |
| amd64, i386, amd64 | libcurl4-nss-dev     |     |
| amd64, i386, amd64 | libstdc++-5-dev      |     |
| amd64, i386, amd64 | libstdc++-6-dev      |     |
| amd64, i386, amd64 | libstdc++-7-dev      |     |
| amd64, i386, amd64 | libstdc++-8-dev      |     |
| amd64, i386, amd64 | libstdc++-9-dev      |     |
| amd64, i386, amd64 | libstdc++-10-dev     |     |
| amd64, i386, amd64 | libstdc++-11-dev     |     |
| amd64, i386, amd64 | libstdc++-12-dev     |     |
| amd64, i386, amd64 | libstdc++-13-dev     |     |
| amd64, i386, amd64 | libstdc++-14-dev     |     |
| amd64, i386, amd64 | libcurl4-openssl-dev |     |
| amd64, i386, amd64 | libffi-dev           |     |
| amd64, i386, amd64 | libgcc-7-dev         |     |
| amd64, i386, amd64 | libgcc-8-dev         |     |
| amd64, i386, amd64 | libgcc-9-dev         |     |
| amd64, i386, amd64 | libgcc-10-dev        |     |
| amd64, i386, amd64 | libgcc-11-dev        |     |
| amd64, i386, amd64 | libgcc-12-dev        |     |
| amd64, i386, amd64 | libgcc-13-dev        |     |
| amd64, i386, amd64 | libgcc-14-dev        |     |
| amd64, i386, amd64 | libgmp-dev           |     |
| amd64, i386, amd64 | libgnutls28-dev      |     |
| amd64, i386, amd64 | libidn2-dev          |     |
| amd64, i386, amd64 | libkeyutils-dev      |     |
| amd64, i386, amd64 | libldap-dev          |     |
| amd64, i386, amd64 | libnghttp2-dev       |     |
| amd64, i386, amd64 | libpcre2-dev         | ✅  |
| amd64, i386, amd64 | libplib-dev          |     |
| amd64, i386, amd64 | libprotobuf-dev      | ✅  |
| amd64, i386, amd64 | libpsl-dev           |     |
| amd64, i386, amd64 | librtmp-dev          |     |
| amd64, i386, amd64 | libsasl2-dev         |     |
| amd64, i386, amd64 | libselinux1-dev      |     |
| amd64, i386, amd64 | libssh-dev           |     |
| amd64, i386, amd64 | libssh-gcrypt-dev    |     |
| amd64, i386, amd64 | libssl-dev           |     |
| amd64, i386, amd64 | libtasn1-6-dev       |     |
| amd64, i386, amd64 | libunistring-dev     |     |
| amd64, i386, amd64 | libzstd-dev          |     |
| amd64, i386, amd64 | musl-dev             | ✅  |
| amd64, i386, amd64 | nettle-dev           |     |
| amd64, i386, amd64 | uuid-dev             |     |
| amd64, i386, amd64 | zlib1g-dev           |     |

### Debian

| Architecture       | Package Name       | Pat |
| ------------------ | ------------------ | --- |
| amd64, i386, amd64 | libc6-dev          | ✅  |
| amd64, i386, amd64 | libgcc-6-dev       | ✅  |
| amd64, i386, amd64 | libgcc-7-dev       | ✅  |
| amd64, i386, amd64 | libgcc-8-dev       | ✅  |
| amd64, i386, amd64 | libgcc-9-dev       | ✅  |
| amd64, i386, amd64 | libgcc-10-dev      | ✅  |
| amd64, i386, amd64 | libgcc-11-dev      | ✅  |
| amd64, i386, amd64 | libgcc-12-dev      | ✅  |
| amd64, i386, amd64 | libgcc-13-dev      | ✅  |
| amd64, i386, amd64 | libgcc-14-dev      | ✅  |
| amd64, i386, amd64 | libcstdc++-6--dev  | ✅  |
| amd64, i386, amd64 | libcstdc++-7--dev  | ✅  |
| amd64, i386, amd64 | libcstdc++-8--dev  | ✅  |
| amd64, i386, amd64 | libcstdc++-9--dev  | ✅  |
| amd64, i386, amd64 | libcstdc++-10--dev | ✅  |
| amd64, i386, amd64 | libcstdc++-11--dev | ✅  |
| amd64, i386, amd64 | libcstdc++-12--dev | ✅  |
| amd64, i386, amd64 | libcstdc++-13--dev | ✅  |
| amd64, i386, amd64 | libcstdc++-14--dev | ✅  |
