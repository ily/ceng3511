from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model
import sys

file = open(sys.argv[1], "r")
output = open(sys.argv[2], "w+")
input = file.readlines()
line1 = input[0].strip('\n').split(", ")
line2 = input[1].strip('\n').split(", ")
line3 = input[2].strip('\n').split(", ")
line4 = input[3].strip('\n').split(", ")
line5 = input[4].strip('\n').split(", ")
line6 = input[5].strip('\n').split(", ")


def SimpleSatProgram():
    """Minimal CP-SAT example to showcase calling the solver."""
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    num_vals = 4
    A1 = model.NewIntVar(1, num_vals, 'a1')
    A2 = model.NewIntVar(1, num_vals, 'a2')
    A3 = model.NewIntVar(1, num_vals, 'a3')
    A4 = model.NewIntVar(1, num_vals, 'a4')
    B1 = model.NewIntVar(1, num_vals, 'b1')
    B2 = model.NewIntVar(1, num_vals, 'b2')
    B3 = model.NewIntVar(1, num_vals, 'b3')
    B4 = model.NewIntVar(1, num_vals, 'b4')
    C1 = model.NewIntVar(1, num_vals, 'c1')
    C2 = model.NewIntVar(1, num_vals, 'c2')
    C3 = model.NewIntVar(1, num_vals, 'c3')
    C4 = model.NewIntVar(1, num_vals, 'c4')
    D1 = model.NewIntVar(1, num_vals, 'd1')
    D2 = model.NewIntVar(1, num_vals, 'd2')
    D3 = model.NewIntVar(1, num_vals, 'd3')
    D4 = model.NewIntVar(1, num_vals, 'd4')


    # Creates the constraints.


    model.Add(A1 != A2)
    model.Add(A1 != A3)
    model.Add(A1 != A4)
    model.Add(A1 != B1)
    model.Add(A1 != C1)
    model.Add(A1 != D1)
    model.Add(A2 != A3)
    model.Add(A2 != A4)
    model.Add(A2 != B2)
    model.Add(A2 != C2)
    model.Add(A2 != D2)
    model.Add(A3 != A4)
    model.Add(A3 != B3)
    model.Add(A3 != C3)
    model.Add(A3 != D3)
    model.Add(A4 != B4)
    model.Add(A4 != C4)
    model.Add(A4 != D4)
    model.Add(B1 != B2)
    model.Add(B1 != B3)
    model.Add(B1 != B4)
    model.Add(B1 != C1)
    model.Add(B1 != D1)
    model.Add(B2 != B3)
    model.Add(B2 != B4)
    model.Add(B2 != C2)
    model.Add(B2 != D2)
    model.Add(B3 != B4)
    model.Add(B3 != C3)
    model.Add(B3 != D3)
    model.Add(B4 != C4)
    model.Add(B4 != D4)
    model.Add(C1 != C2)
    model.Add(C1 != C3)
    model.Add(C1 != C4)
    model.Add(C1 != D1)
    model.Add(C2 != C3)
    model.Add(C2 != C4)
    model.Add(C2 != D2)
    model.Add(C3 != C4)
    model.Add(C3 != D3)
    model.Add(C4 != D4)
    model.Add(D1 != D2)
    model.Add(D1 != D3)
    model.Add(D1 != D4)


    if line1[1].isdigit():
        if line1[0] == "A1":
            model.Add(A1 == int(line1[1]))

        if line1[0] == "A2":
            model.Add(A2 == int(line1[1]))

        if line1[0] == "A3":
            model.Add(A3 == int(line1[1]))

        if line1[0] == "A4":
            model.Add(A4 == int(line1[1]))

        if line1[0] == "B1":
            model.Add(B1 == int(line1[1]))

        if line1[0] == "B2":
            model.Add(B2 == int(line1[1]))

        if line1[0] == "B3":
            model.Add(B3 == int(line1[1]))

        if line1[0] == "B4":
            model.Add(B4 == int(line1[1]))

        if line1[0] == "C1":
            model.Add(C1 == int(line1[1]))

        if line1[0] == "C2":
            model.Add(C2 == int(line1[1]))

        if line1[0] == "C3":
            model.Add(C3 == int(line1[1]))

        if line1[0] == "C4":
            model.Add(C4 == int(line1[1]))

        if line1[0] == "D1":
            model.Add(D1 == int(line1[1]))

        if line1[0] == "D2":
            model.Add(D2 == int(line1[1]))

        if line1[0] == "D3":
            model.Add(D3 == int(line1[1]))

        if line1[0] == "D4":
            model.Add(D4 == int(line1[1]))

    else:
        if line1[0] == "A1":
            if line1[1] == "A2":
                model.Add(A1 > A2)

            if line1[1] == "B1":
                model.Add(A1 >  B1)

        if line1[0] == "A2":
            if line1[1] == "A1":
                model.Add(A2 > A1)

            if line1[1] == "A3":
                model.Add(A2 > A3)

            if line1[1] == "B2":
                model.Add(A2 > B2)

        if line1[0] == "A3":
            if line1[1] == "A2":
                model.Add(A3 > A2)

            if line1[1] == "A4":
                model.Add(A3 > A4)

            if line1[1] == "B3":
                model.Add(A3 > B3)


        if line1[0] == "A4":

            if line1[1] == "B4":
                model.Add(A4 > B4)
            if line1[1] == "A3":
                model.Add(A4 > A3)

        if line1[0] == "B1":
            if line1[1] == "A1":
                model.Add(B1 > A1)

            if line1[1] == "C1":
                model.Add(B1 > C1)

            if line1[1] == "B2":
                model.Add(B1 > B2)

        if line1[0] == "B2":
            if line1[1] == "A2":
                model.Add(B2 > A2)

            if line1[1] == "B1":
                model.Add(B2 > B1)

            if line1[1] == "B3":
                model.Add(B2 > B3)

            if line1[1] == "C2":
                model.Add(B2 > C2)

        if line1[0] == "B3":
            if line1[1] == "A3":
                model.Add(B3 > A3)

            if line1[1] == "B2":
                model.Add(B3 > B2)

            if line1[1] == "B4":
                model.Add(B3 > B4)

            if line1[1] == "C3":
                model.Add(B3 > C3)

        if line1[0] == "B4":
            if line1[1] == "A4":
                model.Add(B4 > A4)

            if line1[1] == "B3":
                model.Add(B4 > B3)

            if line1[1] == "C4":
                model.Add(B4 > C4)

        if line1[0] == "C1":
            if line1[1] == "B1":
                model.Add(C1 > B1)

            if line1[1] == "C2":
                model.Add(C1 > C2)

            if line1[1] == "D1":
                model.Add(C1 > D1)

        if line1[0] == "C2":
            if line1[1] == "B2":
                model.Add(C2 > B2)

            if line1[1] == "C1":
                model.Add(C2 > C1)

            if line1[1] == "C3":
                model.Add(C2 > C3)

            if line1[1] == "D2":
                model.Add(C2 > D2)

        if line1[0] == "C3":
            if line1[1] == "B3":
                model.Add(C3 > B3)

            if line1[1] == "C2":
                model.Add(C3 > C2)

            if line1[1] == "C4":
                model.Add(C3 > C4)

            if line1[1] == "D3":
                model.Add(C3 > D3)

        if line1[0] == "C4":

            if line1[1] == "B4":
                model.Add(C4 > B4)

            if line1[1] == "D2":
                model.Add(C4 > D4)

            if line1[1] == "C3":
                model.Add(C4 > C3)

        if line1[0] == "D1":

            if line1[1] == "C1":
                model.Add(D1 > C1)

            if line1[1] == "D2":
                model.Add(D1 > D2)

        if line1[0] == "D2":
            if line1[1] == "D1":
                model.Add(D2 > D1)

            if line1[1] == "C2":
                model.Add(D2 > C2)

            if line1[1] == "D3":
                model.Add(D2 > D3)

        if line1[0] == "D3":
            if line1[1] == "C3":
                model.Add(D3 > C3)

            if line1[1] == "D2":
                model.Add(D3 > D2)

            if line1[1] == "D4":
                model.Add(D3 > D4)
        if line1[0] == "D4":
            if line1[1] == "D3":
                model.Add(D4 > D3)

            if line1[1] == "C4":
                model.Add(D4 > C4)

#line

    if line2[1].isdigit():
        if line2[0] == "A1":
            model.Add(A1 == int(line2[1]))

        if line2[0] == "A2":
            model.Add(A2 == int(line2[1]))

        if line2[0] == "A3":
            model.Add(A3 == int(line2[1]))

        if line2[0] == "A4":
            model.Add(A4 == int(line2[1]))

        if line2[0] == "B1":
            model.Add(B1 == int(line2[1]))

        if line2[0] == "B2":
            model.Add(B2 == int(line2[1]))

        if line2[0] == "B3":
            model.Add(B3 == int(line2[1]))

        if line2[0] == "B4":
            model.Add(B4 == int(line2[1]))

        if line2[0] == "C1":
            model.Add(C1 == int(line2[1]))

        if line2[0] == "C2":
            model.Add(C2 == int(line2[1]))

        if line2[0] == "C3":
            model.Add(C3 == int(line2[1]))

        if line2[0] == "C4":
            model.Add(C4 == int(line2[1]))

        if line2[0] == "D1":
            model.Add(D1 == int(line2[1]))

        if line2[0] == "D2":
            model.Add(D2 == int(line2[1]))

        if line2[0] == "D3":
            model.Add(D3 == int(line2[1]))

        if line2[0] == "D4":
            model.Add(D4 == int(line2[1]))

    else:
        if line2[0] == "A1":
            if line2[1] == "A2":
                model.Add(A1 > A2)

            if line2[1] == "B1":
                model.Add(A1 >  B1)

        if line2[0] == "A2":
            if line2[1] == "A1":
                model.Add(A2 > A1)

            if line2[1] == "A3":
                model.Add(A2 > A3)

            if line2[1] == "B2":
                model.Add(A2 > B2)

        if line2[0] == "A3":
            if line2[1] == "A2":
                model.Add(A3 > A2)

            if line2[1] == "A4":
                model.Add(A3 > A4)

            if line2[1] == "B3":
                model.Add(A3 > B3)


        if line2[0] == "A4":

            if line2[1] == "B4":
                model.Add(A4 > B4)
            if line2[1] == "A3":
                model.Add(A4 > A3)

        if line2[0] == "B1":
            if line2[1] == "A1":
                model.Add(B1 > A1)

            if line2[1] == "C1":
                model.Add(B1 > C1)

            if line2[1] == "B2":
                model.Add(B1 > B2)

        if line2[0] == "B2":
            if line2[1] == "A2":
                model.Add(B2 > A2)

            if line2[1] == "B1":
                model.Add(B2 > B1)

            if line2[1] == "B3":
                model.Add(B2 > B3)

            if line2[1] == "C2":
                model.Add(B2 > C2)

        if line2[0] == "B3":
            if line2[1] == "A3":
                model.Add(B3 > A3)

            if line2[1] == "B2":
                model.Add(B3 > B2)

            if line2[1] == "B4":
                model.Add(B3 > B4)

            if line2[1] == "C3":
                model.Add(B3 > C3)

        if line2[0] == "B4":
            if line2[1] == "A4":
                model.Add(B4 > A4)

            if line2[1] == "B3":
                model.Add(B4 > B3)

            if line2[1] == "C4":
                model.Add(B4 > C4)

        if line2[0] == "C1":
            if line2[1] == "B1":
                model.Add(C1 > B1)

            if line2[1] == "C2":
                model.Add(C1 > C2)

            if line2[1] == "D1":
                model.Add(C1 > D1)

        if line2[0] == "C2":
            if line2[1] == "B2":
                model.Add(C2 > B2)

            if line2[1] == "C1":
                model.Add(C2 > C1)

            if line2[1] == "C3":
                model.Add(C2 > C3)

            if line2[1] == "D2":
                model.Add(C2 > D2)

        if line2[0] == "C3":
            if line2[1] == "B3":
                model.Add(C3 > B3)

            if line2[1] == "C2":
                model.Add(C3 > C2)

            if line2[1] == "C4":
                model.Add(C3 > C4)

            if line2[1] == "D3":
                model.Add(C3 > D3)

        if line2[0] == "C4":

            if line2[1] == "B4":
                model.Add(C4 > B4)

            if line2[1] == "D2":
                model.Add(C4 > D4)

            if line2[1] == "C3":
                model.Add(C4 > C3)

        if line2[0] == "D1":

            if line2[1] == "C1":
                model.Add(D1 > C1)

            if line2[1] == "D2":
                model.Add(D1 > D2)

        if line2[0] == "D2":
            if line2[1] == "D1":
                model.Add(D2 > D1)

            if line2[1] == "C2":
                model.Add(D2 > C2)

            if line2[1] == "D3":
                model.Add(D2 > D3)

        if line2[0] == "D3":
            if line2[1] == "C3":
                model.Add(D3 > C3)

            if line2[1] == "D2":
                model.Add(D3 > D2)

            if line2[1] == "D4":
                model.Add(D3 > D4)
        if line2[0] == "D4":
            if line2[1] == "D3":
                model.Add(D4 > D3)

            if line2[1] == "C4":
                model.Add(D4 > C4)

#line3

    if line3[1].isdigit():
        if line3[0] == "A1":
            model.Add(A1 == int(line3[1]))

        if line3[0] == "A2":
            model.Add(A2 == int(line3[1]))

        if line3[0] == "A3":
            model.Add(A3 == int(line3[1]))

        if line3[0] == "A4":
            model.Add(A4 == int(line3[1]))

        if line3[0] == "B1":
            model.Add(B1 == int(line3[1]))

        if line3[0] == "B2":
            model.Add(B2 == int(line3[1]))

        if line3[0] == "B3":
            model.Add(B3 == int(line3[1]))

        if line3[0] == "B4":
            model.Add(B4 == int(line3[1]))

        if line3[0] == "C1":
            model.Add(C1 == int(line3[1]))

        if line3[0] == "C2":
            model.Add(C2 == int(line3[1]))

        if line3[0] == "C3":
            model.Add(C3 == int(line3[1]))

        if line3[0] == "C4":
            model.Add(C4 == int(line3[1]))

        if line3[0] == "D1":
            model.Add(D1 == int(line3[1]))

        if line3[0] == "D2":
            model.Add(D2 == int(line3[1]))

        if line3[0] == "D3":
            model.Add(D3 == int(line3[1]))

        if line3[0] == "D4":
            model.Add(D4 == int(line3[1]))

    else:
        if line3[0] == "A1":
            if line3[1] == "A2":
                model.Add(A1 > A2)

            if line3[1] == "B1":
                model.Add(A1 >  B1)

        if line3[0] == "A2":
            if line3[1] == "A1":
                model.Add(A2 > A1)

            if line3[1] == "A3":
                model.Add(A2 > A3)

            if line3[1] == "B2":
                model.Add(A2 > B2)

        if line3[0] == "A3":
            if line3[1] == "A2":
                model.Add(A3 > A2)

            if line3[1] == "A4":
                model.Add(A3 > A4)

            if line3[1] == "B3":
                model.Add(A3 > B3)


        if line3[0] == "A4":

            if line3[1] == "B4":
                model.Add(A4 > B4)
            if line3[1] == "A3":
                model.Add(A4 > A3)

        if line3[0] == "B1":
            if line3[1] == "A1":
                model.Add(B1 > A1)

            if line3[1] == "C1":
                model.Add(B1 > C1)

            if line3[1] == "B2":
                model.Add(B1 > B2)

        if line3[0] == "B2":
            if line3[1] == "A2":
                model.Add(B2 > A2)

            if line3[1] == "B1":
                model.Add(B2 > B1)

            if line3[1] == "B3":
                model.Add(B2 > B3)

            if line3[1] == "C2":
                model.Add(B2 > C2)

        if line3[0] == "B3":
            if line3[1] == "A3":
                model.Add(B3 > A3)

            if line3[1] == "B2":
                model.Add(B3 > B2)

            if line3[1] == "B4":
                model.Add(B3 > B4)

            if line3[1] == "C3":
                model.Add(B3 > C3)

        if line3[0] == "B4":
            if line3[1] == "A4":
                model.Add(B4 > A4)

            if line3[1] == "B3":
                model.Add(B4 > B3)

            if line3[1] == "C4":
                model.Add(B4 > C4)

        if line3[0] == "C1":
            if line3[1] == "B1":
                model.Add(C1 > B1)

            if line3[1] == "C2":
                model.Add(C1 > C2)

            if line3[1] == "D1":
                model.Add(C1 > D1)

        if line3[0] == "C2":
            if line3[1] == "B2":
                model.Add(C2 > B2)

            if line3[1] == "C1":
                model.Add(C2 > C1)

            if line3[1] == "C3":
                model.Add(C2 > C3)

            if line3[1] == "D2":
                model.Add(C2 > D2)

        if line3[0] == "C3":
            if line3[1] == "B3":
                model.Add(C3 > B3)

            if line3[1] == "C2":
                model.Add(C3 > C2)

            if line3[1] == "C4":
                model.Add(C3 > C4)

            if line3[1] == "D3":
                model.Add(C3 > D3)

        if line3[0] == "C4":

            if line3[1] == "B4":
                model.Add(C4 > B4)

            if line3[1] == "D2":
                model.Add(C4 > D4)

            if line3[1] == "C3":
                model.Add(C4 > C3)

        if line3[0] == "D1":

            if line3[1] == "C1":
                model.Add(D1 > C1)

            if line3[1] == "D2":
                model.Add(D1 > D2)

        if line3[0] == "D2":
            if line3[1] == "D1":
                model.Add(D2 > D1)

            if line3[1] == "C2":
                model.Add(D2 > C2)

            if line3[1] == "D3":
                model.Add(D2 > D3)

        if line3[0] == "D3":
            if line3[1] == "C3":
                model.Add(D3 > C3)

            if line3[1] == "D2":
                model.Add(D3 > D2)

            if line3[1] == "D4":
                model.Add(D3 > D4)
        if line3[0] == "D4":
            if line3[1] == "D3":
                model.Add(D4 > D3)

            if line3[1] == "C4":
                model.Add(D4 > C4)


#line4

    if line4[1].isdigit():
        if line4[0] == "A1":
            model.Add(A1 == int(line4[1]))

        if line4[0] == "A2":
            model.Add(A2 == int(line4[1]))

        if line4[0] == "A3":
            model.Add(A3 == int(line4[1]))

        if line4[0] == "A4":
            model.Add(A4 == int(line4[1]))

        if line4[0] == "B1":
            model.Add(B1 == int(line4[1]))

        if line4[0] == "B2":
            model.Add(B2 == int(line4[1]))

        if line4[0] == "B3":
            model.Add(B3 == int(line4[1]))

        if line4[0] == "B4":
            model.Add(B4 == int(line4[1]))

        if line4[0] == "C1":
            model.Add(C1 == int(line4[1]))

        if line4[0] == "C2":
            model.Add(C2 == int(line4[1]))

        if line4[0] == "C3":
            model.Add(C3 == int(line4[1]))

        if line4[0] == "C4":
            model.Add(C4 == int(line4[1]))

        if line4[0] == "D1":
            model.Add(D1 == int(line4[1]))

        if line4[0] == "D2":
            model.Add(D2 == int(line4[1]))

        if line4[0] == "D3":
            model.Add(D3 == int(line4[1]))

        if line4[0] == "D4":
            model.Add(D4 == int(line4[1]))

    else:
        if line4[0] == "A1":
            if line4[1] == "A2":
                model.Add(A1 > A2)

            if line4[1] == "B1":
                model.Add(A1 >  B1)

        if line4[0] == "A2":
            if line4[1] == "A1":
                model.Add(A2 > A1)

            if line4[1] == "A3":
                model.Add(A2 > A3)

            if line4[1] == "B2":
                model.Add(A2 > B2)

        if line4[0] == "A3":
            if line4[1] == "A2":
                model.Add(A3 > A2)

            if line4[1] == "A4":
                model.Add(A3 > A4)

            if line4[1] == "B3":
                model.Add(A3 > B3)


        if line4[0] == "A4":

            if line4[1] == "B4":
                model.Add(A4 > B4)
            if line4[1] == "A3":
                model.Add(A4 > A3)

        if line4[0] == "B1":
            if line4[1] == "A1":
                model.Add(B1 > A1)

            if line4[1] == "C1":
                model.Add(B1 > C1)

            if line4[1] == "B2":
                model.Add(B1 > B2)

        if line4[0] == "B2":
            if line4[1] == "A2":
                model.Add(B2 > A2)

            if line4[1] == "B1":
                model.Add(B2 > B1)

            if line4[1] == "B3":
                model.Add(B2 > B3)

            if line4[1] == "C2":
                model.Add(B2 > C2)

        if line4[0] == "B3":
            if line4[1] == "A3":
                model.Add(B3 > A3)

            if line4[1] == "B2":
                model.Add(B3 > B2)

            if line4[1] == "B4":
                model.Add(B3 > B4)

            if line4[1] == "C3":
                model.Add(B3 > C3)

        if line4[0] == "B4":
            if line4[1] == "A4":
                model.Add(B4 > A4)

            if line4[1] == "B3":
                model.Add(B4 > B3)

            if line4[1] == "C4":
                model.Add(B4 > C4)

        if line4[0] == "C1":
            if line4[1] == "B1":
                model.Add(C1 > B1)

            if line4[1] == "C2":
                model.Add(C1 > C2)

            if line4[1] == "D1":
                model.Add(C1 > D1)

        if line4[0] == "C2":
            if line4[1] == "B2":
                model.Add(C2 > B2)

            if line4[1] == "C1":
                model.Add(C2 > C1)

            if line4[1] == "C3":
                model.Add(C2 > C3)

            if line4[1] == "D2":
                model.Add(C2 > D2)

        if line4[0] == "C3":
            if line4[1] == "B3":
                model.Add(C3 > B3)

            if line4[1] == "C2":
                model.Add(C3 > C2)

            if line4[1] == "C4":
                model.Add(C3 > C4)

            if line4[1] == "D3":
                model.Add(C3 > D3)

        if line4[0] == "C4":

            if line4[1] == "B4":
                model.Add(C4 > B4)

            if line4[1] == "D2":
                model.Add(C4 > D4)

            if line4[1] == "C3":
                model.Add(C4 > C3)

        if line4[0] == "D1":

            if line4[1] == "C1":
                model.Add(D1 > C1)

            if line4[1] == "D2":
                model.Add(D1 > D2)

        if line4[0] == "D2":
            if line4[1] == "D1":
                model.Add(D2 > D1)

            if line4[1] == "C2":
                model.Add(D2 > C2)

            if line4[1] == "D3":
                model.Add(D2 > D3)

        if line4[0] == "D3":
            if line4[1] == "C3":
                model.Add(D3 > C3)

            if line4[1] == "D2":
                model.Add(D3 > D2)

            if line4[1] == "D4":
                model.Add(D3 > D4)
        if line4[0] == "D4":
            if line4[1] == "D3":
                model.Add(D4 > D3)

            if line4[1] == "C4":
                model.Add(D4 > C4)


#line5

    if line5[1].isdigit():
        if line5[0] == "A1":
            model.Add(A1 == int(line5[1]))

        if line5[0] == "A2":
            model.Add(A2 == int(line5[1]))

        if line5[0] == "A3":
            model.Add(A3 == int(line5[1]))

        if line5[0] == "A4":
            model.Add(A4 == int(line5[1]))

        if line5[0] == "B1":
            model.Add(B1 == int(line5[1]))

        if line5[0] == "B2":
            model.Add(B2 == int(line5[1]))

        if line5[0] == "B3":
            model.Add(B3 == int(line5[1]))

        if line5[0] == "B4":
            model.Add(B4 == int(line5[1]))

        if line5[0] == "C1":
            model.Add(C1 == int(line5[1]))

        if line5[0] == "C2":
            model.Add(C2 == int(line5[1]))

        if line5[0] == "C3":
            model.Add(C3 == int(line5[1]))

        if line5[0] == "C4":
            model.Add(C4 == int(line5[1]))

        if line5[0] == "D1":
            model.Add(D1 == int(line5[1]))

        if line5[0] == "D2":
            model.Add(D2 == int(line5[1]))

        if line5[0] == "D3":
            model.Add(D3 == int(line5[1]))

        if line5[0] == "D4":
            model.Add(D4 == int(line5[1]))

    else:
        if line5[0] == "A1":
            if line5[1] == "A2":
                model.Add(A1 > A2)

            if line5[1] == "B1":
                model.Add(A1 >  B1)

        if line5[0] == "A2":
            if line5[1] == "A1":
                model.Add(A2 > A1)

            if line5[1] == "A3":
                model.Add(A2 > A3)

            if line5[1] == "B2":
                model.Add(A2 > B2)

        if line5[0] == "A3":
            if line5[1] == "A2":
                model.Add(A3 > A2)

            if line5[1] == "A4":
                model.Add(A3 > A4)

            if line5[1] == "B3":
                model.Add(A3 > B3)


        if line5[0] == "A4":

            if line5[1] == "B4":
                model.Add(A4 > B4)
            if line5[1] == "A3":
                model.Add(A4 > A3)

        if line5[0] == "B1":
            if line5[1] == "A1":
                model.Add(B1 > A1)

            if line5[1] == "C1":
                model.Add(B1 > C1)

            if line5[1] == "B2":
                model.Add(B1 > B2)

        if line5[0] == "B2":
            if line5[1] == "A2":
                model.Add(B2 > A2)

            if line5[1] == "B1":
                model.Add(B2 > B1)

            if line5[1] == "B3":
                model.Add(B2 > B3)

            if line5[1] == "C2":
                model.Add(B2 > C2)

        if line5[0] == "B3":
            if line5[1] == "A3":
                model.Add(B3 > A3)

            if line5[1] == "B2":
                model.Add(B3 > B2)

            if line5[1] == "B4":
                model.Add(B3 > B4)

            if line5[1] == "C3":
                model.Add(B3 > C3)

        if line5[0] == "B4":
            if line5[1] == "A4":
                model.Add(B4 > A4)

            if line5[1] == "B3":
                model.Add(B4 > B3)

            if line5[1] == "C4":
                model.Add(B4 > C4)

        if line5[0] == "C1":
            if line5[1] == "B1":
                model.Add(C1 > B1)

            if line5[1] == "C2":
                model.Add(C1 > C2)

            if line5[1] == "D1":
                model.Add(C1 > D1)

        if line5[0] == "C2":
            if line5[1] == "B2":
                model.Add(C2 > B2)

            if line5[1] == "C1":
                model.Add(C2 > C1)

            if line5[1] == "C3":
                model.Add(C2 > C3)

            if line5[1] == "D2":
                model.Add(C2 > D2)

        if line5[0] == "C3":
            if line5[1] == "B3":
                model.Add(C3 > B3)

            if line5[1] == "C2":
                model.Add(C3 > C2)

            if line5[1] == "C4":
                model.Add(C3 > C4)

            if line5[1] == "D3":
                model.Add(C3 > D3)

        if line5[0] == "C4":

            if line5[1] == "B4":
                model.Add(C4 > B4)

            if line5[1] == "D2":
                model.Add(C4 > D4)

            if line5[1] == "C3":
                model.Add(C4 > C3)

        if line5[0] == "D1":

            if line5[1] == "C1":
                model.Add(D1 > C1)

            if line5[1] == "D2":
                model.Add(D1 > D2)

        if line5[0] == "D2":
            if line5[1] == "D1":
                model.Add(D2 > D1)

            if line5[1] == "C2":
                model.Add(D2 > C2)

            if line5[1] == "D3":
                model.Add(D2 > D3)

        if line5[0] == "D3":
            if line5[1] == "C3":
                model.Add(D3 > C3)

            if line5[1] == "D2":
                model.Add(D3 > D2)

            if line5[1] == "D4":
                model.Add(D3 > D4)
        if line5[0] == "D4":
            if line5[1] == "D3":
                model.Add(D4 > D3)

            if line5[1] == "C4":
                model.Add(D4 > C4)

#line6


    if line6[1].isdigit():
        if line6[0] == "A1":
            model.Add(A1 == int(line6[1]))

        if line6[0] == "A2":
            model.Add(A2 == int(line6[1]))

        if line6[0] == "A3":
            model.Add(A3 == int(line6[1]))

        if line6[0] == "A4":
            model.Add(A4 == int(line6[1]))

        if line6[0] == "B1":
            model.Add(B1 == int(line6[1]))

        if line6[0] == "B2":
            model.Add(B2 == int(line6[1]))

        if line6[0] == "B3":
            model.Add(B3 == int(line6[1]))

        if line6[0] == "B4":
            model.Add(B4 == int(line6[1]))

        if line6[0] == "C1":
            model.Add(C1 == int(line6[1]))

        if line6[0] == "C2":
            model.Add(C2 == int(line6[1]))

        if line6[0] == "C3":
            model.Add(C3 == int(line6[1]))

        if line6[0] == "C4":
            model.Add(C4 == int(line6[1]))

        if line6[0] == "D1":
            model.Add(D1 == int(line6[1]))

        if line6[0] == "D2":
            model.Add(D2 == int(line6[1]))

        if line6[0] == "D3":
            model.Add(D3 == int(line6[1]))

        if line6[0] == "D4":
            model.Add(D4 == int(line6[1]))

    else:
        if line6[0] == "A1":
            if line6[1] == "A2":
                model.Add(A1 > A2)

            if line6[1] == "B1":
                model.Add(A1 >  B1)

        if line6[0] == "A2":
            if line6[1] == "A1":
                model.Add(A2 > A1)

            if line6[1] == "A3":
                model.Add(A2 > A3)

            if line6[1] == "B2":
                model.Add(A2 > B2)

        if line6[0] == "A3":
            if line6[1] == "A2":
                model.Add(A3 > A2)

            if line6[1] == "A4":
                model.Add(A3 > A4)

            if line6[1] == "B3":
                model.Add(A3 > B3)


        if line6[0] == "A4":

            if line6[1] == "B4":
                model.Add(A4 > B4)
            if line6[1] == "A3":
                model.Add(A4 > A3)

        if line6[0] == "B1":
            if line6[1] == "A1":
                model.Add(B1 > A1)

            if line6[1] == "C1":
                model.Add(B1 > C1)

            if line6[1] == "B2":
                model.Add(B1 > B2)

        if line6[0] == "B2":
            if line6[1] == "A2":
                model.Add(B2 > A2)

            if line6[1] == "B1":
                model.Add(B2 > B1)

            if line6[1] == "B3":
                model.Add(B2 > B3)

            if line6[1] == "C2":
                model.Add(B2 > C2)

        if line6[0] == "B3":
            if line6[1] == "A3":
                model.Add(B3 > A3)

            if line6[1] == "B2":
                model.Add(B3 > B2)

            if line6[1] == "B4":
                model.Add(B3 > B4)

            if line6[1] == "C3":
                model.Add(B3 > C3)

        if line6[0] == "B4":
            if line6[1] == "A4":
                model.Add(B4 > A4)

            if line6[1] == "B3":
                model.Add(B4 > B3)

            if line6[1] == "C4":
                model.Add(B4 > C4)

        if line6[0] == "C1":
            if line6[1] == "B1":
                model.Add(C1 > B1)

            if line6[1] == "C2":
                model.Add(C1 > C2)

            if line6[1] == "D1":
                model.Add(C1 > D1)

        if line6[0] == "C2":
            if line6[1] == "B2":
                model.Add(C2 > B2)

            if line6[1] == "C1":
                model.Add(C2 > C1)

            if line6[1] == "C3":
                model.Add(C2 > C3)

            if line6[1] == "D2":
                model.Add(C2 > D2)

        if line6[0] == "C3":
            if line6[1] == "B3":
                model.Add(C3 > B3)

            if line6[1] == "C2":
                model.Add(C3 > C2)

            if line6[1] == "C4":
                model.Add(C3 > C4)

            if line6[1] == "D3":
                model.Add(C3 > D3)

        if line6[0] == "C4":

            if line6[1] == "B4":
                model.Add(C4 > B4)

            if line6[1] == "D2":
                model.Add(C4 > D4)

            if line6[1] == "C3":
                model.Add(C4 > C3)

        if line6[0] == "D1":

            if line6[1] == "C1":
                model.Add(D1 > C1)

            if line6[1] == "D2":
                model.Add(D1 > D2)

        if line6[0] == "D2":
            if line6[1] == "D1":
                model.Add(D2 > D1)

            if line6[1] == "C2":
                model.Add(D2 > C2)

            if line6[1] == "D3":
                model.Add(D2 > D3)

        if line6[0] == "D3":
            if line6[1] == "C3":
                model.Add(D3 > C3)

            if line6[1] == "D2":
                model.Add(D3 > D2)

            if line6[1] == "D4":
                model.Add(D3 > D4)
        if line6[0] == "D4":
            if line6[1] == "D3":
                model.Add(D4 > D3)

            if line6[1] == "C4":
                model.Add(D4 > C4)



    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        A1 = solver.Value(A1)
        A2 = solver.Value(A2)
        A3 = solver.Value(A3)
        A4 = solver.Value(A4)
        B1 = solver.Value(B1)
        B2 = solver.Value(B2)
        B3 = solver.Value(B3)
        B4 = solver.Value(B4)
        C1 = solver.Value(C1)
        C2 = solver.Value(C2)
        C3 = solver.Value(C3)
        C4 = solver.Value(C4)
        D1 = solver.Value(D1)
        D2 = solver.Value(D2)
        D3 = solver.Value(D3)
        D4 = solver.Value(D4)

        #print(A1,",",A2,",",A3,",",A4)
        #print(B1,",",B2,",",B3,",",B4)
        #print(C1,",",C2,",",C3,",",C4)
        #print(D1,",",D2,",",D3,",",D4)

        list = [A1, A2, A3, A4]
        list2 = [B1, B2, B3, B4]
        list3 = [C1, C2, C3, C4]
        list4 = [D1, D2, D3, D4]

        for i in list:
            output.write(str(i))
            if i == list[3]:
                break
            else:
                output.write(",")
        output.write("\n")

        for i in list2:
            output.write(str(i))
            if i == list2[3]:
                break
            else:
                output.write(",")
        output.write("\n")

        for i in list3:
            output.write(str(i))
            if i == list3[3]:
                break
            else:
                output.write(",")

        output.write("\n")

        for i in list4:
            output.write(str(i))
            if i == list4[3]:
                break
            else:
                output.write(",")

SimpleSatProgram()