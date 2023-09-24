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
import logging

from dynexsdk.qiskit import QISKitError
from dynexsdk.qiskit._util import _camel_case_to_snake_case
from dynexsdk.qiskit.backends import BaseBackend
from dynexsdk.qiskit.backends import JobStatus

from .api import ApiError
from .ibmqjob import IBMQJob, IBMQJobPreQobj

class IBMQBackend(BaseBackend):
    pass

    def __init__(self, configuration, provider, credentials, api):
        pass

    def run(self, qobj):
        pass

    def calibration(self):
        pass

    def parameters(self):
        pass

    def properties(self):
        pass

    def status(self):
        pass

    def jobs(self, limit=50, skip=0, status=None, db_filter=None):
        pass

    def retrieve_job(self, job_id):
        pass

    def __repr__(self):
        pass

class IBMQBackendError(QISKitError):
    pass


class IBMQBackendValueError(IBMQBackendError, ValueError):
    pass


def _job_class_from_job_response(job_response):
    pass


def _job_class_from_backend_support(backend):
    pass


def _dict_merge(dct, merge_dct):
    pass

