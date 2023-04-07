
# ${{ REPOSITORY_NAME }}

![Build](../../actions/workflows/build.yml/badge.svg)
![Version](https://img.shields.io/badge/Version-${{ env.VERSION }}-red.svg)

# Table Of Contents
1. [Description](#description)
2. [How to add to your project](#how-to-add-to-your-project)
3. [How to use](#how-to-use)

## Description
%description%

## How to add to your project


The artifact can be found at the repository https://repo.lightdream.dev or https://jitpack.io (under com.github.L1ghtDream instead of dev.lightdream)

### Maven
```xml
<repositories>
    <repository>
        <id>lightdream-repo</id>
        <url>https://repo.lightdream.dev/</url>
    </repository>
    <repository>
        <id>jitpack.io</id>
        <url>https://jitpack.io</url>
    </repository>
</repositories>
```
```xml
<dependencies>
    <dependency>
        <groupId>dev.lightdream</groupId>
        <artifactId>${{ env.ARTIFACT }}</artifactId>
        <version>${{ env.VERSION }}</version>
    </dependency>
    <dependency>
        <groupId>com.github.L1ghtDream</groupId>
        <artifactId>${{ env.ARTIFACT }}</artifactId>
        <version>${{ env.VERSION }}</version>
    </dependency>
</dependencies>
```

### Gradle - Groovy DSL
```groovy
repositories {
    maven { url "https://repo.lightdream.dev/" }
    maven { url "https://jitpack.io" }
}

dependencies {
    implementation "dev.lightdream:logger:3.1.0"
    implementation "com.github.L1ghtDream:logger:3.1.0"
}
```

### Gradle - Kotlin DSL
```kotlin
repositories {
    maven("https://repo.lightdream.dev/")
    maven("https://jitpack.io")
}

dependencies {
    implementation("dev.lightdream:logger:3.1.0")
    implementation("com.github.L1ghtDream:logger:3.1.0")
}
```

If you want to use an older version that is not available in https://repo.lightdream.dev you can try using https://archive-repo.lightdream.dev


## How to use

Can be found in the [repository](/example)
