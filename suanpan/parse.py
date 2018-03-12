import re

MONETARY_AMOUNT = re.compile(r'''(?:.*)\
(?P<currency_pre>[$£€¥]?(?:CHF)?)\
(?P<amount>\d+\.?\d*)\
(?P<currency_post>[$£€¥]?(?:CHF)?)\
(?:.*)''')


def extract_monetary_value(text):
    """ Given an input string, find the monetary value within.
    """
    match = MONETARY_AMOUNT.match(text)
    if match is not None:
        parts = match.groupdict()
        currency = parts['currency_pre'] or parts['currency_post']
        return float(parts['amount']), currency

    return 0.0, ''
