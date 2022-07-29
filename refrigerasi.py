import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pynverse import inversefunc

class RefrigerasiStat():
    def __init__(self):
        pass

    def h_H2O_L(self, T):
        return 4.19 * (T - 273.15)

    def h_H2O_G(self, T, P):
        h_H2O_G1 = 2.326 * (0.004932 * T - 2.2493008) * P / 6894.76
        h_H2O_G2 = 2.326 * (0.80895 * T + 854.2151086)
        return h_H2O_G1 + h_H2O_G2

    def h_sol(self, T, X):
        A0 = -1015.7
        A1 = 79.5387
        A2 = -2.358016
        A3 = 0.03031583
        A4 = -1.400261 * 10**(-4)
        Sig_AX = A0 * X**0 + A1 * X**1 + A2 * X**2 + A3 * X**3 + A4 * X**4

        B0 = 4.68108
        B1 = -0.3037766
        B2 = 8.44845*10**(-3)
        B3 = -1.047721 * 10**(-4)
        B4 = 4.80097 * 10**(-7)
        Sig_BX = B0 * X**(0) + B1 * X**(1) + B2 * X**(2) + B3 * X**(3) + B4 * X**(4)
        
        C0 = -4.9107 * 10**(-3)
        C1 = 3.83184 * 10**(-4)
        C2 = -1.078963 * 10**(-5)
        C3 = 1.3152 * 10**(-7)
        C4 = -5.897 * 10**(-10)
        Sig_CX = C0 * X**(0) + C1 * X**(1) + C2 * X**(2) + C3 * X**(3) + C4 * X**(4)
            
        # Enthalpy of LiBr-H2O solution
        h_solA = 2.326 * Sig_AX
        h_solB = 2.326 * (1.8 * T - 459.67) * Sig_BX
        h_solC = 2.326 * (1.8 * T - 459.67)**2 * Sig_CX
        
        return h_solA + h_solB + h_solC

    def T_h_sol(self, h, X):
        func = (lambda T: self.h_sol(T, X))
        return int(inversefunc(func, h))
    
    def T_h_H2O_L(self, h):
        func = (lambda T: self.h_H2O_L(T))
        return int(inversefunc(func, h))

    def Q_act(self, E, U, A, Th, Tc):
        return E * U * A * (Th - Tc)

    def P_sp(self, T):
        return 10 ** (10.04999 - (1603.541 / T) - (104095.51 / (T**2)))

class RefrigerasiProp(RefrigerasiStat):
    def __init__(self, Q_gen=0, Q_cond=0, Q_abs=0, Q_eva=0):
        self.Q_gen = Q_gen
        self.Q_cond = Q_cond
        self.Q_eva = Q_eva
        self.Q_abs = Q_abs
    
    # GENERATOR PROP
    def generator(self, T_in, m_in, h_in, m_out1, h_out1, m_out2, h_out2):
        pass
    
    # CONDENSER PROP
    def condenser(self, m_in, h_in, T_in):
        self.Q_cond = m_in * h_in
        m_out = m_in
        h_out = h_in
        T_out = T_in
        return h_out, m_out, T_out, self.Q_cond

    # EVAPORATOR PROP
    def evaporator(self, m_in, h_in, T_in):
        P_evaporator = self.P_sp(T_in)
        m_out = m_in
        h_out = self.Q_eva / m_in + h_in
        T_out = self.T_h_H2O_L(h_out)
        return h_out, m_out, T_out
    
    # ABSORBER PROP
    def absorber(self, m_in1, h_in1, T_in1, m_in2, h_in2, T_in2, X_in, X_out):
        m_out = m_in1 + m_in2
        h_out = (m_in1 * h_in1 + m_in2 * h_in2 - self.Q_abs) / m_out
        T_out = self.T_h_sol(h_out, X_out)
        return h_out, m_out, T_out
