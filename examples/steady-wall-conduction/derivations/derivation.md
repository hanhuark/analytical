# Analytical Derivation

## Problem contract and target prediction

The target is the steady temperature and heat flux in `0<=x<=L` with `T(0)=T_H>T_C=T(L)`.

## Balance-law ancestry

For a stationary slice of area `A`, steady energy conservation with zero generation gives `q_x(x)A-q_x(x+dx)A=0`. Dividing by `A dx` and taking the limit gives `dq_x/dx=0`.

## Constitutive and interfacial closures

Apply C1, `q_x=-k dT/dx`, with constant `k>0`. There is no internal interface; prescribed face temperatures are ideal boundary conditions.

## Nondimensionalization and ordering

Let `X=x/L` and `theta=(T-T_C)/(T_H-T_C)`. The equation is `d2theta/dX2=0`, with `theta(0)=1` and `theta(1)=0`.

## Mathematical method and prerequisites

Integrate the regular constant-coefficient ODE twice. Two independent Dirichlet conditions determine the two constants uniquely.

## Derivation

Integration gives `theta=aX+b`. The boundary conditions give `b=1` and `a=-1`, so `theta=1-X`. Therefore `T=T_H-(T_H-T_C)x/L` and `q_x=k(T_H-T_C)/L`.

## Dimensions, signs, limits, and baseline checks

`k DeltaT/L` has units `W m^-2`; `dT/dx<0`, so `q_x>0`. The ODE and both boundary residuals are zero. As `DeltaT` approaches zero, the uniform solution and zero flux are recovered.

## Validity range, uncertainty, and falsification conditions

The result is exact for the stated mathematical problem. Physical validity is limited by A1-A4 and C1. Curvature or unequal face heat rates beyond uncertainty falsifies the reduced model.
