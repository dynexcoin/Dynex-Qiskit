"""
Qiskit Dynex SDK (beta) Neuromorphic Computing Library
Copyright (c) 2021-2023, Dynex Developers

All rights reserved.

1. Redistributions of source code must retain the above copyright notice, this list of
    conditions and the following disclaimer.
 
2. Redistributions in binary form must reproduce the above copyright notice, this list
   of conditions and the following disclaimer in the documentation and/or other
   materials provided with the distribution.
 
3. Neither the name of the copyright holder nor the names of its contributors may be
   used to endorse or promote products derived from this software without specific
   prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

__version__ = "0.0.1"
__author__ = 'Dynex Developers'
__credits__ = 'Dynex Developers, Contributors, Supporters and the Dynex Community'


import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import (Axes3D, proj3d)

class Arrow3D(FancyArrowPatch):
    pass
    def __init__(self, xs, ys, zs, *args, **kwargs):
        pass

    def draw(self, renderer):
        pass


class Bloch():
    pass

    def __init__(self, fig=None, axes=None, view=None, figsize=None,
                 background=False):
        pass

    def set_label_convention(self, convention):
        pass

    def __str__(self):
        pass

    def clear(self):
        pass

    def add_points(self, points, meth='s'):
        pass

    def add_vectors(self, vectors):
        pass

    def add_annotation(self, state_or_vector, text, **kwargs):
        pass

    def make_sphere(self):
        pass

    def render(self, title=''):
        pass

    def plot_back(self):
        pass

    def plot_front(self):
        pass

    def plot_axes(self):
        pass

    def plot_axes_labels(self):
        pass

    def plot_vectors(self):
        pass

    def plot_points(self):
        pass

    def plot_annotations(self):
        pass

    def show(self, title=''):
        pass

    def save(self, name=None, output='png', dirc=None):
        pass

def _hide_tick_lines_and_labels(axis):
    pass
