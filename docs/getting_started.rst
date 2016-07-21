Getting Started
===============

Getting your application tokens
+++++++++++++++++++++++++++++++

.. danger::

This section is subject to changes made by Yahoo and may not always be completely up-to-date. If you see something change on their end, please create a `new issue on Github <https://github.com/Ray-SunR/woeid/issues/new>`_ or submit a pull request to update it.


In order to use the woeid API client, you first need to acquire the consumer key. The ``consumer key`` will be required in order to create a ``woeid.Api`` object.

Create your app
________________

The first step in doing so is to create a `Yahoo App <https://developer.yahoo.com/apps/>`_. Click the "Create an App" button and fill out the fields on the next page.


.. image:: yahoo-app-creation-part1.png

If there are any problems with the information on that page, Yahoo will complain and you can fix it. (Make sure to get the name correct - it is unclear if you can change this later.) On the next screen, you'll see the application that you created and some information about it:

Your app
_________

Once your app is created, you'll be directed to a new page showing you some information about it.

.. image:: yahoo-app-creation-part2.png

Your Keys
_________

The stirng which is ecnlosed in red rectangle is your ``consumer key``.

.. image:: yahoo-app-creation-part3.png

At this point, you can test out your application using the ``consumer key`` to instantiate a ``woeid.Api(client_id=`YOUR_CLIENT_ID`)`` as follows::

    import woeid
    api = woeid.Api(client_id=[consumer_key])
