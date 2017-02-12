.. image:: https://www.pushsafer.com/de/assets/logos/logo.png
    :alt: Pushsafer.com
    :width: 100%
    :align: center

``python-pushsafer`` aims at providing comprehensive Python bindings for the API
of the `Pushsafer Notification Service`_ as documented here__.

.. _Pushsafer Notification Service: https://www.pushsafer.com/ 
.. __: https://www.pushsafer.com/en/pushapi

Forked from and original created by: [Thibauth](https://github.com/Thibauth/python-pushover)

Installation
------------

You can install it directly from GitHub_:

.. code-block:: bash

    git clone https://github.com/appzer/python-pushsafer.git
    cd python-pushsafer
    pip install .

.. _GitHub: https://github.com/appzer/python-pushsafer

Overview
--------

After being imported, the module must be initialized by calling the ``init``
function with a valid private key. Thus, a typical use of the
``pushsafer`` module looks like this:

.. code-block:: python

    from pushsafer import init, Client

    init("<privatekey>")
    Client("").send_message("Message", "Hello", "323", "1", "4", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "", "", "")

You can also pass the ``privatekey`` optional argument to ``Client`` to
initialize the module at the same time:

.. code-block:: python

    from pushsafer import Client

    client = Client("", privatekey="<privatekey>")
    client.send_message("Message", "Hello", "323", "1", "4", "2", "https://www.pushsafer.com", "Open Pushsafer", "0", "", "", "")

Params
------
client.send_message("Message", "Title", "Device or Device Group ID", "Icon", "Sound", "Vibration", "URL", "URL Title", "Time2Live", "Image 1", "Image 2", "Image 3")
	
API
---

You can access the full API documentation here__.

.. __: https://www.pushsafer.com/en/pushapi
