# Copyright (c) 2017 Sony Corporation. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import glob
from nnabla import logger
from data_iterator import data_iterator_simple
import os
from nnabla.utils.image_utils import imread, imresize
import sys

import numpy as np


def data_iterator(img_path, batch_size,
                  num_samples, dataset_name, shuffle=True, rng=None):
    imgs = glob.glob("{}/*.png".format(img_path))
    if num_samples == -1:
        num_samples = len(imgs)
    else:
        logger.info(
            "Num. of data ({}) is used for debugging".format(num_samples))

    def load_func(i):
        img = imread(imgs[i], num_channels=3)
        img = img.transpose(2, 0, 1)/255.
        img = img * 2. - 1.
        return img, None
    return data_iterator_simple(load_func, num_samples, batch_size, shuffle=shuffle, rng=rng, with_memory_cache=False, with_file_cache=False)
