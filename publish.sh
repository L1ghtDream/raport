# publish.sh [github_repository] [github_token] [self_password]

if [ "$#" -ne 3 ]; then
    echo "You are using the old format with the gitlab header which is disabled. Please update your call"
    GITLAB_AUTH_HEADER_VALUE=$1
    GITHUB_REPOSITORY=$2
    GITHUB_TOKEN=$3
    SELF_PASSWORD=$4
else
    GITHUB_REPOSITORY=$1
    GITHUB_TOKEN=$2
    SELF_PASSWORD=$3
fi

touch ~/.gradle/gradle.properties
echo "
github.url = https://maven.pkg.github.com/$GITHUB_REPOSITORY
github.auth.username = L1ghtDream
github.auth.password = $GITHUB_TOKEN

self.url = https://repository.lightdream.dev/repository/maven-releases/
self.auth.username = admin
self.auth.password = $SELF_PASSWORD
" > ~/.gradle/gradle.properties

echo "Publishing to GitHub"
gradle publishGitHub
echo "Publishing to Self hosted repository"
gradle publishSelf