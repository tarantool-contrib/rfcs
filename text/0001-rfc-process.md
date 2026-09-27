# RFC 0001: The RFC process

- **Status:** Accepted
- **Authors:** @bigbes
- **Created:** 2026-09-27
- **Discussion:** https://github.com/tarantool-contrib/rfcs/pull/1
- **Supersedes:** —

## Summary

Organization-wide decisions of tarantool-contrib are proposed, discussed and
recorded as RFCs in the `tarantool-contrib/rfcs` repository. An RFC is a
Markdown file submitted as a pull request; merging it accepts the proposal.
Accepted RFCs are the organization's rules and are amended as practice shows.

## Motivation

tarantool-contrib brings together modules with different authors, different
maintainers and no shared employer. Rules that bind all of them — what a module
must provide, how maintainership changes hands, where rocks are published —
need a place where they are proposed in the open, where anyone affected can
object, and where the reasons survive after the discussion is over.

A chat decides quickly and forgets just as quickly. An issue tracker keeps the
discussion but not a clean statement of what was decided. An RFC keeps both: the
merged text is the decision, and the pull request is the discussion that led to
it.

## Detailed design

### What needs an RFC

An RFC is required for a change that affects the organization as a whole:

- the governance of the organization: roles, how modules join or leave, how
  maintainers change;
- requirements every module repository must meet;
- shared infrastructure: the rocks server, shared CI, the domain;
- this process.

An RFC is **not** required for:

- anything confined to a single module — that is its maintainers' decision;
- editorial fixes (typos, broken links, clarifications that do not change
  meaning);
- operational actions that follow an accepted RFC.

When in doubt, start a discussion and ask.

### Lifecycle

1. **Idea.** Anyone may start a thread in the repository's Discussions. This
   step is optional but recommended: it is the cheapest place to learn whether
   others share the problem.
2. **Proposal.** The author copies `0000-template.md` to `text/0000-<slug>.md`,
   fills it in, and opens a pull request. Anyone may propose an RFC; being an
   owner or a maintainer is not required.
3. **Number.** The RFC number is the pull request number. The author renames the
   file to `text/NNNN-<slug>.md` (zero-padded to four digits) and fills the
   `Discussion` link. Taking the number from the pull request means two RFCs
   written at the same time can never claim the same number.
4. **Discussion.** Happens in the pull request review, so that comments attach
   to the lines they are about. The author updates the text as the discussion
   goes; the RFC must describe the proposal as it currently stands, not as it
   was first written.
5. **Final comment period (FCP).** When the discussion has settled, an owner
   comments on the pull request announcing an FCP of **7 days** and the proposed
   outcome: accept or reject. The FCP is the last call for objections. A
   substantial objection raised during the FCP ends it; a new FCP starts after
   the objection is addressed.
6. **Decision.** When the FCP ends without open objections:
   - **accept:** the status becomes `Accepted` and the pull request is merged;
   - **reject:** the pull request is closed with a comment giving the reasons.
     Rejected RFCs are not merged; the closed pull request is their record.

The author may withdraw an RFC at any time by closing the pull request.

### Decision makers

Decisions are made by the organization owners, by consensus. An RFC is accepted
only if no owner objects. An owner who is the author of an RFC takes part in
the decision like any other owner.

If the owners cannot reach consensus, the RFC is not accepted. It may be revised
and proposed again.

### Statuses

- `Proposed` — under discussion in an open pull request.
- `Accepted` — merged; the decision is made but not yet reflected everywhere.
- `Implemented` — the infrastructure and the organization profile reflect it.
- `Superseded by NNNN` — replaced by a later RFC.

Rejected and withdrawn RFCs have no status in the repository: they are never
merged.

### Amending an accepted RFC

Accepted RFCs are living documents: they describe the rules as they currently
stand, and amending them as the organization learns is expected.

- **Editorial fixes** — typos, broken links, wording that does not change
  meaning — are merged by any owner without further process.
- **Substantive amendments** — anything that changes a rule — are pull requests
  against the RFC file, decided by the owners by consensus. An owner MAY call an
  FCP on an amendment when it affects many modules; otherwise it is merged once
  the owners agree.
- **Replacing a decision entirely** takes a new RFC that names the old one in
  `Supersedes`. When the new RFC is accepted, the old one's status becomes
  `Superseded by NNNN`.

The git history of an RFC file, together with the pull requests that changed
it, is the record of how a rule evolved.

### RFCs and the organization documents

The accepted RFCs **are** the organization's rules. The documents in
`tarantool-contrib/.github` — the organization profile, `CONTRIBUTING.md` —
are short introductions for newcomers and link to the RFCs rather than restating
them. When the two disagree, the RFC wins, and the document is fixed.

### Requests

Requests that follow from the rules — transferring a module into the
organization, taking over a module's maintainership — are issues in this
repository, filed with the issue forms it provides. Issues and pull requests
share one number sequence, so requests simply skip RFC numbers.

### Language

RFCs, their discussions and the organization documents are written in English.

### License

RFC texts are licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

### Bootstrapping

The first RFCs — this one, 0002 and 0003 — were accepted by the owners directly,
without an FCP, to give the organization a starting set of rules. They are
expected to be amended as practice shows.

## Drawbacks

- The process is slower than deciding in a chat. For an organization whose
  rules bind people outside the chat, that is intended.
- With few owners, consensus is easy to reach but also easy to block. If the
  number of owners grows, the decision rule may need revisiting.

## Alternatives

- **Decide in issues of `tarantool-contrib/.github`.** Keeps everything in one
  repository, but mixes decisions with the organization defaults and leaves no
  single text to point at.
- **Decide in Discussions only.** Good for exploring, poor for reviewing a
  precise text line by line.
- **Sequential numbering by the author.** Two concurrent proposals collide on
  the next free number; the pull request number cannot collide.
- **Frozen RFCs plus separate rule documents.** Every change would need both a
  new RFC and an edit elsewhere, and the two copies of each rule would drift.
  Amending RFCs in place keeps one copy.

## Unresolved questions

None at the time of acceptance.
