# RFC 0003: Module repository requirements

- **Status:** Accepted
- **Authors:** @bigbes
- **Created:** 2026-09-27
- **Discussion:** https://github.com/tarantool-contrib/rfcs/pull/3
- **Supersedes:** —

## Summary

Defines what a module repository in tarantool-contrib MUST, SHOULD, and is not
required to provide. The MUST list is the condition for joining the
organization; the SHOULD list is what maintainers are encouraged to reach.

## Motivation

A user who finds a module in tarantool-contrib should be able to rely on a few
things without reading its code: that it states which Tarantool versions it
supports, that its tests run, that its releases are reproducible, and that its
license allows using it.

The requirements borrow from the Tarantool team's practices for official
repositories, but are deliberately lighter. Most modules here have a single
maintainer working in their spare time. A requirement such as two approvals
per pull request would stop them from merging anything at all, and a module
that cannot move is worse for its users than one reviewed by one person.

## Detailed design

The rules below use RFC 2119 keywords.

### Kinds of modules

The organization currently hosts two kinds of libraries, and the rules name
each where they differ:

- **Tarantool modules** — code that runs inside Tarantool, written in Lua, C or
  Rust, distributed as a rock.
- **Go libraries** — code that talks to Tarantool from Go.

Other kinds (tools, documentation) follow the language-independent rules; rules
specific to them are added to this RFC when the first such repository arrives.

### MUST — required to join the organization

**Repository contents**

- `README.md` with:
  - what the module does and for whom;
  - a quick start: installation and a minimal usage example;
  - the supported Tarantool versions (and, for Go, the supported Go versions);
  - the module status badge (RFC 0002).
- `LICENSE` with one of the licenses allowed by RFC 0002.
- A build description in the repository root:
  - Tarantool modules: `<name>-scm-1.rockspec`, building the current state of
    the default branch;
  - Go libraries: `go.mod` whose module path is the repository's final public
    path, `github.com/tarantool-contrib/<repo>`.
- No git submodules needed to build: a dependency is either vendored or declared
  through the language's package manager.
- Everything in the repository is in English: code, comments, documentation,
  commit messages.

**Continuous integration**

CI runs on every push to the default branch and on every pull request, and is
green on the default branch. It runs at least:

- Tarantool modules:
  - `luacheck` over the Lua sources;
  - the test suite with `luatest` on at least the oldest and the newest
    supported Tarantool version.
- Go libraries:
  - `go vet` or `golangci-lint`;
  - `go test` on at least the oldest and the newest supported Go version.

For Tarantool modules, the organization provides a starter workflow doing
exactly this (*Tarantool module: test*).

**Branches and releases**

- The default branch is named `master`, as in the Tarantool repositories.
- The default branch is protected against force-push and deletion.
- Releases follow Semantic Versioning.
- Release tags:
  - Tarantool modules: `X.Y.Z`, without a `v` prefix, so that the tag matches
    the version in the rockspec;
  - Go libraries: `vX.Y.Z`, as the Go toolchain requires.
- Tarantool module releases are built by CI from the tag, not on a maintainer's
  machine. Where they are published is still being worked out and will be
  decided separately.

### SHOULD — recommended

- `CHANGELOG.md` in the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
  format, with an `Unreleased` section.
- A Lua module exposes its version as a `_VERSION` string field of the module
  table, generated from the release tag rather than edited by hand.
- Test coverage is measured (`luacov` for Lua, `go test -cover` for Go) and
  reported in CI. No threshold is required.
- C and Rust code in a Tarantool module is checked by the language's usual
  formatter and linter in CI.
- Every change comes with a test; a bug fix comes with a test that fails without
  it.
- Commit messages follow the `prefix: short summary` form, with a body that
  explains why the change was made.
- The repository uses the organization-wide issue and pull request templates
  (inherited automatically unless the repository overrides them).
- A new major version comes with migration notes for the incompatible changes.

### Not required

These are common in official Tarantool repositories and deliberately **not**
required here:

- **Two approvals per pull request.** A module with a single maintainer could
  never merge. Instead:
  - a module with two or more maintainers SHOULD require one approval from a
    maintainer other than the author;
  - a module with one maintainer MAY merge its own pull requests once CI is
    green.
- **A coverage threshold** (such as 80%). Coverage is reported, not enforced.
- **A release branch process** (a locked release branch, a documentation-team
  review of the changelog).
- **Support for Tarantool versions the maintainers do not use.** The supported
  versions are the maintainers' call, as long as the README states them and CI
  tests them.

### Existing modules

A module that joins the organization MAY meet some MUST requirements only after
the transfer, as agreed in its transfer request. Modules already in the
organization when these requirements change get at least 6 months to comply;
the owners track the gaps in issues on the affected repositories.

## Drawbacks

- The MUST list is enough to keep a module usable, not to make it good. Quality
  beyond it depends on the maintainers.
- One-person merges mean some changes land without a second pair of eyes.

## Alternatives

- **Adopt the official Tarantool requirements as they are.** Most single-
  maintainer modules could not meet them, and the organization would be empty.
- **No requirements, only recommendations.** Then "in tarantool-contrib" tells a
  user nothing about a module.

## Unresolved questions

- Where Tarantool module releases are published: depends on the rocks server,
  which is still being worked out.
- Whether the MUST list should include a minimum set of supported Tarantool
  versions, such as the current LTS.
