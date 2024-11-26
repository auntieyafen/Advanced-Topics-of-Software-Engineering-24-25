import math


class Calculator:
    def __init__(self):
        self.memory = 0
        self.stack = []

    # Basic Operations
    def add(self, a, b):
        result = a + b
        self._push_stack(result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._push_stack(result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._push_stack(result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self._push_stack(result)
        return result

    # Advanced Operations
    def power(self, a, b):
        result = a ** b
        self._push_stack(result)
        return result

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number.")
        result = math.sqrt(a)
        self._push_stack(result)
        return result

    def factorial(self, a):
        if not isinstance(a, int) or a < 0:
            raise ValueError("Factorial is only for non-negative integers.")
        result = math.factorial(a)
        self._push_stack(result)
        return result

    # Memory Functions
    def memory_store(self, value):
        self.memory = value

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0

    # Stack Functions
    def _push_stack(self, value):
        """Pushes a result onto the stack."""
        self.stack.append(value)

    def get_last_result(self):
        """Retrieves the last result from the stack."""
        if not self.stack:
            return None
        return self.stack[-1]

    def get_stack(self):
        """Returns the entire stack."""
        return self.stack.copy()

    def clear_stack(self):
        """Clears the result stack."""
        self.stack.clear()
