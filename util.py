"""
Utils
"""
import os
import re
import numpy as np
import pandas as pd
import threading
from openpyxl import load_workbook
import logging
logging.basicConfig(level=logging.NOTSET, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def remove_repeat_item_from_list(lis):
    """
    remove the same items from a list
    :param lis: list
    :return: list has removed same items
    """
    n_lis = []
    for _ in lis:
        if _ not in n_lis:
            n_lis.append(_)
    return n_lis


# Overwrite thead.
# In order to get results
class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def strtok(ss, delimiter='\s+'):
    """
    Imitate the function from language C++ or matlab
    :param ss: Input string
    :param delimiter: Delimiter symbol
    :return: A list
    """
    logging.INFO('*****  strrok  *****')
    first_str = re.split(delimiter, ss)[0]
    other_str = re.findall(first_str + delimiter + '(.*)', ss)[0]
    return first_str, other_str


def specified_start_end(file_content, start_symbol, end_symbol):
    """
    Get the content in the middle of the specified start content.
    :param file_content: File content
    :param start_symbol: The line in file start with this as a start symbol
    :param end_symbol: The line in file start with this as a end symbol
    :return: A list had been splited by start and end symbol
    """
    logging.INFO('*****  start: %s, end: %s  *****' % (start_symbol, end_symbol))
    start_line = list(filter(lambda x: re.match(start_symbol, file_content[x], re.I), range(len(file_content))))
    end_line = list(filter(lambda x: re.match(end_symbol, file_content[x], re.I), range(len(file_content))))
    final_data = []
    for i in start_line:
        for j in end_line:
            if i < j:
                match_start = re.findall(start_symbol + '(.*)\s*', file_content[i], re.I)[0]
                match_end = re.findall(end_symbol + '(.*)\s*', file_content[j], re.I)[0]
                if re.search(match_start.strip(), match_end.strip(), re.I):
                    final_data.append(file_content[i: j + 1])
                    break
    return final_data


def _excelAddSheet(dataframe, filename, sheet_name):
    """
    Add the specifical data(DataFrame of pandas) to excel's sheet rather than cover
    :param dataframe: DateFrame from pandas
    :param filename: filepath
    :param sheet_name: sheetname in excel
    """
    logging.INFO('*****  Write: sheet:%s -> excel:%s  *****' % (sheet_name, filename))
    excelWriter = pd.ExcelWriter(filename, engine='openpyxl')
    try:
        book = load_workbook(excelWriter.path)
        excelWriter.book = book
    except:
        pd.DataFrame().to_excel(excelWriter.path, index=False)
    dataframe.to_excel(excel_writer=excelWriter, sheet_name=sheet_name)
    excelWriter.close()


def create_path(goal_path):
    """
    Create path if it doesn't exist.
    :param goal_path: param goal_path: The path you want to check.
    """
    logging.INFO('*****  Create_path: %s  *****' % goal_path)
    goal_path = goal_path.strip()
    # remove the '\' at location of tail
    goal_path = goal_path.rstrip("\\")
    if not os.path.exists(goal_path):
        os.makedirs(goal_path)


def convert_point_to_d(strnum, replace_to):
    """
    Convert the symbol '.' to 'd' or 'p' that you designate
    :param strnum: a number with type string
    :param replace_to: the symbol you want to translate
    :return: the number had handled
    """
    logging.INFO('*****  Convert point to %s  *****' % replace_to)
    if re.match('0.', strnum):
        return strnum.replace('0.', replace_to)
    if re.search('.0$', strnum):
        return strnum[0:-2]
    if '.' in strnum:
        return strnum.replace('.', replace_to)


def is_path(file_path):
    """
    Check the path you choose whether exist
    :param file_path: the file path need to check
    :return: True or False
    """
    logging.INFO('*****  Adjust path: %s  *****' % file_path)
    return True if os.path.exists(file_path) else False


def cal_arr(arr):
    """
    # Remove the bad point from an array, rule: median +/- 3*sigma
    :param arr: input array
    :return: array removed the bad points,
    """
    logging.INFO('Remove the bad point from an array')
    bad_point_num = 0
    cur_median = np.nanmedian(arr)
    cur_std = np.nanstd(arr)
    upper = cur_median + 3 * cur_std
    lower = cur_median - 3 * cur_std
    for j in range(arr.shape[0]):
        if arr[j] < lower or arr[j] > upper:
            arr[j] = np.nan
            bad_point_num += 1
    if bad_point_num > 0:
        return cal_arr(arr)
    else:
        return arr, cur_median, cur_std


def add_a_deep_dict(ori_dict, goal_key):
    """
    Add a key for dictionary, type: dict
    :param ori_dict: origin dictionary
    :param goal_key: if the key is in the dictionary, do nothing,else add the key
    :return:
    """
    logging.INFO('Add a key: %s to dictionary' % goal_key)
    if len(ori_dict.keys()) == 0 or goal_key not in ori_dict.keys():
        ori_dict[goal_key] = {}


def isfloat(num):
    """
    Judge a num is or not a number
    :param num: input string
    :return: True or False
    """
    try:
        float(num)
        return True
    except ValueError:
        return False


def postfix_convert(exp):
    """
    Input a formula,it will convert to another formula to calculate
    Example: 1+1 will convert to 11+,to suit the stack in computer
    :param exp: formula you will convert
    :return:
    """
    logging.INFO('Convert expression to postfix: %s' % exp)
    operator_precedence = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}  # priority

    stack = []  # stack of operators
    postfix = []  # stack of postfix expression

    exp = re.sub('\+', ' + ', exp)
    exp = re.sub('-', ' - ', exp)
    exp = re.sub('E\s+-\s+', 'E-', exp)
    exp = re.sub('e\s+-\s+', 'e-', exp)
    exp = re.sub('\*', ' * ', exp)
    exp = re.sub('/', ' / ', exp)
    exp = re.sub('\(', ' ( ', exp)
    exp = re.sub('\)', ' ) ', exp)

    exp = re.split('\s+', exp)
    for char in exp:
        # print char, stack, postfix
        if char not in operator_precedence:  # not the symbol，go into stack directly
            postfix.append(char)
        else:
            if len(stack) == 0:  # if stack of operators is empty, put it into directly
                stack.append(char)
            else:
                if char == "(":
                    stack.append(char)
                elif char == ")":  # meet the right parenthesis(右括号)，运算符出栈到postfix中，并且将左括号出栈
                    while stack[-1] != "(":
                        postfix.append(stack.pop())
                    stack.pop()

                elif operator_precedence[char] > operator_precedence[stack[-1]]:
                    # priority of number is bigger, contibute to add
                    stack.append(char)
                else:
                    while len(stack) != 0:
                        if stack[-1] == "(":  # 运算符栈一直出栈，直到遇到了左括号或者长度为0
                            break
                        postfix.append(stack.pop())  # 将运算符栈的运算符，依次出栈放到表达式栈里面
                    stack.append(char)  # 并且将当前符号追放到符号栈里面

    while len(stack) != 0:  # 如果符号站里面还有元素，就直接将其出栈到表达式栈里面
        postfix.append(stack.pop())
    return postfix


def calculate(num1, op, num2):
    """
    op:operation, just support '+-*/'
    :param num1: number one
    :param op: operation
    :param num2: number two
    :return:
    """
    num1, num2 = float(num1), float(num2)
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return 0
        else:
            return num1 / num2
    else:
        raise Exception("Operator Exception")


def convert_formula(exp):
    """
    Calculate the formula had conveted
    Example: input string -> must be a formula, support brackets
    :param exp: expression
    :return:
    """
    exp = exp.replace('\'', '')
    if isfloat(exp):
        return float(exp)
    postfix = postfix_convert(exp)
    if '' in postfix:
        postfix.remove('')
    stack = []
    for char in postfix:
        stack.append(char)
        if char in "+-*/":
            op = stack.pop()
            num2 = stack.pop()
            if len(stack) == 0:
                num1 = 0
            else:
                num1 = stack.pop()
            value = calculate(num1, op, num2)
            value = str(value)
            stack.append(value)
    return float(stack[0])


def split_file(file_content, split_symbol, remain_first=False):
    """
    Split file by param: split_symbol, the line should start with it.
    Otherwise, you can give a regular expression if you understand, this function support it.
    :param file_content: One file txt content, an array
    :param split_symbol: Spilt symbol
    :param remain_first: Whether to keep the first part
    :return:
    """
    logging.INFO('*****  Split file by: %s  *****' % split_symbol)
    file_content = list(map(lambda y: y.strip(), file_content))
    split_line = list(filter(lambda x: re.match(split_symbol, file_content[x].strip(), re.I),
                             range(len(file_content))))
    if len(split_line) == 0:
        return file_content
    all_groups = []
    if remain_first:
        all_groups.append(file_content[:split_line[0]])
    except_first = list(map(lambda x: file_content[split_line[x]:split_line[x + 1]], range(len(split_line) - 1)))
    if len(file_content[split_line[-1]:]) == 1 and file_content[split_line[-1]:][0].strip() == '':
        pass
    else:
        except_first.append(file_content[split_line[-1]:])
    all_groups.extend(except_first)
    return all_groups
