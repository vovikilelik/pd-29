def has_allow(response, *fields):
    for field in fields:
        if field not in response:
            return False

    return True


def omit(obj, *fields):
    return {key: value for key, value in obj.items() if key not in fields}