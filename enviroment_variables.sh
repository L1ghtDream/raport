# enviroment_variables.sh [repository_name]

REPOSITORY_NAME=$1

echo "VERSION=$(gradle properties -q | grep "version:" | awk '{print $2}')" >> $GITHUB_ENV
echo "ARTIFACT=$(gradle properties -q | grep "name:" | awk '{print $2}')" >> $GITHUB_ENV
echo "GROUP=$(gradle properties -q | grep "group:" | awk '{print $2}')" >> $GITHUB_ENV
echo "REPOSITORY_NAME=$(echo $REPOSITORY_NAME | awk -F'/' '{print $2}')" >> $GITHUB_ENV