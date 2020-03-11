
class _PolyTermNode(object):
    #degree,coeff,next

    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None


class Polynomial:


    def __init__(self, degree=None, coefficient=None):
       #creating new polynobial
        if degree is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead

    def degree(self):

        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.degree



    def __add__(self, rhsPoly):



        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                coefficient = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                coefficient = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree  # or degree = nodeB.degree
                coefficient = nodeA.coefficient + nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next

            newPoly._appendTerm(degree, coefficient)

        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newPoly


    def _appendTerm(self, degree, coefficient):

        if coefficient != 0.0:
            newTerm = _PolyTermNode(degree, coefficient)
            if self._polyHead is None:
                self._polyHead = newTerm
            else:
                self._polyTail.next = newTerm

            self._polyTail = newTerm

    def printPoly(self):

        curNode = self._polyHead
        while curNode is not None:
            if curNode.next is not None:
                # string format based on the dictionary.
                print("%(coefficient)sx^%(degree)s + " % {"coefficient": curNode.coefficient, "degree": curNode.degree})
            else:
                print("%(coefficient)sx^%(degree)s" % {"coefficient": curNode.coefficient,"degree": curNode.degree})

            curNode = curNode.next

if __name__ == "__main__":
    #(degree,coef)
    leftPoly = Polynomial(2, 5)
    leftPoly += Polynomial(1, 3)
    leftPoly += Polynomial(0, -10)
    print("1st Polynomial= ")
    leftPoly.printPoly()

    rightPoly = Polynomial(3, 2)
    rightPoly += Polynomial(2, 4)
    rightPoly += Polynomial(0, 3)
    print("2nd Polynomial= ")
    rightPoly.printPoly()

    addPoly = leftPoly + rightPoly


    print("The addition of the two polynomials is:")
    addPoly.printPoly()


