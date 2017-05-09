#!/usr/bin/env python
import argparse

from torment import api


def main():
    parser = argparse.ArgumentParser(description='Make people happy.')
    parser.add_argument('method', choices=list(api.METHODS.keys()))
    parser.add_argument('person')
    parser.add_argument('args', metavar='N', nargs='*')
    args = parser.parse_args()

    method, num_args = api.METHODS[args.method]

    if num_args != len(args.args):
        raise Exception("%s takes %i arguments." % (args.method, num_args))

    try:
        number = api.get_phone_number(args.person)
    except KeyError:
        raise Exception("I don't know who %s is." % args.person)

    method(number, *args.args)

if __name__ == '__main__':
    main()
