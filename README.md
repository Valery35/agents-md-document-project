# AGENTS.md for a document project

A sample working-context file for a project whose output is a set of documents
rather than code, the text rules it links to, and a tool that measures what can
be counted. Everything is here in Russian and in English.

[README по-русски](README.ru.md)

Most AGENTS.md and CLAUDE.md samples describe a codebase: how to build, how to
run the tests, which linter to obey. A document project is arranged
differently. The set is approved by two departments of the customer, and every
handover carries a revision number. A regulation is quoted with its clause
number, and a question that took a month to settle is written down so that
nobody brings it back in half a year. The sample here holds that arrangement
with the domain content stripped out.

## Who it is for

For anyone who hands a set of documents to a customer: a scope of work, a
detailed note, a concept, a register of forms. The set is written with an agent
that reads `AGENTS.md`, `CLAUDE.md` or a file of the same kind. The sample
gives the agent the arrangement of such a project. The rules give it a
measurable standard for the text.

For a technical writer or an editor who wants text rules that a script can
check and a person can argue with. The rules here come with the reason behind
each of them and with a tool that quotes numbers.

Not for a code project. The usual samples of `AGENTS.md` fit a codebase better,
and nothing here is about building or testing software. Not a style guide to
adopt as it stands either. The stop-word table is one author's, and the
section below says what to do with it.

## What is inside

| File | Content |
|---|---|
| `AGENTS.example.en.md` | The sample working-context file, 30 sections |
| `AGENTS.example.ru.md` | The same sample in Russian |
| `RULES.en.md` | Requirements for texts, the English set |
| `RULES.ru.md` | The same in Russian, heading for heading |
| `measure.py` | The measuring tool, no dependencies, Python 3.8 and newer |
| `tests/` | Regression checks for the tool, one per entry in `NOTES.md` |
| `NOTES.md` | What has already broken in the tool and what was done about it |
| `LICENSE` | MIT |

## What transfers and what does not

The sample transfers whole. The order of a session, the list of what is not
done without asking and the questions asked before the work do not depend on
the domain or the language. Neither do the criterion of completion named before
the work starts, the revisions of the set and the log of settled questions.

The rules are a form to fill in, not a standard to adopt. The stop-word table
is personal. It was collected from findings in one author's texts, and a word
that grates on him may be neutral to you. What transfers is the mechanism.
Every banned word is recorded with its replacement, because a ban without a
replacement gets applied by deletion. The list grows from findings rather than
from anyone's sense of the language.

The English set is an adaptation rather than a translation. Some of the rules
rest on Russian punctuation and are wrong in English. The em dash and the
semicolon are legitimate in English, and there is nothing to ban. The ban on
the comma splice stands in their place.

## How to attach it to a project

1. Copy `AGENTS.example.en.md` into the project as `AGENTS.md`.
2. Put the content of the project in place of the angle brackets.
3. Replace the stop-word table in `RULES.en.md` with your own findings and keep
   the replacement column.
4. Replace the "Requirements for texts" section of `AGENTS.md` with one line
   linking to `RULES.en.md`. The section is written out in full in the sample
   only because a sample has to be readable on its own.
5. Put `measure.py` next to it and run the texts before handing them over.

## The run

```
python measure.py RULES.en.md
python measure.py --band register AGENTS.example.en.md
python measure.py --lang ru --band letter letter.md
```

The output for a clean text and for a text with findings:

```
== RULES.en.md   [en, register: registers, labels, lists]
   sentences        122
   mean             13.4   norm 10-14
   short <=8        31  25 %
   long >=19        22  18 %
   short in a row   1   limit 3
   longer than 38   0
   longer than 45   0   limit
   no findings
   total: breaches 0, for the eye 0

== draft.md   [en, register: registers, labels, lists]
   ...
   ! rhythm: mean 6.5 outside the band 10-14
   ! stop word: «leverage» -> use
   ? possible comma splice: The file is short, it is read in one pass.
   total: breaches 2, for the eye 1
```

The labels follow the language of the text. The language is detected by the
share of Cyrillic, and `--lang` sets it explicitly. The `--band` key picks the
rhythm band, and the default is `note`.

| Band | Texts |
|---|---|
| `register` | registers, labels, lists |
| `note` | scope of work, note, concept |
| `letter` | letter, announcement |

The tool measures sentence length and spread, looks for stop words, checks the
punctuation of the language and looks at the file name. A breach is marked with
`!` and a place for the eye with `?`. The exit code is 1 when there are
breaches, so the tool fits into a pre-commit hook or a CI step. The workflow
in `.github/workflows/check.yml` runs the checks and the tool on every push.

The tool has its own history of breaking. It is written down in `NOTES.md`,
and every entry there has a regression check in `tests/`.

The length limits are separated by language. English prose runs longer than
Russian for the same content, so the limit belongs to one language rather than
to both.

| Language | Look at it | Rewrite it |
|---|---|---|
| Russian | from 28 words | from 34 words |
| English | from 38 words | from 45 words |

## Recommendations

Take the sample first and the rules second. The sample is the reason to be
here, and the rules are a form whose content you will replace.

Pick the band by the type of document, not by the set. A register of forms and
a concept note have different rhythm, and one band for both fails one of them.

Do not rewrite a sentence to satisfy the tool. A `?` is a place to look, and a
sentence that reads well with a subordinate clause stays as it is. The rule
about stumps is in the set because a tool with a length limit produces them
when it is obeyed without reading.

Keep the rules in one file and link to it from every project. A copy diverges
from the original at the second edit, and the second edit always comes.

Measure English with the English limits. A Russian limit applied to English
prose fails a text for being written in English.

Keep the repository outside Dropbox, OneDrive and their kind, or exclude
`.git` from the sync.

## What the run does not catch

A grammatical phrase with a word missing from it. A statement that is correct
in form and wrong in substance. A paragraph that answers a different question.

Hence the order of work. The run comes first, the reading through comes after
it, and without the reading the text is not ready. The run narrows the place
that has to be read and does not replace it.

## License

MIT. Copy the sample into a project, edit it, and keep the notice.
