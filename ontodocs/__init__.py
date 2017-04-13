# !/usr/bin/env python
#  -*- coding: UTF-8 -*-

# from .builder import *
#
import os
from .VERSION import __version__, VERSION

# python package installation
_dirname, _filename = os.path.split(os.path.abspath(__file__))

ONTODOCS_VIZ_TEMPLATES = _dirname + "/media/templates/"
ONTODOCS_VIZ_STATIC = _dirname + "/media/static/"
