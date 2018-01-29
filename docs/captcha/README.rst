=============================
Koinrex signup with recaptcha
=============================

* To get your own keys for test on local server get recaptchaV2_.
   .. _recaptchaV2: https://www.google.com/recaptcha/intro/android.html

* Then click on 'Get Recaptcha'

* For `Lable type`, use any random keyword to identify the app

* Then select V2 and for domain type in 127.0.0.1

Changelog notes
---------------

* I updated the Koinrex login

* Implementing recaptcha is easy but validating it was the hardest part

* It was hard to find a tutorial to validate it based on our template/layout of the website so the only possible way I could find was to add a JS code in the html page (TODO)

   * So basically it disables the submit button until recaptcha is verified it is simple but not sure if it is ok to do this and it does not alter the other form functions example a field is left blank and so on.

* To change captcha type just replace the div with the new one


.. code:: html

      1) Image

      <div class="g-recaptcha" data-sitekey="6LdJ9kAUAAAAAH6e0YD6EhYNVP1pfBc0UAYgqj1u" data-callback="recaptchaCallback" data-expired-callback="recaptchaExpiredCallback" data-type="image"></div>

      2) Audio

      <div class="g-recaptcha" data-sitekey="6LdJ9kAUAAAAAH6e0YD6EhYNVP1pfBc0UAYgqj1u" data-callback="recaptchaCallback" data-expired-callback="recaptchaExpiredCallback" data-type="audio"></div>

      3)To change captcha theme-color

      <div class="g-recaptcha" data-sitekey="6LdJ9kAUAAAAAH6e0YD6EhYNVP1pfBc0UAYgqj1u" data-callback="recaptchaCallback" data-expired-callback="recaptchaExpiredCallback" data-type="image" data-theme="dark"></div>


Things to note
--------------

config/settings/base.py
=======================

**GOOGLE_RECAPTCHA_SITE_KEY** = "xxx"

**GOOGLE_RECAPTCHA_SECRET_KEY** = 'xxx'

**NOCAPTCHA** = True or **NOCAPTCHA** = False

**Not sure what True and False Does**


requirements/local.txt
======================

* 2 new packages for install, so please re-run `pip 3 install -r requirements/local.txt`

* If that does not work then try

.. code:: python

	$ pip3 install django-nocaptcha-recaptcha
	$ pip3 install django-recaptcha


koinrex/templates/account/signup.html
=====================================

* Please make sure that the keys are correct in all the places including this HTML file

.. code:: html

	<div class="g-recaptcha" data-sitekey="xxx" data-callback="recaptchaCallback" data-expired-callback="recaptchaExpiredCallback"></div>





