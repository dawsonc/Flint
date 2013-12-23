This is {name}'s header
=======================

Insert {key} anywhere in the template, and Flint will replace it with the value for that key. If the key does not appear in Flint's dictionary, it will be ignored.

1 + 1 = {result}


Additionally, if you have a key with an iterable value, you can create a list:

|key_for_iterable|[[This is item {*}]]

The value will be inserted at the {*}