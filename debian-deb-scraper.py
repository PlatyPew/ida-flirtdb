#!/usr/bin/env python3

import requests

import subprocess
import argparse
import os
import re

RMADISON_PATH = "/usr/bin/rmadison"
APT_CACHE_PATH = "/usr/bin/apt-cache"

OUTPUT_PATH = "./debian"


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

        p3 = subprocess.Popen(["head", "-n", "1"], stdin=p2.stdout, stdout=subprocess.PIPE)
        p2.stdout.close()

        p4 = subprocess.Popen(["cut", "-d", " ", "-f", "2"],
                              stdin=p3.stdout,
                              stdout=subprocess.PIPE)
        p3.stdout.close()

        output, _ = p4.communicate()
        source = output.decode().strip()

    urls = []

    for package in packages.split("\n"):
        fields = package.split("|")
        if len(fields) != 4:
            continue

        name = fields[0].strip()
        version = fields[1].strip()

        for arch in fields[3].strip().split(","):

            if not source:
                print(f"No source found for package {name}")
                continue

            arch = arch.strip()

            if source.startswith("lib"):
                head = source[:4]
            else:
                head = source[0]

            filename = f"{name}_{version}_{arch}.deb"
            filename = re.sub(r'.:', "", filename, count=1)

            path = f"{mirror}/debian/pool/main/{head}/{source}/{filename}"

            urls.append(path)

    os.makedirs(OUTPUT_PATH, exist_ok=True)
    for url in urls:
        filename = os.path.basename(url)
        output_path = os.path.join(OUTPUT_PATH, filename)

        if os.path.exists(output_path):
            continue

        print(f"Downloading {url}")

        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()

            with open(output_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")


if __name__ == "__main__":
    main()
