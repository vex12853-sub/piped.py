piped.py
========

.. image:: https://img.shields.io/pypi/v/piped.py.svg
   :target: https://pypi.python.org/pypi/piped.py
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/piped.py.svg
   :target: https://pypi.python.org/pypi/piped.py
   :alt: PyPI supported Python versions

API wrapper for Piped written in Python.

Installing
----------

**Python 3.8 or higher is required**

To install the library, you can just run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U piped.py

    # Windows
    py -3 -m pip install -U piped.py


Quick Example
-------------

.. code:: py

    import piped
    
    print(piped.version_info)
    print(piped.server.latency())
    video = piped.Video("video id here")
    print(video.title)
    print(video.license)
    channel = video.fetch_author()
    print(channel.name)
    print(channel.description)


Links
------

- `Documentation <https://pipedpy.readthedocs.io/en/latest/index.html>`_
- `Piped API <https://docs.piped.video/docs/api-documentation/>`_
