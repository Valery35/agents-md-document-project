# -*- coding: utf-8 -*-
"""Проверки на возврат для measure.py.

Каждая проверка отвечает одной записи раздела «Что уже ломалось» в NOTES.md
и краснеет, если прежнее поведение вернётся. Последняя проверка прогоняет
измеритель по всем текстам репозитория: комплект обязан проходить свой
собственный свод.

    python -m unittest discover tests
"""

import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import measure as m  # noqa: E402


def kinds(findings):
    return [kind for _, kind, _ in findings]


def levels(findings, kind_part):
    return [level for level, kind, _ in findings if kind_part in kind]


def texts(pairs):
    return [s for s, _, _ in pairs]


class LimitsPerLanguage(unittest.TestCase):
    """Запись 1. Предел длины у каждого языка свой."""

    def test_english_sentence_of_40_words_passes_english_limit(self):
        s = " ".join(["word"] * 39) + " end."
        stats, findings = m.check_rhythm(m.sentences(s), "en", "register")
        self.assertEqual(stats["over_error"], 0)
        self.assertEqual(stats["over_warn"], 1)

    def test_russian_sentence_of_36_words_breaks_russian_limit(self):
        s = " ".join(["слово"] * 35) + " конец."
        stats, _ = m.check_rhythm(m.sentences(s), "ru", "register")
        self.assertEqual(stats["over_error"], 1)

    def test_limits_differ(self):
        self.assertLess(m.LIMITS["ru"]["error"], m.LIMITS["en"]["error"])


class LabelIsNotASentence(unittest.TestCase):
    """Запись 2. Подпись абзаца вида **Пунктуация.** предложением не считается."""

    def test_label_is_stripped(self):
        pairs = m.sentences("**Пунктуация.** Тире в прозе только одно.")
        self.assertEqual(texts(pairs), ["Тире в прозе только одно."])


class PlaceholderIsNotText(unittest.TestCase):
    """Запись 3. Угловые скобки образца не измеряются и не склеиваются."""

    def test_placeholders_are_dropped(self):
        pairs = m.sentences("<Предмет работы.> <Состояние кода.> Работа идёт.")
        self.assertEqual(texts(pairs), ["Работа идёт."])

    def test_placeholder_closes_a_sentence(self):
        pairs = m.sentences("Стадия <постановки>. Дальше идёт код.")
        self.assertEqual(len(pairs), 2)


class SemicolonInListLine(unittest.TestCase):
    """Запись 4. Точка с запятой в конце строки перечня прозой не считается."""

    def test_list_line_is_exempt(self):
        pairs = m.sentences("Сверяется следующее:\n\n- один пункт;\n- второй пункт.\n")
        self.assertNotIn("точка с запятой", kinds(m.check_punctuation(pairs, "ru")))

    def test_prose_semicolon_is_still_an_error(self):
        pairs = m.sentences("Раз идёт; два идёт.")
        self.assertIn("точка с запятой", kinds(m.check_punctuation(pairs, "ru")))


class QuotedWordIsAMention(unittest.TestCase):
    """Запись 5. Слово в кавычках упоминание, а не употребление."""

    def test_quoted_stop_word_is_skipped(self):
        pairs = m.sentences("Слово «софт» под запретом.")
        self.assertEqual(m.check_words(pairs, "ru"), [])

    def test_unquoted_stop_word_is_found(self):
        pairs = m.sentences("Поставили новый софт на машину.")
        self.assertEqual(len(m.check_words(pairs, "ru")), 1)


class SilentlyIsAStopWord(unittest.TestCase):
    """Запись 10. «Молча» стоп-слово, а «по умолчанию» нет."""

    def test_silently_is_found(self):
        pairs = m.sentences("Запись, которую поставить нельзя, не пропадает молча.")
        self.assertEqual(len(m.check_words(pairs, "ru")), 1)

    def test_default_is_not_found(self):
        pairs = m.sentences("Длина пикета по умолчанию равна 100 м.")
        self.assertEqual(m.check_words(pairs, "ru"), [])


class ParagraphBreakIsKept(unittest.TestCase):
    """Запись 6. Пустая строка закрывает абзац, подпись снимается у каждого."""

    def test_every_label_is_stripped(self):
        text = "**Абзац.** Открывается тезисом.\n\n**Содержание.** Без воды.\n"
        got = texts(m.sentences(text))
        self.assertEqual(got, ["Открывается тезисом.", "Без воды."])

    def test_short_run_resets_at_paragraph(self):
        text = "Раз два три.\nЧетыре пять.\n\nШесть семь.\nВосемь девять.\n"
        stats, _ = m.check_rhythm(m.sentences(text), "ru", "register")
        self.assertEqual(stats["run"], 2)


class ColonIsAPlaceForTheEye(unittest.TestCase):
    """Запись 7. Двоеточие перед перечислением пропускается, между частями
    сложного предложения идёт к просмотру, а не как нарушение."""

    def test_enumeration_passes(self):
        pairs = m.sentences("Мест много: состав работ, записка, ведомость.")
        self.assertNotIn("двоеточие внутри предложения",
                         kinds(m.check_punctuation(pairs, "ru")))

    def test_clause_join_is_a_warning(self):
        pairs = m.sentences("Буквы ё в именах нет: она портится при передаче.")
        self.assertEqual(levels(m.check_punctuation(pairs, "ru"), "двоеточие"),
                         ["warn"])

    def test_list_intro_passes(self):
        pairs = m.sentences("Сверяется следующее:\n\n- пункт.\n")
        self.assertNotIn("двоеточие внутри предложения",
                         kinds(m.check_punctuation(pairs, "ru")))


class FileNames(unittest.TestCase):
    """Запись 9. Пробелы, знаки вне ASCII и буква ё в имени файла."""

    def test_space_is_an_error(self):
        f = m.check_filename(pathlib.Path("Работа с текстами.md"), "ru")
        self.assertIn("error", levels(f, "имя файла"))

    def test_yo_is_an_error(self):
        f = m.check_filename(pathlib.Path("ёлка.md"), "ru")
        self.assertIn("error", levels(f, "имя файла"))

    def test_clean_name_passes(self):
        self.assertEqual(m.check_filename(pathlib.Path("RULES.en.md"), "en"), [])


class CommaSplice(unittest.TestCase):
    """Английская зацепка на сцепку: настоящая сцепка видна, придаточное нет."""

    def test_real_splice_is_reported(self):
        pairs = m.sentences("The file is short, it is read in one pass.")
        self.assertIn("возможная сцепка / comma splice",
                      kinds(m.check_punctuation(pairs, "en")))

    def test_subordinate_clause_is_not(self):
        pairs = m.sentences("When it is short, it is read in one pass.")
        self.assertEqual(m.check_punctuation(pairs, "en"), [])


class ListItemsAndRuns(unittest.TestCase):
    """Перечень из коротких строк рядом коротких предложений не считается."""

    def test_list_does_not_form_a_run(self):
        text = "Список:\n\n" + "\n".join(f"- пункт {i}" for i in range(6)) + "\n"
        stats, _ = m.check_rhythm(m.sentences(text), "ru", "register")
        self.assertLessEqual(stats["run"], m.MAX_SHORT_RUN)


class MarkdownIsNotProse(unittest.TestCase):
    """Разметка markdown словами автора не считается."""

    def test_badge_line_is_not_prose(self):
        badge = ("[![Установить](https://img.shields.io/badge/a-b-blue.svg)]"
                 "(https://plugins.qgis.org/plugins/planetx/)")
        pairs = m.sentences(badge + " " + badge + "\n")
        self.assertEqual(texts(pairs), [])

    def test_link_address_is_not_counted(self):
        text = ("Модуль бесплатный и открытый. [Поддержать разработку]"
                "(https://github.com/Valery35#%D0%BF%D0%BE%D0%B4%D0%B4)\n")
        pairs = m.sentences(text)
        self.assertEqual([m.word_count(s) for s in texts(pairs)], [4, 2])

    def test_sentence_starting_with_a_bold_word_is_split(self):
        text = "Разница существенная. **stream_km** это длина водотока.\n"
        self.assertEqual(len(m.sentences(text)), 2)

    def test_html_entity_is_not_a_semicolon(self):
        pairs = m.sentences("Ширина 30&nbsp;метров на всём участке реки.\n")
        self.assertEqual(m.check_punctuation(pairs, "ru"), [])

    def test_sentence_starting_with_a_digit_is_split(self):
        text = ("В тот день не было облаков. 15 января 2026 года над "
                "Западной Сибирью снег закрыт на 78 процентов.\n")
        self.assertEqual(len(m.sentences(text)), 2)


class LanguageDetection(unittest.TestCase):

    def test_detects_both(self):
        self.assertEqual(m.detect_lang("Текст на русском языке."), "ru")
        self.assertEqual(m.detect_lang("A text in English."), "en")


class TheSetPassesItsOwnRules(unittest.TestCase):
    """Комплект репозитория проходит собственный свод без нарушений."""

    def test_all_markdown_passes(self):
        files = sorted(str(p) for p in ROOT.glob("*.md"))
        self.assertTrue(files)
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()):
            code = m.main(["--band", "register", *files])
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
