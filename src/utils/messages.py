def get_missing_error_message(arg_name: str):
    return f"Missing required argument: '{arg_name}'"


def get_wrong_type_error_message(arg_name: str, arg_type: type, expected_type: type):
    return f"Wrong type for argument: '{arg_name}' ('{arg_type.__name__}' object) should be '{expected_type.__name__}'"
