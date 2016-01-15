dict2form
==========

python dictionary object to html5 json form generator

installation
==========
**pip install dict2form**


usage
==========

```python
from dict2form import dict2form
my_dictionary = {'name': 'Mehmet', 'surname': 'Kose'}
form = dict2form(my_dictionary, name="profile", method="post", xsrf="XXXXXXXX")
print(form)
```

As we'll see a form like this:

```html
<form enctype='application/json' method="post">
	<input name='profile[name]' value='Mehmet'>
	<input name='profile[surname]' value='Kose'>
	<input type="hidden" name="_xsrf" value="XXXXXXXX"/>
	<input type='submit' value='Submit'>
</form>
```