
mkdir -p tmp
cd tmp

wget https://raw.githubusercontent.com/L1ghtDream/report/cdn/README-v2.md
description=""

cd ..

if [ -f "./readme/description.md" ]; then
    description=$(cat ./readme/description.md)
fi

cat ./tmp/README-template.md | sed "s/%description%/$description/g" > test.txt

