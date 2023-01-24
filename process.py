import json
import requests

API = "https://repository.lightdream.dev/service/rest/v1/search/assets?sort=version&direction=desc&maven.groupId={group_id}&maven.artifactId={artifact_id}"
PROCESS_DATA = "process.data"
PROJECTS_DATA = "projects.data"


def get_latest(group, artifact):
    """
    Returns the latest version of the artifact
    Example: 3.8.0
    """
    URL = API.replace("{group_id}", group).replace("{artifact_id}", artifact)

    print(URL)
    print(requests.get(url=URL, timeout=10).json())
    
    return requests.get(url=URL, timeout=10).json()["items"][0]["maven2"]["version"]


def process_dependency(dependency):
    """
    Processes the raw dependency adding the "latest" version atribute. Calls recursively for sub-dependencies.
    Example:
    {
        "group":"dev.lightdream",
        "artifact":"logger",
        "version":"3.1.0",
        "latest":"3.1.0",
        "dependencies":[

        ]
    }
    """
    latest = get_latest(dependency["group"], dependency["artifact"])

    dependencies = []

    for sub_dependency in dependency["dependencies"]:
        dependencies.append(process_dependency(sub_dependency))

    return {
        "group": dependency["group"],
        "artifact": dependency["artifact"],
        "version": dependency["version"],
        "latest": latest,
        "dependencies": dependencies
    }


def main():
    """
    Main function
    """
    payload = json.loads(open(PROCESS_DATA, "r", encoding="utf-8").read())

    project = {
        "group": payload["group"],
        "artifact": payload["artifact"],
        "version": payload["version"]
    }
    dependencies = payload["dependencies"]

    raw_report_payload = ""
    try:
        raw_report_payload = open(PROJECTS_DATA, "r", encoding="utf-8").read()
    except:
        raw_report_payload = "[]"

    report_payload = json.loads(raw_report_payload)
    report_dependencies = []

    for dependency in dependencies:
        report_dependencies.append(process_dependency(dependency))

    found = False

    for report in report_payload:
        if report["project"]["group"] == project["group"] and report["project"]["artifact"] == project["artifact"]:
            report["project"] = project
            report["dependencies"] = report_dependencies
            found = True

    if not found:
        report_payload.append(
            {
                "project": project,
                "dependencies": report_dependencies
            }
        )

    open(PROJECTS_DATA, "w+", encoding="utf-8").write(json.dumps(report_payload))


if __name__ == "__main__":
    main()
