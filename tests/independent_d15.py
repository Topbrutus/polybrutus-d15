#!/usr/bin/env python3
"""Independent exact rational Polybrutus D15 certificate.

Rebuilds 190 labelled squared distances from the canonical 7-point
rational coordinates, a 5-point regular simplex, and 8 orthogonal axes.
No imports from primary or archived geometry generators.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
report=json.loads((ROOT/"results"/"certificate_d15.json").read_text(encoding="utf8"))
prior=json.loads((ROOT/"prior"/"certificate_d14.json").read_text(encoding="utf8"))
core=[
 (F(0),F(0),F(1)),(F(1,2),F(0),F(1,2)),
 (F(-1,4),F(3,4),F(1,2)),(F(-1,4),F(-3,4),F(1,2)),
 (F(0),F(0),F(-1)),(F(1,2),F(0),F(-1,2)),
 (F(-1,2),F(0),F(-1,2))
]
def squared_distance(i,j):
    if i==j:return F(0)
    if i<7 and j<7:
        a,b,c=(core[i][k]-core[j][k] for k in range(3))
        return 3*a*a+b*b+c*c
    if 7<=i<12 and 7<=j<12:return F(5,2)
    return F(2)

pairs=list(combinations(range(20),2))
exact={(i+1,j+1):squared_distance(i,j) for i,j in pairs}
cert={(int(e["i"]),int(e["j"])):F(e["d2"])
      for e in report["labelled_squared_distances"]}
assert len(exact)==190 and exact==cert
old={(int(e["i"]),int(e["j"])):F(e["d2"])
     for e in prior["labelled_squared_distances"]}
assert len(old)==171 and all(exact[k]==value for k,value in old.items())
assert all(squared_distance(i,19)==F(2) for i in range(19))
hist=Counter(4*squared_distance(i,j) for i,j in pairs)
assert hist==Counter({F(4):6,F(7):2,F(8):159,F(9):3,F(10):10,F(12):6,F(13):2,F(16):2})
assert sum(exact.values(),F(0))==F(1567,4)
D=s.Matrix(20,20,lambda i,j:s.Rational(squared_distance(i,j).numerator,squared_distance(i,j).denominator))
H=s.eye(20)-s.ones(20)/20
B=-H*D*H/2
assert B.rank()==15
D14=D[:19,:19];H14=s.eye(19)-s.ones(19)/19
assert (-H14*D14*H14/2).rank()==14

L=s.zeros(20)
for i,j in pairs:
    w=1/D[i,j]
    L[i,i]+=w;L[j,j]+=w
    L[i,j]-=w;L[j,i]-=w
z=s.Symbol("z");charpoly=L.charpoly(z).as_expr()
for value,multiplicity in [(s.Integer(10),9),(s.Rational(19,2),4)]:
    assert all(s.simplify(s.diff(charpoly,z,k).subs(z,value))==0 for k in range(multiplicity))
    assert s.simplify(s.diff(charpoly,z,multiplicity).subs(z,value))!=0
assert report["affine_rank"]==report["centered_gram_rank"]==15
assert report["parent_distances_preserved"]==171 and report["new_distances"]==19
p=ROOT/"results"/"certificate_d15.json"
print("INDEPENDENT D15 PASS: 190 rational labelled distances, 171 preserved, Gram rank 15")
print("INDEPENDENT MODEL GRAPH PASS: eigenvalue 10 x9; eigenvalue 19/2 x4")
print("CERTIFICATE_SHA256="+hashlib.sha256(p.read_bytes()).hexdigest())
