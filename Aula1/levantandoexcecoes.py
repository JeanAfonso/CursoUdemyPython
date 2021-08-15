# https://docs.python.org/3/library/exceptions.html

# def divide(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:
#         print(f'Log: {error}')
#         raise
#
# try:
#     print(divide(2, 0))
# except ZeroDivisionError as error:
#     print(error)

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 don't be 0.")
    return n1 / n2

try:
    print(divide(n1=2, n2=0))
except ValueError as error:
    print("You're trying to divide by 0.")
    print(f'Log:, {error}')