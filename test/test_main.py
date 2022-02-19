# -*- coding: utf-8 -*-
import unittest

from codehighlighter import main


class MainTestCase(unittest.TestCase):
    def test_highlights_inline_code_to_one_line(self):
        self.assertEqual(
            '<code class="highlight"><span class="nb">true</span><span class="w"></span></code>',
            main.highlight('true', language='c++', inline=True))

