# RULES.md - requirements for texts

Every document of the project is written and checked against these rules. The
working context file links to this page instead of copying it, because a copy
diverges from the original at the second edit.

Two of the rules rest on the language itself and carry other numbers in the
Russian set: the punctuation rules and the limit on sentence length. The rest
holds for both languages.

## General

**Punctuation.** A comma splice is an error and is always broken up: two
independent clauses joined by a comma become two sentences, or the comma gains
a conjunction, or one clause becomes subordinate. The em dash and the semicolon
are legitimate in English and are not banned, but neither one is a way to keep
a run-on sentence alive. A colon may join two clauses when the second explains
the first, and it does not become a substitute for a full stop.

What is not counted as a problem and is not edited: a label in a table
("Deadline: 30 days"), a section heading, a figure caption, a line of a list
and a column head in a register. To the left of such a colon stands a name, not
a sentence.

**Sentence.** Complete, with a subject and a predicate. No naming fragments of
the kind "Modules: the second one in full". Nothing runs longer than 45 words.

What is broken up is the splice, not the subordination. A subordinate clause
inside a sentence stays, because it holds one thought instead of gluing three
together. A thirty-word period with one subordinate clause reads, and three
eight-word stumps in its place do not.

**Rhythm.** Rhythm is measured by spread, not by the mean. The same mean comes
out of live prose and of a row of stumps of equal length, so the mean on its
own says nothing.

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
word the pair stands on was supplied in the author's head and never reached the
page. The check is simple. Drop the second modifier, and a grammatical phrase
has to remain. "Two histograms of the values, one raw and one weighted"
survives it. Pairs such as "before and after", "inner and outer", "first and
second" behave the same way. No automatic check catches this, only reading.

**Paragraph.** Opens with the point and develops it afterwards. Each fact is
stated in one place, and a repetition is replaced by a reference to that place.

**One name in every place it is shown.** A thing is called by one word not only
in prose. A document set has many such places: the scope of work, the detailed
note, the register of forms, a column head in the prototype, the title of a
diagram and its caption. Renaming goes through the list of places in one pass.
Editing one place leaves a divergence in the rest, and the reader who arrives
from the note at the register looks for a name that is not there.

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
list grows by the author's decision. What separates the lists is not vividness,
but whether the image names the thing or stands in for it. A "pocket" names the
shape of an area without data, and there is no other word for it. "Cosmetics"
names nothing and only conveys the author's attitude to what is being written
about.

**Colloquial vocabulary is not allowed.** No household or medical comparisons.
A defect is called a defect and its removal a removal, not an "illness" and a
"cure".

**Count and amount.** "Number of" goes with things that are counted, "amount
of" with a mass that is not. Number of boreholes, number of sections, number of
rows. Amount of water, amount of work.

**A statement without comparison and without evaluation.** What is more
important and what is better is not said. The facts are put side by side and
the reader compares them.

**Content.** No filler, no guesses, no reasoning around the subject. A term is
explained at its first use. A statement is either checkable or it is not there.

**A figure arrives with its source.** Every value in the text has a place it
came from: a clause of a regulation, a worked example, an export from a
program. A figure without a source is struck out at the approval stage together
with the paragraph that stood on it. A value taken provisionally is marked as
such, with a note of who confirms it.

## Voice

In business documents for the customer there is no first person at all. Neither
"we", nor "our", nor "us". Impersonal wording does the work: "the system
keeps", "is performed in the record system".

On behalf of the company in public texts it is "we", "we build", "we develop".
Not "I".

## Business documents for the customer

The technology is described, not the benefits. Nothing of the "what the system
gives you" kind.

There is no comparison with the current order of things. Neither "at present
this is done by hand", nor "the previous tool is no longer needed".

A heading names the subject rather than evaluating it.

No internal jargon. A jargon phrase is replaced by a description of the action.

Terms are taken from the customer's documents. When one value is called
differently in two documents, the synonymy is stated once in the text.

## Release notes and announcements

Written for the one who uses the thing, not for the one who made it. First what
the reader will see with their own eyes, then in one sentence why it is there
for them.

No file names and no internal names. The analysis of the cause and the details
of the work stay in the change log and do not go onto the release page.

Only the figures that are comparable with the reader's own work are quoted.

## Letters and messages in the first person

Restrained and to the point. No emotional statements and no praise of the other
side's words, no self-criticism until it is asked for, and no describing a
solution until it is done. A question has to be a question rather than a polite
form of a statement.

## Checking a text

A text counts as ready after a run, not after an edit. The measurements are
made by `measure.py` rather than by eye, and the numbers are quoted in the
answer. The word "checked" without numbers does not count as a result.

For a set of documents the check runs after every merge of edits from several
sources: edits in docx on the customer's side and edits in markdown on the
developer's side. The merge is exactly what produces the divergences that
neither of the editors sees.

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

**Terms.** One entity is called the same in every document. The pairs that need
a check of their own are listed and the list grows with the findings.

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

**Logic.** Statements that contradict each other within one document. Something
promised in the introduction and not described later. Something described in
the text and not included in the composition of the modules. Elements of the
dependency diagrams with no counterpart in the tables. References to
subsections removed during editing.

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
