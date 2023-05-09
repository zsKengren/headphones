Headphones Plugin
==========

``headphones`` is a plugin that lets you automatically update `Headphones`_'s library whenever you change your beets library.

To use ``headphones`` plugin, enable it in your configuration (see :ref:`using-plugins`). Then, you'll want to configure the specifics of your Headphones server. You can do that using an ``headphones:`` section in your ``config.yaml``, which looks like this::

    headphones:
        host: localhost
        key: api_key
        username: user
        password: pass

To use the ``headphones`` plugin you need to install the `requests`_ library with::

    pip install requests

With that all in place, you'll see beets send the "update" command to your Headphones server every time you change your beets library.

.. _Headphones: https://github.com/rembo10/headphones
.. _requests: https://requests.readthedocs.io/en/master/

Configuration
-------------

The available options under the ``headhphones:`` section are:

- **host**: The Headphones server host. You also can include ``http://`` or ``https://``.
  Default: ``localhost``
- **key**: The Headphones API key.
- **username**: A username of a Headphones user that is allowed to refresh the library.
- **password**: The password for the user.
