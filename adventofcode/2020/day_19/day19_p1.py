import sys
import re
from functools import reduce


def remove_char(string, char):
    return string.replace(char, '')


def full_match(match_obj, string):
    if match_obj:
        start, stop = match_obj.span()
        return stop - start == len(string)

    return False


def generate_words(rules, tokens):
    if '"' in tokens:
        return remove_char(tokens, '"')
    elif "|" in tokens:
        left, right = tokens.split("|")
        return f'"({generate_words(rules, left.strip())}|{generate_words(rules, right.strip())})"'
    else:
        return reduce(lambda x,y: x+generate_words(rules, rules[y]), tokens.split(), "")


def main():
    rules = {}
    counter = 0

    for line in sys.stdin:
        line = line.rstrip()

        if ":" in line:
            k, v = line.split(":")
            rules[k] = v.strip()
        elif len(line) == 0:
            pattern = re.compile(remove_char(generate_words(rules, rules["0"]), '"'))
        elif full_match(pattern.match(line), line):
            counter += 1

    print(counter)


if __name__ == "__main__":
    main()
