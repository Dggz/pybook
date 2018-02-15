import fnmatch
import re

type = "(int|char)"
operator = "(\\+|\\-|\\*|\\/|\\^)"
relation = "(\\<|\\<\\=|\\=|\\>\\=|\\>|\\!\\=|\\=\\=)"
identifier = "[a-z|A-Z]{1,8}"
integer = "\\-?[1-9][0-9]*"
character = "'[0-9,a-z,A-z,\\s]'"
string = "\"[0-9,a-z,A-z,\\s]+\""
constant = "(" + integer + ")|(" + character + ")"
funcCallArgs = "(" + "(\\s?(((" + identifier + ")|(" + constant + ")|(" + string + "))" \
               "(\\s?(" + operator + ")\\s?\\(?\\s?((" + identifier + ")|(" + constant + ")" \
               "|(" + string + "))\\s?\\)?\\s?)*))" + "(\\s?(,\\s?" + "(\\s?(((" + identifier + ")" \
               "|(" + constant + ")|(" + string + "))(\\s?(" + operator + ")\\s?\\(?\\s?((" + identifier + ")" \
               "|(" + constant + ")|(" + string + "))\\s?\\)?\\s?)*))" + ")*)" + ")"

funcCall = "\\s?" + identifier + "\\s?\\(\\s?" + funcCallArgs + "\\s?\\)\\s?"
term = "((" + string + ")|(" + identifier + ")|(" + constant + ")|(" + funcCall + "))"
expression = "(\\s?(" + term + "(\\s?(" + operator + ")\\s?\\(?\\s?" + term + "\\s?\\)?\\s?)*))"
condition = expression + "\\s?" + relation + "\\s?" + expression

func = "func\\s(" + type + ")\\s" + identifier + "\\s?\\(((" + type + ")\\s" + identifier + ")" \
       "(\\s?,\\s?(" + type + ")\\s" + identifier + ")*\\)\\s?\\{\\s?$"

funcReturn = "ret\\s" + expression + "\\s?;"
declaration = "(^" + type + ")\\s" + identifier + "\\s?;"
arrayDeclaration = "array\\s(((" + type + ")\\s" + identifier + "\\[[1-9][0-9]*\\])|(char\\s" + identifier + "\\[\\]));"
ifStmt = "if\\s?\\(\\s?" + condition + "\\s?\\)\\s?\\{\\s?$"
elseStmt = "\\s?\\}\\s?else\\s?\\{\\s?$"
whileStmt = "while\\s?\\(\\s?" + condition + "\\s?\\)\\s?\\{\\s?$"
read = "read\\s" + identifier + "\\s?;"
write = "write\\s" + expression
arrayStmt = identifier + "\\s?\\[[0-9]+\\]\\s?=" + expression + ";"
simpleStmt = identifier + "\\s?=" + expression + ";"
whitespace = r'^\s*\n'
block_end = r'\s*}\s*\n'

rules = {
    'type': type, 'operator': operator, 'relation': relation,
    'identifier': identifier, 'integer': integer, 'character': character,
    'string': string, 'constant': constant, 'funcCallArgs': funcCallArgs,
    'funcCall': funcCall, 'term': term, 'expression': expression,
    'condition': condition, 'func': func, 'funcReturn': funcReturn,
    'declaration': declaration, 'arrayDeclaration': arrayDeclaration,
    'ifStmt': ifStmt, 'elseStmt': elseStmt, 'whileStmt': whileStmt,
    'read': read, 'write': write, 'arrayStmt': arrayStmt, 'simpleStmt': simpleStmt,
    'whitespace': whitespace, 'block_end': block_end
    }

reserved = {

}

progs = ['programFunc'] # , 'programIf', 'programSimplu',
         # 'programString', 'programWhile']

# for prog in progs:
with open(progs[0], 'rt') as prog:
    lines = [re.split(r'(;|,|\s+|\(|\))\s*', line) for line in prog.readlines()]

err = False
for line_nr, line in enumerate(lines, 1):
    matched = 0
    if not any(re.match(rules[pattern], ''.join(line)) for pattern in rules):
        print('\nError line {}'.format(line_nr))
        err = True
    if err:
        exit()

