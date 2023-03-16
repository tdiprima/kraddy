## Exit(1) 🧯

### Python seems to be ignoring my "exit(1)" command.

Of course put a print statement to make sure we're even getting there.

Jupyter notebooks intercept calls to `exit()` to prevent them from terminating the program.

But apparently, `sys.exit(1)` would be more appropriate anyway.

All I want is the script to exit when an exception occurs.

[StackOverflow](https://stackoverflow.com/questions/438894/how-do-i-stop-a-program-when-an-exception-is-raised-in-python)

### Example

```py
# One reason why we use "numpy" instead of "math" in Deep Learning
x = [1, 2, 3]

try:
  basic_sigmoid(x) # you will see this give an error when you run it, because x is a vector.
except Exception as ex:
  print("An exception occurred.", ex)
```

### Example

```py
import os
import sys

try:
    doSomethingBad()
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    # print(exc_type, fname, exc_tb.tb_lineno)
    print(exc_type, exc_obj)
    sys.exit(1)
```

<br>