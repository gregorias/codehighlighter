# -*- coding: utf-8 -*-
from os import path
import pathlib
import unittest

from codehighlighter import main

def get_testdata_dir() -> pathlib.Path:
    test_dir = pathlib.Path(path.dirname(path.realpath(__file__)))
    return test_dir / 'testdata'

def read_file(p: pathlib.Path) -> str:
    with open(p, 'r') as f:
        return f.read()

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.testdata_dir = get_testdata_dir()

    def test_highlights_inline_code_to_one_line(self):
        self.assertEqual(
            '<code class="highlight"><span class="nb">true</span><span class="w"></span></code>',
            main.highlight('true', language='c++', inline=True))

    def test_highlights_block_python_code(self):
        input = read_file(self.testdata_dir / "in0.py")
        expected = read_file(self.testdata_dir / "out0.html")
        self.assertEqual(
            expected,
            main.highlight(input, language='python', inline=False))

