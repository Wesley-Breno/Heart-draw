from time import sleep

print('\033[1;31m')


def heart():
    print()
    print()
    print()

    # primeira linha
    for c in range(0, 25):
        print(" ", end='')
    for c in range(0, 3):
        print("--", end='')
        sleep(0.5)
    for c in range(0, 5):
        print(' ', end='')
    for c in range(0, 3):
        print("--", end='')
        sleep(0.5)
    print()

    # segunda linha
    for c in range(0, 24):
        print(' ', end='')
    print('/', end='')
    sleep(0.5)
    for c in range(0, 7):
        print(' ', end='')
    print('|', end='')
    sleep(0.5)
    for c in range(0, 2):
        print(' ', end='')
    print('|', end='')
    sleep(0.5)
    for c in range(0, 6):
        print(' ', end='')
    print('\\', end='')
    sleep(0.5)
    print()

    # terceira linha
    for c in range(0, 23):
        print(' ', end='')
    print('/', end='')
    sleep(0.5)
    for c in range(0, 9):
        print(' ', end='')
    print('||', end='')
    sleep(0.5)
    for c in range(0, 8):
        print(' ', end='')
    print('\\', end='')
    sleep(0.5)
    print()

    # quarta linha
    for c in range(0, 22):
        print(' ', end='')
    print('|', end='')
    sleep(0.5)
    for c in range(0, 21):
        print(' ', end='')
    print("|", end='')
    sleep(0.5)
    print()

    # quinta linha
    for c in range(0, 22):
        print(' ', end='')
    print('|', end='')
    sleep(0.5)
    for c in range(0, 21):
        print(' ', end='')
    print("|", end='')
    sleep(0.5)
    print()

    # sexta linha
    for c in range(0, 22):
        print(' ', end='')
    print('|', end='')
    sleep(0.5)
    for c in range(0, 21):
        print(' ', end='')
    print("|", end='')
    sleep(0.5)
    print()

    # setima linha
    for c in range(0, 23):
        print(' ', end='')
    print('\\', end='')
    sleep(0.5)
    for c in range(0, 19):
        print(' ', end='')
    print('/')
    sleep(0.5)

    # oitava linha
    for c in range(0, 24):
        print(' ', end='')
    print('\\', end='')
    sleep(0.5)
    for c in range(0, 17):
        print(' ', end='')
    print('/')
    sleep(0.5)

    # nona linha
    for c in range(0, 25):
        print(' ', end='')
    print('\\', end='')
    sleep(0.5)
    for c in range(0, 15):
        print(' ', end='')
    print('/')
    sleep(0.5)

    # decima linha
    for c in range(0, 26):
        print(' ', end='')
    print('\\', end='')
    sleep(0.5)
    for c in range(0, 13):
        print(' ', end='')
    print('/')
    sleep(0.5)

    # decima primeira linha
    for c in range(0, 27):
        print(' ', end='')
    print('\\', end='')
    sleep(0.5)
    for c in range(0, 11):
        print(' ', end='')
    print('/')
    sleep(0.5)

    # decima segunda linha
    for c in range(0, 29):
        print(' ', end='')
    print('\\', end='')
    sleep(0.5)
    for c in range(0, 7):
        print(' ', end='')
    print('/')
    sleep(0.5)

    # decima terceira linha
    for c in range(0, 31):
        print(' ', end='')
    print('\\', end='')
    sleep(0.5)
    for c in range(0, 3):
        print(' ', end='')
    print('/')
    sleep(0.5)

    # ultima linha
    for c in range(0, 32):
        print(' ', end='')
    print('\\', end='')
    sleep(0.5)
    for c in range(0, 1):
        print(' ', end='')
    print('/')
    sleep(0.5)


heart()
print('\033[m')
