"""
Script to automatically create rc tags and release tags in a Git repository.
"""

import argparse
import re
from git import Repo

VERSION_REGEX = r"rc/(\d+)\.(\d+)\.(\d+)"


def get_latest_rc_version(repo):
    """Finds the latest rc/X.Y.Z tag in the repository."""
    versions = []

    for tag in repo.tags:
        match = re.match(VERSION_REGEX, str(tag))
        if match:
            major, minor, patch = map(int, match.groups())
            versions.append((major, minor, patch))

    if not versions:
        return (1, 0, 0)

    versions.sort()
    return versions[-1]


def create_tag(repo, tag_name):
    """Creates a tag on the current 'main' branch."""
    commit = repo.heads.main.commit
    repo.create_tag(tag_name, commit)
    print(f"Created tag: {tag_name}")


def main():
    """Handles arguments, generates next tag, and creates release tag if requested."""
    parser = argparse.ArgumentParser(description="GitHub tag release helper.")
    parser.add_argument("--create-release", action="store_true")
    args = parser.parse_args()

    repo = Repo(".")

    major, minor, patch = get_latest_rc_version(repo)

    # Create next RC tag
    minor += 1
    new_rc_tag = f"rc/{major}.{minor}.{patch}"
    create_tag(repo, new_rc_tag)

    if args.create_release:
        release_tag = f"{major}.{minor}.{patch}"
        create_tag(repo, release_tag)


if __name__ == "__main__":
    main()
