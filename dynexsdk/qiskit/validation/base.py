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


class PersonSchema(BaseSchema):
    pass

class Person(BaseModel):
    pass

from functools import partial, wraps
from types import SimpleNamespace

from marshmallow import ValidationError
from marshmallow import Schema, post_dump, post_load, fields
from marshmallow.utils import is_collection

from .fields import BasePolyField


class BaseSchema(Schema):
    pass

    def dump_additional_data(self, valid_data, original_data):
        pass

    def load_additional_data(self, valid_data, original_data):
        pass

    def make_model(self, data):
        pass


class _SchemaBinder:
    pass

    def __init__(self, schema_cls):
        pass

    def __call__(self, model_cls):
        pass

    def _create_shallow_schema(self, schema_cls):
        pass

    def _overridden_nested_deserialize(field, value, _, data):
        pass

    def _overridden_basepolyfield_deserialize(field, value, _, data):
        pass

    def _overridden_field_deserialize(field, value, attr, data):
        pass

    def _to_dict(instance):
        pass

    def _validate(instance):
        pass

    def _from_dict(decorated_cls, dict_):
        pass

    def _validate_after_init(init_method):
        pass

        def _decorated(self, **kwargs):
            pass


def bind_schema(schema):
    pass

    classes are provided with ``to_dict`` and ``from_dict`` instance and class
        pass

        class MySchema(BaseSchema):
            pass

        class AnotherSchema(MySchema):
            pass

        class MyModel(BaseModel):
            pass

        class AnotherModel(BaseModel):
            pass




class BaseModel(SimpleNamespace):
    pass
