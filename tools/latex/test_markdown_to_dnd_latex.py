#!/usr/bin/env python3
import unittest

from markdown_to_dnd_latex import Converter


class InlineMarkdownTests(unittest.TestCase):
    def setUp(self) -> None:
        self.converter = Converter(follow_links=False, language="italian")

    def test_emphasis_wrapping_internal_link(self) -> None:
        value = "_[Protezione dal bene e dal male](#Protection_from_Evil_and_Good_protection_from_evil_and_good)_"
        self.assertEqual(
            self.converter.inline(value),
            r"\emph{\hyperref[Protection_from_Evil_and_Good_protection_from_evil_and_good]{Protezione dal bene e dal male}}",
        )

    def test_strong_wrapping_external_link(self) -> None:
        value = "**[D&D](https://www.dndbeyond.com/)**"
        self.assertEqual(
            self.converter.inline(value),
            r"\textbf{\href{https://www.dndbeyond.com/}{D\&D}}",
        )

    def test_duplicate_generated_heading_labels_are_unique(self) -> None:
        first = self.converter.heading(5, "Incantesimi del giuramento")
        second = self.converter.heading(5, "Incantesimi del giuramento")
        self.assertIn(r"\label{incantesimi_del_giuramento}", first)
        self.assertIn(r"\label{incantesimi_del_giuramento_2}", second)


if __name__ == "__main__":
    unittest.main()
