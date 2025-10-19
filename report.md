# Example Report
> This is just an example template, but feel free to edit it and make it your own.

Author: *mataiodoxion*


## Security Report
- *What you sent*;
I entered <script>alert(1)</script> into the /vulnerable_echo form.
- *What happened in the browser*;
A pop-up alert that says "1" appeared
- *Why the server was vulnerable*;
The server put my input straight into the HTML without escaping it, which let the browser run my code

## Pytest
```bash
(venv) lilianwu@Lilians-Air procedures-lab % pytest -v --tb=no
==================================================== test session starts ====================================================
platform darwin -- Python 3.11.5, pytest-7.4.2, pluggy-1.6.0 -- /opt/homebrew/opt/python@3.11/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/lilianwu/nighthawk/procedures-lab
configfile: pytest.ini
plugins: anyio-4.8.0
collected 8 items                                                                                                           

tests/test_endpoints.py::test_add_endpoint PASSED                                                                     [ 12%]
tests/test_endpoints.py::test_fib_endpoint PASSED                                                                     [ 25%]
tests/test_endpoints.py::test_item_crud PASSED                                                                        [ 37%]
tests/test_endpoints.py::test_vulnerable_echo_reflection SKIPPED (Reflection test ignored because fixed test passes)  [ 50%]
tests/test_endpoints.py::test_vulnerable_echo_fixed PASSED                                                            [ 62%]
tests/test_utils.py::test_add_simple PASSED                                                                           [ 75%]
tests/test_utils.py::test_fib_basic PASSED                                                                            [ 87%]
tests/test_utils.py::test_db_crud PASSED                                                                              [100%]

=============================================== 7 passed, 1 skipped in 0.02s ================================================
```