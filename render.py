print("Script Disabled")

"""
import json

PROJECTS_DATA = "projects.data"
RAPORT_FILE = "README.md"

def write_dependency(file, dependency, tabs_count=0):
    """
    Writes the dependency to the file
    """
    d_group = dependency["group"]
    d_artifact = dependency["artifact"]
    d_version = dependency["version"]
    d_latest = dependency["latest"]

    if d_version == d_latest:
        version_raport = f"![](https://img.shields.io/badge/Up%20To%20Date-{d_latest}-green.svg)"
    else:
        d_version_major = d_version.split(".")[0]
        d_version_minor = d_version.split(".")[1]
        d_version_patch = d_version.split(".")[2]

        d_latest_major = d_latest.split(".")[0]
        d_latest_minor = d_latest.split(".")[1]
        d_latest_patch = d_latest.split(".")[2]

        if d_version_major is not d_latest_major:
            version_raport = f"![](https://img.shields.io/badge/Outdated-{d_latest}-red.svg)"
        if d_version_minor is not d_latest_minor:
            version_raport = f"![](https://img.shields.io/badge/Outdated-{d_latest}-orange.svg)"
        if d_version_patch is not d_latest_patch:
            version_raport = f"![](https://img.shields.io/badge/Outdated-{d_latest}-yellow.svg)"

    tabs = ""
    for _ in range(tabs_count):
        tabs += "\t"

    file.write(f"{tabs}* {d_group}:{d_artifact}:{d_version} {version_raport}\n")
    for sub_dependency in dependency["dependencies"]:
        write_dependency(file, sub_dependency, tabs_count + 1)

def main():
    """
    Main fuinction
    """
    f = open(RAPORT_FILE, "w+", encoding="utf-8")

    raw_raport_payload = open(PROJECTS_DATA, "r", encoding="utf-8").read()
    raport_payload = json.loads(raw_raport_payload)

    for raport in raport_payload:
        project = raport["project"]
        dependencies = raport["dependencies"]
        p_group = project["group"]
        p_artifact = project["artifact"]
        p_version = project["version"]

        f.write(f"### {p_group}:{p_artifact}:{p_version} \n")
        for dependency in dependencies:
            write_dependency(f, dependency)

if __name__ == "__main__":
    main()
"""