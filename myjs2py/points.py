__all__ = ['points']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['A', 'Ba', 'B', 'Aa'])
var.put('Aa', Js([Js(10.0), Js(5.0)]))
var.put('Ba', Js([Js(15.0), Js(90.0)]))
var.put('A', Js([Js(10.0), Js(5.0)]))
var.put('B', Js([Js(15.0), Js(90.0)]))
pass


# Add lib to the module scope
points = var.to_python()