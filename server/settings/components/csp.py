"""
This file contains a definition for Content-Security-Policy headers.

Read more about it:
https://developer.mozilla.org/ru/docs/Web/HTTP/Headers/Content-Security-Policy

We are using `django-csp` to provide these headers.
Docs: https://github.com/mozilla/django-csp
# """

CSP_SCRIPT_SRC = ("'none'",)
CSP_IMG_SRC = ("'none'",)
CSP_FONT_SRC = ("'none'",)
CSP_STYLE_SRC = ("'none'",)
CSP_DEFAULT_SRC = ("'none'",)
