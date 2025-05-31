def get_missing_error_message(arg_name: str):
    return f"Missing required argument: '{arg_name}'"


def get_wrong_type_error_message(arg_name: str, arg_type: type, expected_type: type):
    return f"Wrong type for argument: '{arg_name}' ('{arg_type.__name__}' object) should be '{expected_type.__name__}'"


def get_not_in_range_error_message(arg_name: str, value: int, int_range: tuple):
    return f"'{arg_name}' value ({value}) not in [{int_range[0]}, {int_range[1]}]"

