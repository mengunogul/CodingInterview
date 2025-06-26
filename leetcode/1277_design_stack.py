class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack: list[int] = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        return -1 if not self.stack else self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val
