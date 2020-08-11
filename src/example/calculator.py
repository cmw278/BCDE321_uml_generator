class Calculator:
    # An example module to demonstrate python packaging concepts.
    @staticmethod
    def add(*args):
        # Adds any number of numeric arguments together
        sum = 0
        for i in args:
            sum = sum + i
        return sum
