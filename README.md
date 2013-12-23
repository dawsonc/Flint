Flint
=====

Dynamic Markdown


What?
-----

Flint is a python engine for generating dynamic webpages from [Markdown](http://daringfireball.net/projects/markdown/) templates.


How?
----

I think the best way to demonstrate the syntax is with an example, so here goes:

### Python snippet: ###
```python
from flint import Flint

my_flint = Flint("example.md")
flint_dict = {"name": "Foobar",
			  "result": 1+1,
			  "key_for_iterable": [1, 2, 3, 4, 5]}
my_flint.render()
my_flint.getHTML()
# This will return the rendered HTML, with all the values substituted
# 	Alternatively, you can export the HTML to a file by using
# 		my_flint.exportHTML("path/to/export")
```

### template.md ###
```
This is {name}'s header
=======================

Insert {key} anywhere in the template, and Flint will replace it with the value for that key. If the key does not appear in Flint's dictionary, it will be ignored.

1 + 1 = {result}


Additionally, if you have a key with an iterable value, you can create a list:

|key_for_iterable|[[This is item {*}]]

The value will be inserted at the {*}
```


This will produce the following HTML:
```
<h1>This is Foobar's header</h1>
<p>Insert {key} anywhere in the template, and Flint will replace it with the value for that key. If the key does not appear in Flint's dictionary, it will be ignored.</p>
<p>1 + 1 = 2</p>
<p>Additionally, if you have a key with an iterable value, you can create a list:</p>
<ul>
	<li>This is item 1</li>
	<li>This is item 2</li>
	<li>This is item 3</li>
	<li>This is item 4</li>
	<li>This is item 5</li>
</ul>
<p>The value will be inserted at the {*}</p>
```

For more examples, see the examples folder.

More information on [my blog](http://www.cdawson.net/LINK)