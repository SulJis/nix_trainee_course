def error_catcher(func):
    """
    Catches an error and prints it
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(e)

    return wrapper


@error_catcher
def divider(a, b):
    return a / b


a = divider(2, 0)
