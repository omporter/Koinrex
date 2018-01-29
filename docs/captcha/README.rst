
Koinrex signup with recaptcha
=============================

* To get your own keys for captcha for test on local server 

.. _google recaptcha: https://www.google.com/recaptcha/intro/android.html

* then click on get recaptcha

* for lable type test1 or whatever you want then select recaptcha V2 and for domain type in 127.0.0.1

Updates
-------

I updated the koinrex login 

Implementing recaptcha is easy but validating it was the hardest part.
It was hard to find a tutorial to validate it based on our template/layout of the website so the only possible way I could find was to add a JS code in the html page.

So basically it diables the submit button until recaptcha is verified it is simple but not sure if it is ok to do this and it does not alter the other form functions example a field is left blank and so on.

I just uploaded on my github before merging with master on gitlab.

to change captcha type just replace the div with the new one



.. code:: html <div class="g-recaptcha" data-sitekey="6LdJ9kAUAAAAAH6e0YD6EhYNVP1pfBc0UAYgqj1u" data-callback="recaptchaCallback" data-expired-callback="recaptchaExpiredCallback" data-type="image"></div>

.. code:: html <div class="g-recaptcha" data-sitekey="6LdJ9kAUAAAAAH6e0YD6EhYNVP1pfBc0UAYgqj1u" data-callback="recaptchaCallback" data-expired-callback="recaptchaExpiredCallback" data-type="audio"></div>

- to change color 

.. code:: html <div class="g-recaptcha" data-sitekey="6LdJ9kAUAAAAAH6e0YD6EhYNVP1pfBc0UAYgqj1u" data-callback="recaptchaCallback" data-expired-callback="recaptchaExpiredCallback" data-type="image" data-theme="dark"></div>


Things to note changes in the following 
=======================================

config/settings/base.py 
-----------------------

GOOGLE_RECAPTCHA_SITE_KEY = "xxx"
GOOGLE_RECAPTCHA_SECRET_KEY = 'xxx'

NOCAPTCHA = True or NOCAPTCHA = False

 - Not sure what True and False Does



requirements/local.txt 
----------------------

2 new packages for install 

if that does not work then try 

 .. pip3 install django-nocaptcha-recaptcha`
 .. pip3 install django-recaptcha`



koinrex/templates/account/signup.html
-------------------------------------

 .. <div class="g-recaptcha" data-sitekey="xxx" data-callback="recaptchaCallback" data-expired-callback="recaptchaExpiredCallback"></div>

 - and a JS code




