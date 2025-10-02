class Foobar:
    def __init__(self) -> None:
        self.foo: int = 0

class Bar(Foobar):
    def __init__(self) -> None:
        super().__init__()
        self.qux: float = 2