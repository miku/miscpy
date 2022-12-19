import typing

class Bucket:  # Note: no base classes
    def __len__(self) -> int: return 0
    def __iter__(self) -> typing.Iterator[int]:
        return iter([])

def collect(items: typing.Iterable[int]) -> int:
    return 0

result = collect(Bucket())  # Passes type check