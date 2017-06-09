from pathlib import Path
from typing import List
import re
import pymysql

def extract_mod_list(path: Path) -> List[str]:
    """
    Extracts the list of mods from the featured mod updates folder
    :param path: path to the featured mod updates
    :return: list of featured mods by technical name
    """

    mods = []  # type: List[str]

    mods_regex = re.compile("updates_(\w*)_files")

    for folder in path.iterdir():  # type: Path
        mod = mods_regex.search(folder.name)
        if mod is not None:
            mods.append(mod.group(1))

    return mods


def get_version_list(mysql_connection,  featured_mod: str) -> List[str]:
    versions = []

    sql = "SELECT DISTINCT version FROM updates_%s_files" % featured_mod
    with mysql_connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()

        for row in result:
            versions.append(result)

    return versions


def get_files_for_version(mysql_connection, featured_mod: str, version: str):
    pass
