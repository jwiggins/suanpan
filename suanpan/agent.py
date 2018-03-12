from __future__ import absolute_import, print_function, unicode_literals

import argparse

from imessage.api import (
    get_all_recipients, send_message, wait_for_next_message)


def loop(recipients):
    all_recips = get_all_recipients()
    recipients = [r for r in all_recips if r.phone_or_email in recipients]
    row_id = 0

    while True:
        msg, sender, row_id = wait_for_next_message(recipients,
                                                    last_row_id=row_id)
        print('Recieved message:', msg)
        send_message(sender, "Hi there! I'm a bot!")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('recipients', nargs='+', required=True)
    args = ap.parse_args()
    loop(args.recipients)


if __name__ == '__main__':
    main()
