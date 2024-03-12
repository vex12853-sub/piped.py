"""
Piped API Wrapper
~~~~~~~~~~~~~~~~~~~

A basic wrapper for the Piped API.

:copyright: (c) 2024-present vex12853
:license: MIT, see LICENSE for more details.

"""


__title__ = 'piped'
__author__ = 'vex12853'
__license__ = 'MIT'
__copyright__ = 'Copyright 2024-present vex12853'
__version__ = '0.1.2'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal

from .video import Video
from .channel import Channel
from . import server


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=0, minor=0, micro=0, releaselevel='alpha', serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())

del logging, NamedTuple, Literal, VersionInfo