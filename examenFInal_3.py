import time


def mesureTime(function):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = function(*args, **kwargs)

        total = time.time() - start
        print("La demora de ejecución fue de: {}".format(total))

        return result

    return wrapper


@mesureTime
def division(a, b):
    time.sleep(1)  # Pausa la ejeción del código por 1 segundo
    s = a / b
    return s


print(division(100, 5))
