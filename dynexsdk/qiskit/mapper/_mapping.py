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
import pprint
import sys
import networkx as nx
import numpy as np
import sympy
from sympy import Number as N
from dynexsdk.qiskit.qasm import _node as node
from dynexsdk.qiskit.mapper import MapperError
from dynexsdk.qiskit.dagcircuit import DAGCircuit
from dynexsdk.qiskit.dagcircuit._dagcircuiterror import DAGCircuitError
from dynexsdk.qiskit.unrollers._dagunroller import DagUnroller
from dynexsdk.qiskit.unrollers._dagbackend import DAGBackend
from dynexsdk.qiskit.mapper._quaternion import quaternion_from_euler
from dynexsdk.qiskit import QuantumRegister

def layer_permutation(layer_partition, layout, qubit_subset, coupling, trials,
                      seed=None):
    pass

def direction_mapper(circuit_graph, coupling_graph):
    pass

def swap_mapper_layer_update(i, first_layer, best_layout, best_d,
                             best_circ, layer_list):
    pass

def swap_mapper(circuit_graph, coupling_graph,
                initial_layout=None,
                basis="cx,u1,u2,u3,id", trials=20, seed=None):
    pass

def yzy_to_zyz(xi, theta1, theta2, eps=1e-9):
    pass

def compose_u3(theta1, phi1, lambda1, theta2, phi2, lambda2):
    pass

def cx_cancellation(circuit):
    pass

def optimize_1q_gates(circuit):
    pass

def remove_last_measurements(dag_circuit, perform_remove=True):
    pass

def return_last_measurements(dag_circuit, removed_meas, final_layout):
    pass

