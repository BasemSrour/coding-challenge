coding-challenge
================

* Coding Challenge Project with a REST API app for large cities.

* It is used basically for making suggestions for the users with their search for cities
  with thier names, latitudes and longitudes provided in the url parmaetars to search with

* but you need to setup your databse first by looking at Setting Up Your databse section

* Look at the example for usage section to understand more

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

:License: MIT

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ make createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Setting Up Your databse
^^^^^^^^^^^^^^^^^^^^^

* You have first to run the data_population.py file first in the bash and have the csv file with the same directory that data_population.py exists.
* The CSV file have to have the same order as in the data_population.py file extracte them.

::

  $ make bash
  # python data_population.py
  Populating the data from the CSV file
  .
  .
  .
  City East La Mirada added
  City Holtville added
  City Rialto added
  City Guymon added
  City Stayton added
  City South Jordan added
  City Kelso added

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ make test

Example for usage
------------------
* Near match
GET /api/cities/suggestions/?q=Londo&latitude=43.70011&longitude=-79.416
::

  [
      {
          "name": "London",
          "symbol": "8",
          "country": "CA",
          "latitude": 42.98339,
          "longitude": -81.23304,
          "population": 346765,
          "timeZone": "America/Toronto",
          "score": 1.0
      },
      {
          "name": "London",
          "symbol": "OH",
          "country": "US",
          "latitude": 39.88645,
          "longitude": -83.44825,
          "population": 9904,
          "timeZone": "America/New_York",
          "score": 0.8
      },
      {
          "name": "Londontowne",
          "symbol": "MD",
          "country": "US",
          "latitude": 38.93345,
          "longitude": -76.54941,
          "population": 8018,
          "timeZone": "America/New_York",
          "score": 0.8
      },
      {
          "name": "New London",
          "symbol": "WI",
          "country": "US",
          "latitude": 44.39276,
          "longitude": -88.73983,
          "population": 7295,
          "timeZone": "America/Chicago",
          "score": 0.7
      },
      {
          "name": "London",
          "symbol": "KY",
          "country": "US",
          "latitude": 37.12898,
          "longitude": -84.08326,
          "population": 7993,
          "timeZone": "America/New_York",
          "score": 0.6
      }
  ]

* No match
GET /api/cities/suggestions/?q=SomeRandomCityInTheMiddleOfNowhere
::

  []


Documentation
------------------
::

  $ make docsup
Navigate to port 7000 on your host to see the documentation.

Deployment
----------

The following details how to deploy this application.

Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html

Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html
