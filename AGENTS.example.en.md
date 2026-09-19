# AGENTS.md - the working context of a project

A sample working-context file. The domain content has been stripped out and
the structure and the working rules have been kept. Angle brackets mark the
places where your own project goes.

This file is read first at the start of any new chat about the project. The
single source of truth is this file and the set of documents next to it, not
the correspondence. When something changes in the statement of work or in the
process, the change is written here.

This is not a translation of the Russian sample but an adaptation. The rules
that depend on Russian punctuation and Russian word pairs have been replaced
by their English counterparts, and the rhythm norms carry their own numbers.
The rest is the same, because it does not depend on the language.

The "Requirements for texts" section is often shared between several
projects. When it is edited in one place, it is edited in the others.

## How a session starts

1. Read this file in full.
2. Read the documents of the set that the task touches.
3. Check the revision number of the set here against the one on the desk.
4. Name the task and the criterion of completion before changing anything.

The correspondence of past sessions is not recoverable and does not count as a
source. If it held a decision that is not here, the decision is written here
first and used afterwards.

## What this is

<The subject of the work in one sentence: what system, for whom, on what
site.> The work is at the stage of <statement, design, development>. <The
state of the code.>

Approval takes <number> steps. First <the customer department> accepts <list
of sections>. Then <the second department> approves <list of sections>.

## The set of documents

| File | Content | Readers |
|---|---|---|
| `<scope_of_work>.md` | Scope of work, <number> sections | <customer department> |
| `<detailed_note>.md` | Detail of module <number> | <second department> |
| `<rollout>.md` | Stages, acceptance, risks, training | those who plan and pay |
| `<concept>.md` | Two pages about the system | management |
| `<findings>.md` | Discrepancies in the source documents | <customer department> |
| `<register>.xlsx` | List of forms with module and template file | both departments |
| `<prototype>.xlsx` | Calculation tables with a worked example | <customer department> |
| `<Form_*>.xlsx` | Prototypes of the record forms, future templates | both departments |

Diagrams are listed on a line of their own, each as png and svg. The single
source of the text is markdown, and the docx files are built from it by pandoc
with a reference document.

## Where things live and which copy is the master

- Working copy: `<path>`. This is the master, and every edit goes here first.
- Exchange folder: `<path>`. Finished work is collected from it and nothing is
  edited there.
- Version store: `<repository or folder of revisions>`.

When copies disagree, the working copy wins. A disagreement is not settled in
silence. First it is stated which files differ and how, then a decision is
taken.

## The customer's regulatory base

Abbreviations are agreed once and hold across every document of the set. For
each document the full title, the issuer, the year and the sections that are
cited are given.

- **<Abbreviation>** - <full title, issuer, year>. <What it settles: the forms
  of the documents, the order of calculation, worked examples.>
- **<Abbreviation>** - <full title, volume, sections>. <Deadlines in section N.>

Revisions of one document are listed as a chain. It is stated which revision
each previously accepted document was made against and which revision is in
force now. An intermediate link is not skipped.

A regulation is quoted verbatim and with the clause number. A retelling in
one's own words does not go into the document, because at the approval stage
the letter is what gets compared.

Not received and requested: <list>. The list is kept in this file, not in the
correspondence.

## The customer's existing programs

- **<Program>** (<development environment>) - <what data it holds>. <Volume of
  data, storage format, way of exporting.>
- **<Program>** (<development environment>, <DBMS>) - <what data it holds>.
- **<Program>** - <what data it holds, deployed or not>.

Each kind of data is held in one program. The system reads the data of the
neighbouring programs and does not change it.

## The composition of the modules

The numbering follows the order in which the modules are used in the work, not
the order in which they were analysed.

| No. | Module | Period |
|---|---|---|
| 1 | <Reference data and the initial model> | precondition |
| 2 | <Module> | <period> |
| ... | ... | ... |

The modules of the detailed note are a detail of module <number> and do not
form a numbering of their own.

The dependency graph within a reporting period is acyclic. Closed loops, where
they exist, run across the year boundary and are named explicitly.

## Decisions not to be reopened without discussion

The section holds the agreements that the conversation keeps returning to.
Each decision is written as a statement in the first sentence, with the
grounds after it.

**<The unit of record.>** <What is taken as the unit and what sets it.>

**<The model of a fact.>** <How the main data object is built, what is taken
from the source documents, what is measured.> <The clause of the regulation
that requires it.>

**<The separation of data layers.>** <What data is held as a separate layer
and with what rights.> <Who does not edit what.>

**Versioning of the calculation.** For every closed unit the revision of the
method, the revision of the input parameters and the calculation data are
kept. An approved document is not recalculated after the fact. A change of the
input data shows the list of affected units and the size of the divergence.

**The client has no write access to the record tables.** Only the database
writes, through stored procedures that check whether the operation is
admissible. This is the condition the whole protection rests on, and the rest
is an addition to it.

**Architecture.** <The store and its version at the customer.> <What the
record part runs on, what the graphical part runs on, what ties them.> <When
the decision about a single stack is taken.>

**Exchange with neighbouring systems.** <Format, direction, the way objects
are identified.> <What is deferred and until what answer.>

## What the customer decides, not the developer

The list removes the repeated analysis of the same questions.

- the source of the input values while there is no statistics of one's own
- the forms of the documents in use, set by the orders of the company
- the agreements on exchange with neighbouring systems
- the list of controlled parameters and the size of the tolerances
- the distribution of access rights to the database, fixed by an order
- the boundaries of the work on disputed sites

## What is not done without asking

Actions that cannot be undone or that a third party sees.

- sending anything to the customer, drafts included
- publishing and mailing out
- deleting files and overwriting someone else's edits
- writing to the shared version store
- changing a document that has already been approved

Readiness for such an action is reported, and the action itself waits for an
answer.

## Questions before the work

Before starting, the questions whose answers change the shape of the solution
are written out and asked as one list, in one go. Not one at a time and not
along the way, when half the work is done and redoing it is expensive.

What goes on the list is what turns the work around:

- the composition and the meaning of the input values, when the document is
  not at hand
- what counts as missing data and what is done with such a row
- what the check runs on and which result counts as correct
- where the boundary of the work runs, that is, what is deliberately not done

What does not go on the list is anything with an obvious default. That is
decided alone, and the default taken is named aloud in the first line of the
answer, so that it can be overturned in one line. Choosing in silence is not
allowed. An unspoken assumption surfaces at handover and costs more than the
question would have.

## Acceptance of the work

A task has a criterion of completion that can be checked. The criterion is
named before the work starts, not after.

To fix an error, a reproduction is written first. It states on what data the
error shows and what exactly is wrong. If the error could not be reproduced,
that is said, and a guess about the cause is not passed off as the cause.

For a new piece of work, the way to run it and the expected result are named
first, and the work itself is done after that.

Work of several steps gets a short plan with a check at every step.

"Done" is said only after a run. When there was no run, what is said is "made,
not checked, needs a run on your side". "Should work" does not count as a
result.

An error that has been worked out gets a regression check, that is, a test
that turns red on the previous behaviour. The check is itself verified by
putting the old behaviour back, otherwise there is no telling whether it
catches anything.

## Revisions of the set

Every revision that is handed over gets its own number. Two different
revisions under one number are not allowed, because afterwards there is no way
to tell what anyone is holding.

The number changes at the moment of handover, not at the moment of editing. A
number handed over is closed, and the next edit goes under a new one.

Who moves which part of the number is agreed in advance. <The rule of the
project.>

## Open questions

The full lists are in the documents of the set, the key ones are here.

<The question in one sentence. Grounds: what the document says, what the
department reports.>

<The question in one sentence.>

<The question in one sentence.>

## When the data is not enough

What is missing is called missing. The text is not completed with plausible
values, and the absence of an answer is not replaced by a guess.

When the work needs a document or a file that is not there, it is requested
before the work starts, not after handover.

When a question can only be settled by the customer, it goes into the section
of open questions and into a document of the set, rather than staying in the
correspondence.

## People

- **<Surname and name>** - <organisation, department>, <role in the project>.
- **<Surname and name>** - <organisation>, <role in the project>.

## Requirements for texts

The general part always holds, and the refinements by type of document follow
it.

In a live project this section is replaced by one line linking to the shared
model, because a copy diverges from the original at the second edit. The shared
model of this set is the file `RULES.en.md` next to it. The section is written
out in full here only because a sample has to be readable on its own.

### General

**Punctuation.** A comma splice is an error and is always broken up: two
independent clauses joined by a comma become two sentences, or the comma gains
a conjunction, or one clause becomes subordinate. The em dash and the
semicolon are legitimate in English and are not banned, but neither is a way
to keep a run-on sentence alive. A colon may join two clauses when the second
explains the first, and it does not become a substitute for a full stop.

What is not counted as a problem and is not edited: a label in a table
("Deadline: 30 days"), a section heading, a figure caption, a line of a list
and a column head in a register. To the left of such a colon stands a name,
not a sentence.

**Sentence.** Complete, with a subject and a predicate. No naming fragments of
the kind "Modules: the second one in full". Nothing runs longer than 45 words.

What is broken up is the splice, not the subordination. A subordinate clause
inside a sentence stays, because it holds one thought instead of gluing three
together. A thirty-word period with one subordinate clause reads, and three
eight-word stumps in its place do not.

Rhythm is measured by spread, not by the mean. The same mean comes out of live
prose and of a row of stumps of equal length, so the mean on its own says
nothing.

| Text | Mean | Short (up to 8 words) | Long (from 19) |
|---|---|---|---|
| Registers, labels, lists | 10-14 | up to half | from 0 % |
| Scope of work, note, concept | 15-20 | up to a quarter | from 25 % |
| Letter, announcement | 10-15 | up to two fifths | from 0 % |

English prose runs longer than Russian for the same content, and the numbers
above differ from the Russian ones for that reason. No more than three short
sentences in a row. A paragraph made entirely of short sentences is allowed
only when it is a list of steps.

**The missing word.** A pair of modifiers rests on a noun that has been named.
"The report shows the raw against the weighted" cannot be read, because the
word the pair stands on was supplied in the author's head and never reached
the page. The check is simple. Drop the second modifier, and a grammatical
phrase has to remain. "Two histograms of the values, one raw and one weighted"
survives it. Pairs such as "before and after", "inner and outer", "first and
second" behave the same way. No automatic check catches this, only reading.

**Paragraph.** Opens with the point and develops it afterwards. Each fact is
stated in one place, and a repetition is replaced by a reference to that
place.

**One name in every place it is shown.** A thing is called by one word not
only in prose. A document set has many such places: the scope of work, the
detailed note, the register of forms, a column head in the prototype, the
title of a diagram and its caption. Renaming goes through the list of places
in one pass. Editing one place leaves a divergence in the rest, and the reader
who arrives from the note at the register looks for a name that is not there.

**Stop words.** Each one is recorded with its replacement. Without the
replacement the ban gets applied by deletion, because deleting is cheaper than
rewriting.

| Do not write | Write |
|---|---|
| leverage, utilise | use |
| in order to | to |
| simply, just, obviously | nothing, cut the word |
| seamless, robust, powerful | what the thing actually does |
| easy to use, intuitive | the number of steps it takes |
| state of the art, best in class | the measured figure |
| a number of | the count, or nothing |

The list grows from findings, and every new line arrives with a replacement of
its own.

**Imagery is allowed by list.** An image that names a thing and is accepted in
the industry stays in the text. Anything not on the list is banned, and the
list grows by the author's decision. What separates the lists is not
vividness, but whether the image names the thing or stands in for it. A
"pocket" names the shape of an area without data, and there is no other word
for it. "Cosmetics" names nothing and only conveys the author's attitude to
what is being written about.

**Colloquial vocabulary is not allowed.** No household or medical comparisons.
A defect is called a defect and its removal a removal, not an "illness" and a
"cure".

**Count and amount.** "Number of" goes with things that are counted, "amount
of" with a mass that is not. Number of boreholes, number of sections, number
of rows. Amount of water, amount of work.

**A statement without comparison and without evaluation.** What is more
important and what is better is not said. The facts are put side by side and
the reader compares them.

**Content.** No filler, no guesses, no reasoning around the subject. A term is
explained at its first use. A statement is either checkable or it is not
there.

**A figure arrives with its source.** Every value in the text has a place it
came from: a clause of a regulation, a worked example, an export from a
program. A figure without a source is struck out at the approval stage
together with the paragraph that stood on it. A value taken provisionally is
marked as such, with a note of who confirms it.

### Voice

In business documents for the customer there is no first person at all.
Neither "we", nor "our", nor "us". Impersonal wording does the work: "the
system keeps", "is performed in the record system".

On behalf of the company in public texts it is "we", "we build", "we develop".
Not "I".

### Business documents for the customer

The technology is described, not the benefits. Nothing of the "what the system
gives you" kind.

There is no comparison with the current order of things. Neither "at present
this is done by hand", nor "the previous tool is no longer needed".

A heading names the subject rather than evaluating it.

No internal jargon. A jargon phrase is replaced by a description of the
action.

Terms are taken from the customer's documents. When one value is called
differently in two documents, the synonymy is stated once in the text.

### Release notes and announcements

Written for the one who uses the thing, not for the one who made it. First
what the reader will see with their own eyes, then in one sentence why it is
there for them.

No file names and no internal names. The analysis of the cause and the details
of the work stay in the change log and do not go onto the release page.

Only the figures that are comparable with the reader's own work are quoted.

### Letters and messages in the first person

Restrained and to the point. No emotional statements and no praise of the
other side's words, no self-criticism until it is asked for, and no describing
a solution until it is done. A question has to be a question rather than a
polite form of a statement.

## Checking the set

Runs after every merge of edits from several sources: edits in docx on the
customer's side and edits in markdown on the developer's side. The merge is
exactly what produces the divergences that neither of the editors sees.

A text counts as ready after a run, not after an edit. The measurements are
made by a tool rather than by eye, and the numbers are quoted in the answer.
The word "checked" without numbers does not count as a result.

### What is checked

**Punctuation and vocabulary.** Comma splices, stop words, colloquial
vocabulary, "amount" where "number" belongs.

**Sentence length.** The mean and the count of sentences longer than 38 and 45
words are measured and quoted as numbers.

**Divergences between documents.** The following are compared:

- one statement put in different ways;
- a different count of stages, modules and periods;
- different deadlines and dates;
- different names for the same documents, forms and programs;
- a description of work done by a person against work done by the system.

**Terms.** One entity is called the same in every document. The pairs that
need a check of their own are listed and the list grows with the findings.

**References.** The following are compared:

- the numbers of sections within a document and between documents;
- the numbers of tables and of clauses of regulations;
- the numbers and captions of figures;
- references to modules by number and by name;
- the template file names in the register against the files of the set.

**Numeric values and reference data.** The following are compared:

- the dates and numbers of minutes, orders and letters;
- the values of the worked example and the rounding;
- the deadlines in days and in days of the month;
- the numeric limits and tolerances.

**Logic.** Statements that contradict each other within one document.
Something promised in the introduction and not described later. Something
described in the text and not included in the composition of the modules.
Elements of the dependency diagrams with no counterpart in the tables.
References to subsections removed during editing.

**Separation of content.** The data model and the calculation algorithms are
described in the scope of work. The detailed notes refer to them and do not
repeat them. The concept does not retell the calculation tables and does not
quote clause numbers of regulations.

### What the check does not catch

Everything above is countable and is therefore caught by a script. None of the
following is caught: a grammatical phrase with a word missing from it, a
statement that is correct in form and wrong in substance, a paragraph that
answers a different question.

Hence the order of work. The run comes first, the reading through comes after
it, and without the reading the text is not ready. The run narrows the place
that has to be read and does not replace it. The rules about the missing word
and about one name in every place were both written after a finding, and a
person reading found both of them.

### What is not checked

Style, length, the order of the sections, the composition of the questions to
the customer.

### The format of the answer in an external check

A list of findings. For each one the file, the section, the quotation and the
substance of the divergence are given. No edits are made to the text. No
corrections are proposed, even where the divergence is removed in an obvious
way. When there are no findings, that is what is stated.

## Building the documents

The single source is markdown. The docx files are built by pandoc with a
reference document: Times New Roman 12, black bold headings, a 3 cm left
margin, the page number centred at the foot, tables with borders.

```
pandoc <document>.md -o <Document>.docx --reference-doc=<reference>.docx
```

Diagrams are inserted without alternative text, and the caption stands on a
line of its own in italics. Alternative text produces a second caption in
Word.

File names carry no spaces and no characters outside ASCII. Both survive
poorly through archives and mail, and a name with a space breaks a command
line that was written without quotes.

### Limits of the environment

The section holds what has already broken and what must not be done on this
machine.

- <List of programs with versions> is required. Without them the build does
  not run.
- <What must not be used and why.> <What replaces it.>
- <A known limit of the workplace: network, rights, volume.>

A control figure for the build is a value that changes on any noticeable edit.
The page count of the finished document, for instance. The value is named in
this file and updated when it changes.

## The log of settled questions

The section keeps the questions that took a long time to settle and may come
up again. An entry consists of the point in the heading, the circumstances and
the decision taken. An entry ends with what must not be brought back, because
otherwise it will be brought back in half a year.

**<An error in the source table.>** <What the discrepancy is, what the
calculation gives by the letter of the document and what it gives by the
worked example.> <What was adopted in the prototype and where the finding was
recorded.> <What not to bring back.>

**<The chain of revisions of a document.>** <Which revision is in force, which
one the previously accepted documents were made against.>

**<An added module.>** <On whose finding it was added and which clause of the
regulation had already required it.>

**<A renumbering of the modules.>** <The grounds for the new order.>

**Edits on the customer's side arrive as docx.** The comparison runs against
the current markdown, the edits are carried into the source and the docx is
rebuilt. The file that arrives may have been built from an outdated version,
and this is checked before the merge.
