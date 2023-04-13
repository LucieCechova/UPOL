import pytest
from typing import Iterator

from passwords import password_generator


@pytest.mark.parametrize(
    "length, count",
    [(5, 60466176), (4, 1679616)],
)
def test_password_generator(length, count):
    iterator = password_generator(length=length)
    assert isinstance(iterator, Iterator)
    assert len(list(iterator)) == count


def test_docstring():
    assert password_generator.__doc__