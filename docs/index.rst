.. piped.py documentation master file, created by
   sphinx-quickstart on Sun Mar 10 10:19:14 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

piped.pyへようこそ。
===================

リリース v\ |version|. (:ref:`インストール<install>`)

.. image:: https://img.shields.io/pypi/v/piped.py.svg
   :target: https://pypi.python.org/pypi/piped.py
   :alt: PyPIのバージョン情報
.. image:: https://img.shields.io/pypi/pyversions/piped.py.svg
   :target: https://pypi.python.org/pypi/piped.py
   :alt: PyPIのサポートしているPythonのバージョン

**piped.py**はPythonで作られた軽量なPipedAPIのラッパーライブラリです。


使用例
-------------------

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


特徴
-------------------

- オブジェクト指向を利用した直感的な運用が可能
- コマンドラインツールとしてのサポート

.. toctree::
   :maxdepth: 2
   :caption: Contents:

ユーザーガイド
-------------------

基本的なサンプルコードなど。

.. toctree::
   :maxdepth: 2

   user/install
   user/quickstart
   user/streams
   user/captions
   user/playlist
   user/channel
   user/search
   user/cli
   user/exceptions

APIドキュメント
-------------------

全ての関数、クラス、メソッドのリファレンス。

.. toctree::
  :maxdepth: 2

  api


目次とテーブル
===================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
