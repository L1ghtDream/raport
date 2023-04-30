# Usage: python readme.py [repository] [artifact] [version]

import os
import sys

DESCRIPTION_FILE = "readme/description.md"
HOW_FILE = "readme/how.md"
TEMPLATE_URL = "https://raw.githubusercontent.com/L1ghtDream/report/cdn/README-v3.md"
README_TEMPLATE_FILE = "tmp-README-template.md"
README_FILE = "README.md"

os.system(f"wget -O {README_TEMPLATE_FILE} {TEMPLATE_URL}")

description = ""
how = ""

if os.path.exists(DESCRIPTION_FILE):
    with open(DESCRIPTION_FILE, "r") as file:
        description = file.read()

if os.path.exists(HOW_FILE):
    with open(DESCRIPTION_FILE, "r") as file:
        how = file.read()

PLACEHOLDERS = {
    "description": description,
    "how": how,
    "repository": sys.argv[1],
    "artifact": sys.argv[2],
    "version": sys.argv[3],
}

readme_template = ""

with open(README_TEMPLATE_FILE, "r") as file:
    readme_template = file.read()

for key, value in PLACEHOLDERS.items():
    readme_template = readme_template.replace(f"%{key}%", value)

with open(README_FILE, "w+") as file:
    file.write(readme_template)