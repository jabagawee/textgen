#! /usr/bin/env python3

import sys

def parse_grammar_file(f):
    raise NotImplementedError

def generate_from_grammar(grammar):
    raise NotImplementedError

grammar = parse_grammar_file(sys.argv[1])

if __name__ == "__main__":
    print(generate_from_grammar(grammar))
