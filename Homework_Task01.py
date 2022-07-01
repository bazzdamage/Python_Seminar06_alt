import re
# import operator
#
# ops = {
#     '+': operator.add,
#     '-': operator.sub,
#     '*': operator.mul,
#     '/': operator.truediv
# }
#
#
# def eval_expression(op1, oper, op2):
#     op1, op2 = int(op1), int(op2)
#     return ops[oper](op1, op2)
#
#
# print(eval_binary_expr(*("5 + 3".split())))
# print(eval_binary_expr(*("5 * 3".split())))
# print(eval_binary_expr(*("5 % 3".split())))
# print(eval_binary_expr(*("5 ^ 3".split())))


def exp_eval(expression: str):

    operators = {
        "^": lambda x, y: str(float(x) ** float(y)),
        "*": lambda x, y: str(float(x) * float(y)),
        "/": lambda x, y: str(float(x) / float(y)),
        "+": lambda x, y: str(float(x) + float(y)),
        "-": lambda x, y: str(float(x) - float(y))
    }

    # search exp in parentheses
    parenthetical_exp = r"\((.+?)\)"
    # r'\d+(\.\d*)?' - integer or decimal number
    # \s = whitespaces, * - any repetitions
    simple_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"

    # operator := for return and assignment in one str
    # re.search = search in whole str
    # re.match = search in begin of str
    # match(0) = entire match
    # match(1) = first parenthesized subgroup

    while match := re.search(parenthetical_exp, expression):
        expression: str = expression.replace(match.group(0), exp_eval(match.group(1)))

    for symbol, operator in operators.items():
        while match := re.search(simple_exp.format(symbol), expression):
            expression: str = expression.replace(match.group(0), operator(*match.groups()))

    return expression


exp = "(1 + 4) * (5 * (10 - 2)) / 5"
print(exp_eval(exp), eval(exp))
