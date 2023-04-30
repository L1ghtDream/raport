# Requirements
# - Have at least one of the files `gradle/libs.versions.toml` `build.gradle.kts` `build.gradle`
# - Have at least one of them have either `project = "some_version"` or version = `"some_version"`

import os

version_containers_files = ["gradle/libs.versions.toml", "build.gradle.kts", "build.gradle"]

os.system("gradle properties -q | grep \"^version:\" | awk \'{print $2}\' > tmp-current_version")

version_file = open("tmp-current_version", "r")

current_version = version_file.read().replace("\n", "").replace(" ", "")

if current_version == "":
    os.system("chmod u+x gradlew")
    os.system("./gradlew properties -q | grep \"^version:\" | awk \'{print $2}\' > tmp-current_version")
    version_file = open("tmp-current_version", "r")
    current_version = version_file.read().replace("\n", "").replace(" ", "")

version_codes = current_version.split(".")

version_codes[-1] = str(int(version_codes[-1]) + 1)

new_version = ".".join(version_codes)

for version_container_file in version_containers_files:
    os.system(f"sed -i \"s/version = \\\"{current_version}\\\"/version = \\\"{new_version}\\\"/g\" {version_container_file}")
    os.system(f"sed -i \"s/project = \\\"{current_version}\\\"/project = \\\"{new_version}\\\"/g\" {version_container_file}")
