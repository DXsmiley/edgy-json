"""edgy-json

Verifies json data by comparing it against a schema.

This is not an implementation of json-schema, rather
an alternative for people who move fast and break things.

"""

import json
import itertools
import re
import warnings


DEV = False


def _merge_dicts(a, b):
    r = a.copy()
    r.update(b)
    return r


def _param_deprecation_warning(schema, deprecated, context):
    """Raises warning about using the 'old' names for some parameters.

    The new naming scheme just has two underscores on each end of the word for consistency
    """
    for i in deprecated:
        if i in schema:
                warnings.warn('When matching {}, parameter {} is deprecated, use __{}__ instead', Warning)


def _check(schema, data, named_schemas={}, trace=None):
    if trace:
        print('    ' * trace, schema)
        print('    ' * trace, data)
        print('    ' * trace, named_schemas)
        print()
        trace += 1

    if isinstance(schema, bool):
        return schema is data

    elif isinstance(schema, str):
        if schema == 'none':
            return data is None
        elif schema == 'anything':
            return True
        elif schema == 'nothing':
            return False
        elif schema == 'string':
            return isinstance(data, str)
        elif schema == 'float':
            return isinstance(data, float)
        elif schema == 'int':
            return isinstance(data, int)
        elif schema == 'bool':
            return isinstance(data, bool)
        elif schema[0] == '@':
            name = schema[1:]
            if name not in named_schemas:
                raise ValueError('Unknown named schema: ' + name)
            return _check(named_schemas[name], data, named_schemas, trace)
        else:
            raise ValueError('Invalid string schema: ' + schema)

    elif isinstance(schema, list):
        for i in schema:
            if _check(i, data, named_schemas, trace):
                return True
        return False

    elif isinstance(schema, dict):
        if '__named__' in schema:
            named_schemas = _merge_dicts(named_schemas, schema['__named__'])
        if '__this__' in schema:
            return _check(schema['__this__'], data, named_schemas, trace)
        dtype = schema.get('__type__', 'object')
        if dtype == 'object':
            if not isinstance(data, dict):
                return False
            key_set = set()
            for k, s in schema.items():
                if k.startswith('~'):
                    key_set.add(k[1:])
                    if not _check(s, data.get(k[1:]), named_schemas, trace):
                        return False
                elif not k.startswith('__'):
                    key_set.add(k)
                    if not _check(s, data.get(k), named_schemas, trace):
                        return False
            extra = schema.get('__extra__', 'nothing')
            for k, v in data.items():
                if k not in key_set:
                    return _check(extra, v, named_schemas, trace)
            return True
        elif dtype == 'list':
            if not isinstance(data, list):
                return False
            for i in data:
                if not _check(schema['__item__'], i, named_schemas, trace):
                    return False
            return True
        elif dtype == 'int':
            if not isinstance(data, int):
                return False
            _param_deprecation_warning(schema, ['minimum', 'maximum', 'equals'], 'int')
            minimum = schema.get('minimum') or schema.get('__minimum__')
            if minimum and data < minimum:
                return False
            maximum = schema.get('maximum') or schema.get('__maximum__')
            if maximum and data > maximum:
                return False
            equals = schema.get('equals') or schema.get('__equals__')
            if equals and data != equals:
                return False
            return True
        elif dtype == 'string':
            if not isinstance(data, str):
                return False
            _param_deprecation_warning(schema, ['equals', 'matches'], 'string')
            equals = schema.get('equals') or schema.get('__equals__')
            if equals and data != equals:
                return False
            matches = schema.get('matches') or schema.get('__matches__')
            if matches:
                if re.fullmatch(matches, data) == None:
                    return False
            return True
        else:
            raise ValueError('Unknown values for __type__: ' + str(dtype))

    raise TypeError('Unknown schema type: ' + str(type(schema)))


def check(schema, data, trace=False):
    """Verify some json.

    Args:
        schema - the description of a general-case 'valid' json object.
        data - the json data to verify.

    Returns:
        bool: True if data matches the schema, False otherwise.

    Raises:
        TypeError:
            If the schema is of an unknown data type.
        ValueError:
            If the schema contains a string with an invalid value.
            If the schema attempts to reference a non-existent named schema.

    """
    if trace == True:
        trace = 1
    else:
        trace = None
    return _check(schema, data, trace=trace)
