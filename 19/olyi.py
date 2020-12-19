import regex as re

intl = lambda x: [int(i) if i.isdigit() else i for i in x.split()]


def parse(line):
    name, rule = line.strip().split(": ")
    ors = [intl(x) for x in rule.split(" | ")]
    return int(name), ors


with open("input.txt") as f:
    rules, queries = f.read().split("\n\n")
    rules = [parse(x) for x in rules.splitlines()]
    rules = {k: v for k, v in rules}
    queries = queries.splitlines()


def build(idx):
    def indiv(x):
        if x == idx: return f"(?&G{idx})"
        elif isinstance(x, int): return build(x)
        else: return x.replace('"', "")

    ors = [[indiv(x) for x in case] for case in rules[idx]]
    return f"(?P<G{idx}>" + "|".join("".join(x) for x in ors) + ")"
reg = build(0)
print(reg)
total = sum(1 for x in queries if re.fullmatch(reg, x))

print(total)

