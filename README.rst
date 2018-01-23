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

The following code below shows the commands to run when building a new feature, namely "water-on-mars".

.. code-block:: guess

    $ git checkout -b <feature/water-on-mars>

Make all your changes for the feature development on the newly created feature. When pushing to Gitlab, use this:

.. code-block:: guess

    $ git push origin feature/water-on-mars

Once done with the feature development, merge the latest copy of the **master** branch into your feature branch. The reason we do this is because any conflict resolution can be done on the feature branch as opposed to the master branch. On your **feature-branch**, run the following command:

.. code-block:: guess

    $ git merge master

Resolve any conflicts that may arise and commit the merge to the feature branch.

Once that is done, create a merge request for your feature branch to commit into the master branch. This needs to be done from the repository on Gitlab. (https://gitlab.com/koinrex/koinrex/merge_requests)