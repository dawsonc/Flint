# !/usr/bin/python
# Filename: flint.py

from markdown import markdown
import re


class Flint:

	def __init__(self, path_to_template):
		with open(path_to_template, "r") as file:
			self.text = file.read()
		self.vals = {}
		self.html = None

	def add(self, key, value):
		self.vals[key] = value

	def add_dict(self, dict):
		self.vals.update(dict)

	def get(self, key):
		if key in self.vals:
			return self.vals[key]

	def render(self):
		## TODO: Find a more robust way to strip file extensions (regex)

		self.rendered_text = self.text

		# Render the iterable items
		matches = re.findall(r'\|(.*?)\|\[\[(.*?)\]\]', self.rendered_text)
		for match in matches:
			key = match[0]
			if key in self.vals:
				value = self.vals[key]
				string_to_replace = "|" + str(key) + "|[[" + str(match[1]) + "]]"
				replacement = ""
				for item in value:
					replacement += "+ " + match[1].replace("{*}", str(item)) +"\n"
				self.rendered_text = self.rendered_text.replace(string_to_replace,
																replacement)

		# Render the values
		for key, value in self.vals.items():
			if str(key) in self.text:
				flint_string = "{" + str(key) + "}"
				self.rendered_text = self.rendered_text.replace(flint_string,
															    str(value))

		self.html = markdown(self.rendered_text)
		

	def getHTML(self):
		if self.html != None:
			return self.html

	def exportHTML(self, path_to_export):
		with open(path_to_export, "w") as f:
			f.write(self.html)

	def getText(self):
		return self.text

	def exportText(self, path_to_export):
		with open(path_to_export, "w") as f:
			f.write(self.text)

	def getRenderedText(self):
		return self.rendered_text

	def exportRenderedText(self, path_to_export):
		with open(path_to_export, "w") as f:
			f.write(self.rendered_text)