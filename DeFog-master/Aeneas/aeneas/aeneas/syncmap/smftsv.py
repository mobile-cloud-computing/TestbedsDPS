#!/usr/bin/env python
# coding=utf-8

# aeneas is a Python/C library and a set of tools
# to automagically synchronize audio and text (aka forced alignment)
#
# Copyright (C) 2012-2013, Alberto Pettarin (www.albertopettarin.it)
# Copyright (C) 2013-2015, ReadBeyond Srl   (www.readbeyond.it)
# Copyright (C) 2015-2017, Alberto Pettarin (www.albertopettarin.it)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import
from __future__ import print_function

from aeneas.syncmap.smfgtabular import SyncMapFormatGenericTabular


class SyncMapFormatTSV(SyncMapFormatGenericTabular):
    """
    Handler for tab-separated plain text (TSV) I/O format.
    """

    TAG = u"SyncMapFormatTSV"

    DEFAULT = "tsv"

    HUMAN = "tsvh"

    MACHINE = "tsvm"

    TAB = "tab"

    MACHINE_ALIASES = [DEFAULT, MACHINE, TAB]

    FIELD_DELIMITER = u"\t"

    FIELDS = {
        "begin": 0,
        "end": 1,
        "identifier": 2,
    }

    TEXT_DELIMITER = None
