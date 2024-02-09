from modules_example.math_operations.helpers import sign_mapper


def execute_expression(exp):
    num1_text, sign, num2_text = exp.split()
    num1 = float(num1_text)
    num2 = float(num2_text)

    return sign_mapper[sign](num1, num2)