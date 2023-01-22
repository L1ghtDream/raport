# usage [artifact] [version] [github_access_token]

ARTIFACT=$1
VERSION=$2
TOKEN=$3

wget https://raw.githubusercontent.com/L1ghtDream/raport/cdn/dependencies.py
python3 dependencies.py
git clone $RAPORT_URL raport
cp process.data raport/process.data
cd raport
git add *
git checkout -b "$ARTIFACT/$VERSION"
git config --global user.email "bot@voinearadu.com"
git config --global user.name "Radu Voinea [bot]"
git commit -m "$ARTIFACT/$VERSION"
git remote set-url origin https://L1ghtDream:$TOKEN@github.com/L1ghtDream/raport
git push --set-upstream origin $ARTIFACT/$VERSION