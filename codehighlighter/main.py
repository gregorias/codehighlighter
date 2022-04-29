# -*- coding: utf-8 -*-
"""A code highlighter

Usage:
    ./run haskell
"""
import getopt
import pygments # type: ignore
import pygments.formatters # type: ignore
import pygments.lexers # type: ignore
import re
import sys

def apply_eye_candy(content: str, language):
    content = re.sub('&lt;-', '←', content)
    content = re.sub('&gt;=', '≥', content)
    content = re.sub('!=', '≠', content)
    content = re.sub('/=', '≠', content)
    content = re.sub(' &gt;&gt; ', ' » ', content)
    content = re.sub('&lt;&lt;', '«', content)
    if language == 'haskell':
        content = re.sub('Bool', '𝔹', content)
        content = re.sub('Integer', 'ℤ', content)
        content = re.sub('Rational', 'ℚ', content)
    return content

def remove_spurious_inline_newline(html: str) -> str:
    return re.sub('</span>\n</code>$', '</span></code>', html)


def highlight(content: str, language='haskell', inline=False):
    lexer = pygments.lexers.get_lexer_by_name(language)

    if inline:
        htmlf = pygments.formatters.get_formatter_by_name('html',
                                                          nowrap=True)
        highlighted = pygments.highlight(content, lexer, htmlf)
        highlighted = '<code class="highlight">' + highlighted + '</code>'
    else:
        htmlf = pygments.formatters.get_formatter_by_name('html')
        highlighted = pygments.highlight(content, lexer, htmlf)
        highlighted = highlighted.strip()
        highlighted = highlighted.removeprefix('<div class="highlight">')
        highlighted = highlighted.removesuffix('</div>')
        highlighted = highlighted.removeprefix('<pre>')
        highlighted = highlighted.removesuffix('</pre>')
        highlighted = highlighted.removeprefix('<span></span>')
        highlighted = (
            f'<div class="pygments pygments-block">\n  <pre><code>{highlighted}'
            + '</code></pre>\n</div>\n'
        )
    highlighted = apply_eye_candy(highlighted, language=language)
    if inline:
        highlighted = remove_spurious_inline_newline(highlighted)
    return highlighted

if __name__ == '__main__':
    options, args = getopt.getopt(sys.argv[1:],
                                  shortopts="",
                                  longopts=["inline"])
    optionsDict = dict(options)
    input = sys.stdin.read()
    print(highlight(input, args[0], inline="--inline" in optionsDict))
