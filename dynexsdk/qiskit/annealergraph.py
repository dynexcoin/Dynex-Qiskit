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

from dynexsdk.qiskit._quantumregister import QuantumRegister
from dynexsdk.qiskit._classicalregister import ClassicalRegister
from math import floor, copysign
import sys
import dynex
                
class annealer_graph():
    def __init__(self, regs):
        self.qubits = self.getqubitnames(regs)
        self.qubitbiases = {}
        self.couplerstrengths = {}
        self.gatenum = 0     
        self.topleftofgatecells = [392, 136, 152, 408, 424, 168, 184, 440, 456, 200, 216, 472, 488,
                                   744, 728, 984, 968, 712, 696, 952, 936, 680, 664, 920, 904,
                                   1160,1176,1432,1448,1192,1208,1464,1480,1224,1240,1496,1512,
                                   1768,1752,2008,1992,1736,1720,1976,1960,1704,1688,1944,1928,1672]  
        self.fullnodelist = [i for i in range(2048)]
        self.fulledgelist = self.generatefulledgelist()
        self.numgatecouplers = 0
        self.unavailablecouplers = list()
        self.unavailablenodes = list()
        self.dontuse = list()
        self.skipgates = list()

        print("\n=====================================\nQiskit on Dynex Neuromorphic Platform\n=====================================\n")

    def generatefulledgelist(self):
        fulledgelist = list()
        for i in range(2048):
            celltopleft = i - i%8
            graphcolumn = (celltopleft/8)%16
            graphrow = ((celltopleft)-((celltopleft)/8 % 16)*8)/128 % 16
            # if on left of cell
            if i%8<4:
                # connect to right side of cell
                for j in range(celltopleft+4,celltopleft+8):
                    fulledgelist.append((i,j))
                # connect to cell below if not in last row of graph
                if graphrow!=15:
                    fulledgelist.append((i,i+128))
            else:
                # connect to cell to the right if not in last column of graph
                if graphcolumn!=15:
                    fulledgelist.append((i,i+8))
        return fulledgelist

    def getqubitnames(self, regs):
        qubits = {}
        for reg in regs:
            for i in range(regs[reg].size):
                qubits['{}_{}'.format(regs[reg].name,i)] = {'components': list(), 'measured': False}
    
        qubits['annealer_ancillas'] = list()

        return qubits

    def add_X(self, targ):
        while self.gatenum in self.skipgates:
            print("Skip gate {}".format(self.gatenum))
            self.gatenum = self.gatenum + 1

        topleft = self.topleftofgatecells[self.gatenum]
        
        if self.gatenum % 2 == 0:
            outname = 0 + topleft
            inname = 4 + topleft

        else:
            outname = 4 + topleft
            inname = 0 + topleft

        inval = -4
        outval = -4
        
        inoutcouplerval = 10
        
        self.numgatecouplers=self.numgatecouplers+1

        if len(self.qubits[targ]['components']) > 0:
            injoin = self.qubits[targ]['components'][-1]
            injointopleft = injoin - injoin % 8
            injoincell = self.topleftofgatecells.index(injointopleft) 
            # if coming from last cell
            if self.gatenum - injoincell == 1:
                #find row
                injoinrow = injoin % 4

                # change position of row being connected
                # if there were more rows occupied in this 
                # gate the qubits previously in this row
                # would have to be switched with inname and outname
                inname = inname + injoinrow
                outname = outname + injoinrow

                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if injoincell % 4 == 0:
                    if (self.gatenum-1)%12==0 and (self.gatenum-1)>0:
                        newqubit = injoin + 128
                    else:
                        newqubit = injoin - 128

                elif injoincell % 2 == 0:
                    newqubit = injoin + 128
                else:
                    if floor((self.gatenum-1)/12) % 2 == 0:
                        newqubit = injoin + 8
                    else:
                        newqubit = injoin - 8
               
                # add new qubit chain with injoin
                self.qubitbiases[injoin] = self.qubitbiases[injoin] + 5
                self.qubits[targ]['components'].append(newqubit) 
                self.qubitbiases[newqubit] = 10
                self.couplerstrengths[(min(injoin, newqubit), max(injoin, newqubit))] = -10
                
                # chain inname with newqubit
                inval = inval + 5
            
                self.couplerstrengths[(min(newqubit, inname), max(newqubit,inname))] = -10

            else:
                inname, outname, inval, outval = self.make_chain(inname, outname, inval, outval, injoin, targ)
        
        inoutcouplername = (min(inname,outname), max(inname, outname))

        self.qubits[targ]['components'].append(inname)
        self.qubits[targ]['components'].append(outname)

        self.qubitbiases[inname] = inval
        self.qubitbiases[outname] = outval

        self.couplerstrengths[inoutcouplername] = inoutcouplerval

        self.gatenum = self.gatenum + 1

    def add_CNOT(self, ctl, targ):
        while self.gatenum in self.skipgates:
            print("Skip gate {}".format(self.gatenum))
            self.gatenum = self.gatenum + 1

        topleft = self.topleftofgatecells[self.gatenum]

        if self.gatenum % 2 == 0:
            # out side left
            ancout_name = topleft
            out_name = 1 + topleft
            ctlout_name = 2 + topleft
            
            # in side right
            ancin_name = 4 + topleft
            targ_name = 5 + topleft
            ctlin_name = 6 + topleft
        else:
            # out side right 
            ancout_name = 4 + topleft
            out_name = 5 + topleft
            ctlout_name = 6 + topleft
            
            # in side left
            ancin_name = topleft
            targ_name = 1 + topleft
            ctlin_name = 2 + topleft
        
        #qubitbiases
        ctlin_val = 6
        ancin_val = 9
        targ_val = 1
            
        ctlout_val = 6
        ancout_val = 9
        out_val = 1
        
        #couplerstrengths
        ancin_ancout_couplerval = -14
        ancin_ctlout_couplerval = -4
        ancout_targ_couplerval = -4
        ancin_out_couplerval = 4
        ctlin_ctlout_couplerval = -11
        ctlin_out_couplerval = -2
        ctlout_targ_couplerval = 2
        targ_out_couplerval = -2
 
        self.numgatecouplers = self.numgatecouplers + 8
 
        assignedins = {}
        
        if len(self.qubits[targ]['components']) > 0:
            targjoin = self.qubits[targ]['components'][-1]
            targjointopleft = targjoin - targjoin % 8
            targjoincell = self.topleftofgatecells.index(targjointopleft)
            # if coming from last cell
            if self.gatenum - targjoincell == 1:
                #find row
                rowoffset = targjoin % 4 - targ_name % 4

                # change position of row being connected
                # if there were more rows occupied in this 
                # gate the qubits previously in this row
                # would have to be switched with inname and outname

                targ_name = targ_name + rowoffset
                out_name = out_name + rowoffset

                for row in [[ctlin_name, ctlout_name], [ancin_name, ancout_name]]:
                    if row[0] == targ_name:
                        row[0] = row[0] - rowoffset
                        row[1] = row[1] - rowoffset

                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if targjoincell % 4 == 0:
                    if (self.gatenum-1)%12==0 and (self.gatenum-1)>0:
                        newqubit = targjoin + 128
                    else:
                        newqubit = targjoin - 128

                elif targjoincell % 2 == 0:
                    newqubit = targjoin + 128
                else:
                    if floor((self.gatenum-1)/12) % 2 == 0:
                        newqubit = targjoin + 8
                    else:
                        newqubit = targjoin - 8


                # add new qubit chain with injoin
                self.qubitbiases[targjoin] = self.qubitbiases[targjoin] + 5
                self.qubits[targ]['components'].append(newqubit)
                self.qubitbiases[newqubit] = 10 
                self.couplerstrengths[(min(targjoin, newqubit), max(targjoin, newqubit))] = -10

                # chain inname with newqubit
                targ_val = targ_val + 5

                self.couplerstrengths[(min(newqubit, targ_name), max(newqubit,targ_name))] = -10

                self.qubits[targ]['components'].append(targ_name)
                self.qubitbiases[targ_name] = targ_val

                assignedins['targ'] = targ_name

        if len(self.qubits[ctl]['components']) > 0:
            ctlinjoin = self.qubits[ctl]['components'][-1]
            ctlinjointopleft = ctlinjoin - ctlinjoin % 8
            ctlinjoincell = self.topleftofgatecells.index(ctlinjointopleft)
            # if coming from last cell
            if self.gatenum - ctlinjoincell == 1:
                #find row
                rowoffset = ctlinjoin % 4 - ctlin_name % 4

                # change position of row being connected
                # if there were more rows occupied in this 
                # gate the qubits previously in this row
                # would have to be switched with inname and outname

                ctlin_name = ctlin_name + rowoffset
                ctlout_name = ctlout_name + rowoffset

                for row in [[targ_name, out_name], [ancin_name, ancout_name]]:
                    if row[0] == ctlin_name:
                        row[0] = row[0] - rowoffset
                        row[1] = row[1] - rowoffset


                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if ctlinjoincell % 4 == 0:
                    if (self.gatenum-1)%12==0 and (self.gatenum-1)>0:
                        newqubit = ctlinjoin + 128
                    else:
                        newqubit = ctlinjoin - 128

                elif ctlinjoincell % 2 == 0:
                    newqubit = ctlinjoin + 128
                else:
                    if floor((self.gatenum-1)/12) % 2 == 0:
                        newqubit = ctlinjoin + 8
                    else:
                        newqubit = ctlinjoin - 8

                # add new qubit chain with injoin
                self.qubitbiases[ctlinjoin] = self.qubitbiases[ctlinjoin] + 5
                self.qubits[ctl]['components'].append(newqubit)
                self.qubitbiases[newqubit] = 10 
                self.couplerstrengths[(min(ctlinjoin, newqubit), max(ctlinjoin, newqubit))] = -10

                # chain inname with newqubit
                ctlin_val = ctlin_val + 5

                self.couplerstrengths[(min(newqubit, ctlin_name), max(newqubit, ctlin_name))] = -10

                self.qubits[ctl]['components'].append(ctlin_name)
                self.qubitbiases[ctlin_name] = ctlin_val

                assignedins['ctlin'] = ctlin_name

        if len(self.qubits[targ]['components']) > 0:
            if self.gatenum - targjoincell > 1:
                targjoin = self.qubits[targ]['components'][-1]
                targ_name, out_name, targ_val, out_val = self.make_chain(targ_name, out_name, targ_val, out_val, targjoin, targ)
                
                self.qubits[targ]['components'].append(targ_name)
                self.qubitbiases[targ_name] = targ_val

                assignedins['targ'] = targ_name

        if len(self.qubits[ctl]['components']) > 0:
            if self.gatenum - ctlinjoincell > 1:
                ctlinjoin = self.qubits[ctl]['components'][-1]
                ctlin_name, ctlout_name, ctlin_val, ctlout_val = self.make_chain(ctlin_name, ctlout_name, ctlin_val, ctlout_val, ctlinjoin, ctl)
                
                self.qubits[ctl]['components'].append(ctlin_name)
                self.qubitbiases[ctlin_name] = ctlin_val

                assignedins['ctlin'] = ctlin_name

        availablerows = [0,1,2,3]
        for key in assignedins.keys():
            availablerows.pop(availablerows.index(assignedins[key]%4))
        if 'targ' not in assignedins:
            if targ_name % 4 not in availablerows:
                rowoffset = availablerows[0] - targ_name % 4
                targ_name = targ_name + rowoffset
                out_name = out_name + rowoffset
                availablerows.pop(availablerows.index(targ_name%4))
            else:
                availablerows.pop(availablerows.index(targ_name%4))

        if 'ctlin' not in assignedins:
            if ctlin_name % 4 not in availablerows:
                rowoffset = availablerows[0] - ctlin_name % 4
                ctlin_name = ctlin_name + rowoffset
                ctlout_name = ctlout_name + rowoffset
                availablerows.pop(availablerows.index(ctlin_name%4))
            else:
                availablerows.pop(availablerows.index(ctlin_name%4))

        if 'ancin' not in assignedins:
            if ancin_name %4 not in availablerows:
                rowoffset = availablerows[0] - ancin_name % 4
                ancin_name = ancin_name + rowoffset
                ancout_name = ancout_name + rowoffset
                availablerows.pop(availablerows.index(ancin_name%4))
            else:
                availablerows.pop(availablerows.index(ancin_name%4))


        #couplernames
        ancin_ancout_couplername = (min(ancin_name, ancout_name), max(ancin_name, ancout_name))
        ancin_ctlout_couplername = (min(ancin_name, ctlout_name), max(ancin_name, ctlout_name))
        ancout_targ_couplername = (min(ancout_name, targ_name), max(ancout_name, targ_name))
        ancin_out_couplername = (min(ancin_name, out_name), max(ancin_name, out_name))
        ctlin_ctlout_couplername = (min(ctlin_name, ctlout_name), max(ctlin_name, ctlout_name))
        ctlin_out_couplername = (min(ctlin_name, out_name), max(ctlin_name, out_name))
        ctlout_targ_couplername = (min(ctlout_name, targ_name), max(ctlout_name, targ_name))
        targ_out_couplername = (min(targ_name, out_name), max(targ_name, out_name))

        if 'ctlin' not in assignedins:
            self.qubits[ctl]['components'].append(ctlin_name)
            self.qubitbiases[ctlin_name] = ctlin_val
        self.qubits[ctl]['components'].append(ctlout_name)
        self.qubitbiases[ctlout_name] = ctlout_val

        if 'targ' not in assignedins:
            self.qubits[targ]['components'].append(targ_name)
            self.qubitbiases[targ_name] = targ_val
        self.qubits[targ]['components'].append(out_name)
        self.qubitbiases[out_name] = out_val

        self.qubits['annealer_ancillas'].append(ancin_name)
        self.qubits['annealer_ancillas'].append(ancout_name)
        self.qubitbiases[ancin_name] = ancin_val
        self.qubitbiases[ancout_name] = ancout_val

        self.couplerstrengths[ancin_ancout_couplername] = ancin_ancout_couplerval
        self.couplerstrengths[ancin_ctlout_couplername] = ancin_ctlout_couplerval
        self.couplerstrengths[ancout_targ_couplername] = ancout_targ_couplerval
        self.couplerstrengths[ancin_out_couplername] = ancin_out_couplerval
        self.couplerstrengths[ctlin_ctlout_couplername] = ctlin_ctlout_couplerval
        self.couplerstrengths[ctlin_out_couplername] = ctlin_out_couplerval
        self.couplerstrengths[ctlout_targ_couplername] = ctlout_targ_couplerval
        self.couplerstrengths[targ_out_couplername] = targ_out_couplerval

        self.gatenum = self.gatenum + 1
    
    def add_Toffoli(self, ctl1, ctl2, targ):
        while self.gatenum in self.skipgates:
            print("Skip gate {}".format(self.gatenum)) 
            self.gatenum = self.gatenum + 1

        topleft = self.topleftofgatecells[self.gatenum]

        if self.gatenum % 2 == 0:
            # out side left
            outout_name = topleft
            ctl1out_name = 1 + topleft
            ctl2out_name = 2 + topleft
            anc_name = 3 + topleft

            # in side right
            targ_name = 4 + topleft
            ctl1in_name = 5 + topleft
            ctl2in_name = 6 + topleft
            outin_name = 7 + topleft

        else:
            # out side right
            outout_name = 4 + topleft
            ctl1out_name = 5 + topleft
            ctl2out_name = 6 + topleft
            anc_name = 7 + topleft

            # in side left
            targ_name = topleft
            ctl1in_name = 1 + topleft
            ctl2in_name = 2 + topleft
            outin_name = 3 + topleft


        #qubitbiases
        targ_val = 4
        ctl1in_val = 5
        ctl2in_val = 5
        outin_val = 8

        outout_val = 8 
        ctl1out_val = 5
        ctl2out_val = 5 
        anc_val = 9

        #couplerstrengths
        clt1in_ctl1out_couplerval = -10
        ctl2in_ctl2out_couplerval = -10
        outin_outout_couplerval = -13

        anc_targ_couplerval = -9
        anc_ctl1in_couplerval = -4
        anc_ctl2in_couplerval = -5
        anc_outin_couplerval = 9

        outout_targ_couplerval = -7
        outin_ctl1out_couplerval = -2
        outin_ctl2out_couplerval = -2

        targ_ctl1out_couplerval = 2
        targ_ctl2out_couplerval = 2

        ctl1in_ctl2out_couplerval = 1

        self.numgatecouplers = self.numgatecouplers + 13

        assignedins = {}

        if len(self.qubits[targ]['components']) > 0:
            targjoin = self.qubits[targ]['components'][-1]
            targjointopleft = targjoin - targjoin % 8
            targjoincell = self.topleftofgatecells.index(targjointopleft)
            # if coming from last cell
            if self.gatenum - targjoincell == 1:
                #find row
                rowoffset = targjoin % 4 - targ_name % 4

                # change position of row being connected
                # if there were more rows occupied in this 
                # gate the qubits previously in this row
                # would have to be switched with inname and outname

                targ_name = targ_name + rowoffset
                outout_name = outout_name + rowoffset

                for row in [[ctl1in_name, ctl1out_name], [ctl2in_name, ctl2out_name], [outin_name, anc_name]]:
                    if row[0] == targ_name:
                        row[0] = row[0] - rowoffset
                        row[1] = row[1] - rowoffset

                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if targjoincell % 4 == 0:
                    if (self.gatenum-1)%12==0 and (self.gatenum-1)>0:
                        newqubit = targjoin + 128
                    else:
                        newqubit = targjoin - 128

                elif targjoincell % 2 == 0:
                    newqubit = targjoin + 128
                else:
                    if floor((self.gatenum-1)/12) % 2 == 0:
                        newqubit = targjoin + 8
                    else:
                        newqubit = targjoin - 8

                # add new qubit chain with injoin
                self.qubitbiases[targjoin] = self.qubitbiases[targjoin] + 5
                self.qubits[targ]['components'].append(newqubit)
                self.qubitbiases[newqubit] = 10 
                self.couplerstrengths[(min(targjoin, newqubit), max(targjoin, newqubit))] = -10

                # chain inname with newqubit
                targ_val = targ_val + 5

                self.couplerstrengths[(min(newqubit, targ_name), max(newqubit,targ_name))] = -10

                self.qubits[targ]['components'].append(targ_name)
                self.qubitbiases[targ_name] = targ_val
            
                assignedins['targ'] = targ_name

        if len(self.qubits[ctl1]['components']) > 0:
            ctl1injoin = self.qubits[ctl1]['components'][-1]
            ctl1injointopleft = ctl1injoin - ctl1injoin % 8
            ctl1injoincell = self.topleftofgatecells.index(ctl1injointopleft)
            # if coming from last cell
            if self.gatenum - ctl1injoincell == 1:
                #find row
                rowoffset = ctl1injoin % 4 - ctl1in_name % 4

                # change position of row being connected
                # if there were more rows occupied in this
                # gate the qubits previously in this row
                # would have to be switched with inname and outname

                ctl1in_name = ctl1in_name + rowoffset
                ctl1out_name = ctl1out_name + rowoffset

                for row in [[targ_name, outout_name], [ctl2in_name, ctl2out_name], [outin_name, anc_name]]:
                    if row[0] == ctl1in_name:
                        row[0] = row[0] - rowoffset
                        row[1] = row[1] - rowoffset

                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if ctl1injoincell % 4 == 0:
                    if (self.gatenum-1)%12==0 and (self.gatenum-1)>0:
                        newqubit = ctl1injoin + 128
                    else:
                        newqubit = ctl1injoin - 128

                elif ctl1injoincell % 2 == 0:
                    newqubit = ctl1injoin + 128
                else:
                    if floor((self.gatenum-1)/12) % 2 == 0:
                        newqubit = ctl1injoin + 8
                    else:
                        newqubit = ctl1injoin - 8

                # add new qubit chain with injoin
                self.qubitbiases[ctl1injoin] = self.qubitbiases[ctl1injoin] + 5
                self.qubits[ctl1]['components'].append(newqubit)
                self.qubitbiases[newqubit] = 10 
                self.couplerstrengths[(min(ctl1injoin, newqubit), max(ctl1injoin, newqubit))] = -10

                # chain inname with newqubit
                ctl1in_val = ctl1in_val + 5

                self.couplerstrengths[(min(newqubit, ctl1in_name), max(newqubit, ctl1in_name))] = -10

                self.qubits[ctl1]['components'].append(ctl1in_name)
                self.qubitbiases[ctl1in_name] = ctl1in_val
                
                assignedins['ctl1in'] = ctl1in_name

        if len(self.qubits[ctl2]['components']) > 0:
            ctl2injoin = self.qubits[ctl2]['components'][-1]
            ctl2injointopleft = ctl2injoin - ctl2injoin % 8
            ctl2injoincell = self.topleftofgatecells.index(ctl2injointopleft)
            # if coming from last cell
            if self.gatenum - ctl2injoincell == 1:
                #find row
                rowoffset = ctl2injoin % 4 - ctl2in_name % 4

                # change position of row being connected
                # if there were more rows occupied in this
                # gate the qubits previously in this row
                # would have to be switched with inname and outname

                ctl2in_name = ctl2in_name + rowoffset
                ctl2out_name = ctl2out_name + rowoffset

                for row in [[targ_name, outout_name], [ctl1in_name, ctl1out_name], [outin_name, anc_name]]:
                    if row[0] == ctl1in_name:
                        row[0] = row[0] - rowoffset
                        row[1] = row[1] - rowoffset

                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if ctl2injoincell % 4 == 0:
                    if (self.gatenum-1)%12==0 and (self.gatenum-1)>0:
                        newqubit = ctl2injoin + 128
                    else:
                        newqubit = ctl2injoin - 128
                elif ctl2injoincell % 2 == 0:
                    newqubit = ctl2injoin + 128
                else:
                    if floor((self.gatenum-1)/12) % 2 == 0:
                        newqubit = ctl2injoin + 8
                    else:
                        newqubit = ctl2injoin - 8

                # add new qubit chain with injoin
                self.qubitbiases[ctl2injoin] = self.qubitbiases[ctl2injoin] + 5
                self.qubits[ctl2]['components'].append(newqubit)
                self.qubitbiases[newqubit] = 10
                self.couplerstrengths[(min(ctl2injoin, newqubit), max(ctl2injoin, newqubit))] = -10

                # chain inname with newqubit
                ctl2in_val = ctl2in_val + 5

                self.couplerstrengths[(min(newqubit, ctl2in_name), max(newqubit, ctl2in_name))] = -10

                self.qubits[ctl2]['components'].append(ctl2in_name)
                self.qubitbiases[ctl2in_name] = ctl2in_val

                assignedins['ctl2in'] = ctl2in_name

        if len(self.qubits[targ]['components']) > 0:
            if self.gatenum - targjoincell > 1:
                targjoin = self.qubits[targ]['components'][-1]
                targ_name, outout_name, targ_val, outout_val = self.make_chain(targ_name, outout_name, targ_val, outout_val, targjoin, targ)
                self.qubits[targ]['components'].append(targ_name)
                self.qubitbiases[targ_name] = targ_val
                assignedins['targ'] = targ_name

        if len(self.qubits[ctl1]['components']) > 0:
            if self.gatenum - ctl1injoincell > 1:
                ctl1injoin = self.qubits[ctl1]['components'][-1]
                ctl1in_name, ctl1out_name, ctl1in_val, ctl1out_val = self.make_chain(ctl1in_name, ctl1out_name, ctl1in_val, ctl1out_val, ctl1injoin, ctl1)
                self.qubits[ctl1]['components'].append(ctl1in_name)
                self.qubitbiases[ctl1in_name] = ctl1in_val
                assignedins['ctl1in'] = ctl1in_name

        if len(self.qubits[ctl2]['components']) > 0:
            if self.gatenum - ctl2injoincell > 1:
                ctl2injoin = self.qubits[ctl2]['components'][-1]
                ctl2in_name, ctl2out_name, ctl2in_val, ctl2out_val = self.make_chain(ctl2in_name, ctl2out_name, ctl2in_val, ctl2out_val, ctl2injoin, ctl2)
                self.qubits[ctl2]['components'].append(ctl2in_name)
                self.qubitbiases[ctl2in_name] = ctl2in_val
                assignedins['ctl2in'] = ctl2in_name    
        
        availablerows = [0,1,2,3]

        for key in assignedins.keys():
            availablerows.pop(availablerows.index(assignedins[key]%4))
    
        if 'outin' not in assignedins:
            if outin_name % 4 not in availablerows:
                rowoffset = availablerows[0] - outin_name % 4
                outin_name = outin_name + rowoffset
                anc_name = anc_name + rowoffset
                availablerows.pop(availablerows.index(outin_name%4))
            else:
                availablerows.pop(availablerows.index(outin_name%4))
         
        if 'ctl1in' not in assignedins:
            if ctl1in_name % 4 not in availablerows:
                rowoffset = availablerows[0] - ctl1in_name % 4
                ctl1in_name = ctl1in_name + rowoffset
                ctl1out_name = ctl1out_name + rowoffset
                availablerows.pop(availablerows.index(ctl1in_name%4))
            else:
                availablerows.pop(availablerows.index(ctl1in_name%4))
        
        if 'ctl2in' not in assignedins:
            if ctl2in_name %4 not in availablerows:
                rowoffset = availablerows[0] - ctl2in_name % 4
                ctl2in_name = ctl2in_name + rowoffset
                ctl2out_name = ctl2out_name + rowoffset
                availablerows.pop(availablerows.index(ctl2in_name%4))
            else:
                availablerows.pop(availablerows.index(ctl2in_name%4))
        if 'targ' not in assignedins:
            if targ_name %4 not in availablerows:
                rowoffset = availablerows[0] - targ_name % 4
                targ_name = targ_name + rowoffset
                outout_name = outout_name + rowoffset
                availablerows.pop(availablerows.index(targ_name%4))
            else:
                availablerows.pop(availablerows.index(targ_name%4))

        # coupler names
        clt1in_ctl1out_couplername = (min(ctl1in_name, ctl1out_name), max(ctl1in_name, ctl1out_name))
        ctl2in_ctl2out_couplername = (min(ctl2in_name, ctl2out_name), max(ctl2in_name, ctl2out_name))
        outin_outout_couplername = (min(outin_name, outout_name), max(outin_name, outout_name))
        anc_targ_couplername = (min(anc_name, targ_name), max(anc_name, targ_name))
        anc_ctl1in_couplername = (min(anc_name, ctl1in_name), max(anc_name, ctl1in_name))
        anc_ctl2in_couplername = (min(anc_name, ctl2in_name), max(anc_name, ctl2in_name))
        anc_outin_couplername = (min(anc_name, outin_name), max(anc_name, outin_name))
        outout_targ_couplername = (min(outout_name, targ_name), max(outout_name, targ_name))
        outin_ctl1out_couplername = (min(outin_name, ctl1out_name), max(outin_name, ctl1out_name))
        outin_ctl2out_couplername = (min(outin_name, ctl2out_name), max(outin_name, ctl2out_name))
        targ_ctl1out_couplername = (min(targ_name, ctl1out_name), max(targ_name, ctl1out_name))
        targ_ctl2out_couplername = (min(targ_name, ctl2out_name), max(targ_name, ctl2out_name))
        ctl1in_ctl2out_couplername = (min(ctl1in_name, ctl2out_name), max(ctl1in_name, ctl2out_name))

        if 'ctl1in' not in assignedins:
            self.qubits[ctl1]['components'].append(ctl1in_name)
            self.qubitbiases[ctl1in_name] = ctl1in_val
        self.qubits[ctl1]['components'].append(ctl1out_name)
        self.qubitbiases[ctl1in_name] = ctl1in_val
        self.qubitbiases[ctl1out_name] = ctl1out_val
        
        if 'ctl2in' not in assignedins:
            self.qubits[ctl2]['components'].append(ctl2in_name)
            self.qubitbiases[ctl2in_name] = ctl2in_val
        self.qubits[ctl2]['components'].append(ctl2out_name)
        self.qubitbiases[ctl2out_name] = ctl2out_val
        
        if 'targ' not in assignedins:
            self.qubits[targ]['components'].append(targ_name)
            self.qubitbiases[targ_name] = targ_val
        self.qubits[targ]['components'].append(outin_name)
        self.qubits[targ]['components'].append(outout_name)
        self.qubitbiases[outin_name] = outin_val
        self.qubitbiases[outout_name] = outout_val

        self.qubits['annealer_ancillas'].append(anc_name)
        self.qubitbiases[anc_name] = anc_val

        self.couplerstrengths[clt1in_ctl1out_couplername] = clt1in_ctl1out_couplerval
        self.couplerstrengths[ctl2in_ctl2out_couplername] = ctl2in_ctl2out_couplerval
        self.couplerstrengths[outin_outout_couplername] = outin_outout_couplerval
        self.couplerstrengths[anc_targ_couplername] = anc_targ_couplerval
        self.couplerstrengths[anc_ctl1in_couplername] = anc_ctl1in_couplerval
        self.couplerstrengths[anc_ctl2in_couplername] = anc_ctl2in_couplerval
        self.couplerstrengths[anc_outin_couplername] = anc_outin_couplerval
        self.couplerstrengths[outout_targ_couplername] = outout_targ_couplerval
        self.couplerstrengths[outin_ctl1out_couplername] = outin_ctl1out_couplerval
        self.couplerstrengths[outin_ctl2out_couplername] = outin_ctl2out_couplerval
        self.couplerstrengths[targ_ctl1out_couplername] = targ_ctl1out_couplerval
        self.couplerstrengths[targ_ctl2out_couplername] = targ_ctl2out_couplerval
        self.couplerstrengths[ctl1in_ctl2out_couplername] = ctl1in_ctl2out_couplerval

        self.gatenum = self.gatenum + 1
    
    def add_swap(self, targ1, targ2):        
        while self.gatenum in self.skipgates:
            print("Skip gate {}".format(self.gatenum))
            self.gatenum = self.gatenum + 1

        topleft = self.topleftofgatecells[self.gatenum]

        if self.gatenum % 2 == 0:
            # out side left
            out1_name = topleft
            out2_name = 1 + topleft

            # in side right
            targ1_name = 4 + topleft
            targ2_name = 5 + topleft

        else:
            # out side right
            out1_name = 4 + topleft
            out2_name = 5 + topleft

            # in side left
            targ1_name = topleft
            targ2_name = 1 + topleft


        targ1_val = 2
        targ2_val = 2
        out1_val = 2
        out2_val = 2

        targ1_out2_couplerval = -4
        targ2_out1_couplerval = -4

        self.numgatecouplers = self.numgatecouplers + 2

        assignedins = {}

        if len(self.qubits[targ1]['components']) > 0:
            targ1join = self.qubits[targ1]['components'][-1]
            targ1jointopleft = targ1join - targ1join % 8
            targ1joincell = self.topleftofgatecells.index(targ1jointopleft)
            # if coming from last cell
            if self.gatenum - targ1joincell == 1:
                #find row
                rowoffset = targ1join % 4 - targ1_name % 4

                # change position of row being connected
                # if there were more rows occupied in this 
                # gate the qubits previously in this row
                # would have to be switched with inname and outname

                targ1_name = targ1_name + rowoffset
                out1_name = out1_name + rowoffset

                for row in [[targ2_name, out2_name]]:
                    if row[0] == targ1_name:
                        row[0] = row[0] - rowoffset
                        row[1] = row[1] - rowoffset

                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if targ1joincell % 4 == 0:
                    if (self.gatenum-1)%12==0 and (self.gatenum-1)>0:
                        newqubit = targ1join + 128
                    else:
                        newqubit = targ1join - 128

                elif targ1joincell % 2 == 0:
                    newqubit = targ1join + 128
                else:
                    if floor((self.gatenum-1)/12) % 2 == 0:
                        newqubit = targ1join + 8
                    else:
                        newqubit = targ1join - 8

                # add new qubit chain with injoin
                self.qubitbiases[targ1join] = self.qubitbiases[targ1join] + 5
                self.qubits[targ1]['components'].append(newqubit)
                self.qubitbiases[newqubit] = 10
                self.couplerstrengths[(min(targ1join, newqubit), max(targ1join, newqubit))] = -10

                # chain inname with newqubit
                targ1_val = targ1_val + 5

                self.couplerstrengths[(min(newqubit, targ1_name), max(newqubit,targ1_name))] = -10

                self.qubits[targ1]['components'].append(targ1_name)
                self.qubitbiases[targ1_name] = targ1_val

                assignedins['targ1'] = targ1_name

        if len(self.qubits[targ2]['components']) > 0:
            targ2join = self.qubits[targ2]['components'][-1]
            targ2jointopleft = targ2join - targ2join % 8
            targ2joincell = self.topleftofgatecells.index(targ2jointopleft)
            # if coming from last cell
            if self.gatenum - targ2joincell == 1:
                #find row
                rowoffset = targ2join % 4 - targ2_name % 4

                # change position of row being connected
                # if there were more rows occupied in this
                # gate the qubits previously in this row
                # would have to be switched with inname and outname

                targ2_name = targ2_name + rowoffset
                out2_name = out2_name + rowoffset

                for row in [[targ1_name, out1_name]]:
                    if row[0] == targ2_name:
                        row[0] = row[0] - rowoffset
                        row[1] = row[1] - rowoffset

                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if targ2joincell % 4 == 0:
                    if (self.gatenum-1)%12==0 and (self.gatenum-1)>0:
                        newqubit = targ2join + 128
                    else:
                        newqubit = targ2join - 128

                elif targ2joincell % 2 == 0:
                    newqubit = targ2join + 128
                else:
                    if floor((self.gatenum-1)/12) % 2 == 0:
                        newqubit = targ2join + 8
                    else:
                        newqubit = targ2join - 8

                # add new qubit chain with injoin
                self.qubitbiases[targ2join] = self.qubitbiases[targ2join] + 5
                self.qubits[targ2]['components'].append(newqubit)
                self.qubitbiases[newqubit] = 10
                self.couplerstrengths[(min(targ2join, newqubit), max(targ2join, newqubit))] = -10

                # chain inname with newqubit
                targ2_val = targ2_val + 5

                self.couplerstrengths[(min(newqubit, targ2_name), max(newqubit,targ2_name))] = -10

                self.qubits[targ2]['components'].append(targ2_name)
                self.qubitbiases[targ2_name] = targ2_val

                assignedins['targ2'] = targ2_name

        if len(self.qubits[targ1]['components']) > 0:
            if self.gatenum - targ1joincell > 1:
                targ1join = self.qubits[targ1]['components'][-1]
                targ1_name, out1_name, targ1_val, out1_val = self.make_chain(targ1_name, out1_name, targ1_val, out1_val, targ1join, targ1)
                self.qubits[targ1]['components'].append(targ1_name)
                self.qubitbiases[targ1_name] = targ1_val
                assignedins['targ1'] = targ1_name

        if len(self.qubits[targ2]['components']) > 0:
            if self.gatenum - targ2joincell > 1:
                targ2join = self.qubits[targ2]['components'][-1]
                targ2_name, out2_name, targ2_val, out2_val = self.make_chain(targ2_name, out2_name, targ2_val, out2_val, targ2join, targ2)
                self.qubits[targ2]['components'].append(targ2_name)
                self.qubitbiases[targ2_name] = targ2_val
                assignedins['targ2'] = targ2_name

        availablerows = [0,1,2,3]

        for key in assignedins.keys():
            availablerows.pop(availablerows.index(assignedins[key]%4))
    
        if 'targ1' not in assignedins:
            if targ1_name % 4 not in availablerows:
                rowoffset = availablerows[0] - targ1_name
                targ1_name = targ1_name + rowoffset
                out1_name = out1_name + rowoffset
                availablerows.pop(availablerows.index(targ1_name%4))
            else:
                availablerows.pop(availablerows.index(targ1_name%4))

        if 'targ2' not in assignedins:
            if targ2_name % 4 not in availablerows:
                rowoffset = availablerows[0] - targ2_name
                targ2_name = targ2_name + rowoffset
                out2_name = out2_name + rowoffset
                availablerows.pop(availablerows.index(targ2_name%4))
            else:
                availablerows.pop(availablerows.index(targ2_name%4))
        
        # coupler names
        targ1_out2_couplername = (min(targ1_name, out2_name), max(targ1_name, out2_name))
        targ2_out1_couplername = (min(targ2_name, out1_name), max(targ2_name, out1_name))

        if 'targ1' not in assignedins:
            self.qubits[targ1]['components'].append(targ1_name)
            self.qubitbiases[targ1_name] = targ1_val
        self.qubits[targ1]['components'].append(out1_name)
        self.qubitbiases[out1_name] = out1_val

        if 'targ2' not in assignedins:
            self.qubits[targ2]['components'].append(targ2_name)
            self.qubitbiases[targ2_name] = targ2_val
        self.qubits[targ2]['components'].append(out2_name)
        self.qubitbiases[out2_name] = out2_val

        self.couplerstrengths[targ1_out2_couplername] = targ1_out2_couplerval 
        self.couplerstrengths[targ2_out1_couplername] = targ2_out1_couplerval

        self.gatenum = self.gatenum + 1

    def add_Fredkin(self, ctl, targ1, targ2):
        self.add_CNOT(targ1,targ2)
        self.add_Toffoli(ctl,targ2,targ1)
        self.add_CNOT(targ1,targ2)

    def join(self, q1, q2, circ_qubit):
        if q1 not in self.qubitbiases:
            self.qubits[circ_qubit]['components'].append(q1)
            self.qubitbiases[q1] = 5 
        else:
            self.qubitbiases[q1] = self.qubitbiases[q1] + 5
        if q2 not in self.qubitbiases:
            self.qubits[circ_qubit]['components'].append(q2)
            self.qubitbiases[q2] = 5      
        else:
            self.qubitbiases[q2] = self.qubitbiases[q2] + 5
            
        self.couplerstrengths[(min(q1, q2), max(q1, q2))] = -10
        
    def check_and_get_row_offset(self, checkqubit, dependency = None, otherdependency = None):
        checkqubit = int(checkqubit)
        row = checkqubit % 4
        if dependency is None and otherdependency is None:
            if checkqubit in self.qubitbiases or checkqubit in self.dontuse:
                found = False
                first = checkqubit-row
                for i in range(4):
                    if first + i not in self.qubitbiases and first + i not in self.dontuse:
                        found = True
                        row = i
                if found == False:
                    print('/nGate {}. Failed to make connection: {}/n'.format(self.gatenum, checkqubit))
                    self.print_chimera_graph_to_file()
                    input()

        elif dependency is not None and otherdependency is None:
            deprow = dependency % 4
            if checkqubit in self.qubitbiases or checkqubit in self.dontuse or dependency in self.qubitbiases or dependency in self.dontuse:
                found = False
                first = checkqubit-row
                depfirst = dependency-deprow
                for i in range(4):
                    if first + i not in self.qubitbiases and depfirst + i not in self.qubitbiases \
                            and first + i not in self.dontuse and depfirst + i not in self.dontuse:
                        found = True
                        row = i
                if found == False:
                    print('/nGate {}. Failed to make connection: {}, {}/n'.format(self.gatenum, checkqubit, dependency))
                    self.print_chimera_graph_to_file()
                    input()
        else:
            deprow = dependency % 4
            odeprow = otherdependency % 4
            if checkqubit in self.qubitbiases or checkqubit in self.dontuse or dependency in self.qubitbiases or dependency in self.dontuse or otherdependency in self.qubitbiases or otherdependency in self.dontuse:
                found = False
                first = checkqubit-row
                depfirst = dependency - deprow
                odepfirst = otherdependency - odeprow
                for i in range(4):
                    if first + i not in self.qubitbiases and depfirst+i not in self.qubitbiases and odepfirst+i not in self.qubitbiases \
                            and first + i not in self.dontuse and depfirst+i not in self.dontuse and odepfirst+i not in self.dontuse:
                        found = True
                        row = i
                if found == False:
                    print('/nGate {}. Failed to make connection: {}, {}, {}/n'.format(self.gatenum, checkqubit, dependency, otherdependency))
                    self.print_chimera_graph_to_file()
                    input()

        rowoffset = row - checkqubit % 4
    
        return int(rowoffset)

    def make_chain(self, inname, outname, inval, outval, lastinstance, circ_qubit):
        topleft = self.topleftofgatecells[self.gatenum]
        lastinstancetopleft = lastinstance - lastinstance % 8
        lastinstancecell = self.topleftofgatecells.index(lastinstancetopleft)
         
        if lastinstancecell % 4 == 0:
            if (lastinstancecell)%12==0 and (lastinstancecell)>0:
                newqubit = lastinstance - 128
            else:
                newqubit = lastinstance + 128
        elif lastinstancecell % 2 == 0:
            newqubit = lastinstance - 128
        else:
            if floor((lastinstancecell)/12) % 2 == 0:
                newqubit = lastinstance - 8
            else:
                newqubit = lastinstance + 8

        newqubittopleft = newqubit - newqubit % 8
        horizontaldist = floor(topleft/8)%16 - floor(newqubittopleft/8)%16
        if horizontaldist == 0:
            horizontaldist = -2 # this just makes it work right for this case
        verticaldist = floor(topleft/128) - floor(newqubittopleft/128)

        # join with newqubit
        self.join(lastinstance, newqubit, circ_qubit)

        # if exiting on horizontally connected couplers
        # do certain things
        if lastinstancecell % 2 == 1:
            # if cell number is 3, 7, 11 etc. move down
            if lastinstancecell % 4 == 3:
                # see if ideal move is good if not find move
                offset = self.check_and_get_row_offset(newqubit-4, dependency = newqubit-4-128)
                
                #position to move vertically
                newqubit = newqubit - 4 + offset
                #connect
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
                # move up once
                newqubit = newqubit + 128
                # connect
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

            # if cell number is 1, 5, 9 etc. move up
            else:
                # see if ideal move is good if not find move
                offset = self.check_and_get_row_offset(newqubit-4, dependency = newqubit-4+128)
                #position to move vertically
                newqubit = newqubit - 4 + offset
                #connect
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
                
                # move down once
                newqubit = newqubit - 128
                # connect
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

        # see if ideal move is good if not find move
        offset = self.check_and_get_row_offset(newqubit+4, dependency = newqubit+4 + int(8*copysign(1, horizontaldist)))
        
        # position to move horizontally
        newqubit = newqubit + 4 + offset
        # connect
        self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

        # move horizontally toward new gate
        if floor(self.gatenum/12)%2==0:
            horizontaladjust = -1*int(copysign(1,horizontaldist))
        else:
            horizontaladjust = 1*int(copysign(1,horizontaldist))
        
        for i in range(abs(horizontaldist)+horizontaladjust):

            offset = self.check_and_get_row_offset(newqubit + int(8*copysign(1, horizontaldist)))
            if offset != 0:
                # find a row that will work and change to it
                offset = self.check_and_get_row_offset(newqubit, dependency = newqubit-4, otherdependency = newqubit + int(8*copysign(1, horizontaldist)))
                newqubit = newqubit - 4 + offset
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
                newqubit = newqubit + 4
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
            newqubit = newqubit + int(8*copysign(1, horizontaldist))
            # connect 
            self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

        # position to move vertically
        offset = self.check_and_get_row_offset(newqubit-4, dependency = newqubit - 4 + int(128*copysign(1, verticaldist)))
        newqubit = newqubit - 4 + offset
        # connect
        self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

        #recalculate vertical distance to simplify things
        newqubittopleft = newqubit - newqubit % 8
        verticaldist = floor(topleft/128) - floor(newqubittopleft/128)
    
        # move vertically to input assembly cell
        # if destination even, move verticaldist (THIS IS STILL TRUE)
        if self.gatenum % 2 == 0:
            for i in range(abs(verticaldist)):
                offset = self.check_and_get_row_offset(newqubit + int(128*copysign(1, verticaldist)))
                if offset != 0:
                    #find a row that works and change to it
                    offset = self.check_and_get_row_offset(newqubit, dependency = newqubit+4, otherdependency = newqubit + int(128*copysign(1, verticaldist)))
                    newqubit = newqubit + 4 + offset
                    self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
                    newqubit = newqubit - 4
                    self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
                newqubit = newqubit + int(128*copysign(1, verticaldist))
            
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
            
            # check if row available in gate cell and move there
            if floor(self.gatenum/12)%2==0:
                checkswitch = 8
            else:
                checkswitch = -8
            offset = self.check_and_get_row_offset(newqubit + 4, dependency = newqubit + 4 + checkswitch)
            newqubit = newqubit + 4 + offset
            self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
        
            # place inname and outname according to newqubit row
            rowoffset = newqubit % 4 - inname % 4
            
            inname = inname + rowoffset
            outname = outname + rowoffset

            # connect newqubit and inname
            self.qubitbiases[newqubit] = self.qubitbiases[newqubit] + 5
            inval = inval + 5
            self.couplerstrengths[(min(inname, newqubit), max(inname, newqubit))] =-10
            
        # if destination odd 
        else:
            # one more if input cell above gate
            # one less if input cell below gate
            # these numbers dont say that but they do it
            # im tired
            #print(verticaldist, abs(verticaldist)%6) 
            if abs(verticaldist)%4 == 1 or (abs(verticaldist)%6==1 and lastinstancecell%12==0 and lastinstancecell!=0):
                adjust = 1
            else: 
                adjust = -1

            if floor((self.gatenum-1)%12)==0 and self.gatenum>1:
                adjust = -adjust

            for i in range(abs(verticaldist)+int(adjust)):
                offset = self.check_and_get_row_offset(newqubit + 128*copysign(1, verticaldist))
                if offset != 0:
                    #find a row that works and change to it
                    offset = self.check_and_get_row_offset(newqubit, dependency = newqubit+4, otherdependency = newqubit + int(128*copysign(1,verticaldist)))
                    newqubit = newqubit + 4 + offset
                    self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
                    newqubit = newqubit - 4
                    self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)        
                newqubit = newqubit + int(128*copysign(1, verticaldist))
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

            # position to move horizontally
            offset = self.check_and_get_row_offset(newqubit+4)
            newqubit = newqubit + 4 + offset
            # connect
            self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

            # move horizontally into input assembly cell
            if floor(self.gatenum/12)%2==0:
                offset = self.check_and_get_row_offset(newqubit+8)
                newqubit = newqubit + 8 + offset
            else:
                offset = self.check_and_get_row_offset(newqubit-8)
                newqubit = newqubit - 8 + offset
            # connect
            self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
            
            if (self.gatenum-1)%12==0 and self.gatenum>1:
                changesign=-1
            else:
                changesign=1

            if self.gatenum % 4 == 3:
                offset = self.check_and_get_row_offset(newqubit - 4, dependency = newqubit - 4 + changesign*128)
                newqubit = newqubit - 4 + offset
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
            else:
                offset = self.check_and_get_row_offset(newqubit - 4, dependency = newqubit - 4 - changesign*128)
                newqubit = newqubit - 4 + offset
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
 
            # place inname and outname according to newqubit row
            rowoffset = newqubit % 4 - inname % 4
            inname = inname + rowoffset
            outname = outname + rowoffset

            # connect newqubit and inname
            self.qubitbiases[newqubit] = self.qubitbiases[newqubit] + 5
            inval = inval + 5
            self.couplerstrengths[(min(inname, newqubit), max(inname, newqubit))] = -10               
            
        return inname, outname, inval, outval

    def print_chimera_graph_to_file(self):
        filename = 'chimera_graph.txt'
        f = open(filename, 'w')

        for graphrow in range(16):
            if graphrow != 0:
                f.write("\n\n\n")
            for cellrow in range(4):
                if cellrow != 0:
                    f.write("\n")
                for graphcolumn in range(16):
                    if graphcolumn != 0:
                        f.write("   ")
                    for cellcolumn in range(2):
                        if cellcolumn*4+cellrow+graphcolumn*8+graphrow*128 not in self.qubitbiases.keys():
                            f.write('-')
                        else:
                            f.write('X')
                        f.write("   ")
        f.close()
