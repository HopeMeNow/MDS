def exception_logger(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ArithmeticError, AssertionError, ZeroDivisionError) as e:
            if isinstance(e, AssertionError):
                print('AssertionError')
            elif isinstance(e, ArithmeticError):
                if isinstance(e, ZeroDivisionError):
                    print('ZeroDivisionError')
                else:
                    print('ArithmeticError')
    return inner
