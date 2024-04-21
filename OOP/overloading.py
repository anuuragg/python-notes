class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()

print(calc.add(1, 2))
print(calc.add(1, 2, 3, 4))
print(calc.add())
