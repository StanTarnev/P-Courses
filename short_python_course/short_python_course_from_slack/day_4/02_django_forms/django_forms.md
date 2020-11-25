# Django Forms

**Duration: 120 minutes**

## Learning Objectives

- Understand how Django can build forms for us
- Add a form using Django to accept user input.

## Introduction

Unless you’re planning to build websites and applications that do nothing but publish content, and don’t accept input from your visitors, you’re going to need to understand and use forms.

Django provides a range of tools and libraries to help you build forms to accept input from site visitors, and then process and respond to the input.

Handling forms is a complex business. There may be data that may need to be prepared for display in a form, rendered as HTML, edited using a convenient interface, returned to the server, validated and cleaned up, and then saved or passed on for further processing.

Django’s form functionality can simplify and automate vast portions of this work, and can also do it more securely than most programmers would be able to do in code they wrote themselves.

Django handles three distinct parts of the work involved in forms:

 - preparing and restructuring data to make it ready for rendering
 - creating HTML forms for the data
 - receiving and processing submitted forms and data from the client

It is possible to write code that does all of this manually, but Django can take care of it all for you.

### The brief

We're going to expand our record shop application to allow users to add and edit an Album/Artist.

Django's admin is cool, but it is rather hard to customise and make pretty. With forms we will have absolute power over our interface – we can do almost anything we can imagine!

I recommend you download the start point for this lesson as there has been some CSS added and a nav added to `base.html`

Download the start point and run the following commands:

```bash
cd record_shop
python -m venv .env
source .env/bin/activate

pip3 install django

cd record_store

python manage.py flush (yes)

python manage.py loaddata seeds.json

python manage.py runserver
```

We have added a seeds.json file with a few artists set up.

`flush` will clear the existing data in the database.

`loaddata` uses the JSON data to populate the database.

### A note on CSS

 > This has already been completed for you. This is for information only. Do not code along!

In Django CSS, images, etc files need to be stored in a directory called `static`.

Django will automatically find any folders called "static" inside any of your apps' folders. Then it will be able to use their contents as static files.

To use them in the application we need to do 3 things:

We need to tell our HTML template that we added some CSS. In `base.html` file in we added this line at the very beginning of it:

```html
<!-- base.html -->

{% load static %}
```

Next add a link to the CSS file:

```html
<!-- base.html -->

<link rel="stylesheet" href="{% static 'css/blog.css' %}">
```

And lastly pointing to the static filepath in `settings.py`

```python
# settings.py

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

Now we can add Images and CSS to our site. Again we have already added some styling to the app but feel free to play around with it after the lesson.


### Adding a Django form

We’ve used HTML forms in previous lessons, but an HTML `<form>` is just one part of what we need in order to process data.

In the context of a Web application, ‘form’ might refer to that HTML <form>, or to the Django Form that produces it, or to the structured data returned when it is submitted, or to everything included to get the form working.

Django’s has it's own in-built Form class. A Form class describes a form and determines how it works and appears.

When we created our model classes we used them to map the class fields to database fields. With the form class, fields map to HTML form `<input>` elements.

All of the form’s fields are classes in their own right; they control and manage form data and perform validation when a form is submitted.

A form field is represented to a user in the browser as an HTML “widget”. Each field type has a default Widget class, but these can be overridden if we so wish.

### Instantiating, processing, and rendering forms

When we are rendering our objects we:

 - read it from the database and pass to the view
 - pass it to the template context
 - convert it to HTML markup using template variables

Rendering a form in a template involves nearly the same work as rendering any other kind of object, but there are some key differences.

When we’re dealing with a form we instantiate it in the view.

### Building a form

The nice thing about Django forms is that we can either define one from scratch or create a ModelForm which will save the result of the form to the model.

This is exactly what we want to do: we will start by creating a form for our Album model.

Like every important part of Django, forms have their own file: `forms.py`.

We need to create a file with this name in the `inventory` directory.

```bash
touch inventory/forms.py
```

We already know what we want our HTML form to look like. Our starting point for it in Django is this:

```python
from django import forms

from .models import Album, Artist

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title', 'year', 'stock_level', 'artist')
```

We need to import Django forms first (`from django import forms`) and our Album and Artist models.

AlbumForm, as you probably suspect, is the name of our form. We need to tell Django that this form is a ModelForm (so Django will do some magic for us) – forms.ModelForm is responsible for that.

Next, we have class Meta, where we tell Django which model should be used to create this form (model = Album).

Finally, we can say which field(s) should end up in our form. In this scenario we want `title`, `year`, `stock_level` and `album` to be exposed. Django will create these form fields for us and use the appropriate input type. In the case of album Django is clever and knows the relationship so populates a dropdown with all of the albums in the database.

We could manually assign the types of inputs we wanted above the `meta` class.

So if we wanted to add a field to get the albums in a dropdown we can use `ModelChoiceField`.

Two fields are available for representing relationships between models: `ModelChoiceField` and `ModelMultipleChoiceField`.

 > Upon form validation, these fields will place either one model object (in the case of ModelChoiceField) or multiple model objects (in the case of ModelMultipleChoiceField) into the dictionary of the form.

```python
# forms.py

class AlbumForm(forms.ModelForm):

    artist = forms.ModelChoiceField(Artist.objects.all())

    class Meta:
        model = Album
        fields = ('title', 'year', 'stock_level', 'artist')
```

And that's it! All we need to do now is use the form in a view and display it in a template.

So once again we will create a link to the page, a URL, a view and a template. We will put this link in a `nav` section.

In the `base.html` in the templates folder. Add the following lines:

```html

<div class="header">
		<div>
			<nav class="navbar navbar-expand-lg">
				<ul class="navbar-nav">
					<li class="nav"><a class="navbar-brand" href="{% url 'index' %}">Home</a></li>
					<li class="nav"><a class="navbar-brand " href="{% url 'album_new' %}" >Add Album</a></li> <!--ADDED -->
				</div>
			</ul>
		</nav>
	</div>
</div>
```

This gives us a link. If we look at the browser though we get an error telling us that Django doesn't know about  `album_new`. We need to include this in our `urls` file.

### Urls

In the `urls.py` file we need to add the url for the POST request and which function we want to run when that URL is called.

```python
# inventory/urls.py

urlpatterns = [
    path('', views.index, name='index'),
    path('album/new/', views.album_new, name='album_new'),
]
```

After refreshing the site, we still see an AttributeError, since we don't have the `album_new` view implemented.

### The view

Form data sent back to a Django website is processed by a view, generally the same view which published the form. This allows us to reuse some of the same logic.

To handle the form we need to instantiate it in the view for the URL where we want it to be published:

```python
# inventory/views.py

from .forms import AlbumForm # ADDED

# ...

# AS BEFORE

# ....

def album_new(request):
    form = AlbumForm()
    return render(request, 'inventory/album_form.html', {'form': form})

```

Now if we click on the link we get a new error. It will take us to `localhost:8000/inventory/album/new` but we have no template set up to render the form in!

Let's set that up now.

### The template

In the view we said we would render a template called `album_form.html` so we need to create that file in the `templates/inventory` directory.

```bash
touch templates/inventory/album_form.html
```

To make a form work we need several things:

- We have to display the form. We can do that with (for example) `{{ form.as_p }}`.
- The line above needs to be wrapped with an HTML form tag: `<form method="POST">...</form>.`
- We need a Save button. We do that with an HTML button: ` <button type="submit" class="save btn btn-default">Save</button>`.

And finally, just after the opening `<form ...>` tag we need to add `{% csrf_token %}`. This is very important, since it makes your forms secure! If you forget about this bit, Django will complain when you try to save the form:

```html
<!-- album_form.html -->
{% extends 'base.html' %}

{% block content %}
<h2>New Album</h2>
<form method="POST" class="inventory-form">
  {% csrf_token %}
  <div class="form-group">
    {{ form.as_p }}
  </div>
  <button type="submit" class="save btn btn-default">Save</button>
</form>
{% endblock %}
```

All the form’s fields and their attributes will be unpacked into HTML markup from that {{ form.as_p }} by Django’s template language.

Time to refresh! Yay! Your form is displayed!

If we look at the source code we will see that all of the form fields are wrapped up in a `<p>` tag.

Forms have a few optional rendering options in Django: `as_p`, `as_table`, `as_ul` to give us more control over how the form is rendered.

Try some of them out and see how it affects the rendering of the form.

### Forms and Cross Site Request Forgery protection

Django ships with an easy-to-use protection against Cross Site Request Forgeries. When submitting a form via POST with CSRF protection enabled you must use the `csrf_token` template tag as in the preceding example.

### HTML5 input types and browser validation

If your form includes a `URLField`, an `EmailField` or any `integer` field type, Django will use the url, email and number HTML5 input types. By default, browsers may apply their own validation on these fields, which may be stricter than Django’s validation. If you would like to disable this behaviour, set the `novalidate` attribute on the form tag, or specify a different widget on the field, like `TextInput`.

### Submitting the form

We now have a web form, described by a Django Form, processed by a view, and rendered as an HTML `<form>`.

But, wait a minute! When you type something in the fields and try to save it, what will happen?

Nothing! We are once again on the same page and our text is gone… and no new album is added. So what went wrong?

The answer is: nothing. We need to do a little bit more work in our view.

### Saving the data

Open `inventory/views.py` once again in the code editor. Currently all we have in the `album_new` view is the following:

```python
def album_new(request):
    form = AlbumForm()
    return render(request, 'inventory/album_form.html', {'form': form})
```

When we submit the form, we are brought back to the same view, but this time we have some more data in request, more specifically in request.POST.

 > Remember how in the HTML file, our `<form>` definition had the variable `method="POST"`? All the fields from the form are now in `request.POST`. You should not rename `POST` to anything else.

So in our view we have two separate situations to handle: first, when we access the page for the first time and we want a blank form, and second, when we go back to the view with all form data we just typed.

So we need to add a condition (we will use `if` for that):

```python
#inventory/views.py

if request.method == "POST":
    #TODO Save the data
else:
    form = AlbumForm()
    return render(request, 'inventory/album_form.html', {'form': form})
```

If method is `POST` then we want the view to once again create a Django form instance and populate it with data from the request.

This is called “binding data to the form” (it is now a bound form).

We will do that as follows:

```python
# views.py
def album_new(request):
  if request.method == "POST":
    form = AlbumForm(request.POST) # ADDED
  else:
    form = AlbumForm()
    return render(request, 'inventory/album_form.html', {'form': form})
```

Now our Django form will have been populated with the data from the request. This is important as it will be used to create an instance of our Album model.  

We want to make sure that the data in the form is valid. Fortunately Django forms will provide this validation for us.

Just like normal form validation, Django form validation is triggered implicitly when calling is_valid().

If `is_valid()` is `True`, we use the Django forms `save` method to save the data in a new instance of the Album class.

This is possible because we specified the Album as the model in our forms.py.

```python
class meta:
    model = Album
```

```python
# views.py

def album_new(request):
  if request.method == "POST":
    form = AlbumForm(request.POST)
    if form.is_valid():
      album = form.save(commit=False)
  else:
    form = AlbumForm()
    return render(request, 'inventory/album_form.html', {'form': form})

```

This `save()` method accepts an optional `commit` keyword argument, which accepts either `True` or `False`. If you call `save()` with `commit=False`, then it will return an object that hasn't yet been saved to the database. (We may at this point want to do some other things in the instance before saving to the database, like adding current timestamps, etc)

```python
# views.py

def album_new(request):
  if request.method == "POST":
    form = AlbumForm(request.POST)
    if form.is_valid():
      album = form.save(commit=False)
      album.save()
  else:
    form = AlbumForm()
    return render(request, 'inventory/album_form.html', {'form': form})

```

Lastly once the album is saved we will redirect back to the inventory page.

To redirect we need to import this from Django. Add this to the top of the file.  

```python
# views.py

from django.shortcuts import redirect
```

And after the album is saved redirect back to the index view.

```python
# views.py

def album_new(request):
  if request.method == "POST":
    form = AlbumForm(request.POST)
    if form.is_valid():
      album = form.save(commit=False)
      album.save()
      return redirect('index') # ADDED
  else:
    form = AlbumForm()
    return render(request, 'inventory/album_form.html', {'form': form})
```

Let's see if it works.

Go to the page http://localhost:8000/album/new/, add new album, save it… and hey presto! The new album is added and we are redirected to the index page!

## Task

Create a form to add a new artist to the collection. Use the same classes for the form.

Create:

- Link in the navigation
- New form class in the `forms.py` file
- New Url
- New view method
- New template

### Note!

Be careful when adding the fields to the ArtistFrom. If you add it like:

```python
fields = ('name')
```

Django will complain. It expects a tuple. You need at least one comma after the first field to change the type to a tuple (I know, I know it seems silly but it's what is expected).

So you need to type

```python
fields = ('name',)
```

Try it in pythons REPL:

```bash
>>> type(("name"))
<type 'str'>
>>> type(("name",))
<type 'tuple'>
```

<details>
<summary>Example solution</summary>

```html
<!-- base.html -->
<nav>
  <ul>
    <li><a href="{% url 'index' %}">Home</a></li>
    <li class="nav"><a class="navbar-brand " href="{% url 'album_new' %}" >Add Album</a></li>
		<li class="nav"><a class="navbar-brand " href="{% url 'artist_new' %}" >Add Artist</a></li>
  </ul>
</nav>
```

```python
# urls.py

urlpatterns = [
    path('', views.index, name='index'),
    path('album/new/', views.album_new, name='album_new'),
    path('artist/new/', views.artist_new, name='artist_new'),
]

```

```python
# forms.py

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title', 'year', 'stock_level', 'artist')

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('name',)
```

```html
<!-- atrist_form.html -->

{% extends 'base.html' %}

{% block content %}
    <h2>New Artist</h2>
    <form method="POST" class="inventory-form">
      {% csrf_token %}
      <div class="form-group">
        {{ form.as_p }}
        </div>
        <button type="submit" class="save btn btn-default">Save</button>
    </form>
{% endblock %}

```

```python
# views.py

def artist_new(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.save()
            return redirect('index')
    else:
        form = ArtistForm()
        return render(request, 'inventory/artist_form.html', {'form': form})

```
</details>

## Summary

Creating forms in Django, is really similar to creating a model.

Django can default the field type to be added to the form or we can specify and extend directly.

In Django, the request object passed as parameter to your view has an attribute called "method" where the type of the request is set, and all data passed via POST can be accessed via the request.POST dictionary.
