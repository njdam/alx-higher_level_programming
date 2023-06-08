# Third Project in Alx High level programming for imports of modules

Modules are a file or a python file which contain executable statements as known as functions. Then Module name can be used to access it's items by using this form like `modname.itemname()`, then to import it to local file and assign it to local variables by as follows:
```
>>> import modname
>>> loc = modname.itemname() # or you can use `modname.itemname()`
>>> loc(var) # Then you can start using it as the same as `modname.itemname(var)`
```

Then also you can import modename's items directly to locally as follows:
```
>>> import modname
>>> from modname import item1, item2
>>> item1(var) # then can be used as item 1
>>> item2(var) # then can be used as item 2
```

or you can use the followings:
```
>>> import modname
>>> from modname import * # means to import all items in modname
>>> item1(var) # then can be used as item 1
>>> item2(var) # then can be used as item 2
```

then you can change the name of `modname` or modname's items as follows:
```
>>> import modname as modu
>>> modu.itemname() # like this
>>>
>>> # then to import items is like follows
>>> from modname import item1 as item, item 2 as item0
>>> item(var) # like item1(var)
>>> item0(var) # like item2(var)
```

[Note](): For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change your modules, you must restart the interpreter – or, if it’s just one module you want to test interactively, use `importlib.reload()` like as follows:
```
>>> import importlib
>>> importlib.reload(modname)
```
 
