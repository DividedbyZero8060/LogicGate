#subject to further edit
#Implementation of logic gate. Tweak the driver code to get necessary results
#assignment of runestone academy's python dsa course

class LogicGate:
    """ This class acts as the pathway to output. Output is stored in the output variable.
     Name variable is for convenience. Mother/super class for all"""
    def __init__(self,n):
        self.name = n
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    """ Super class for logic gates with dual input, e.g- And,OR, NAND, NOR,XOR,XNOR gates.
    setnextpin instance method is for complex circuits"""
    def __init__(self,n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    """ Inherits BinaryGate class. It is expected that user use this gate for dual input case
    Basic logic gate which multiplies"""
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    """Inherits BinaryGate class. Works with 2 inputs
    Basic logic gate which adds"""
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):
    """Mother class for classes that work with one inputs like NOT, NOR gate
    setnextpin class is for complex circuits"""
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):
    """Inherits UnaryGate class. Works with one input
    Basic logic gate which reverses a input"""
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

class NandGate(BinaryGate):
    """Inherits BinaryGate class, works with one input
    Universal logic gate, works with two inputs"""
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a==1 and b==1:
            return 0
        else:
            return 1

class NorGate(OrGate):
    """Inherits OrGate for convenience. Grandchild of BinaryGate class
    Universal logic gate, works with two inputs"""

    def performGateLogic(self):

        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

class XORGate(BinaryGate):
    """Inherits BinaryGate class, works with two input
    Exclusive logic gate, works with two inputs. Important for Half adder and Full adder circuits"""
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == b:
            return 0
        else:
            return 1

class XNORGate(XORGate):
    """Inherits XORGate for calculations convenience. Grandchild of BinaryGate class
    Exclusive logic gate, work with two inputs"""
    def performGateLogic(self):

        if super().performGateLogic() == 0:
            return 1
        else:
            return 0

class Half_Adder(BinaryGate):
    """Basic arithmatic circuit. Works with XOR gate
    Works with two input, hence why it inherits BinaryGate class
    getoutput instance method is modified because we have to show the carry out value too"""
    def __init__(self,n):
        BinaryGate.__init__(self,n)
        self.carry = 0
        self.a = 0
        self.b = 0
    def performGateLogic(self):


        self.a = self.getPinA()
        self.b = self.getPinB()

        if self.a == self.b:
            if self.a==1:
                self.carry = 1
            return 0
        else:
            return 1

    def getOutput(self):

        self.output = self.performGateLogic()

        return (f'Output: {self.output} and Carry Value: {self.carry}'.format(self.output,self.carry))

class Full_Adder(Half_Adder):
    """8-bit full adder circuit implemantation. Inherits Half_Adder class because two half
    adder circuits creates a full adder circuit. Works with two input
    """
    def __init__(self,n):

        BinaryGate.__init__(self,n)
        self.carry2 = 0

    def performGateLogic(self):

        initial_value = super().performGateLogic()
        self.carry = int(input("Enter Carry in value: "))
        self.carry2 = self.carry_calculation(initial_value)


        if initial_value == self.carry:
            return 0
        else:
            return 1

    def carry_calculation(self,x):

        temp = 0  # upper AND Gate
        temp1 = 0  # Lower AND Gate

        if self.a == 1 and self.b == 1:
            return 1
        else:
            if x == 1 and self.carry == 1:
                return 1
            return 0

    def getOutput(self):

        self.output = self.performGateLogic()
        return (f'Output: {self.output} and Carry Value: {self.carry}'.format(self.output, self.carry2))












class Connector:
    """Class that enables connection for complex circuits.
    takes two object of different class as input
    Works with setnextpin instance method of each class to stack the answers"""
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():

   #NOT((A AND B) OR (C AND D)) driver code
   # g1 = AndGate("G1")
   # g2 = AndGate("G2")
   # g3 = OrGate("G3")
   # g4 = NotGate("G4")
   # c1 = Connector(g1,g3)
   # c2 = Connector(g2,g3)
   # c3 = Connector(g3,g4)

   #NOT(A AND B) AND NOT(C AND D) driver code
   # g1 = NandGate("A")
   # g2 = NandGate("B")
   # g3 = AndGate("C")
   # c1 = Connector(g1,g3)
   # c2 = Connector(g2,g3)
   # print(g3.getOutput())

   a1 = Full_Adder("test")
   print(a1.getOutput()) #1 1 1 should result in 1 in value and 1 in carryOut

main()