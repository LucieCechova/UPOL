def test_output(script_runner):
    ret = script_runner.run("matrix_max_value.py")
    assert ret.success
    assert ret.stdout == "0 (-1, -2, -5, -20)\n1 (-10, -2, -3, -400)\n2 (-100, -2, -3, -4)\nmaximal=-1, summation=-552\n"
    assert ret.stderr == ""