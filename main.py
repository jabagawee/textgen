#! /usr/bin/env python3

import random
import re
import sys

def parse_rule(rule, mappings_dict):
    parsed_rule = []
    for choice in rule:
        subgrammar = []
        for part in re.findall(r'\b\w+\b|".*"', choice):
            if part.startswith('"') and part.endswith('"'):
                subgrammar.append(part)
            else:
                subgrammar.append(parse_rule(mappings_dict[part], mappings_dict))
        parsed_rule.append(subgrammar)
    return parsed_rule

def parse_grammar_file(grammar_file):
    mappings = {}
    with open(grammar_file) as f:
        for line in f:
            token, definition = line.rstrip().split(': ')
            mappings[token] = definition.split(' | ')
    grammar = parse_rule(mappings['main'], mappings)
    return grammar[0]

def eval_token(token):
    if isinstance(token, str):
        return token
    return random.choice(token)

def generate_from_grammar(grammar):
    line = grammar
    while not all(isinstance(token, str) for token in line):
        print(line)
        line = [eval_token(token) for token in line]
    return ''.join(eval(safe_token) for safe_token in line)

if __name__ == '__main__':
    grammar = parse_grammar_file(sys.argv[1])
    import pprint
    pprint.pprint(grammar)
    print(generate_from_grammar(grammar))
