version_string=$(gradle properties -q | grep "^version:" | awk '{print $2}')

IFS='.'

read -ra version_codes <<< "$version_string"

max_index=0
for val in "${version_codes[@]}"; do
    max_index=$((max_index+1))
done

new_version=""

for (( i=0 ; i<$max_index ; i++ )); do
    version_code=$((version_codes[i] + 1))

    if (( $i == $((max_index-1)))); then
        version_code=$((version_codes[i] + 1))
    else
        version_code=$((version_codes[i]))
    fi

    new_version="$new_version$version_code"
    if (( $i == $((max_index-1)))); then
        tmp=""
    else
        new_version="$new_version."
    fi
    
done

sed -i "s/version = \"$version_string\"/version = \"$new_version\"/" build.gradle.kts
