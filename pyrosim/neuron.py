import math
import numpy
import pybullet

import pyrosim.pyrosim as pyrosim

import pyrosim.constants as c

class NEURON: 

    def __init__(self,line):

        self.Determine_Name(line)

        self.Determine_Type(line)

        self.Search_For_Link_Name(line)

        self.Search_For_Joint_Name(line)

        self.Set_Value(0.0, 0.0)

    def Add_To_Value( self, value ):

        self.Set_Value( self.Get_Value() + value, self.Get_Value())

    def Get_Joint_Name(self):

        return self.jointName

    def Get_Link_Name(self):

        return self.linkName

    def Get_Name(self):

        return self.name

    def Get_Value(self):

        return self.value

    def Get_Prev_Value(self):
        return self.prev_value

    def Is_Sensor_Neuron(self):

        return self.type == c.SENSOR_NEURON

    def Is_Hidden_Neuron(self):

        return self.type == c.HIDDEN_NEURON

    def Is_Motor_Neuron(self):

        return self.type == c.MOTOR_NEURON

    # def Get_Type(self):
    #     return self.type


    def Print(self):

        # self.Print_Name()

        # self.Print_Type()

        self.Print_Value()

        # print("")

    def Set_Value(self,value, prev_value):
        self.value = value
        self.prev_value = prev_value


    def Update_Sensor_Neuron(self):
        self.Set_Value(pyrosim.Get_Touch_Sensor_Value_For_Link(self.Get_Link_Name()), self.Get_Value())


#Pay attention here for adding recurrent connections
    def Update_Hidden_Or_Motor_Neuron(self, neurons, synapses):
        self.Set_Value(0, self.Get_Value())
        #print("before: " + str(self.Get_Value()))
        for s_key in synapses:
            if neurons[s_key[0]].Is_Hidden_Neuron() and neurons[s_key[1]].Is_Hidden_Neuron():
                # print("J")
                # print(s_key)
                self.Allow_Presynaptic_Neuron_To_Influence_Me(synapses[s_key].Get_Weight(), neurons[s_key[0]].Get_Prev_Value())
            elif s_key[1] == self.Get_Name():
                # print("K")
                # print(s_key)
                self.Allow_Presynaptic_Neuron_To_Influence_Me(synapses[s_key].Get_Weight(), neurons[s_key[0]].Get_Value())
                                                              #pre synaptic weight           value of pre neuron

        self.Threshold()

        #print("after: " + str(self.Get_Value()))

    def Allow_Presynaptic_Neuron_To_Influence_Me(self, synaptic_weight, neuron_value ):
        value = synaptic_weight * neuron_value
        self.Add_To_Value(value)
# -------------------------- Private methods -------------------------

    def Determine_Name(self,line):

        if "name" in line:

            splitLine = line.split('"')

            self.name = splitLine[1]

    def Determine_Type(self,line):

        if "sensor" in line:

            self.type = c.SENSOR_NEURON

        elif "motor" in line:

            self.type = c.MOTOR_NEURON

        else:

            self.type = c.HIDDEN_NEURON

    def Print_Name(self):

       print(self.name)

    def Print_Type(self):

       print(self.type)




    def Print_Value(self):

       print(self.value , " " , end="" )

    def Search_For_Joint_Name(self,line):

        if "jointName" in line:

            splitLine = line.split('"')

            self.jointName = splitLine[5]

    def Search_For_Link_Name(self,line):

        if "linkName" in line:

            splitLine = line.split('"')

            self.linkName = splitLine[5]

    def Threshold(self):

        self.value = math.tanh(self.value)
