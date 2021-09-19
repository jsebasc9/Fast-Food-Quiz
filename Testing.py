def inputInt(prompt):
    while True:
        value = input(prompt)
        try:
            numResponse = int(value)
        except ValueError:
            print('Invalid input - Try again.')
            continue
        return numResponse

inputInt(1)