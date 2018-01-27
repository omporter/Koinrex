# koinrex_login
Koinrex login with recaptcha

To get your own keys for captcha for test on local server 

https://www.google.com/recaptcha/intro/android.html

then click on get recaptcha

for lable type test1 or whatever you want then select recaptcha V2 and for domain type in 127.0.0.1

----------------------------------------------------------------------------------------------------------------------------------

I updated the koinrex login 

Implementing recaptcha is easy but validating it was the hardest part.
It was hard to find a tutorial to validate it based on our template/layout of the website so the only possible way I could find was to add a JS code in the html page.

So basically it diables the submit button until recaptcha is verified it is simple but not sure if it is ok to do this and it does not alter the other form functions example a field is left blank and so on.

I just uploaded on my github before merging with master on gitlab.

to change captcha type just replace the div with the new one

```<div class="g-recaptcha" data-sitekey="6LdJ9kAUAAAAAH6e0YD6EhYNVP1pfBc0UAYgqj1u" data-callback="recaptchaCallback" data-expired-callback="recaptchaExpiredCallback" data-type="image"></div>

<div class="g-recaptcha" data-sitekey="6LdJ9kAUAAAAAH6e0YD6EhYNVP1pfBc0UAYgqj1u" data-callback="recaptchaCallback" data-expired-callback="recaptchaExpiredCallback" data-type="audio"></div>

to change color 

<div class="g-recaptcha" data-sitekey="6LdJ9kAUAAAAAH6e0YD6EhYNVP1pfBc0UAYgqj1u" data-callback="recaptchaCallback" data-expired-callback="recaptchaExpiredCallback" data-type="image" data-theme="dark"></div>
```
----------------------------------------------------------------------------------------------------------------------------------
Things to note changes in the following 

-----------------------------------------------------------------------------------------------------------------------------------
config/settings/base.py 

GOOGLE_RECAPTCHA_SITE_KEY = "xxx"
GOOGLE_RECAPTCHA_SECRET_KEY = 'xxx'

NOCAPTCHA = True or NOCAPTCHA = False

Not sure what True and False Does

-----------------------------------------------------------------------------------------------------------------------------------

requirements/local.txt 

2 new packages for install 

if that does not work then try 

`pip3 install django-nocaptcha-recaptcha`
`pip3 install django-recaptcha`

-----------------------------------------------------------------------------------------------------------------------------------

koinrex/templates/account/signup.html

<div class="g-recaptcha" data-sitekey="xxx" data-callback="recaptchaCallback" data-expired-callback="recaptchaExpiredCallback"></div>

and a JS code

----------------------------------------------------------------------------------------------------------------------------------
















Koinrex
=======

A kickass crypto to crypto exchange

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command:

.. code-block:: guess

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

.. Test coverage
.. ^^^^^^^^^^^^^

.. To run the tests, check your test coverage, and generate an HTML coverage report:

.. .. code-block:: guess

..     $ coverage run manage.py test
..     $ coverage html
..     $ open htmlcov/index.html

.. Running tests with py.test
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~

.. .. code-block:: guess

..     $ py.test

.. Live reloading and Sass CSS compilation
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. Moved to `Live reloading and SASS compilation`_.

.. .. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html

Deployment
----------

The following details how to deploy this application.

Local Development
^^^^^^^^^^^^^^^^^

To deploy locally for development on your machine:

.. code-block:: guess

    $ git clone https://gitlab.com/koinrex/koinrex.git
    $ cd koinrex
    $ mkvirtualenv koinrex
    $ workon koinrex / source bin/activate
    $ pip3 install -r requirements/local.txt
    $ ./manage.py migrate
    $ ./manage.py runserver

Contributing & Creating a Feature Branch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instructions for creating a feature branch and contributing to the codebase.

The following code below shows the commands to run when building a new feature, namely ``water-on-mars``. Make sure to use the namespace used below for consistency, i.e. using the ``feature`` tag before the actual name of the feature, separated by a ``/``.

.. code-block:: guess

    $ git checkout -b feature/water-on-mars

Make all your changes for the feature development on the newly created feature. When pushing to Gitlab, use this:

.. code-block:: guess

    $ git push origin feature/water-on-mars

Once done with the feature development, merge the latest copy of the ``master`` branch into your feature branch. The reason we do this is because any conflict resolution can be done on the feature branch as opposed to the master branch. On your ``feature/water-on-mars``, run the following command:

.. code-block:: guess

    $ git merge master

Resolve any conflicts that may arise and commit the merge to the feature branch.

Once that is done, create a merge request for your feature branch to commit into the master branch. This needs to be done from the repository on Gitlab. (https://gitlab.com/koinrex/koinrex/merge_requests)
