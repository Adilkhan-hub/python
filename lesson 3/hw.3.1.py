def div(x, y):
    try:
         res = x / y
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Нельзя делить на ноль!"

    return res

print(div(6, 0))
