# coding: utf-8

import misaka

def md(text):
    return misaka.html(text, extensions=misaka.EXT_FENCED_CODE |
            misaka.EXT_AUTOLINK, render_flags=misaka.HTML_SKIP_HTML)
