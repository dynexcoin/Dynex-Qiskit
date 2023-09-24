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

import errno
import logging
import os
import subprocess
import tempfile
import warnings
from PIL import Image

from dynexsdk.qiskit.dagcircuit import DAGCircuit
from dynexsdk.qiskit.tools.visualization import _error
from dynexsdk.qiskit.tools.visualization import _latex
from dynexsdk.qiskit.tools.visualization import _matplotlib
from dynexsdk.qiskit.tools.visualization import _text
from dynexsdk.qiskit.tools.visualization import _utils
from dynexsdk.qiskit.transpiler import transpile_dag

def plot_circuit(circuit,
                 basis="id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,"
                       "cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap",
                 scale=0.7,
                 style=None):
    pass

def circuit_drawer(circuit,
                   basis=None,
                   scale=0.7,
                   filename=None,
                   style=None,
                   output=None,
                   interactive=False,
                   line_length=None,
                   plot_barriers=True,
                   reverse_bits=False):
    pass

def qx_color_scheme():
    pass

def _text_circuit_drawer(circuit, filename=None,
                         basis="id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,"
                               "cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap", line_length=None,
                         reversebits=False, plotbarriers=True):
    pass

def latex_circuit_drawer(circuit,
                         basis="id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,"
                               "cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap",
                         scale=0.7,
                         filename=None,
                         style=None):
    pass

def _latex_circuit_drawer(circuit,
                          basis="id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,"
                                "cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap",
                          scale=0.7,
                          filename=None,
                          style=None,
                          plot_barriers=True,
                          reverse_bits=False):
    pass

def generate_latex_source(circuit, filename=None,
                          basis="id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,"
                                "cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap",
                          scale=0.7, style=None):
    pass

def _generate_latex_source(circuit, filename=None,
                           basis="id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,"
                                 "cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap",
                           scale=0.7, style=None, reverse_bits=False,
                           plot_barriers=True):
    pass

def matplotlib_circuit_drawer(circuit,
                              basis='id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,ry,rz,'
                                    'cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,cswap',
                              scale=0.7,
                              filename=None,
                              style=None):
    pass

def _matplotlib_circuit_drawer(circuit,
                               basis='id,u0,u1,u2,u3,x,y,z,h,s,sdg,t,tdg,rx,'
                                     'ry,rz,cx,cy,cz,ch,crz,cu1,cu3,swap,ccx,'
                                     'cswap',
                               scale=0.7,
                               filename=None,
                               style=None,
                               plot_barriers=True,
                               reverse_bits=False):
    pass



