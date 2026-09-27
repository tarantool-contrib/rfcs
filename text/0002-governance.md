# RFC 0002: Governance of tarantool-contrib

- **Status:** Accepted
- **Authors:** @bigbes
- **Created:** 2026-09-27
- **Discussion:** https://github.com/tarantool-contrib/rfcs/pull/2
- **Supersedes:** —

## Summary

Defines what tarantool-contrib is, who decides what, how a module joins the
organization, how a module's maintainership changes hands, how a module's status
is shown to users, and how a module moves to the official `tarantool`
organization.

## Motivation

tarantool-contrib exists so that useful Tarantool modules outlive their authors'
interest. That only works if a few things are settled in advance, before the
first conflict: who may push to a module, what happens to a module whose
maintainer disappeared, and what a user can expect from a module found here.
Without written answers, each case is decided ad hoc, and the users of a module
learn its state from the date of the last commit.

## Detailed design

### Scope

tarantool-contrib hosts **unofficial, community-maintained** code built around
Tarantool: Tarantool modules in Lua, C or Rust, Go libraries, and tools.

- Modules here are not developed, supported or endorsed by the Tarantool team,
  and the organization says so in its profile.
- A module MUST be related to Tarantool: it runs inside Tarantool, talks to it,
  or exists to operate it.
- A module MUST be licensed under BSD-2-Clause, BSD-3-Clause, MIT or
  Apache-2.0. BSD-2-Clause is recommended, as it matches Tarantool.

### Roles

- **Owners** — the organization owners on GitHub. They run the organization's
  infrastructure, accept modules, make the decisions described in RFC 0001,
  moderate, and step in where a module has no maintainer.
- **Maintainers** — the people responsible for a particular module. They have
  the admin role on its repository and make all decisions about it: design,
  reviews, releases.
- **Contributors** — anyone sending issues or pull requests.

Owners do not push to a module, merge into it, or release it without its
maintainers' agreement, with two exceptions:

1. a security fix, when the maintainers do not respond in time;
2. a module without an active maintainer (see *Module status*).

### Joining the organization

1. The author opens a *Module transfer request* issue in
   `tarantool-contrib/rfcs`. The form lists the module requirements
   (RFC 0003).
2. The owners check the requirements. Unmet requirements are listed in the
   issue; the author may fix them before or after the transfer, as agreed in
   the issue.
3. The author **transfers** the repository to the organization. A transfer
   keeps the stars, issues, pull requests and releases, and GitHub redirects the
   old URL. A fork is not accepted as a replacement for a transfer: it splits
   the history and leaves the original URL pointing elsewhere.
4. The author stays the module's maintainer and keeps the admin role on the
   repository.

A new module MAY also be created directly in the organization by an owner, with
its maintainers named in the issue that requested it.

### Module status

Each module has exactly one status, shown in two places: a repository topic and
a badge at the top of its README.

- `maintained` — has at least one active maintainer.
- `looking-for-maintainer` — works as it is, but nobody is responding to issues
  and pull requests. Users are warned; a new maintainer is welcome.
- `archived` — no longer maintained. The repository is archived on GitHub
  (read-only); published releases remain available.

Transitions:

- A maintainer MAY move their module to any status at any time.
- The owners MAY move a module from `maintained` to `looking-for-maintainer`
  when its maintainers have not responded to issues and pull requests for **at
  least 6 months**. The owners try to reach the maintainers before doing so.
- The owners MAY move a module from `looking-for-maintainer` to `archived`
  after **at least 6 more months** without a new maintainer.
- Beyond these minimums, the timing is at the owners' discretion: a module
  whose users depend on it may be given longer.
- An archived module MAY be unarchived when a new maintainer steps in.

### Changing maintainers

- A current maintainer MAY add or remove maintainers of their module.
- A person wishing to become a maintainer of a module in
  `looking-for-maintainer` status opens a *Maintainer request* issue in
  `tarantool-contrib/rfcs`. The owners decide, preferring people with merged
  contributions to the module.
- A maintainer who leaves SHOULD say so, so that the module's status can be
  updated instead of being discovered months later.

### Rock names

- A module's rock name MUST NOT coincide with a rock published by the official
  Tarantool rocks server, or with another module in the organization.
- The rock name SHOULD match the repository name.

Where the organization publishes rocks is still being worked out and will be
decided separately.

### Moving to the official organization

A module MAY move to the official `tarantool` organization once it has proven
itself. Each case is discussed with the Tarantool team individually; they decide
whether to take the module. Things that usually matter:

- the module is used in production outside its authors' own projects;
- it has been actively maintained for a substantial time;
- it meets the Tarantool team's own requirements for official repositories,
  which are stricter than RFC 0003;
- the Tarantool team is willing to maintain it.

The move is a repository transfer, so the URL redirect and the history are kept.
The rock name stays the same.

### Conduct

There is no formal code of conduct. Be reasonable. The owners moderate every
repository in the organization: they may hide or delete comments, lock
threads, and block users from the organization.

## Drawbacks

- Owners have broad discretion: over module status timing and over moderation.
  The organization relies on the owners using it sensibly; if that fails, the
  rules here can be amended.
- Requiring a transfer rather than a fork excludes authors who want to keep the
  repository under their own account. Those modules can still be linked from
  the organization profile without joining it.

## Alternatives

- **Owners maintain every module.** Does not scale, and removes the reason
  authors would bring modules here: they keep ownership in practice.
- **No status labels; users judge by activity.** That is the situation the
  organization exists to fix.
- **Accept forks.** Leaves two copies with diverging histories and the original
  URL, which users already know, pointing at the stale one.
- **A formal code of conduct** such as the Contributor Covenant. It needs an
  enforcement process and a private reporting channel that a small volunteer
  organization cannot staff; the owners' moderation rights cover the same need.

## Unresolved questions

- Where rocks are published: still being worked out, to be decided in a
  separate RFC.
