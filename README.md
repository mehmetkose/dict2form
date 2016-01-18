dict2form
==========

python dictionary object to html5 json form generator

more information about [HTML JSON form submission](https://www.w3.org/TR/html-json-forms)

installation
==========
**pip install dict2form**


usage
==========

```python
from dict2form import dict2form
my_dictionary = {'name': 'Mehmet', 'surname': 'Kose'}
form = dict2form(my_dictionary, name="profile", method="post")
print(form)
```

As we'll see a form like this:

```html
<form enctype='application/json' method="post">
	<input name='profile[name]' value='Mehmet'>
	<input name='profile[surname]' value='Kose'>
	<input type='submit' value='Submit'>
</form>
```

input hiding
==========
```python
from dict2form import dict2form
my_dictionary = {'name': 'Mehmet', 'surname': 'Kose', 'password':'123456LOL'}
form = dict2form(my_dictionary, name="profile", hide=['password'])
```

xsrf
==========

```python
form = dict2form(my_dictionary, xsrf="XXXXXXXX")
print(form)
```

```html
<form enctype='application/json'>
	...
	<input type="hidden" name="_xsrf" value="XXXXXXXX"/>
</form>
```


defaults
==========
name = object
hide = []
method = GET
xsrf = None
submit_name = Submit