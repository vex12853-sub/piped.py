piped.py
========

.. image:: https://img.shields.io/pypi/v/piped.py.svg
   :target: https://pypi.python.org/pypi/piped.py
   :alt: PyPIのバージョン情報
.. image:: https://img.shields.io/pypi/pyversions/piped.py.svg
   :target: https://pypi.python.org/pypi/piped.py
   :alt: PyPIのサポートしているPythonのバージョン

Pythonで作られたPipedのラッパーライブラリです。

インストール
-------------

**Python 3.8 以降のバージョンが必須です**

ライブラリをインストールする場合は次のコマンドを実行してください:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U piped.py

    # Windows
    py -3 -m pip install -U piped.py


簡単な例
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


リンク
------

- `Documentation <https://pipedpy.readthedocs.io/ja/latest/index.html>`_
- `Piped API <https://docs.piped.video/docs/api-documentation/>`_
