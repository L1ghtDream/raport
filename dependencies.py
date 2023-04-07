print("Script Disabled")

"""
import os
import json

TRACKING_GROUPS=["dev.lightdream", "com.pokeninjas"]
DEPENDENCIES_OUTPUT = "dependencies.output"
ARTIFACT_OUTPUT = "artifact.output"
VERSION_OUTPUT = "version.output"
GROUP_OUTPUT = "group.output"
PROCESS_DATA = "process.data"


def create_dependency(group, artifact, version):
    """
    Creates a dependency like dictionary
    Example:
    {
        "group": "dev.lightdream",
        "artifact": "logger",
        "version": "1.0.0",
        "dependencies": []
    }
    """
    return {
        "group": group,
        "artifact": artifact,
        "version": version,
        "dependencies": []
    }

def shell(command):
    """
    Execute shell command
    """
    os.system(command)


def starting_spaces(s):
    """
    Returns number of spaces (" ") leading a string
    Example: 4
    """

    return len(s) - len(s.lstrip())


def main():
    """
    Main function
    """
    shell(f"gradle dependencies --configuration runtimeClasspath > {DEPENDENCIES_OUTPUT}")
    shell(f"gradle properties -q | grep \"^name:\" | awk '{{print $2}}' > {ARTIFACT_OUTPUT}")
    shell(f"gradle properties -q | grep \"^version:\" | awk '{{print $2}}' > {VERSION_OUTPUT}")
    shell(f"gradle properties -q | grep \"^group:\" | awk '{{print $2}}' > {GROUP_OUTPUT}")

    raw_dependencies = open(f"{DEPENDENCIES_OUTPUT}", "r", encoding="utf-8").read()

    project_artifact = open(f"{ARTIFACT_OUTPUT}", "r", encoding="utf-8").read().replace("\n", "")
    project_version = open(f"{VERSION_OUTPUT}", "r", encoding="utf-8").read().replace("\n", "")
    project_group = open(f"{GROUP_OUTPUT}", "r", encoding="utf-8").read().replace("\n", "")

    dependencies_lines = raw_dependencies.replace("+", "").replace("\\", "").replace("|", "").split("\n")

    dependencies_entries = []

    for line in dependencies_lines:
        for group in TRACKING_GROUPS:
            if group in line:
                dependencies_entries.append(line)
                break

    dependencies = create_dependency(project_group, project_artifact, project_version)

    for entry in dependencies_entries:
        tree_depth = int(starting_spaces(entry)/4)
        entry = entry.replace(" ", "").replace("->", "").replace("(*)", "")

        group = entry.split(":")[0].replace("-", "")
        artifact = entry.split(":")[1]
        version = entry.split(":")[2]

        if group not in TRACKING_GROUPS:
            continue

        dependency = create_dependency(group, artifact, version)

        last_dependency = dependencies

        for _ in range(tree_depth):
            last_dependency = last_dependency["dependencies"][-1]

        last_dependency["dependencies"].append(dependency)

    open(f"{PROCESS_DATA}", "w+", encoding="utf-8").write(json.dumps(dependencies))

if __name__ == "__main__":
    main()
"""