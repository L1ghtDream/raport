
mkdir -p tmp
cd tmp

wget -O README-template-i1.md https://raw.githubusercontent.com/L1ghtDream/report/cdn/README-v2.md
description=""

cd ..

if [ -f "./readme/description.md" ]; then
    description=$(cat ./readme/description.md)
fi

cat ./tmp/README-template-i1.md | sed "s/%description%/$description/g" > ./tmp/README-template.md

