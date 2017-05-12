__all__ = ['calcPointsOnLine']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['A', 'B', 'slope', 'intercept', 'coordinates', 'b', 'x', 'y', 'm'])
@Js
def PyJsHoisted_intercept_(point, slope, this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments, 'point':point, 'slope':slope}, var)
    var.registers(['point', 'slope'])
    if PyJsStrictEq(var.get('slope'),var.get(u"null")):
        return var.get('point').get('0')
    return (var.get('point').get('1')-(var.get('slope')*var.get('point').get('0')))
PyJsHoisted_intercept_.func_name = 'intercept'
var.put('intercept', PyJsHoisted_intercept_)
@Js
def PyJsHoisted_slope_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['a', 'b'])
    if (var.get('a').get('0')==var.get('b').get('0')):
        return var.get(u"null")
    return ((var.get('b').get('1')-var.get('a').get('1'))/(var.get('b').get('0')-var.get('a').get('0')))
PyJsHoisted_slope_.func_name = 'slope'
var.put('slope', PyJsHoisted_slope_)
var.put('A', Js([Js(10.0), Js(5.0)]))
var.put('B', Js([Js(15.0), Js(90.0)]))
pass
pass
var.put('m', var.get('slope')(var.get('A'), var.get('B')))
var.put('b', var.get('intercept')(var.get('A'), var.get('m')))
var.put('coordinates', Js([]))
#for JS loop
var.put('x', var.get('A').get('0'))
while (var.get('x')<=var.get('B').get('0')):
    try:
        var.put('y', ((var.get('m')*var.get('x'))+var.get('b')))
        var.get('coordinates').callprop('push', Js([var.get('x'), var.get('y')]))
        print (x,y)
    finally:
            (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
pass


# Add lib to the module scope
calcPointsOnLine = var.to_python()
