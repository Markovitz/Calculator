from calculator import Calculator

def main():
    x = 10
    y = 20
    calculator = Calculator(x,y)
    print(f'Calculate:')
    print(f'{x} + {y} = {calculator.sum()}')
    print(f'{x} - {y} = {calculator.subtract()}')
    print(f'{x} * {y} = {calculator.multiply()}')
    print(f'{x} / {y} = {calculator.divide()}')


if __name__ == '__main__':
    main()
