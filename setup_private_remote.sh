#!/bin/bash
# Sets up the private remote and local branch on a new machine.
#
# Remote layout:
#   origin         -> https://github.com/NadavAharoni/AlgorithmsCourse.git        (public)
#   private-origin -> https://github.com/NadavAharoni/AlgorithmsCourse-Private.git (private)
#
# Branch layout:
#   main    -> origin/main         (exercise/student-facing version)
#   private -> private-origin/main (full solution, rebased on top of main)

set -e

if git remote get-url private-origin &>/dev/null; then
    echo "Remote 'private-origin' already exists, skipping."
else
    git remote add private-origin https://github.com/NadavAharoni/AlgorithmsCourse-Private.git
    echo "Remote 'private-origin' added."
fi

git fetch private-origin

if git show-ref --verify --quiet refs/heads/private; then
    echo "Local branch 'private' already exists, setting upstream."
    git branch --set-upstream-to=private-origin/main private
else
    git checkout -b private --track private-origin/main
    echo "Local branch 'private' created, tracking private-origin/main."
fi

git checkout main
echo "Done. Use 'git checkout private' to switch to the solution branch."
