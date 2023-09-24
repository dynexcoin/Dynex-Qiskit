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


import logging
import numpy as np
import scipy.sparse as sp
import scipy.sparse.csgraph as cs

from dynexsdk.qiskit.transpiler._transpilererror import TranspilerError
from dynexsdk.qiskit._qiskiterror import QISKitError
from dynexsdk.qiskit.dagcircuit import DAGCircuit
from dynexsdk.qiskit import _quantumcircuit
from dynexsdk.qiskit.unrollers import _dagunroller
from dynexsdk.qiskit.unrollers import _dagbackend
from dynexsdk.qiskit.unrollers import _jsonbackend
from dynexsdk.qiskit.mapper import (Coupling, optimize_1q_gates, coupling_list2dict, swap_mapper,
                                     cx_cancellation, direction_mapper,
                                     remove_last_measurements, return_last_measurements)
from dynexsdk.qiskit._pubsub import Publisher, Subscriber
from ._parallel import parallel_map

def transpile(circuits, backend, basis_gates=None, coupling_map=None, initial_layout=None,
              seed_mapper=None, hpc=None, pass_manager=None):
    pass

def _circuits_2_dags(circuits):
    pass

def _dags_2_dags(dags, basis_gates='u1,u2,u3,cx,id', coupling_map=None,
                 initial_layouts=None, seed_mapper=None, pass_manager=None):
    pass

    def _emmit_start(num_dags):
        pass

    def _emmit_done(progress):
        pass

    def _emmit_finish():
        pass



def _transpile_dags_parallel(dag_layout_tuple, basis_gates='u1,u2,u3,cx,id',
                            coupling_map=None, seed_mapper=None, pass_manager=None):
    pass



def transpile_dag(dag, basis_gates='u1,u2,u3,cx,id', coupling_map=None,
                 initial_layout=None, get_layout=False,
                 format='dag', seed_mapper=None, pass_manager=None):
    pass


def _best_subset(backend, n_qubits):
    pass

def _matches_coupling_map(dag, coupling_map):
    pass

def _pick_best_layout(dag, backend):
    pass



