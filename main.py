import sys
import re
from functools import reduce
import operator

class Arg:
	def __init__(self, name, value=None):
		self.name = name
		self.value = value


def parse_file(arg):
	try:
		return [el for el in open(arg)]
	except NameError:
		print('Wrong file %s!' % arg, file=sys.stderr)
		return False
	except PermissionError:
		return False
	except FileNotFoundError:
		return False


def remove_empty_elements(data):
	return [el for el in data if el]


def remove_comments(data):
	for i in range(len(data)):
		if '#' in data[i]:
			data[i] = data[i][:data[i].index('#')]
	return data

def parse_file_data(filename):
	data = [line for line in open(filename)]
	without_comments_data = remove_comments(data)
	rstripped_data = [el.rstrip() for el in without_comments_data]
	clear_data = remove_empty_elements(rstripped_data)
	return clear_data
	print(clear_data)



def parse_and_validate(filename):
	data = parse_file_data(filename)
	true_data = {el: True for el in list(data[-2][1:])}
	unknown_data = {el: None for el in list(data[-1][1:])}
	all_variables = [] # can be set?!

	for el in data:
		if el[0] not in '=?':
			all_variables += re.findall('\w', el[:el.index('=>')])
		else:
			all_variables += list(el[1:])
	false_data = {el : False for el in list(set(all_variables) - set(true_data.keys()) - set(unknown_data.keys()))}

	parsed_args = set(reduce(operator.add, [list(el.keys()) for el in [true_data, false_data, unknown_data]]))
	if parsed_args != set(all_variables):
		# print(parsed_args)
		# print(set(all_variables))
		# print(parsed_args - set(all_variables))
		print('Parse error. Arguments error')

	args = dict(reduce(operator.add, [list(arg.items()) for arg in [true_data, false_data, unknown_data]]))
	return data, args


def perform_an_operation(operation, args_tfu):
	...


def perform_operations(operations, args_tfu):
	for operation in operations:
		perform_an_operation(operation, args_tfu)



if __name__ == '__main__':
	if sys.argv[1]:
		data, args = parse_and_validate(sys.argv[1])
		perform_operations(data[:-2], args)