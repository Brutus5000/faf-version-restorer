import json


info_json = {
    "config": {
        "name": 'repo A',
        "latest_version": '500',
        "mode": 'abc'
    },
    "versions": []
}

version_list = []

for i in range(100001, 100500):
    version_stats = dict()

    version_stats["name"] = i

    is_major = (i % 10) == 0

    if is_major:
        if i < 10:
            version_stats["prev_major"] = None
        else:
            version_stats["prev_major"] = i - i % 10

        version_stats["next_major"] = i + 10 - i % 10

    version_stats["reaches"] = []

    for p in range(0,11):
        if i<10 and p==0:
            continue

        if i % 10 != p:
            version_stats["reaches"].append(i - i % 10 + p)

    info_json["versions"].append(version_stats)

print(info_json)
