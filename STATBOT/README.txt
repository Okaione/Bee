1. Indentation issues are rampant. For that, use BLACK.
    `pip install black`
    `black STATBOT`

2. Statements after a `return`.
    As soon as execution hits a `return` statement, execution of that function stops. Any statements directly following a `return` with the same indentation will never be executed.
    There are a few `print`s around that will never be executed. Do anything you need to do before returning.

3. `skw` function didn't have a return statement. It just printed some text.

4. `kurt` function didn't have a return statement. It just printed some text.

5. Within a function's `def` block you can only access variables that were either created within that function OR passed in as parameters.

6. You had a function and a variable named `sse`. This confuses the interpreter as it doesn't know which you mean. Everything must have a unique name.

7. In many `print` statements in functions you have things like: `print("The smallest datapoint is", mini(data))`
    Since the function is called `mini` when you try to print you're calling the function again which then gets to a print statement where... it calls the function again which then gets to a print statement where... it calls the function again. Forever.
    In this case what you really want is to return the _variable_ that has the data you want. For that function it's `smallest`.

8. Most (all?) of the stats functions you're implementing have an equivalent `numpy` version. You could choose to use those rather than reinvent the wheel.
    https://numpy.org/doc/2.1/reference/routines.statistics.html

9. There are some architectural changes I'd make to the code too to make it more user friendly.
    For example, you might use classes to hang this together or allow it to be invoked from the command line.
    A bit of time on writing down what you want to go IN to this model and what you want OUT of it might focus the mind on what functionality you need.

10. I've not actually run any of this (I don't have some of the packages installed) and I've not verified any of the maths, just the code.