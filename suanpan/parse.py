# -*- coding: utf8 -*-

from __future__ import unicode_literals

import re

MONETARY_AMOUNT = re.compile(r'([$£€¥]?(?:CHF)?)(\d+\.*\d*)([$£€¥]?(?:CHF)?)')


def extract_monetary_value(text):
    """ Given an input string, find the monetary value within.
    """
    matches = MONETARY_AMOUNT.findall(text)
    if matches:
        currency_pre, amount, currency_post = matches[0]
        currency = currency_pre or currency_post
        return float(amount), currency

    return 0.0, ''
