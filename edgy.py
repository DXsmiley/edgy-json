import json
import itertools

def merge_dicts(a, b):
	r = a.copy()
	r.update(b)
	return r

def check(schema, data, named_schemas = {}, trace = False):

	if trace is True:
		trace = 0
	if type(trace) is int:
		print('    ' * trace, schema)
		print('    ' * trace, data)
		print('    ' * trace, named_schemas)
		print()
		trace += 1

	if type(schema) is bool:
		return schema is data

	if type(schema) is str:
		if schema == 'none':
			return data is None
		elif schema == 'string':
			return type(data) is str
		elif schema == 'float':
			return type(data) is float
		elif schema == 'int':
			return type(data) is int
		elif schema == 'bool':
			return type(data) is bool
		elif schema[0] == '@':
			name = schema[1:]
			if name not in named_schemas:
				raise Exception('Unknown named schema: ' + name)
			return check(named_schemas[name], data, named_schemas, trace)
		else:
			raise Exception('Invalid string schema: ' + schema)
	
	if type(schema) is list:
		for i in schema:
			if check(i, data, named_schemas, trace):
				return True
		return False

	if type(schema) is dict:
		if '__named__' in schema:
			named_schemas = merge_dicts(named_schemas, schema['__named__'])
		if '__this__' in schema:
			return check(schema['__this__'], data, named_schemas, trace)
		dtype = schema.get('__type__', 'object')
		if dtype == 'object':
			if type(data) is not dict:
				return False
			for k, s in schema.items():
				if not k.startswith('__'):
					if not check(s, data.get(k), named_schemas, trace):
						return False
			for k, v in data.items():
				if k not in schema:
					return False
			return True
		elif dtype == 'list':
			if type(data) is not list:
				return False
			for i in data:
				if not check(schema['__item__'], i, named_schemas, trace):
					return False
			return True
		elif dtype == 'int':
			if type(data) is not int:
				return False
			if 'minimum' in schema and data < schema['minimum']:
				return False
			if 'maximum' in schema and data > schema['maximum']:
				return False
			return True

	raise TypeError('Unknown schema type: ' + str(type(schema)))