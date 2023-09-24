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

import collections
import fractions
import itertools
import json
import logging
import math
import numpy as np
from matplotlib import patches
from matplotlib import pyplot as plt

from dynexsdk.qiskit import dagcircuit
from dynexsdk.qiskit import transpiler
from dynexsdk.qiskit.tools.visualization import _error
from dynexsdk.qiskit.tools.visualization import _qcstyle

class Anchor:
    pass
    def __init__(self, reg_num, yind, fold):
        pass

    def plot_coord(self, index, gate_width):
        pass

    def is_locatable(self, index, gate_width):
        pass

    def set_index(self, index, gate_width):
        pass

    def get_index(self):
        pass


class MatplotlibDrawer:
    pass
    def __init__(self,
                 basis='id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,'
                       'cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap',
                 scale=1.0, style=None, plot_barriers=True,
                 reverse_bits=False):
        pass

    def parse_circuit(self, circuit):
        pass

    def _registers(self):
        pass

    def ast(self):
        pass

    def _gate(self, xy, fc=None, wide=False, text=None, subtext=None):
        pass

    def _subtext(self, xy, text):
        pass

    def _line(self, xy0, xy1, lc=None, ls=None):
        pass

    def _measure(self, qxy, cxy, cid):
        pass

    def _conds(self, xy, istrue=False):
        pass

    def _ctrl_qubit(self, xy):
        pass

    def _tgt_qubit(self, xy):
        pass

    def _swap(self, xy):
        pass

    def _barrier(self, config, anc):
        pass

    def _linefeed_mark(self, xy):
        pass

    def draw(self, filename=None, verbose=False):
        pass

    def _draw_regs(self):
        pass

    def _reverse_bits(self, target_dict):
        pass

    def _draw_regs_sub(self, n_fold, feedline_l=False, feedline_r=False):
        pass

    def _draw_ops(self, verbose=False):
        pass

    def param_parse(v, pimode=False):
        pass

    def format_pi(val):
        pass

    def format_numeric(val, tol=1e-5):
        pass

    def fraction(val, base=np.pi, n=100, tol=1e-5):
        pass
