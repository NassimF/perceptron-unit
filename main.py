#Author: Nasim Faridnia




from logging import exception
import perceptron_unit
from perceptron_unit import *


gate = input("enter gate:").lower()
if gate not in ["and", "or", "nand", "nor"]:
    raise exception("Error! Gate must be 'and', 'or', 'nand', 'nor'f")
alpha = float(input("enter alpha:"))
w1 = float(input("enter w1:"))
w2 = float(input("enter w2:"))
max_iter = int(input("enter max steps:"))




p = perceptron_unit(gate, alpha, w1, w2,max_iter)
p.learningAlgorithm()
p.result()