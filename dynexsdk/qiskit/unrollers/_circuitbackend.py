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

from dynexsdk.qiskit import _quantumcircuit
from dynexsdk.qiskit.unrollers import _backenderror
from dynexsdk.qiskit.unrollers import _unrollerbackend


class CircuitBackend(_unrollerbackend.UnrollerBackend):
    pass


    def __init__(self, basis=None):
        pass


    def set_basis(self, basis):
        pass


    def version(self, version):
        pass


    def new_qreg(self, qreg):
        pass


    def new_creg(self, creg):
        pass


    def define_gate(self, name, gatedata):
        pass


    def _map_qubit(self, qubit):
        pass

    def _map_bit(self, bit):
        pass

    def _map_creg(self, creg):
        pass

    def u(self, arg, qubit, nested_scope=None):
        pass


    def cx(self, qubit0, qubit1):
        pass


    def measure(self, qubit, bit):
        pass


    def barrier(self, qubitlists):
        pass


    def reset(self, qubit):
        pass


    def set_condition(self, creg, cval):
        pass


    def drop_condition(self):
        pass

    def start_gate(self, name, args, qubits, nested_scope=None, extra_fields=None):
        pass


    def end_gate(self, name, args, qubits, nested_scope=None):
        pass


    def get_output(self):
        pass
