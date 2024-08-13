# IDA Flirt Database

Tool that converts Linux libraries into sig files for IDA

## Usage

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

- `comerr-dev`
- `heimdal-multidev`
- `lib32z1-dev`
- `libbrotli-dev`
- `libc6-dev`
- `libcap-dev`
- `libcrypto++-dev`
- `libcurl4-gnutls-dev`
- `libcurl4-nss-dev`
- `libstdc++`
    - `libstdc++-5-dev`
    - `libstdc++-6-dev`
    - `libstdc++-7-dev`
    - `libstdc++-8-dev`
    - `libstdc++-9-dev`
    - `libstdc++-10-dev`
    - `libstdc++-11-dev`
    - `libstdc++-12-dev`
    - `libstdc++-13-dev`
    - `libstdc++-14-dev`
- `libcurl4-openssl-dev`
- `libffi-dev`
- `libgcc`
    - `libgcc-7-dev`
    - `libgcc-8-dev`
    - `libgcc-9-dev`
    - `libgcc-10-dev`
    - `libgcc-11-dev`
    - `libgcc-12-dev`
    - `libgcc-13-dev`
    - `libgcc-14-dev`
- `libgmp-dev`
- `libgnutls28-dev`
- `libidn2-dev`
- `libidn2-dev`
- `libkeyutils-dev`
- `libldap-dev`
- `libnghttp2-dev`
- `libpcre2-dev`
- `libpli-dev`
- `libprotobuf-dev`
- `libpsl-dev`
- `librtmp-dev`
- `libsasl2-dev`
- `libselinux1-dev`
- `libssh-dev`
- `libssh-gcrypt-dev`
- `libssl-dev`
- `libtasn1-6-dev`
- `libunistring-dev`
- `libzstd-dev`
- `musl-dev`
- `nettle-dev`
- `uuid-dev`
- `zlib1g-dev`
