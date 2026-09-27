# tarantool-contrib RFCs

Organization-wide rules of [tarantool-contrib](https://github.com/tarantool-contrib)
are decided and kept here as RFCs: how modules join the organization, what a
module repository must provide, how rocks are published, and how the process
itself works.

Decisions that concern a single module belong to that module's repository, not
here.

## Index

| RFC | Title | Status |
| --- | ----- | ------ |
| [0001](text/0001-rfc-process.md) | The RFC process | Accepted |
| [0002](text/0002-governance.md) | Governance of tarantool-contrib | Accepted |
| [0003](text/0003-module-requirements.md) | Module repository requirements | Accepted |

## How it works

The process is defined in [RFC 0001](text/0001-rfc-process.md). In short:

1. **Discuss the idea** in [Discussions](https://github.com/tarantool-contrib/rfcs/discussions).
   An idea that nobody else needs does not need an RFC.
2. **Write the RFC.** Copy [`0000-template.md`](0000-template.md) to
   `text/0000-<slug>.md`, fill it in, and open a pull request.
3. **Take the number.** Rename the file to the pull request number, zero-padded:
   pull request #7 becomes `text/0007-<slug>.md`.
4. **Discuss the text** in the pull request review.
5. **Final comment period.** When the discussion settles, an owner announces a
   final comment period of 7 days with a proposed outcome.
6. **Decision.** After the period the pull request is merged (accepted) or
   closed with the reasons (rejected).

Accepted RFCs are the rules themselves, and they are amended in place as
practice shows: a pull request against the RFC file, decided by the owners.

## Requests

To bring a module into the organization or to take over a module that is
looking for a maintainer, [open an issue](https://github.com/tarantool-contrib/rfcs/issues/new/choose)
with the matching form.

## License

The RFC texts are licensed under [CC BY 4.0](LICENSE).
