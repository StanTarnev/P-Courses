# Django Authentication

**Duration: 100 minutes**

## Learning Objectives

- Understand how to implement Django authentication
- Add Login pages and secure actions on record store

## Introduction

You might have noticed that you didn't have to use your password on our own templates, apart from back when we used the admin interface. You might also have noticed that this means that anyone can add or edit albums/artists in your inventory. We probably want this to be limited to users with privileges to do this. So let's do something about it.

Django comes with a user authentication system. It handles user accounts, groups, permissions and cookie-based user sessions.

The Django authentication system handles both authentication and authorisation. Briefly, authentication verifies a user is who they claim to be, and authorisation determines what an authenticated user is allowed to do.

The auth system consists of:

 - Users
 - Permissions: Binary (yes/no) flags designating whether a user may perform a certain task.
 - Groups: A generic way of applying labels and permissions to more than one user.
 - A configurable password hashing system
 - Forms and view tools for logging in users, or restricting content
 - A pluggable backend system

The authentication system in Django aims to be very generic and doesn’t provide some features commonly found in web authentication systems. Solutions for some of these common problems have been implemented in third-party packages:

 - Password strength checking
 - Throttling of login attempts
 - Authentication against third-parties (OAuth, for example)
 - Object-level permissions

We are just going to add a very rudimentary login page to our app and only display the add buttons if the user is authenticated.

### Securing add actions

First let's make things secure. We will protect our album_new and artist_new views so that only logged-in users can access them.

Django comes with some nice decorators for doing that.

The decorator we want to use is bundled in Django in the module `django.contrib.auth.decorators` and is called login_required.

So in `inventory/views.py`  add these lines at the top along with the rest of the imports:

```python
# inventory/views.py

from django.contrib.auth.decorators import login_required

```

Then add a line before each of the album_new and artist_new views (decorating them):

```python
# inventory/views.py

@login_required
def album_new(request):
  # ...
  # AS BEFORE

@login_required
def artist_new(request):

```

Now try to access `http://localhost:8000/inventory/album/new/`. Notice the difference?

> If you just got the empty form, you are probably still logged in from the chapter on the admin-interface. Go to http://localhost:8000/admin/logout/ to log out, then go to http://localhost:8000/post/new again. If still not working clear the browser cache.

You should get one of Djangos errors.

What is actually happening here is that the decorator we added will redirect you to the login page, but since that's not yet available, it raises a "Page not found (404)".


But we've reached part of our goal!! Now other people can't create albums or artists on our site anymore.

Unfortunately no-one else can either! So let's fix that next.

If you notice it is trying to hit a url `/accounts/login` then once logged in will next go to the add album page. We need to add a route to `/accounts/login` in order for this to work

### Logging users in

We could now try to do lots of complicated stuff to implement users and passwords and authentication, but doing this correctly is rather complicated.

As Django is "out of the box", someone has done the hard work for us, so we will make further use of the authentication tools provided.

We will need to add this login view to our whole site (not just inventory) so we will add it in the `record_store/views.py` file.

In your record_store/urls.py add a url `path('accounts/login/', views.LoginView.as_view(), name='login')`.

We also need to import the `LoginView` that will come bundled with Django Auth.

So the file should now look similar to this:

```python
# record_store/urls.py

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('inventory/', include('inventory.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),

]
```

Next we need to create a template for the login page. Again this will not be in the inventory folder. Django will look for this in a folder called `registration`.

We will create a new folder in `templates` called `registration` and create a file called `login.html` here.

```bash
mkdir templates/registration
touch templates/registration/login.html
```

And in this file we will add a log in form.

```html
<!-- login.html -->

{% extends "base.html" %}

{% block content %}
{% if form.errors %}
<p>Your username and password didn't match. Please try again.</p>
{% endif %}

<form method="post" action="{% url 'login' %}">
  {% csrf_token %}
  <table>
    <tr>
      <td>{{ form.username.label_tag }}</td>
      <td>{{ form.username }}</td>
    </tr>
    <tr>
      <td>{{ form.password.label_tag }}</td>
      <td>{{ form.password }}</td>
    </tr>
  </table>

  <input type="submit" value="login" />
  <input type="hidden" name="next" value="{{ next }}" />
</form>
{% endblock %}
```

You will see that this also makes use of our base template for the overall look and feel of our site

The nice thing here is that this just works. We don't have to deal with handling of the form submission nor with passwords and securing them.

 Only more thing is left to do. We should add a setting to `record_store/settings.py`:

```python
# record_store/settings.py

LOGIN_REDIRECT_URL = '/inventory'
```

Now when the login page is accessed directly, it will redirect a successful login to the top-level index (the homepage of our inventory).

Try it out! Go to  `http://localhost:8000/inventory/album/new/` and you should see that we now have a login form.

### Tidying up our login

We already set things up so that only authorized users (i.e. us) can actually add albums and artists. But everyone can see the links to add these. Let's make sure that if the user is not logged in then they are presented with a login option instead.

We will add a login button that looks like this: `<a href="{% url 'login' %}" class="top-menu">Log in</a>`

For this we need to edit the templates, so let's open up templates/base.html and change it so the part between the <nav> tags looks like this:

```html
<!-- base.html -->

<nav class="navbar navbar-expand-lg">
				<ul class="navbar-nav">
					<li class="nav"><a class="navbar-brand" href="{% url 'index' %}">Home</a></li>
					{% if user.is_authenticated %}
					<li class="nav"><a class="navbar-brand " href="{% url 'album_new' %}" >Add Album</a></li>
					<li class="nav"><a class="navbar-brand " href="{% url 'artist_new' %}" >Add Artist</a></li>
				</div>
				{% else %}
				<li class="nav"><a class="navbar-brand " href="{% url 'login' %}">Log in</a></li>
			</div>
				{% endif %}
			</ul>
		</nav>
```

You might recognise the pattern here. There is an if-condition in the template that checks for authenticated users to show the add buttons. Otherwise it shows a login button.


### Accessing user detail

Let's add some sugar to our templates while we're at it.

First we will add some details to show when we are logged in.

Edit `templates/base.html `like this:

```html
<!-- base.html -->

{% if user.is_authenticated %}
<li class="nav"><a class="navbar-brand " href="{% url 'album_new' %}" >Add Album</a></li>
<li class="nav"><a class="navbar-brand " href="{% url 'artist_new' %}" >Add Artist</a></li>
</div>
<div >
  <p class="welcome">Hello {{ user.username }} <small>(<a href="{% url 'logout' %}">Log out</a>)</small></p>
</div>
```

This adds a nice "Hello <username>" to remind us who we are logged in as, and that we are authenticated. Also, this adds a link to log out of the blog -- but as you might notice this isn't working yet. Let's fix it!

We decided to rely on Django to handle login, so let's see if Django can also handle logout for us. Check https://docs.djangoproject.com/en/2.0/topics/auth/default/ and see if you find something.

Like login we can add a URL in `record_store/urls.py` pointing to Django's logout view (i.e. django.contrib.auth.views.logout), like this:

```python
# record_store/urls.py

from django.contrib.auth.views import LoginView, LogoutView # MODIFIED


urlpatterns = [
    path('inventory/', include('inventory.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/inventory'), name='logout'), # ADDED
]
```

Now when we go to the site and log in we should see our welcome message and a link to log out.

But it gives us the user name.

We can go back to the Django admin area and update our user details and add a first name then save.

And back in base.html change `user.username` to `user.first_name`.

And that's it.

We now have a record store site where users:

- need a username and password to log in,
- need to be logged in to add albums or artists,
- and can log out again.
