import io

import pytest


@pytest.mark.parametrize(
    "input_, output",
    [
        (123, "Digit in the tens position is 2"),
        (-123, "Digit in the tens position is 2"),
        (12345, "Digit in the tens position is 4"),
        (-12, "Error: -12 has less than three digits"),
        (1, "Error: 1 has less than three digits"),
        (124, "Digit in the tens position is 2"),
    ],
)
def test_output(script_runner, input_, output):
    ret = script_runner.run("integer_input.py", stdin=io.StringIO(str(input_)))

    assert ret.success
    assert f"{output}\n" in ret.stdout
    assert ret.stderr == ""