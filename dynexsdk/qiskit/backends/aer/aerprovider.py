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

from collections import OrderedDict
import logging

from dynexsdk.qiskit._qiskiterror import QISKitError
from dynexsdk.qiskit.backends import BaseProvider
from dynexsdk.qiskit.backends.providerutils import resolve_backend_name, filter_backends

from .qasm_simulator import CliffordSimulator, QasmSimulator
from .qasm_simulator_py import QasmSimulatorPy
from .statevector_simulator import StatevectorSimulator
from .statevector_simulator_py import StatevectorSimulatorPy
from .unitary_simulator import UnitarySimulator

class AerProvider(BaseProvider):
    pass

    def __init__(self, *args, **kwargs):
        pass

    def get_backend(self, name=None, **kwargs):
        pass

    def backends(self, name=None, filters=None, **kwargs):
        pass

    def grouped_backend_names():
        pass

    def deprecated_backend_names():
        pass

    def _verify_aer_backends(self):
        pass

    def _get_backend_instance(self, backend_cls):
        pass

    def __str__(self):
        pass
