#!/usr/bin/env python3
import glob
import os
import re
import shutil
import subprocess

TAR_PATH = "/opt/homebrew/bin/gtar"
AR_PATH = "/usr/bin/ar"
FLAIR_PATH = "./flair/"
SIG_PATH = "./sig/"
PELF_PATH = os.path.join(FLAIR_PATH, "pelf")
SIGMAKE_PATH = os.path.join(FLAIR_PATH, "sigmake")
ZIPSIG_PATH = os.path.join(FLAIR_PATH, "zipsig")


def extract_a(deb_path: str) -> str:
    """Extract all .a files from .deb package

    Args:
        deb_name: location of deb file

    Returns:
        directory location of package
    """
    pkg_path = deb_path[:-4]

    # Create a folder package_name
    os.makedirs(pkg_path, exist_ok=True)

    # Extract a deb file and only extract data.tar.zst and store the stdout into a variable
    ar_files = subprocess.run([AR_PATH, 't', deb_path], capture_output=True).stdout
    data_tar_type = ar_files.decode().strip().split("\n")[2]
    data_tar = subprocess.run([AR_PATH, 'p', deb_path, data_tar_type], capture_output=True).stdout

    # Extract the contents of data.tar.zst from the data_tar variable
    _ = subprocess.run([TAR_PATH, '-C', pkg_path, '--zstd', '-xv', '--wildcards', "*.a"],
                       input=data_tar,
                       check=True,
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)

    return pkg_path


def a_to_pat(pkg_path: str, pat_name: str) -> str:
    """Converts all .a files into a .pat file

    Args:
        pkg_path: directory of package
        pat_name: name to give pat file

    Returns:
        file location of pat
    """
    # Glob the .a files in the package folder
    a_path = glob.glob(os.path.join(pkg_path, "**/*.a"), recursive=True)
    pat_path = os.path.join(pkg_path, pat_name)
    _ = subprocess.run([PELF_PATH] + a_path + [pat_path],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)

    return pat_path


def _clean_exc(exc_name: str) -> None:
    """Fixes any collisions
    Taken from https://github.com/push0ebp/ALLirt/blob/master/flair.py

    Args:
        exc_name (str): location of collision file
    """
    with open(exc_name, 'r') as f:
        s = f.read()

    with open(exc_name, 'w') as f:
        cleaned_funcs: list[str] = []
        s = re.sub(r';.+', '', s).strip()
        funcs_pairs = s.split(os.linesep * 2)
        for funcs_pair in funcs_pairs:
            funcs = funcs_pair.splitlines()
            start = 0
            if len(funcs) > 1:  #if only one collision, not add '+'
                cleaned_funcs.append('+' + funcs[0])
                start += 1
            funcs.append('')  #double linesep
            cleaned_funcs.extend(funcs[start:])
        s = os.linesep.join(cleaned_funcs)
        _ = f.write(s)


def pat_to_sig(pat_path: list[str], sig_path: str) -> str:
    """Convert .pat file into .sig file

    Args:
        pat_path: list of all pat file location
        sig_path: path of sig file

    Returns:
        file location of sig file
    """
    exit_code = subprocess.run([SIGMAKE_PATH] + pat_path + [sig_path],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL).returncode
    if exit_code != 0:
        _clean_exc(sig_path[:-4] + ".exc")
    _ = subprocess.run([SIGMAKE_PATH] + pat_path + [sig_path],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
    os.remove(sig_path[:-4] + ".exc")

    _ = subprocess.run([ZIPSIG_PATH, sig_path],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)

    return sig_path


def main():
    packages = {
        "distro": "ubuntu",
        "arch": "amd64",
        "name": "libc6-dev",
    }

    all_deb_paths = glob.glob(
        f"./{packages['distro']}/*/{packages['arch']}/{packages['name']}/**/*.deb", recursive=True)

    all_pat_paths: list[str] = []

    for deb_path in all_deb_paths:
        print(f"Extracting {deb_path}")
        pkg_path = extract_a(deb_path)
        print(f"Converting to pat format")
        pat_path = a_to_pat(pkg_path, packages['name'])
        all_pat_paths.append(pat_path)
        print(f"Deleting extracted files")
        shutil.rmtree(pkg_path)

    os.makedirs(os.path.join(SIG_PATH, packages['arch']), exist_ok=True)

    _ = pat_to_sig(
        all_pat_paths,
        os.path.join(SIG_PATH,
                     f"./{packages['name'][:-4]}-{packages['distro']}-{packages['arch']}.sig"))

    for pat_paths in all_pat_paths:
        os.remove(pat_paths)


if __name__ == "__main__":
    main()
