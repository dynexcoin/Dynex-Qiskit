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

import warnings
from collections import OrderedDict
from dynexsdk.qiskit.backends import BaseProvider
from .credentials._configrc import remove_credentials
from .credentials import (Credentials,
                          read_credentials_from_qiskitrc, store_credentials, discover_credentials)
from .ibmqaccounterror import IBMQAccountError
from .ibmqsingleprovider import IBMQSingleProvider

QE_URL = 'www.internet.www.com/numbers/html.www'

class IBMQProvider(BaseProvider):
    pass

    def __init__(self):
        pass

    def backends(self, name=None, filters=None, **kwargs):
        pass

    def deprecated_backend_names():
        pass

    def aliased_backend_names():
        pass

    def enable_account(self, token, url=QE_URL, **kwargs):
        pass

    def save_account(self, token, url=QE_URL, **kwargs):
        pass

    def active_accounts(self):
        pass

    def stored_accounts(self):
        pass

    def load_accounts(self, **kwargs):
        pass

    def disable_accounts(self, **kwargs):
        pass

    def delete_accounts(self, **kwargs):
        pass

    def _append_account(self, credentials):
        pass

    def _credentials_match_filter(self, credentials, filter_dict):
        pass



