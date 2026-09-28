#!/usr/bin/env python3
"""Check the RFC files, the README index and the relative links.

Run from the repository root. In a pull request, set PR_NUMBER and BASE_SHA:
an RFC added by the pull request must then carry the pull request's number.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

REPO_URL = "https://github.com/tarantool-contrib/rfcs"
FILE_RE = re.compile(r"^(\d{4})-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
TITLE_RE = re.compile(r"^# RFC (\d{4}): (.+)$")
FIELD_RE = re.compile(r"^- \*\*(Status|Authors|Created|Discussion|Supersedes):\*\* (.+)$")
STATUS_RE = re.compile(r"^(Proposed|Accepted|Superseded by \d{4})$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
INDEX_RE = re.compile(r"^\| \[(\d{4})\]\((text/[^)]+)\) \| (.+?) \| (.+?) \|$")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")

errors = []


def error(path, line, message):
    errors.append(f"{path}:{line}: {message}")


def check_rfc(path):
    """Check one RFC file; return (number, title, status) or None."""
    match = FILE_RE.match(path.name)
    if not match:
        error(path, 1, "file name must be NNNN-slug.md, lowercase")
        return None
    number = match.group(1)
    if number == "0000":
        error(path, 1, "rename the file to the pull request number")

    lines = path.read_text(encoding="utf-8").splitlines()
    title_match = TITLE_RE.match(lines[0]) if lines else None
    if not title_match:
        error(path, 1, 'first line must be "# RFC NNNN: Title"')
        return None
    if title_match.group(1) != number:
        error(path, 1, f"title says RFC {title_match.group(1)}, "
                       f"file name says {number}")

    fields = {}
    for lineno, line in enumerate(lines[1:], start=2):
        if line.startswith("## "):
            break
        field = FIELD_RE.match(line)
        if field:
            fields[field.group(1)] = (lineno, field.group(2).strip())
    for name in ("Status", "Authors", "Created", "Discussion", "Supersedes"):
        if name not in fields:
            error(path, 2, f"missing metadata field {name}")

    status = fields.get("Status", (0, ""))[1]
    if "Status" in fields and not STATUS_RE.match(status):
        error(path, fields["Status"][0], f"unknown status {status!r}")
    if "Created" in fields and not DATE_RE.match(fields["Created"][1]):
        error(path, fields["Created"][0], "Created must be YYYY-MM-DD")
    if "Discussion" in fields and number != "0000":
        expected = f"{REPO_URL}/pull/{int(number)}"
        if fields["Discussion"][1] != expected:
            error(path, fields["Discussion"][0],
                  f"Discussion must be {expected}")

    return number, title_match.group(2), status


def check_index(rfcs):
    readme = Path("README.md")
    seen = set()
    for lineno, line in enumerate(readme.read_text(encoding="utf-8")
                                  .splitlines(), start=1):
        row = INDEX_RE.match(line)
        if not row:
            continue
        number, link, title, status = row.groups()
        if number in seen:
            error(readme, lineno, f"RFC {number} is listed twice")
        seen.add(number)
        if number not in rfcs:
            error(readme, lineno, f"RFC {number} has no file in text/")
            continue
        path, rfc_title, rfc_status = rfcs[number]
        if link != path.as_posix():
            error(readme, lineno, f"RFC {number} links to {link}, "
                                  f"the file is {path.as_posix()}")
        if title != rfc_title:
            error(readme, lineno, f"RFC {number} title is {rfc_title!r} "
                                  f"in its file, {title!r} here")
        if status != rfc_status:
            error(readme, lineno, f"RFC {number} status is {rfc_status!r} "
                                  f"in its file, {status!r} here")
    for number, (path, _, _) in sorted(rfcs.items()):
        if number not in seen:
            error(readme, 1, f"RFC {number} ({path}) is missing from the index")


def check_links(path):
    text = path.read_text(encoding="utf-8")
    in_code = False
    for lineno, line in enumerate(text.splitlines(), start=1):
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        for target in LINK_RE.findall(line):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0]
            if not (path.parent / file_part).exists():
                error(path, lineno, f"broken relative link {target}")


def check_pr_numbers():
    pr_number = os.environ.get("PR_NUMBER")
    base = os.environ.get("BASE_SHA")
    if not pr_number or not base:
        return
    added = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=A",
         f"{base}...HEAD", "--", "text/"],
        check=True, capture_output=True, text=True).stdout.split()
    for name in added:
        match = FILE_RE.match(Path(name).name)
        if match and int(match.group(1)) != int(pr_number):
            error(name, 1, f"a new RFC takes the pull request number: "
                           f"rename it to {int(pr_number):04d}-...")


def main():
    rfcs = {}
    for path in sorted(Path("text").glob("*.md")):
        result = check_rfc(path)
        if result is None:
            continue
        number, title, status = result
        if number in rfcs:
            error(path, 1, f"RFC {number} is also {rfcs[number][0]}")
        rfcs[number] = (path, title, status)
    check_index(rfcs)
    for path in sorted(Path(".").rglob("*.md")):
        if ".git" not in path.parts:
            check_links(path)
    check_pr_numbers()

    for message in errors:
        print(message)
    if errors:
        print(f"{len(errors)} problem(s)", file=sys.stderr)
        return 1
    print(f"{len(rfcs)} RFCs checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
