#!/usr/bin/python3

from pathlib import Path

versions = Path("versions").open("r").read().splitlines()

sql = ""

for version in versions:
    sql = sql + \
"""SELECT b.filename AS `name`, latest.master_version, file.version AS `last_change_version`, b.path AS `group`, file.md5 AS `md5`, file.id AS `id`, file.name AS `url`
FROM updates_faf_files file
INNER JOIN
(
	SELECT fileId, MAX(version) AS version, $version$ As master_version FROM updates_faf_files
	WHERE version <= '$version$'
	GROUP BY fileId
) latest
ON file.fileId = latest.fileId
AND file.version = latest.version
LEFT JOIN updates_faf b
ON b.id = file.fileId
UNION
""".replace("$version$", version)

print(sql)