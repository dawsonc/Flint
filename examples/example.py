from flint import Flint

my_flint = Flint("example.md")
flint_dict = {"name": "Foobar",
			  "result": 1+1,
			  "key_for_iterable": [1, 2, 3, 4, 5]}
my_flint.add_dict(flint_dict)
my_flint.render()
my_flint.getHTML()
# This will return the rendered HTML, with all the values substituted
# 	Alternatively, you can export the HTML to a file by using
# 		my_flint.exportHTML("path/to/export")