# dict2form
===========

python dictionary object to html5 json form generator


> import dict2form
> my_dictionary = {'name': 'Mehmet', 'surname': 'Kose'}
> html_form = dict2form.dict2form(my_dictionary, name="profile")
> print(html_form)


> <form enctype='application/json'>
>  <input name='profile[name]' value='Mehmet'>
>   <input name='profile[surname]' value='Kose'>
> </form>

