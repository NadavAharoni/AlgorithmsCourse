#!/bin/bash
# Sets up the private remote and local branch on a new machine.
#
# Remote layout:
#   origin  -> https://github.com/NadavAharoni/AlgorithmsCourse.git        (public)
#   private -> https://github.com/NadavAharoni/AlgorithmsCourse-Private.git (private)
#
# Branch layout:
#   main    -> origin/main    (exercise/student-facing version)
#   private -> private/main   (full solution, rebased on top of main)

set -e

if git remote get-url private &>/dev/null; then
    echo "Remote 'private' already exists, skipping."
else
    git remote add private https://github.com/NadavAharoni/AlgorithmsCourse-Private.git
    echo "Remote 'private' added."
fi

git fetch private

if git show-ref --verify --quiet refs/heads/private; then
    echo "Local branch 'private' already exists, setting upstream."
    git branch --set-upstream-to=private/main private
else
    git checkout -b private --track private/main
    echo "Local branch 'private' created, tracking private/main."
fi

git checkout main
echo "Done. Use 'git checkout private' to switch to the solution branch."
