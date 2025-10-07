#!/usr/bin/env python3

import subprocess
import argparse

RMADISON_PATH = "/usr/bin/rmadison"
APT_CACHE_PATH = "/usr/bin/apt-cache"


def main():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options]',
        description="Debian Deb Scraper",
    )
    _ = parser.add_argument('-a', '--arch', type=str, help="architecture to use", required=True)
    _ = parser.add_argument('-m', '--mirror', type=str, help="mirror to use", required=True)
    _ = parser.add_argument('-p', '--package', type=str, help="package to use", required=True)
    _ = parser.add_argument('-s', '--source', type=str, help="package source")

    args = parser.parse_args()
    arch: str = args.arch
    mirror: str = args.mirror
    package: str = args.package
    source: str = args.source

    # Get list of packages
    result = subprocess.run([RMADISON_PATH, "-a", arch, package], capture_output=True, text=True)

    if result.returncode != 0:
        print("No packages found")
        return

    packages = result.stdout

    if not source:
        p1 = subprocess.Popen([APT_CACHE_PATH, "show", package],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.DEVNULL)

        p2 = subprocess.Popen(["grep", "Source:"], stdin=p1.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()

        p3 = subprocess.Popen(["cut", "-d", " ", "-f", "2"],
                              stdin=p2.stdout,
                              stdout=subprocess.PIPE)
        p2.stdout.close()

        output, _ = p3.communicate()
        source = output.decode().strip()

    for package in packages.split("\n"):
        fields = package.split("|")
        if len(fields) != 4:
            continue

        name = fields[0].strip()
        version = fields[1].strip()

        for arch in fields[3].strip().split(","):

            if not source:
                source = "#FILL IT IN YOURSELF"

            arch = arch.strip()
            path = f"{mirror}/debian/pool/main/{source[0]}/{source}/{name}_{version}_{arch}.deb"

            print(path)


if __name__ == "__main__":
    main()
