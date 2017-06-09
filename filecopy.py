#!/usr/bin/python3

from pathlib import Path

import shutil

root = Path("M:\\BiReUS\\FAF")
data = Path("M:\\FAF-assets")
versions = Path("versions").open("r").read().splitlines()

for version in versions:
    root.joinpath(version).mkdir(exist_ok=True)
    root.joinpath(version, "bin").mkdir(exist_ok=True)
    root.joinpath(version, "gamedata").mkdir(exist_ok=True)

version_files = Path("version files.csv").open("r").read().splitlines()

for version_file in version_files:
    name, master_version, last_change_version, group, md5, id, url = version_file.split(";")

    if name== "name" and master_version== "master_version":
        continue

    if master_version == "3608":
        continue

    source = data.joinpath(url)
    dest = root.joinpath(master_version, group, name)

    shutil.copyfile(str(source), str(dest))
