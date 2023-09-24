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


from copy import deepcopy
import uuid
import logging
import sys

def compile(circuits, backend,
            config=None, basis_gates=None, coupling_map=None, initial_layout=None,
            shots=1024, max_credits=10, seed=None, qobj_id=None, hpc=None,
            skip_transpiler=False, seed_mapper=None):
    pass

def dags_2_qobj(dags, backend_name, config=None, shots=None,
                max_credits=None, qobj_id=None, basis_gates=None, coupling_map=None,
                seed=None):
    pass

def _dags_2_qobj_parallel(dag, config=None, basis_gates=None, coupling_map=None):
    pass


def execute(circuit, backend = None,
            config=None, basis_gates=None, coupling_map=None, initial_layout=None,
            shots=1024, max_credits=10, seed=None, qobj_id=None, hpc=None,
            skip_transpiler=False, seed_mapper=None):

    outputs = list()
    inputs = list()
    
    qubit_biases = circuit.annealergraph.qubitbiases
    coupler_strengths = circuit.annealergraph.couplerstrengths

    print("\n[DYNEX] Embedding has been built:")
    print("\tnumber of qubits: ", len(qubit_biases))
    print("\tnumber of couplers: ", len(coupler_strengths))
    print("\tnumber of non-gate couplers: {}\n".format(len(coupler_strengths)-circuit.annealergraph.numgatecouplers))

    qubits = [];

    for qubit in circuit.annealergraph.qubits.keys():
        if isinstance(circuit.annealergraph.qubits[qubit], dict):
            if circuit.annealergraph.qubits[qubit]['measured'] == True:
                outputs.append(circuit.annealergraph.qubits[qubit]['components'][-1])
                # can't omit output bit from being included as input, but is its put
                # first in the list, it will be zero the top portion of the readout
                ans = input("Constrain input of measured qubit {} to be 0 (y/n)? ".format(qubit))
                if ans == 'y':
                    change = circuit.annealergraph.qubits[qubit]['components'][0]
                    circuit.annealergraph.qubitbiases[change] = circuit.annealergraph.qubitbiases[change] + 5
                else:
                    inputs.append(circuit.annealergraph.qubits[qubit]['components'][0])
                qubits.append(qubit);

    for qubit in circuit.annealergraph.qubits.keys():
        if isinstance(circuit.annealergraph.qubits[qubit], dict):
            if circuit.annealergraph.qubits[qubit]['measured'] == False:
                ans = input("Constrain input of unmeasured qubit {} to be 0 (y/n)? ".format(qubit))
                if ans == 'y':
                    change = circuit.annealergraph.qubits[qubit]['components'][0]
                    circuit.annealergraph.qubitbiases[change] = circuit.annealergraph.qubitbiases[change] + 5
                else:
                    inputs.append(circuit.annealergraph.qubits[qubit]['components'][0])
                qubits.append(qubit);
            
    circuit.annealergraph.print_chimera_graph_to_file()
 
    samp = input("\nHow many samples (=num_reads)? ")
    samp = int(samp)

    steps = input("\nHow many ODE integration steps (=annealing_time)? ")
    steps = int(samp)

    if 'sim' in sys.argv:
        try:
            import dimod
            from dwave.system.samplers import DWaveSampler
            from dwave.cloud.exceptions import SolverOfflineError
            from dwave.system.composites import EmbeddingComposite
            import minorminer
        except:
            print('Dimod not installed - cannot run or simulate generated embedding. Install dimod with pip install dimod')
            return


        ans = 'y'
        if len(circuit.annealergraph.qubitbiases) > 19:
            ans = input("WARNING: Embedding uses {} qubits - ExactSolver simulation could take way too long or cause your computer to crash. Type 'y' to continue: ".format(len(circuit.annealergraph.qubitbiases)))
        
        if ans == 'y' or ans == 'Y':
            print("Simulating problem with {} qubits".format(len(circuit.annealergraph.qubitbiases)))
            qubit_biases = circuit.annealergraph.qubitbiases
            coupler_strengths = circuit.annealergraph.couplerstrengths
        
            print("\nQubit Biases:")
            for key in qubit_biases.keys():
                print(key, "\t", qubit_biases[key])
            print("\nCoupler Strengths:")
            for key in coupler_strengths.keys():
                print(key, "\t", coupler_strengths[key])
            print("\n")

            bqm = dimod.BinaryQuadraticModel(qubit_biases, coupler_strengths, 0, dimod.BINARY)
            sampler = dimod.ExactSolver()
    
            response = sampler.sample(bqm)

            groundstate = 1000000
            for sample, energy in response.data(['sample','energy']):
                if energy<groundstate:
                    groundstate = round(energy,1)
        
            print("Ground State: ", groundstate)
            function = list()
            for sample, energy in response.data(['sample', 'energy']):
                if round(energy,1) == groundstate:
                    print(sample, round(energy,1))
                    row = []
                    for inp in inputs:
                        row.append(sample[inp])
                    for outp in outputs:
                        row.append(sample[outp])
                    function.append(row)
            print('\n')

            function.sort()
            for i in range(len(function)):
                print(function[i])
        else:
            print('Quitting.')
            
    else:
        try:
            import dimod
            import dynex
        except:
            print('Dynex SDK not installed - cannot run generated embeddings. Please install and configure the Dynex SDK with pip install dynex.')
            return

        bqm = dimod.BinaryQuadraticModel(qubit_biases, coupler_strengths, 0, dimod.BINARY)
        print('\nQubit biases:\n',qubit_biases)
        print('\nCoupler strength:\n',coupler_strengths)
        print('\n#bqm variables:\n',len(bqm.variables))
        kwargs = {}
        print("\nRunning Qiskit Circuit on the Dynex Neuromorphic Platform...")
        model = dynex.BQM(bqm, logging=True);
        sampler = dynex.DynexSampler(model,  mainnet=True, description='IBM Qiskit', logging=True);
        response = sampler.sample(num_reads=samp, annealing_time = steps, debugging=False);
        print("Done.")
        print(response)

        groundstate = 1000000
        for sample, energy in response.data(['sample','energy']):
            if energy<groundstate:
                groundstate = round(energy,1)
        print("Ground State: ", groundstate)

        function = list()
        for sample, energy in response.data(['sample', 'energy']):
            if round(energy,1) == groundstate:
                #print(sample, round(energy,1))
                row = []
                for inp in inputs:
                    row.append(sample[inp])
                for outp in outputs:
                    row.append(sample[outp])
                function.append(row)
        print('\n')
    
        # output qubit reads:
        print('qubits:')
        print(qubits);
        print('reads:')
        function.sort()
        for i in range(len(function)):
            print(function[i])
