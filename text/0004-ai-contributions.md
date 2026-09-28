# RFC 0004: AI-assisted contributions

- **Status:** Proposed
- **Authors:** @bigbes
- **Created:** 2026-09-28
- **Discussion:** https://github.com/tarantool-contrib/rfcs/pull/4
- **Supersedes:** —

## Summary

Contributions made with the help of AI tools are welcome in tarantool-contrib,
as long as a person stands behind the result. Contributors are asked to
disclose how much of the work the AI did, on a scale from 0 to 10; disclosure
is not mandatory, but a contribution without it is judged by the maintainers'
own estimate of its level. By default the organization accepts contributions up
to level 7, where a person set the requirements and tested the result, even
without reading every line. A module's maintainers MAY set a different policy
for their repository, including whether disclosure is required there. In no
repository does a commit or a file credit an AI: no `Co-authored-by` naming a
model, no *Generated with* lines.

The scale is taken from [VisiData](https://visidata.org/ai).

## Motivation

AI tools are already part of how people write code, and most modules here are
maintained by one person in their spare time. A contribution prepared with an
agent and properly tested is worth more to such a module than no contribution
at all, so banning AI would cost the organization help it needs.

The trouble is the cost the tools move onto the maintainer. Generating a
plausible pull request takes minutes; reviewing it takes the maintainer's
evening. Without disclosure the maintainer cannot tell a change its author
understands from one nobody has run, and has to review every pull request as if
it were the latter. And if nobody answers for a change, there is nobody to
answer review questions or to fix what breaks later.

A disclosed level fixes the first problem: the maintainer knows what kind of
review a change needs before starting it. The requirement for a person fixes
the second.

Disclosure is asked for, not required. A self-reported level cannot be
verified, so making disclosure mandatory would only add a rule that cannot be
enforced. Instead, a contributor who does not disclose leaves the estimate to
the maintainer, and the maintainer's estimate is what the contribution is
judged by.

## Detailed design

The rules below use RFC 2119 keywords.

### AI levels

The level measures how much human attention and understanding went into a
contribution, whatever the tool. A change gets the highest level that applies
to any substantial part of it.

- 0: no AI at all.
- 1: the author asked a chatbot for ideas, but wrote every line by hand, with
  no copy-paste and no AI autocompletion.
- 2: the author wrote nearly all of the code; small pieces were generated
  (boilerplate, a regular expression). AI autocompletion is fine at this level.
- 3: the author wrote the code, with non-trivial generated parts in it:
  multi-line fragments, algorithms with loops.
- 4: the author wrote most of the code, but an AI tool created or edited files
  itself, typically tests and documentation. Any agent that edits the
  repository directly (Claude Code, Codex, Cursor's agent mode, Aider and the
  like) puts a contribution at level 4 or above.
- 5: an AI generated most of the code; the author read every line and fully
  understands it.
- 6: an AI generated most of the code; the author directed the work like a team
  lead and verified it by testing, without fully understanding the logic.
- 7: the author wrote the requirements and an AI produced a working solution;
  the author worked on the specification and the testing, and did not read
  the code closely.
- 8: the author handed the task to an AI and did little beyond a basic check
  of the result.
- 9: the author set the task and did nothing after that.
- 10: an autonomous bot with no human attention at all.

### Disclosure

- A pull request SHOULD state its AI level in the description, as a line of
  the form `AI level: N`.
- At level 4 and above, the description SHOULD also name the model and its
  version (for example, `AI level: 6, Claude Opus 5.5`).
- An issue, a review comment or a security report whose text is substantially
  AI-generated SHOULD say so.
- A disclosed level is the contributor's own honest assessment. When in doubt
  between two levels, the higher one is the right answer.
- When a contribution does not disclose its level, the maintainers estimate it
  themselves, and their estimate decides how the change is reviewed and whether
  it is accepted. A contributor who disagrees with the estimate can disclose
  the level; there is no other appeal.

### The person behind a contribution

At every accepted level, the person who opens a pull request vouches for it.
They MUST:

- have run the change and its tests themselves, and seen that it works;
- be able to explain what the change does and why it is needed;
- answer review questions and make the requested changes themselves, or
  through their tools, remaining responsible for the result;
- make sure the contribution can be licensed under the repository's license.

A pull request opened from a bot account MUST name the person operating it;
otherwise nobody answers for it.

A pull request description SHOULD be short and state what was tested and how.
A long generated description is not a substitute for that.

### No AI attribution in the repository

AI involvement is disclosed in the pull request. The repository itself, its
history and its files, names only people.

- Commit messages MUST NOT carry a `Co-authored-by:` trailer naming an AI
  model, an AI tool or its bot account.
- Commit messages MUST NOT carry any other AI attribution either: trailers such
  as `Assisted-by:` or `Generated-by:`, and lines such as *Generated with
  Claude Code*, whatever the tool adds by default.
- Code, comments and documentation MUST NOT carry markers such as *generated by
  AI* or *written with ChatGPT*.
- The author of a pull request that carries such attribution is asked to
  remove it, or the maintainers remove it when merging.

A commit's author is the person who vouches for it. `Co-authored-by` names
someone who shares that responsibility and can be asked about the change; a
model can do neither, and GitHub would list it among the repository's
contributors. Other attribution lines are the tools' advertising, and they stay
in the history long after anyone cares which version of which tool was used.

`Co-authored-by` for people is not affected, nor are the headers that
deterministic code generators write (`Code generated by ... DO NOT EDIT`).

This section applies to every repository in the organization; a repository
policy does not change it.

### The default policy

Unless a repository sets its own policy:

- Contributions at levels 0 to 7 are accepted. The level tells the maintainer
  how much review the change needs; a level 7 pull request gets a closer review
  of the code than a level 2 one, because nobody but the maintainer has read
  it.
- Contributions at levels 8 to 10 are not accepted. Nobody has checked them
  beyond a glance, so the whole cost of the change would fall on the
  maintainer.
- A maintainer MAY decline a large pull request at a high AI level that they
  do not have time to review, and ask for it to be split or discussed in an
  issue first.

Level 7 is the limit because it is the last level at which a person owns the
result: they decided what the change must do and checked that it does it. At
level 8 nobody has done even that, and the maintainer would be reviewing a
change that nobody can answer for.

### Repository policies

- A module's maintainers MAY set a different AI policy for their repository:
  stricter (for example, no AI-generated code at all, or nothing above
  level 3) or looser (for example, accepting level 8 changes from an agent the
  maintainers run themselves). The ban on AI attribution in the repository is
  the one rule a repository policy cannot change.
- When the maintainers disagree, the module's **lead maintainer** decides. The
  lead maintainer is the maintainer the others name as lead, or, if nobody is
  named, the maintainer who brought the module into the organization.
- A repository policy MUST be written in the repository's `CONTRIBUTING.md`,
  in a section titled *AI-assisted contributions*. It replaces the default
  policy for that repository from the moment it is published.
- A repository policy MAY make disclosure mandatory, or waive it entirely, for
  example in a module whose maintainers assume that every contribution is
  AI-assisted and review accordingly. A repository policy that does not mention
  disclosure keeps the disclosure rules of this RFC.

### Consequences

- A pull request above the accepted level, disclosed or estimated, MAY be
  closed without review.
- A contribution whose disclosed level is clearly lower than the real one is
  closed. Repeated misrepresentation is a moderation matter (RFC 0002).
  Not disclosing is not misrepresentation: a wrong number is worse than none.
- Pull requests, issues and comments from bots nobody asked for (levels 9 and
  10) are spam. The owners block such accounts from the organization.
- A security report that nobody has reproduced, typically a vulnerability
  claimed by an AI tool, MAY be closed with a request that the reporter
  reproduce it first.

### What this RFC does not cover

- Tools the maintainers themselves configured, such as Dependabot or Renovate:
  they are part of the repository's setup, not outside contributions.
- The maintainers' own commits pushed without a pull request, apart from the
  ban on AI attribution, which applies to every commit.

## Drawbacks

- The level is self-reported and cannot be verified. The policy relies on
  honesty, and on the maintainers' eye for a contribution that does not match
  its declared level.
- An undisclosed contribution is judged by a guess. A human-written change may
  be estimated at a high level and reviewed with suspicion, or turned away,
  until its author discloses the level.
- Level 7 lets in code its author has not read. The maintainer becomes the
  first person to read it. This RFC makes that review cost visible; it does not
  remove it.
- Different policies in different repositories mean a contributor has to check
  the module's `CONTRIBUTING.md` before sending AI-assisted work.

## Alternatives

- **Ban AI-generated contributions.** Unenforceable, and costs the
  organization contributions it needs. A maintainer who wants this can still
  set it for their repository.
- **Mandatory disclosure**, as in VisiData. A rule that cannot be checked is
  kept only by the honest, and they would disclose when asked anyway. Leaving
  the estimate to the maintainer gives the same incentive without pretending
  to enforce anything.
- **Disclose in commit messages**, with `Co-authored-by` or an `AI-level:`
  trailer, so that the history records it. The history is about the code, and
  every commit already leads to its pull request, where the disclosure is.
- **Accept everything, disclosure only.** Leaves maintainers to review level 8
  to 10 changes nobody has checked; for a single-maintainer module that is
  enough to bring it to a halt.
- **Cap the default at level 5**, where the author understands every line.
  Safer for review, but it turns away tested contributions from users who can
  describe and verify a fix without being fluent in the module's code, and the
  maintainer's review covers the understanding anyway.
- **A yes/no "AI was used" checkbox.** Says nothing useful: autocompletion and
  an unattended agent both answer "yes".
- **Write our own scale.** VisiData's is already public, reasonably precise,
  and familiar to contributors who have encountered it elsewhere.

## Unresolved questions

- Whether the lead maintainer role belongs in RFC 0002, rather than being
  defined here.
- Whether the organization-wide pull request template should get an
  `AI level:` field, so that disclosure is prompted rather than remembered.
