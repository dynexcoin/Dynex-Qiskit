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
import copy
from collections import OrderedDict
import numpy
from dynexsdk.qiskit import QISKitError, QuantumCircuit

class ExperimentResult(object):
    pass

    def __init__(self, qobj_result_experiment):
        pass

    def counts(self):
        pass

    def snapshots(self):
        pass

    def statevector(self):
        pass

    def unitary(self):
        pass


class Result(object):
    pass

    def __init__(self, qobj_result, experiment_names=None):
        pass

    def __str__(self):
        pass

    def __getitem__(self, i):
        pass

    def __len__(self):
        pass

    def __iadd__(self, other):
        pass

    def __add__(self, other):
        pass

    def _is_error(self):
        pass

    def get_status(self):
        pass

    def circuit_statuses(self):
        pass

    def get_circuit_status(self, icircuit):
        pass

    def get_job_id(self):
        pass

    def get_ran_qasm(self, name):
        pass

    def get_data(self, circuit=None):
        pass

    def _get_experiment(self, key=None):
        pass

    def get_counts(self, circuit=None):
        pass

    def get_statevector(self, circuit=None):
        pass

    def get_unitary(self, circuit=None):
        pass

    def get_snapshots(self, circuit=None):
        pass

    def get_snapshot(self, slot=None, circuit=None):
        pass

    def get_names(self):
        pass

    def average_data(self, name, observable):
        pass

    def get_qubitpol_vs_xval(self, nqubits, xvals_dict=None):
        pass

def _status_or_success(obj):
    pass
