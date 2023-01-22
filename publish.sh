# publish.sh [gitlab_header] [github_repository] [github_token] [self_password]

GITLAB_AUTH_HEADER_VALUE=$1
GITHUB_REPOSITORY=$2
GITHUB_TOKEN=$3
SELF_PASSWORD=$4


touch ~/.gradle/gradle.properties
echo "
gitlab.url = https://gitlab.com/api/v4/projects/41661215/packages/maven/
gitlab.auth.header.name = Private-Token
gitlab.auth.header.value = $GITLAB_AUTH_HEADER_VALUE

github.url = https://maven.pkg.github.com/$GITHUB_REPOSITORY
github.auth.username = L1ghtDream
github.auth.password = $GITHUB_TOKEN

self.url = https://repository.lightdream.dev/repository/maven-releases/
self.auth.username = admin
self.auth.password = $SELF_PASSWORD
" > ~/.gradle/gradle.properties

echo "Publishing to GitHub"
gradle publishGitHub || echo "Failed to publish to GitHub"
echo "Publishing to GitLab"
gradle publishGitLab || echo "Failed to publish to GitLab"
echo "Publishing to Self hosted repository"
gradle publishSelf || echo "Failed to publish to Self hosted repository"