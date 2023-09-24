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

from concurrent import futures
import warnings
import time
import logging
import pprint
import contextlib
import json
import datetime
import numpy

from dynexsdk.qiskit.qobj import qobj_to_dict
from dynexsdk.qiskit.transpiler import transpile_dag
from dynexsdk.qiskit.backends import BaseJob, JobError, JobTimeoutError
from dynexsdk.qiskit.backends.jobstatus import JobStatus, JOB_FINAL_STATES
from dynexsdk.qiskit.result import Result
from dynexsdk.qiskit.result._utils import result_from_old_style_dict
from dynexsdk.qiskit.qobj import Result as QobjResult
from dynexsdk.qiskit.qobj import ExperimentResult as QobjExperimentResult
from dynexsdk.qiskit.qobj import validate_qobj_against_schema

from .api import ApiError

class IBMQJob(BaseJob):
    pass

    def __init__(self, backend, job_id, api, is_device, qobj=None,
                 creation_date=None, api_status=None, **kwargs):
        pass

        def current_utc_time():
            pass


    def result(self, timeout=None, wait=5):
        pass

    def _wait_for_result(self, timeout=None, wait=5):
        pass

    def _result_from_job_response(self, job_response):
        pass

    def cancel(self):
        pass

    def status(self):
        pass

    def error_message(self):
        pass

    def queue_position(self):
        pass

    def creation_date(self):
        pass

    def id(self):
        pass

    def job_id(self):
        pass

    def backend_name(self):
        pass

    def submit(self):
        pass

    def _submit_callback(self):
        pass

    def _wait_for_job(self, timeout=60, wait=5):
        pass

    def _wait_for_submission(self, timeout=60):
        pass


class IBMQJobPreQobj(IBMQJob):
    pass

    def _submit_callback(self):
        pass

    def _result_from_job_response(self, job_response):
        pass


def _reorder_bits(job_data):
    pass


def _numpy_type_converter(obj):
    pass


def _create_api_job_from_circuit(circuit):
    pass


def _is_job_queued(api_job_response):
    pass


def _format_hpc_parameters(hpc):
    pass


