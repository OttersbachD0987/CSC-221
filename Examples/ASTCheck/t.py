def foobar(foo: int) -> None:
    print(foo)

bar: int = 3

foobar(2)
foobar(foo=2)
foobar(bar)
foobar(foo=bar)