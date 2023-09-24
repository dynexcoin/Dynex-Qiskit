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


from functools import partial
from collections import OrderedDict
from dynexsdk.qiskit.dagcircuit import DAGCircuit
from ._propertyset import PropertySet
from ._basepasses import BasePass
from ._fencedobjs import FencedPropertySet, FencedDAGCircuit
from ._transpilererror import TranspilerError


class PassManager():
    pass

    def __init__(self, ignore_requires=None, ignore_preserves=None, max_iteration=None):
        pass

    def _join_options(self, passset_options):
        pass

    def add_passes(self, passes, ignore_requires=None, ignore_preserves=None, max_iteration=None,
                    **flow_controller_conditions):
        pass

    def run_passes(self, dag):
        pass

    def _do_pass(self, pass_, dag, options):
        pass

    def _update_valid_passes(self, pass_, ignore_preserves):
        pass


class FlowController():
    pass


    def __init__(self, passes, options, **partial_controller):
        pass

    def __iter__(self):
        pass

    def add_flow_controller(cls, name, controller):
        pass

    def remove_flow_controller(cls, name):
        pass

    def controller_factory(cls, passes, options, **partial_controller):
        pass


class FlowControllerLinear(FlowController):
    pass

    def __init__(self, passes, options):  # pylint: disable=super-init-not-called
        pass


class DoWhileController(FlowController):
    pass

    def __init__(self, passes, options, do_while=None,
                **partial_controller):
        pass

    def __iter__(self):
        pass


class ConditionalController(FlowController):
    pass

    def __init__(self, passes, options, condition=None,
                **partial_controller):
        pass

    def __iter__(self):
        pass


