# Contributing to ali

Hey, thanks for you interest in the project !

No matter your level, your contribution is welcome :)

## Table of Contents

- [Issues](#issues)
- [Developing](#developing)
  - [Setting up the environment](#setting-up-the-environment)
  - [Project Structure](#project-structure)
  - [Common commands](#common-commands)
  - [Before Submitting](#before-submitting)
  - [Submitting a Pull Request](#submitting-a-pull-request)
- [AI Usage](#ai-usage)

## Issues
When writing issues, please provide enough informations so we can fix your problem. It is recommanded to use the issues templates so we can have enough infos.
Please be nice, and remember that it can take a long time to fix a bug.

## Developing

#### Setting up the environment
- Clone the repository :
```
git clone https://github.com/skueee/ali.git
```
- Install Ruff (for style check)
```
npx install ruff
```

#### Project structure
```
ali/
  .github/workflows      Workflows
  ali/                   The folder with the code
    __init__.py
    ali.py               The entry point of the tool
    ali_configure.py     The module used for the ali configure command
    ali_create.py        The module used for the ali create command
    ali_manage.py        The module used for the ali manage command
    ali_module.py        A module used for misceallanous tasks
  .gitignore             Files to ignore (from github/gitignore repo)
  CONTRIBUTING.md        Contributing guide
  LICENSE.md             MIT License
  pyproject.toml         Pyproject (for pipx)
  README.md              README file
```

#### Common commands
- Execute the tool
```
python3 ali.py [command]
```
- Execute a style check
```
ruff check
```

#### Before submitting
- Check the quality of your code with `ruff check`

#### Submitting a Pull Request
- Ensure that the PR covers only one thing
- Allow edit by mainteners
- Speak in English

## AI Usage
You may use AI tools to help you, but you need to understand and check everything.

You need to document yourself your code, and you cannot ask an AI Agent to write a PR description or an Issue for you.

A notice on ai usage on your comment is appreciated, but not required
