def reverse_notation(s):
    stack = []
    for i in range(len(s)):
        if not s[i] in ['+', '-', '*', '/']:
            # add operand to stack
            stack.append(s[i])
        else:
            # to execute operation get operands from the stack
            # be careful with operands order during execution
            second_operand = stack.pop()
            first_operand = stack.pop()
            res = eval(str(first_operand) + s[i] + str(second_operand))
            stack.append(res)

    return stack[0]


print(reverse_notation([4, 3, "-", 2, "*"]))
