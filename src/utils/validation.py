from utils import get_missing_error_message, get_wrong_type_error_message, get_not_in_range_error_message

def validate_arg_not_none(value, arg_name: str, msg: str=None):
    msg = msg if msg is not None else get_missing_error_message(arg_name)
    if value is None:
        raise ValueError(msg)


def validate_arg_type(value, arg_name: str, expected_type: type, msg: str=None):
    msg = msg if msg is not None else get_wrong_type_error_message(arg_name, type(value), expected_type)
    if value is not None and not isinstance(value, expected_type):
        raise TypeError(msg)


def validate_required_arg_type(value, arg_name: str, expected_type: type):
    validate_arg_not_none(value, arg_name)
    validate_arg_type(value, arg_name, expected_type)


def validate_int_in_range(value: int, int_range: tuple, arg_name: str, msg: str=None):
    msg = msg if msg is not None else get_not_in_range_error_message(arg_name, value, int_range)
    if value < int_range[0] or value > int_range[1]:
        raise ValueError(msg)
