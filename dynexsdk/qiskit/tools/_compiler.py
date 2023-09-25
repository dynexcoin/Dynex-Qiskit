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
            skip_transpiler=False, seed_mapper=None,
            sampler = 'sa', num_reads = 5000, annealing_time = 300, mainnet=False, logging=False, 
            constrain_measured_qubits=True, constraint_strength = 10):

    outputs = list()
    inputs = list()
    
    qubit_biases = circuit.annealergraph.qubitbiases
    coupler_strengths = circuit.annealergraph.couplerstrengths

    print('[DYNEX] Qiskit circuit qubits:',len(circuit.annealergraph.qubits));
    print("[DYNEX] Embedding has been built:")
    print("\tnumber of qubits: ", len(qubit_biases))
    print("\tnumber of couplers: ", len(coupler_strengths))
    print("\tnumber of non-gate couplers: {}".format(len(coupler_strengths)-circuit.annealergraph.numgatecouplers))

    qubits = [];
    qubits_in = [];
    qubits_out = [];
    

    # measured qubits:
    for qubit in circuit.annealergraph.qubits.keys():
        if isinstance(circuit.annealergraph.qubits[qubit], dict):
            if circuit.annealergraph.qubits[qubit]['measured'] == True:
                outputs.append(circuit.annealergraph.qubits[qubit]['components'][-1])
                qubits_out.append(qubit);
                # can't omit output bit from being included as input, but is its put
                # first in the list, it will be zero the top portion of the readout
                if constrain_measured_qubits:
                	ans = 'y'
                	print('[DYNEX] INFO:',qubit,'was constrained to be 0 (contrain_measured_qubits=True)');
                else:
                	ans = input("Constrain input of measured qubit {} to be 0 (y/n)? ".format(qubit))
                if ans == 'y':
                    change = circuit.annealergraph.qubits[qubit]['components'][0]
                    circuit.annealergraph.qubitbiases[change] = circuit.annealergraph.qubitbiases[change] + constraint_strength
                else:
                    inputs.append(circuit.annealergraph.qubits[qubit]['components'][0])
                    qubits_in.append(qubit);
                qubits.append(qubit);

    # unmeasured qubits:
    for qubit in circuit.annealergraph.qubits.keys():
        if isinstance(circuit.annealergraph.qubits[qubit], dict):
            if circuit.annealergraph.qubits[qubit]['measured'] == False:
                if constrain_measured_qubits:
                	ans = 'n'
                else:
                	ans = input("Constrain input of unmeasured qubit {} to be 0 (y/n)? ".format(qubit))
                if ans == 'y':
                    change = circuit.annealergraph.qubits[qubit]['components'][0]
                    circuit.annealergraph.qubitbiases[change] = circuit.annealergraph.qubitbiases[change] + constraint_strength
                else:
                    inputs.append(circuit.annealergraph.qubits[qubit]['components'][0])
                    qubits_in.append(qubit);
                qubits.append(qubit);
            
    circuit.annealergraph.print_chimera_graph_to_file()
 
    if 'sim' in sys.argv:
    	# simulated:
    	print('not implemented');
    else:
        try:
            import dimod
            import dynex
            from dimod import SimulatedAnnealingSampler
        except:
            print('Dynex SDK not installed - cannot run generated embeddings. Please install and configure the Dynex SDK with pip install dynex.')
            return

        bqm = dimod.BinaryQuadraticModel(qubit_biases, coupler_strengths, 0, dimod.BINARY)
        #print('\nQubit biases:\n',qubit_biases)
        #print('\nCoupler strength:\n',coupler_strengths)
        print('[ÐYNEX] BQM gnerated');
        print('\tnumber of variables:',len(bqm.variables));
        print('\tnumber of qubit biases:',len(qubit_biases));
        print('\tnumber of coupler_strengths:',len(coupler_strengths));

        kwargs = {}
        
        if sampler == 'dynex':
        	print("[DYNEX] Running Qiskit Circuit on the Dynex Neuromorphic Platform...")
        	model = dynex.BQM(bqm, logging=logging);
        	sampler = dynex.DynexSampler(model,  mainnet=mainnet, description='IBM Qiskit', logging=logging);
        	response = sampler.sample(num_reads=num_reads, annealing_time = annealing_time, debugging=False);
        else:        
        	print("[DYNEX] Running Qiskit Circuit with Simulated Annealing Sampler...")
        	sampler = SimulatedAnnealingSampler()
        	response = sampler.sample(bqm, num_reads=10)
        
        print("[DYNEX] Sampling completed. Result:")
        print(response)

        groundstate = round(response.first.energy, 1);
        print("[DYNEX] Found ground state (energy): ", groundstate)

        function = list()
        for sample, energy in response.data(['sample', 'energy']):
            if round(energy,1) == groundstate:
                row = []
                for inp in inputs:
                    row.append(sample[inp])
                for outp in outputs:
                    row.append(sample[outp])
                function.append(row)
        
        # output qubit reads:
        function.sort()
        for i in range(len(function)):
            print('[DYNEX]',function[i])
        
        # generate return values:
        best_sample = response.first.sample;
        qubits_measured = {};
        qubits_unmeasured = {};
        for q in range(0, len(qubits_in)):
        	qubits_unmeasured[qubits_in[q]] = best_sample[inputs[q]];
        for q in range(0, len(qubits_out)):
        	qubits_measured[qubits_out[q]] = best_sample[outputs[q]];
        
        # return qubit reads:
        return qubits_measured, qubits_unmeasured
            
            
            
            
            
