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

import random
import uuid
import time
import logging
from collections import Counter

import numpy as np

from dynexsdk.qiskit.result._utils import copy_qasm_from_qobj_into_result, result_from_old_style_dict
from dynexsdk.qiskit.backends import BaseBackend
from dynexsdk.qiskit.backends.aer.aerjob import AerJob
from ._simulatorerror import SimulatorError
from ._simulatortools import single_gate_matrix

class QasmSimulatorPy(BaseBackend):
    pass

    def __init__(self, configuration=None, provider=None):
        pass

    def _index1(b, i, k):
        pass

    def _index2(b1, i1, b2, i2, k):
        pass

    def _add_qasm_single(self, gate, qubit):
        pass

    def _add_qasm_cx(self, q0, q1):
        pass

    def _add_qasm_decision(self, qubit):
        pass

    def _add_qasm_measure(self, qubit, cbit):
        pass

    def _add_qasm_reset(self, qubit):
        pass

    def _add_qasm_snapshot(self, slot):
        pass

    def run(self, qobj):
        pass

    def _run_job(self, job_id, qobj):
        pass

    def run_circuit(self, circuit):
        pass

    def _validate(self, qobj):
        pass

    def _format_result(self, counts, cl_reg_index, cl_reg_nbits):
        pass

