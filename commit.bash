#!/bin/bash

git add .

echo 'Commit message: '
read commitMessage

git commit -m "$commitMessage"

echo 'Branch name: '
read branch

git push origin $branch