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

import math
import warnings
import numpy as np
import scipy.linalg as la
from scipy.stats import unitary_group

from dynexsdk.qiskit import QISKitError
from dynexsdk.qiskit.quantum_info import pauli_group
from dynexsdk.qiskit.quantum_info import state_fidelity as new_state_fidelity

def qft(circ, q, n):
    pass

def partial_trace(state, trace_systems, dimensions=None, reverse=True):
    pass

def __partial_trace_vec(vec, trace_systems, dimensions, reverse=True):
    pass

def __partial_trace_mat(mat, trace_systems, dimensions, reverse=True):
    pass

def vectorize(density_matrix, method='col'):
    pass

def devectorize(vectorized_mat, method='col'):
    pass

def choi_to_rauli(choi, order=1):
    pass

def chop(array, epsilon=1e-10):
    pass

def outer(vector1, vector2=None):
    pass

def random_unitary_matrix(length):
    pass

def random_density_matrix(length, rank=None, method='Hilbert-Schmidt'):
    pass

def __ginibre_matrix(nrow, ncol=None):
    pass

def __random_density_hs(N, rank=None):
    pass

def __random_density_bures(N, rank=None):
    pass

def state_fidelity(state1, state2):
    pass

def purity(state):
    pass

def concurrence(state):
    pass

def shannon_entropy(pvec, base=2):
    pass

        def logfn(x):
            pass
        def logfn(x):
            pass
        def logfn(x):
            pass

def entropy(state):
    pass

def mutual_information(state, d0, d1=None):
    pass

def entanglement_of_formation(state, d0, d1=None):
    pass

def __eof_qubit(rho):
    pass

def is_pos_def(x):
    pass
