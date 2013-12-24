from flint import Flint

class TestFelt:

	def test_empty_file(self):
		flint = Flint("test_resources/test_empty_file.md")
		flint.add("key", "value")
		flint.render()
		assert flint.getHTML() == ""

	def test_bare_markdown(self):
		flint = Flint("test_resources/test_bare_markdown.md")
		flint.render()
		with open("test_resources/test_bare_markdown.html") as correctHTML:
			assert correctHTML.read() == flint.getHTML()

	def test_add_individual_keys(self):
		flint = Flint("test_resources/general_test.md")
		flint.add("key1", "Hello")
		flint.add("key2", "world")
		flint.render()
		html = flint.getHTML()
		with open("test_resources/general_test.html") as correctHTML:
			assert correctHTML.read() == html

	def test_add_dict(self):
		flint = Flint("test_resources/general_test.md")
		my_dict = {"key1": "Hello", "key2": "world"}
		flint.add_dict(my_dict)
		flint.render()
		html = flint.getHTML()
		with open("test_resources/general_test.html") as correctHTML:
			assert correctHTML.read() == html

	def test_export_html(self):
		flint = Flint("test_resources/test_bare_markdown.md")
		flint.render()
		flint.exportHTML("test_resources/test_html_export.html")
		with open("test_resources/test_html_export.html") as exported:
			with open("test_resources/test_bare_markdown.html") as html:
				assert exported.read() == html.read()

	def test_iterate(self):
		flint = Flint("test_resources/test_iterate.md")
		flint.add_dict({"key1": [1, 2, 3, 4, 5], "key2": [1, 2, 3, 4, 5]})
		flint.render()
		with open("test_resources/test_iterate.html") as html:
			assert flint.getHTML() == html.read()

	def test_template_dict_mismatch(self):
		flint = Flint("test_resources/test_mismatch.md")
		flint.add_dict({"key": "hello",
						"this key is not in the template": "Uh oh"})
		flint.render()
		assert flint.getHTML() == "<p>hello, {world}</p>"

	def test_multiple_keys_in_template(self):
		flint = Flint("test_resources/test_multiple_keys_in_template.md")
		flint.add_dict({"key1": "hello",
						"list": [1]})
		flint.render()
		correctHTML = "<p>hello hello</p>\n<ul>\n<li>1 1</li>\n</ul>"
		assert flint.getHTML() == correctHTML

	def test_edge_cases(self):
		flint = Flint("test_resources/test_edge_cases.md")
		dict = {"int_value_key": 1,
				1: "int key",
				"iteration_key": [1, 2, 3, 4, 5]}
		flint.add_dict(dict)
		flint.render()
		with open("test_resources/test_edge_cases.html") as correctHTML:
			assert flint.getHTML() == correctHTML.read()