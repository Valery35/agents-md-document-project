# Notes on the measuring tool

What has already broken while the tool was being built, and what was done
about it. The list is kept for the same reason the sample keeps its own section
of limits. What broke once breaks again unless it is written down.

Each entry that concerns the code has a regression check in `tests/`. Each
check was verified by putting the old behaviour back and watching it go red.
The entry about the synced folder has no check, because it is about where the
repository lives and not about the code.

**One length limit for two languages.** The first measurer had 34 words as the
limit for both. The English sample tripped on it while its Russian original
passed. The reason was the language, not the text. The limits were
separated, and the rule about English prose running longer was written into
the set at the same time.

**Paragraph labels counted as sentences.** A label of the kind
`**Punctuation.**` was split off as a sentence of one word. A run of such
labels then showed up as a run of short sentences. The text was marked for
rhythm it did not have. A label stands to the left of a full stop the way a
heading does, and it is no longer counted.

**Placeholders glued into one sentence.** The sample is full of angle-bracket
slots. The splitter did not break after a closing bracket. Five slots in a row
became one sentence of 78 words, and the sample failed its own hard limit. A
slot is a place for text, not text, and it is no longer measured.

**A semicolon at the end of a list line.** The Russian set bans the semicolon
in prose, and the Russian sample uses it to close list items. The measurer
flagged every one. A list line is not a sentence. It is now exempt, as the
rule itself says it should be.

**Stop words found in the list of stop words.** The paragraph that bans a word
has to name it. The first measurer reported a breach on every name. A word in
quotation marks is a mention, not a use, and quoted text is now skipped.

**Paragraph breaks lost.** The measurer joined every paragraph between two
lists into one chunk. Only the first paragraph label was removed, and the rest
became sentences again. A blank line now closes a paragraph.

**Every colon reported as a breach.** The Russian rule bans a colon inside a
sentence and allows it before a list. A colon before an inline enumeration
looks the same to a regular expression as a colon joining two clauses. The
check now reports a colon as a place for the eye, not as a breach, and skips
the ones followed by a comma-separated enumeration. One real finding survived
in the Russian sample and is left there on purpose.

**A repository inside a synced folder.** The working folder lived in Dropbox.
Dropbox syncs `.git` along with everything else. On two machines that produces
conflicted copies inside `.git` and a repository that has to be repaired by
hand. The repository is created outside the synced folder.

**Cyrillic and spaces in file names.** The source files carried both. They
survive poorly through archives and mail, and a name with a space breaks a
command line written without quotes. The rule is in the set, and the files
were renamed before the first commit.

**"Молча" passed the check.** A plugin announcement said that a record "не
пропадает молча", does not vanish silently. The word was not in the list of stop
words, the measurer let it through, and a person noticed it while reading. The
image gives the program a voice and does not name the action. The word is added
to the list with the replacement "без сообщения, без записи об ошибке", without
a message or a record of the error. The same check found two more places in the
Russian sample AGENTS.example.ru.md, and both were rewritten.

**Markdown markup counted as prose.** Three places gave false figures in every
README. A badge line ran as text. The address inside a link counted as words. A
sentence starting with a digit was not split off. Four badge lines in a row
merged into one sentence of 234 words. A line holding two sentences of 4 and 2
words counted as one of 50. A line of badges alone is markup now, only the text
of a link is counted, and the split happens before a digit and before a link as
well. In the PlanetX module README the mean fell from 10.9 to 9.4. Sentences
over 34 words went from 3 to 0.

## Running the checks

```
python -m unittest discover tests
```

The last check runs the tool over every markdown file of the repository with
the `register` band. The set has to pass its own rules, and this is where that
is enforced.
