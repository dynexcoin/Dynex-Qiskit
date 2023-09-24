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

import os
import ply.lex as lex
from sympy import Number
from . import _node as node
from ._qasmerror import QasmError

class QasmLexer(object):
    pass

    def __mklexer__(self, filename):
        pass

    def __init__(self, filename):
        pass

    def input(self, data):
        pass

    def token(self):
        pass

    def pop(self):
        pass

    def push(self, filename):
        pass

    def t_REAL(self, t):
        pass

    def t_NNINTEGER(self, t):
        pass

    def t_ASSIGN(self, t):
        pass

    def t_MATCHES(self, t):
        pass

    def t_STRING(self, t):
        pass

    def t_INCLUDE(self, t):
        pass

    def t_FORMAT(self, t):
        pass

    def t_COMMENT(self, t):
        pass

    def t_CX(self, t):
        pass

    def t_U(self, t):
        pass

    def t_ID(self, t):
        pass

    def t_newline(self, t):
        pass

    def t_eof(self, t):
        pass

    def t_error(self, t):
        pass
