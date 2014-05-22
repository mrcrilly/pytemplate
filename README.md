# pytemplate

Template Python project.

## env/ & Symlinks

Our "virtualenv env" environment. I create symlinks to the pip and python binaries, inside this directory, at the top level. This makes it easier to utilise them and they're cheap/light.

The env/ directory is usually excluded from Git commits by placing it in the .gitignore directory. No harm in having it here though.

## BDD & Behave

Both are missing from this project to keep it "development style" agnostic. However I usually create "mkdir -p features/steps" and use the Behave library for BDD style development practices.

## Requirements.txt

Easily created with "./pip freeze > requirements.txt". Useful for quickly setting the project up elsewhere.
