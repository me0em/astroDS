'''
##                                                                  ##
##   Transformations between SDSS and UBV(RI)c photometric systems  ##
##    sdss3.org/dr8/algorithms/sdssUBVRITransform.php#Jester2005    ##
##                                                                  ##
'''

# DOCUMENTATION

# :CONSTANTS:
# obj_type - 'quasar', 'galaxy' or 'star'
# ugriz = (u, g, r, i, z)

# :FUNCTIONS:
''' Jester et al. (2005) '''
''' Stars: U_B, B_V, V_R, R_I, B, V; (R-I < 1.15) '''
''' Quasars: U_B, B_V, V_R, R_I, B, V; (z <= 2.1)  '''

''' Jordi et al. (2005) '''
''' Stars: U_B '''

''' Karaali, Bilir & Tunçel (2005) '''
''' Stars: B_V '''

''' Lupton (2005) '''
''' Stars: B, V, R, I, B_V, V_R '''



''' Jester et al. (2005) '''
def Jester(obj_type, ugriz) -> dict:
    U = B = V = R = I = None
    U_B = B_V = V_R = R_I = None
    u, g, r, i, z = ugriz

    # Quasar
    if obj_type == 'quasar' and z <= 2.1:
        U_B = 0.75 * (u-g) - 0.81
        B_V = 0.62 * (g-r) + 0.15
        V_R = 0.38 * (r-i) + 0.27
        R_I = 0.72 * (r-i) + 0.27
        B = g + 0.17 * (u-g) + 0.11
        V = g - 0.52 * (g-r) - 0.03

    # Stars with R-I < 1.15 and U-B < 0
    elif obj_type == 'star' and (0.77 * (u-g) - 0.88) < 0 and (1.02 * (r-i) + 0.21) < 1.15:
        U_B = 0.77 * (u-g) - 0.88
        B_V = 0.90 * (g-r) + 0.21
        V_R = 0.96 * (r-i) + 0.21
        R_I = 1.02 * (r-i) + 0.21
        B = g + 0.33 * (g-r) + 0.20
        V = g - 0.58 * (g-r) - 0.01

    # All stars with R-I < 1.15
    elif obj_type == 'star' and (1.00 * (r-i) + 0.21) < 1:
        U_B = 0.78 * (u-g) - 0.88
        B_V = 0.98 * (g-r) + 0.22
        V_R = 1.09 * (r-i) + 0.22
        R_I = 1.00 * (r-i) + 0.21
        B = g + 0.39 * (g-r) + 0.21
        V = g - 0.59 * (g-r) - 0.01

    else:
        return None

    result = dict()
    result['U'] = U
    result['B'] = B
    result['V'] = V
    result['R'] = R
    result['I'] = I
    result['U_B'] = U_B
    result['B_V'] = B_V
    result['V_R'] = V_R
    result['R_I'] = R_I

    return result


''' Jordi et al. (2005) '''


''' Karaali, Bilir & Tunçel (2005) '''
def Karaali(obj_type, ugriz) -> list:
    U = B = V = R = I = None
    U_B = B_V = V_R = R_I = None
    u, g, r, i, z = ugriz
    # Stars (0.3 < B-V < 1.1)
    if obj_type == 'star' and 0.3 < (0.992*(g-r) - 0.0199*(u-g) + 0.202) < 1.1:
        result = dict()
        result['B_V'] = 0.992*(g-r) - 0.0199*(u-g) + 0.202
        return result
    else:
        return None

''' Lupton (2005) '''
def Lupton(obj_type, ugriz) -> dict:
    U = B = V = R = I = None
    U_B = B_V = V_R = R_I = None
    u, g, r, i, z = ugriz
    # Stars
    if obj_type == 'star':
        B = ((u - 0.8116*(u - g) + 0.1313) + (g + 0.3130*(g - r) + 0.2271)) / 2
        V = ((g - 0.2906*(u - g) + 0.0885) + (g - 0.5784*(g - r) - 0.0038)) / 2
        R = ((r - 0.1837*(g - r) - 0.0971) + (r - 0.2936*(r - i) - 0.1439)) / 2
        I = ((r - 1.2444*(r - i) - 0.3820) + (i - 0.3780*(i - z) - 0.3974)) / 2

        result = dict()
        result['B'] = B
        result['V'] = V
        result['R'] = R
        result['I'] = I
        result['B_V'] = B - V
        result['V_R'] = V - R
        return result
    else:
        return None


'''
Eсть ещё для дварфов 2 метода конвертирования: Bilir, Karaali & Tunçel (2005), West, Walkowicz & Hawley (2005)

И для звёзд из Main Sequence: Rodgers et al. (2006)
'''
