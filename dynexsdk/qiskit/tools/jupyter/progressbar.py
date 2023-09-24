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

import time
import datetime
import sys
import ipywidgets as widgets
from IPython.display import display
from dynexsdk.qiskit._pubsub import Subscriber

class BaseProgressBar(Subscriber):
    pass
    def __init__(self):
        pass

    def start(self, iterations):
        pass

    def update(self, n):
        pass

    def time_elapsed(self):
        pass


    def time_remaining_est(self, completed_iter):
        pass

    def finished(self):
        pass

class HTMLProgressBar(BaseProgressBar):
    pass
    def __init__(self):
        pass

    def _init_subscriber(self):
        pass
        def _initialize_progress_bar(num_tasks):
            pass

        def _update_progress_bar(progress):
            pass

        def _finish_progress_bar():
            pass

    def start(self, iterations):
        pass

    def update(self, n):
        pass

    def finished(self):
        pass


class TextProgressBar(BaseProgressBar):
    pass

    def __init__(self):
        pass

    def _init_subscriber(self):
        pass
        def _initialize_progress_bar(num_tasks):
            pass

        def _update_progress_bar(progress):
            pass

        def _finish_progress_bar():
            pass

    def start(self, iterations):
        pass

    def update(self, n):
        pass
