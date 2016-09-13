.. image:: https://www.pushsafer.com/de/assets/logos/logo.png
    :alt: Pushsafer.com
    :width: 100%
    :align: center

``pushsafer-python`` aims at providing comprehensive Python bindings for the API
of the `Pushsafer Notification Service`_ as documented here__.

.. _Pushsafer Notification Service: https://www.pushsafer.com/ 
.. __: https://www.pushsafer.com/en/pushapi

Forked from and original created by: [Thibauth](https://github.com/Thibauth/python-pushover)

Installation
------------

You can install pushsafer-python from Pypi_ with:

.. code-block:: bash

    $ pip install pushsafer-python

Or you can install it directly from GitHub_:

.. code-block:: bash

    git clone https://github.com/appzer/pushsafer-python.git
    cd pushsafer-python
    pip install .

.. _Pypi: https://pypi.python.org/pypi/pushsafer-python/
.. _GitHub: https://github.com/appzer/pushsafer-python

Overview
--------

After being imported, the module must be initialized by calling the ``init``
function with a valid private key. Thus, a typical use of the
``pushsafer`` module looks like this:

.. code-block:: python

    from pushsafer import init, Client

    init("<privatekey>")
    Client("").send_message("Hello!", title="Hello")

You can also pass the ``privatekey`` optional argument to ``Client`` to
initialize the module at the same time:

.. code-block:: python

    from pushsafer import Client

    client = Client("", privatekey="<privatekey>")
    client.send_message("Hello!", title="Hello")

Command line
~~~~~~~~~~~~

``pushsafer-python`` also comes with a command line utility ``pushsafer`` that
you can use as follows:

.. code-block:: bash

    pushsafer --privatekey <privatekey> "Hello!"

Use ``pushsafer --help`` to see the list of available options.

Configuration
~~~~~~~~~~~~~

Both the ``pushsafer`` module and the ``pushsafer`` command line utility support
reading arguments from a configuration file.

The most basic configuration file looks like this:

.. code-block:: ini

    [Default]
    privatekey=aaaaaa

You can have additional sections and specify a device as well:

.. code-block:: ini

    [my-iPhone]
    privatekey=bbbbbb
    device=233

``pushsafer-python`` will attempt to read the configuration from
``~/.pushsaferrc`` by default. The section to read can be specified by using the
``profile`` argument. With the configuration file above, you can send a message
by simply doing:

.. code-block:: python

    from pushsafer import Client

    Client().send_message("Hello!", title="Hello")

or ``pushsafer --title "Hello" "Hello!"`` from the command line.

API
---

You can access the full API documentation here__.

.. __: https://www.pushsafer.com/en/pushapi
