# dict2form
===========

*python dictionary object to html5 json form generator*
**pip install dict2form**


```python
import dict2form
my_dictionary = {'name': 'Mehmet', 'surname': 'Kose'}
html_form = dict2form.dict2form(my_dictionary, name="profile", method="post", xsrf="xxxx")
print(html_form)
```

As we'll see a form like this:

```html
<form enctype='application/json' method="post">
	<input name='profile[name]' value='Mehmet'>
	<input name='profile[surname]' value='Kose'>
	<input type="hidden" name="_xsrf" value="xxxx"/>
</form>
```