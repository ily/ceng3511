from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ortools.sat.python import cp_model
import sys

file = open(sys.argv[1], "r")
output = open(sys.argv[2], "w+")
input = file.readlines()
fline = input[0].split(", ")
sline = input[1].split(", ")
fline0 = int(fline[0])
fline1 = int(fline[1])
fline2 = int(fline[2])
sline0 = int(sline[0])
sline1 = int(sline[1])
sline2 = int(sline[2])

def SimpleSatProgram():
    """Minimal CP-SAT example to showcase calling the solver."""
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    num_vals = 10
    a = model.NewIntVar(1, num_vals - 1, 'a')
    b = model.NewIntVar(1, num_vals - 1, 'b')
    c = model.NewIntVar(1, num_vals - 1, 'c')
    d = model.NewIntVar(1, num_vals - 1, 'd')
    e = model.NewIntVar(1, num_vals - 1, 'e')
    f = model.NewIntVar(1, num_vals - 1, 'f')
    g = model.NewIntVar(1, num_vals - 1, 'g')
    h = model.NewIntVar(1, num_vals - 1, 'h')
    ı = model.NewIntVar(1, num_vals - 1, 'ı')

    # Creates the constraints.
    model.Add((a + d + g) == fline0)
    model.Add((b + e + h) == fline1)
    model.Add((c + f + ı) == fline2)
    model.Add((a + b + c) == sline0)
    model.Add((d + e + f) == sline1)
    model.Add((g + h + ı) == sline2)
    model.Add(a != b)
    model.Add(a != c)
    model.Add(a != d)
    model.Add(a != g)
    model.Add(b != c)
    model.Add(b != e)
    model.Add(b != h)
    model.Add(c != f)
    model.Add(c != ı)
    model.Add(d != g)
    model.Add(d != e)
    model.Add(d != f)
    model.Add(e != f)
    model.Add(e != h)
    model.Add(f != ı)
    model.Add(g != h)
    model.Add(g != ı)
    model.Add(h != ı)

    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:

        a = solver.Value(a)
        b = solver.Value(b)
        c = solver.Value(c)
        d = solver.Value(d)
        e = solver.Value(e)
        f = solver.Value(f)
        g = solver.Value(g)
        h = solver.Value(h)
        ı = solver.Value(ı)

        #print('x,',fline[0],',',fline[1],',',fline[2].strip('\n'))
        #print(sline[0],',', a,',',b, ',',c)
        #print(sline[1],',',d,',',e,',',f)
        #print(sline[2],',',g,',',h,',',ı)

        list = ["x", fline[0],fline[1],fline[2].strip('\n')]
        list1 = [sline[0], a, b, c]
        list2 = [sline[1], d, e, f]
        list3 = [sline[2], g, h, ı]

        for i in list:
            output.write(str(i))
            if i == list[3]:
                break
            else:
                output.write(",")
        output.write("\n")

        for i in list1:
            output.write(str(i))
            if i == list1[3]:
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



SimpleSatProgram()