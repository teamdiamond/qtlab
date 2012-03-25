# hdf5_data.py, class for handling data in hdf5 container
#
# Wolfgang Pfaff <wolfgangpfff@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import gobject
import os
import os.path
import time
import numpy
import types
import re
import logging
import copy
import shutil
import h5py

from gettext import gettext as _L

from lib import namedlist, temp
from lib.misc import dict_to_ordered_tuples, get_arg_type
from lib.config import get_config
config = get_config()
in_qtlab = config.get('qtlab', False)
from lib.network.object_sharer import SharedGObject, cache_result

if in_qtlab:
    import qt

import data


class DateTimeGenerator(data.DateTimeGenerator):
    
    def new_filename(self, data_obj):
        base, ext = os.path.splitext(data.DateTimeGenerator.new_filename(
            self, data_obj))
        return base + '.hdf5'


class HDF5Data(SharedGObject):

    _data_list = data.Data._data_list
    _filename_generator = DateTimeGenerator()

    # TODO: open existing data (via kwarg in init)
    def __init__(self, *args, **kwargs):
        """
        Creates an empty data set including the file, for which the currently
        set file name generator is used.
        
        kwargs:
            name (string) : default is 'data'

        """
        
        name = kwargs.get('name', 'data')
        
        # FIXME: the name generation here is a bit nasty
        name = data.Data._data_list.new_item_name(self, name)
        self._name = name

        self._localtime = time.localtime()
        self._timestamp = time.asctime(self._localtime)
        self._timemark = time.strftime('%H%M%S', self._localtime)
        self._datemark = time.strftime('%Y%m%d', self._localtime)        
        
        self._filepath =  self._filename_generator.new_filename(self)
        self._dir, self._filename = os.path.split(self._filepath)
        if not os.path.isdir(self._dir):
            os.makedirs(self._dir)
        self._file = h5py.File(self._filepath, 'w')

    def __getitem__(self, name):
        return self._file[name]

    def __setitem__(self, name, val):
        self._file[name] = val

    def __repr__(self):
        ret = "HDF5Data '%s', filename '%s'" % (self._name, self._filename)
        return ret

    def create_dataset(self, *args, **kwargs):
        self._file.create_dataset(*args, **kwargs)

    def create_group(self, *args, **kwargs):
        self._file.create_group(*args, **kwargs)
    
    def close(self):
        self._file.close()





        

    
