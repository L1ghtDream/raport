import json

PROJECTS_DATA = "projects.data"
RAPORT_FILE = "README.md"

f = open(RAPORT_FILE, "w+")

raw_raport_payload = open(PROJECTS_DATA, "r").read()
raport_payload = json.loads(raw_raport_payload)

for raport in raport_payload:
    project = raport["project"]
    dependencies = raport["dependencies"]
    p_group = project["group"]
    p_artifact = project["artifact"]
    p_version = project["version"]

    f.write(f"### {p_group}:{p_artifact}:{p_version} \n")
    for dependency in dependencies:
        version_raport=""

        d_group = dependency["group"]
        d_artifact = dependency["artifact"]
        d_version = dependency["version"]
        d_latest = dependency["latest"]

        if d_version == d_latest:
            version_raport = f"![](https://img.shields.io/badge/Up%20To%20Date-{d_version}-green.svg)"
        else:
            version_raport = f"![](https://img.shields.io/badge/Outdated-{d_version}-red.svg) ![](https://img.shields.io/badge/Latest-{d_latest}-yellow.svg)"

        f.write(
        f"- {d_group}:{d_artifact}:{d_version} {version_raport}\n"
        )