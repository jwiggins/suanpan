from __future__ import absolute_import, print_function, unicode_literals

import argparse

from nahash.api import (
    get_all_recipients, send_message, wait_for_next_message)

from .db import add_transaction
from .parse import extract_monetary_value


def loop(recipients):
    row_id = 0
    while True:
        msg, sender, row_id = wait_for_next_message(recipients,
                                                    last_rowid=row_id)
        print('Recieved message:', msg)
        amount, currency = extract_monetary_value(msg)
        if amount > 0 and len(currency) > 0:
            add_transaction(sender.phone_or_email, amount, currency)
            send_message(sender, "Added {}({})".format(amount, currency))
        else:
            send_message(sender, "Sorry, I didn't understand you")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-s', '--show-recipients', action='store_true')
    ap.add_argument('-r', '--recipients', nargs='+')
    args = ap.parse_args()

    all_recips = get_all_recipients()
    if args.show_recipients:
        for r in all_recips:
            print(r)
    else:
        recipients = [r for r in all_recips
                      if r.phone_or_email in args.recipients]
        loop(recipients)


if __name__ == '__main__':
    main()
