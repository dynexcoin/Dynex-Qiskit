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

from functools import reduce
import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from scipy import linalg

from dynexsdk.qiskit.quantum_info import pauli_group, Pauli
from dynexsdk.qiskit.tools.visualization import VisualizationError
from dynexsdk.qiskit.tools.visualization._bloch import Bloch


class Arrow3D(FancyArrowPatch):
    pass

    def __init__(self, xs, ys, zs, *args, **kwargs):
        pass

    def draw(self, renderer):
        pass


def plot_hinton(rho, title='', filename=None):
    pass

def plot_bloch_vector(bloch, title="", filename=None):
    pass

def plot_state_city(rho, title="", filename=None):
    pass

def plot_state_paulivec(rho, title="", filename=None):
    pass

def n_choose_k(n, k):
    pass

def lex_index(n, k, lst):
    pass

def bit_string_index(s):
    pass

def phase_to_color_wheel(complex_number):
    pass

def plot_state_qsphere(rho, filename=None):
    pass

def plot_state(quantum_state, method='city', filename=None):
    pass

def plot_wigner_function(state, res=100, filename=None):
    pass

def plot_wigner_curve(wigner_data, xaxis=None, filename=None):
    pass

def plot_wigner_plaquette(wigner_data, max_wigner='local', filename=None):
    pass

def plot_wigner_data(wigner_data, phis=None, method=None, filename=None):
    pass


