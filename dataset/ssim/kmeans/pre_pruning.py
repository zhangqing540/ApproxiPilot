import ctypes
import os
import random
import numpy as np
from ctypes import *
from functools import reduce
add12u_0AF = ctypes.CDLL("basic_lib/c/add12/add12u_0AF.so")
add12u_0AZ = ctypes.CDLL("basic_lib/c/add12/add12u_0AZ.so")
add12u_0B6 = ctypes.CDLL("basic_lib/c/add12/add12u_0B6.so")
add12u_0C9 = ctypes.CDLL("basic_lib/c/add12/add12u_0C9.so")
add12u_0G8 = ctypes.CDLL("basic_lib/c/add12/add12u_0G8.so")
add12u_0JK = ctypes.CDLL("basic_lib/c/add12/add12u_0JK.so")
add12u_0LN = ctypes.CDLL("basic_lib/c/add12/add12u_0LN.so")
add12u_0PX = ctypes.CDLL("basic_lib/c/add12/add12u_0PX.so")
add12u_0UZ = ctypes.CDLL("basic_lib/c/add12/add12u_0UZ.so")
add12u_0Z5 = ctypes.CDLL("basic_lib/c/add12/add12u_0Z5.so")
add12u_0ZP = ctypes.CDLL("basic_lib/c/add12/add12u_0ZP.so")
add12u_2KC = ctypes.CDLL("basic_lib/c/add12/add12u_2KC.so")
add12u_2L1 = ctypes.CDLL("basic_lib/c/add12/add12u_2L1.so")
add12u_2UF = ctypes.CDLL("basic_lib/c/add12/add12u_2UF.so")
add12u_2UH = ctypes.CDLL("basic_lib/c/add12/add12u_2UH.so")
add12u_3K3 = ctypes.CDLL("basic_lib/c/add12/add12u_3K3.so")
add12u_3L3 = ctypes.CDLL("basic_lib/c/add12/add12u_3L3.so")
add12u_3R0 = ctypes.CDLL("basic_lib/c/add12/add12u_3R0.so")
add12u_3UT = ctypes.CDLL("basic_lib/c/add12/add12u_3UT.so")
add12u_4NT = ctypes.CDLL("basic_lib/c/add12/add12u_4NT.so")
add12u_4TF = ctypes.CDLL("basic_lib/c/add12/add12u_4TF.so")
add12u_06R = ctypes.CDLL("basic_lib/c/add12/add12u_06R.so")
add12u_22J = ctypes.CDLL("basic_lib/c/add12/add12u_22J.so")
add12u_28B = ctypes.CDLL("basic_lib/c/add12/add12u_28B.so")
add12u_38J = ctypes.CDLL("basic_lib/c/add12/add12u_38J.so")
add12u_39N = ctypes.CDLL("basic_lib/c/add12/add12u_39N.so")
add12u_50U = ctypes.CDLL("basic_lib/c/add12/add12u_50U.so")
add12u_103 = ctypes.CDLL("basic_lib/c/add12/add12u_103.so")
add12u_187 = ctypes.CDLL("basic_lib/c/add12/add12u_187.so")
add12u_uint_lib = {
    "add12u_0AF": add12u_0AF,
    "add12u_0AZ": add12u_0AZ,
    "add12u_0B6": add12u_0B6,
    "add12u_0C9": add12u_0C9,
    "add12u_0G8": add12u_0G8,
    "add12u_0JK": add12u_0JK,
    "add12u_0LN": add12u_0LN,
    "add12u_0PX": add12u_0PX,
    "add12u_0UZ": add12u_0UZ,
    "add12u_0Z5": add12u_0Z5,
    "add12u_0ZP": add12u_0ZP,
    "add12u_2KC": add12u_2KC,
    "add12u_2L1": add12u_2L1,
    "add12u_2UF": add12u_2UF,
    "add12u_2UH": add12u_2UH,
    "add12u_3K3": add12u_3K3,
    "add12u_3L3": add12u_3L3,
    "add12u_3R0": add12u_3R0,
    "add12u_3UT": add12u_3UT,
    "add12u_4NT": add12u_4NT,
    "add12u_4TF": add12u_4TF,
    "add12u_06R": add12u_06R,
    "add12u_22J": add12u_22J,
    "add12u_28B": add12u_28B,
    "add12u_38J": add12u_38J,
    "add12u_39N": add12u_39N,
    "add12u_50U": add12u_50U,
    "add12u_103": add12u_103,
    "add12u_187": add12u_187,
}
add8u_1HG=ctypes.CDLL("basic_lib/c/add8/add8u_1HG.so")
add8u_6PT=ctypes.CDLL("basic_lib/c/add8/add8u_6PT.so")
add8u_0NS=ctypes.CDLL("basic_lib/c/add8/add8u_0NS.so")
add8u_0NQ=ctypes.CDLL("basic_lib/c/add8/add8u_0NQ.so")
add8u_0NH=ctypes.CDLL("basic_lib/c/add8/add8u_0NH.so")
add8u_0PA=ctypes.CDLL("basic_lib/c/add8/add8u_0PA.so")
add8u_6MZ=ctypes.CDLL("basic_lib/c/add8/add8u_6MZ.so")
add8u_0PL=ctypes.CDLL("basic_lib/c/add8/add8u_0PL.so")
add8u_0UK=ctypes.CDLL("basic_lib/c/add8/add8u_0UK.so")
add8u_05G=ctypes.CDLL("basic_lib/c/add8/add8u_05G.so")
add8u_6LG=ctypes.CDLL("basic_lib/c/add8/add8u_6LG.so")
add8u_2J3=ctypes.CDLL("basic_lib/c/add8/add8u_2J3.so")
add8u_2AM=ctypes.CDLL("basic_lib/c/add8/add8u_2AM.so")
add8u_0D0=ctypes.CDLL("basic_lib/c/add8/add8u_0D0.so")
add8u_4M7=ctypes.CDLL("basic_lib/c/add8/add8u_4M7.so")
add8u_3RE=ctypes.CDLL("basic_lib/c/add8/add8u_3RE.so")
add8u_0E2=ctypes.CDLL("basic_lib/c/add8/add8u_0E2.so")
add8u_2LL=ctypes.CDLL("basic_lib/c/add8/add8u_2LL.so")
add8u_6TH=ctypes.CDLL("basic_lib/c/add8/add8u_6TH.so")
add8u_6FT=ctypes.CDLL("basic_lib/c/add8/add8u_6FT.so")
add8u_02Y=ctypes.CDLL("basic_lib/c/add8/add8u_02Y.so")
add8u_108=ctypes.CDLL("basic_lib/c/add8/add8u_108.so")
add8u_6P8=ctypes.CDLL("basic_lib/c/add8/add8u_6P8.so")
add8u_6K6=ctypes.CDLL("basic_lib/c/add8/add8u_6K6.so")
add8u_0JM=ctypes.CDLL("basic_lib/c/add8/add8u_0JM.so")
add8u_6QU=ctypes.CDLL("basic_lib/c/add8/add8u_6QU.so")
add8u_6S4=ctypes.CDLL("basic_lib/c/add8/add8u_6S4.so")
add8u_6R6=ctypes.CDLL("basic_lib/c/add8/add8u_6R6.so")
add8u_00M=ctypes.CDLL("basic_lib/c/add8/add8u_00M.so")
add8u_6SM=ctypes.CDLL("basic_lib/c/add8/add8u_6SM.so")
add8u_0TP=ctypes.CDLL("basic_lib/c/add8/add8u_0TP.so")
add8_uint_lib= {
        'add8u_1HG': add8u_1HG,
        'add8u_6PT': add8u_6PT,
        'add8u_0NS': add8u_0NS,
        'add8u_0NQ': add8u_0NQ,
        'add8u_0NH': add8u_0NH,
        'add8u_0PA': add8u_0PA,
        'add8u_6MZ': add8u_6MZ,
        'add8u_0PL': add8u_0PL,
        'add8u_0UK': add8u_0UK,
        'add8u_05G': add8u_05G,
        'add8u_6LG': add8u_6LG,
        'add8u_2J3': add8u_2J3,
        'add8u_2AM': add8u_2AM,
        'add8u_0D0': add8u_0D0,
        'add8u_4M7': add8u_4M7,
        'add8u_3RE': add8u_3RE,
        'add8u_0E2': add8u_0E2,
        'add8u_2LL': add8u_2LL,
        'add8u_6TH': add8u_6TH,
        'add8u_6FT': add8u_6FT,
        'add8u_02Y': add8u_02Y,
        'add8u_108': add8u_108,
        'add8u_6P8': add8u_6P8,
        'add8u_6K6': add8u_6K6,
        'add8u_0JM': add8u_0JM,
        'add8u_6QU': add8u_6QU,
        'add8u_6S4': add8u_6S4,
        'add8u_6R6': add8u_6R6,
        'add8u_00M': add8u_00M,
        'add8u_6SM': add8u_6SM,
        'add8u_0TP': add8u_0TP,
}
sub10_1 =ctypes.CDLL("basic_lib/c/sub10/sub10_1.so")
sub10_5 =ctypes.CDLL("basic_lib/c/sub10/sub10_5.so")
sub10_6 =ctypes.CDLL("basic_lib/c/sub10/sub10_6.so")
sub10_15 =ctypes.CDLL("basic_lib/c/sub10/sub10_15.so")
sub10_26 =ctypes.CDLL("basic_lib/c/sub10/sub10_26.so")
sub10_65 =ctypes.CDLL("basic_lib/c/sub10/sub10_65.so")
sub10_85 =ctypes.CDLL("basic_lib/c/sub10/sub10_85.so")
sub10_90 =ctypes.CDLL("basic_lib/c/sub10/sub10_90.so")
sub10_130 =ctypes.CDLL("basic_lib/c/sub10/sub10_130.so")
sub10_135 =ctypes.CDLL("basic_lib/c/sub10/sub10_135.so")
sub10_200 =ctypes.CDLL("basic_lib/c/sub10/sub10_200.so")
sub10_210 =ctypes.CDLL("basic_lib/c/sub10/sub10_210.so")
sub10_260 =ctypes.CDLL("basic_lib/c/sub10/sub10_260.so")
sub10_270 =ctypes.CDLL("basic_lib/c/sub10/sub10_270.so")
sub10_uint_lib={
    "sub10_1":sub10_1 ,
"sub10_5":sub10_5 ,
"sub10_6":sub10_6 ,
"sub10_15":sub10_15 ,
"sub10_26":sub10_26 ,
"sub10_65":sub10_65 ,
"sub10_85":sub10_85 ,
"sub10_90":sub10_90 ,
"sub10_130":sub10_130 ,
"sub10_135":sub10_135 ,
"sub10_200":sub10_200 ,
"sub10_210":sub10_210 ,
"sub10_260":sub10_260 ,
"sub10_270":sub10_270 ,
}
add16u_0BC = ctypes.CDLL("basic_lib/c/add16u/add16u_0BC.so")
add16u_0C8 = ctypes.CDLL("basic_lib/c/add16u/add16u_0C8.so")
add16u_0EZ = ctypes.CDLL("basic_lib/c/add16u/add16u_0EZ.so")
add16u_0GN = ctypes.CDLL("basic_lib/c/add16u/add16u_0GN.so")
add16u_0GX = ctypes.CDLL("basic_lib/c/add16u/add16u_0GX.so")
add16u_0HE = ctypes.CDLL("basic_lib/c/add16u/add16u_0HE.so")
add16u_0HK = ctypes.CDLL("basic_lib/c/add16u/add16u_0HK.so")
add16u_0J3 = ctypes.CDLL("basic_lib/c/add16u/add16u_0J3.so")
add16u_0K3 = ctypes.CDLL("basic_lib/c/add16u/add16u_0K3.so")
add16u_0KG = ctypes.CDLL("basic_lib/c/add16u/add16u_0KG.so")
add16u_0KU = ctypes.CDLL("basic_lib/c/add16u/add16u_0KU.so")
add16u_0NL = ctypes.CDLL("basic_lib/c/add16u/add16u_0NL.so")
add16u_0NT = ctypes.CDLL("basic_lib/c/add16u/add16u_0NT.so")
add16u_0P8 = ctypes.CDLL("basic_lib/c/add16u/add16u_0P8.so")
add16u_0PT = ctypes.CDLL("basic_lib/c/add16u/add16u_0PT.so")
add16u_0RH = ctypes.CDLL("basic_lib/c/add16u/add16u_0RH.so")
add16u_0RJ = ctypes.CDLL("basic_lib/c/add16u/add16u_0RJ.so")
add16u_0SD = ctypes.CDLL("basic_lib/c/add16u/add16u_0SD.so")
add16u_0SL = ctypes.CDLL("basic_lib/c/add16u/add16u_0SL.so")
add16u_0TA = ctypes.CDLL("basic_lib/c/add16u/add16u_0TA.so")
add16u_0U8 = ctypes.CDLL("basic_lib/c/add16u/add16u_0U8.so")
add16u_0UV = ctypes.CDLL("basic_lib/c/add16u/add16u_0UV.so")
add16u_0VA = ctypes.CDLL("basic_lib/c/add16u/add16u_0VA.so")
add16u_1A5 = ctypes.CDLL("basic_lib/c/add16u/add16u_1A5.so")
add16u_07T = ctypes.CDLL("basic_lib/c/add16u/add16u_07T.so")
add16u_08V = ctypes.CDLL("basic_lib/c/add16u/add16u_08V.so")
add16u_15Q = ctypes.CDLL("basic_lib/c/add16u/add16u_15Q.so")
add16u_067 = ctypes.CDLL("basic_lib/c/add16u/add16u_067.so")
add16u_110 = ctypes.CDLL("basic_lib/c/add16u/add16u_110.so")
add16u_126 = ctypes.CDLL("basic_lib/c/add16u/add16u_126.so")
add16u_162 = ctypes.CDLL("basic_lib/c/add16u/add16u_162.so")
add16_uint_lib= {
        'add16u_0BC': add16u_0BC,
        'add16u_0C8': add16u_0C8,
        'add16u_0EZ': add16u_0EZ,
        'add16u_0GN': add16u_0GN,
        'add16u_0GX': add16u_0GX,
        'add16u_0HE': add16u_0HE,
        'add16u_0HK': add16u_0HK,
        'add16u_0J3': add16u_0J3,
        'add16u_0K3': add16u_0K3,
        'add16u_0KG': add16u_0KG,
        'add16u_0KU': add16u_0KU,
        'add16u_0NL': add16u_0NL,
        'add16u_0NT': add16u_0NT,
        'add16u_0P8': add16u_0P8,
        'add16u_0PT': add16u_0PT,
        'add16u_0RH': add16u_0RH,
        'add16u_0RJ': add16u_0RJ,
        'add16u_0SD': add16u_0SD,
        'add16u_0SL': add16u_0SL,
        'add16u_0TA': add16u_0TA,
        'add16u_0U8': add16u_0U8,
        'add16u_0UV': add16u_0UV,
        'add16u_0VA': add16u_0VA,
        'add16u_1A5': add16u_1A5,
        'add16u_07T': add16u_07T,
        'add16u_08V': add16u_08V,
        'add16u_15Q': add16u_15Q,
        'add16u_067': add16u_067,
        'add16u_110': add16u_110,
        'add16u_126': add16u_126,
        'add16u_162': add16u_162,
}
mul8u_0AB=ctypes.CDLL("basic_lib/c/mul8/mul8u_0AB.so")
mul8u_1A0M=ctypes.CDLL("basic_lib/c/mul8/mul8u_1A0M.so")
mul8u_1DMU=ctypes.CDLL("basic_lib/c/mul8/mul8u_1DMU.so")
mul8u_1JJQ=ctypes.CDLL("basic_lib/c/mul8/mul8u_1JJQ.so")
mul8u_1SX=ctypes.CDLL("basic_lib/c/mul8/mul8u_1SX.so")
mul8u_2NDH=ctypes.CDLL("basic_lib/c/mul8/mul8u_2NDH.so")
mul8u_2V0=ctypes.CDLL("basic_lib/c/mul8/mul8u_2V0.so")
mul8u_4TF=ctypes.CDLL("basic_lib/c/mul8/mul8u_4TF.so")
mul8u_4X5=ctypes.CDLL("basic_lib/c/mul8/mul8u_4X5.so")
mul8u_8U3=ctypes.CDLL("basic_lib/c/mul8/mul8u_8U3.so")
mul8u_12KA=ctypes.CDLL("basic_lib/c/mul8/mul8u_12KA.so")
mul8u_12YX=ctypes.CDLL("basic_lib/c/mul8/mul8u_12YX.so")
mul8u_17C8=ctypes.CDLL("basic_lib/c/mul8/mul8u_17C8.so")
mul8u_17MJ=ctypes.CDLL("basic_lib/c/mul8/mul8u_17MJ.so")
mul8u_17MN=ctypes.CDLL("basic_lib/c/mul8/mul8u_17MN.so")
mul8u_17R6=ctypes.CDLL("basic_lib/c/mul8/mul8u_17R6.so")
mul8u_18UH=ctypes.CDLL("basic_lib/c/mul8/mul8u_18UH.so")
mul8u_19XF=ctypes.CDLL("basic_lib/c/mul8/mul8u_19XF.so")
mul8u_27Y=ctypes.CDLL("basic_lib/c/mul8/mul8u_27Y.so")
mul8u_197B=ctypes.CDLL("basic_lib/c/mul8/mul8u_197B.so")
mul8u_874=ctypes.CDLL("basic_lib/c/mul8/mul8u_874.so")
mul8u_BG1=ctypes.CDLL("basic_lib/c/mul8/mul8u_BG1.so")
mul8u_C67=ctypes.CDLL("basic_lib/c/mul8/mul8u_C67.so")
mul8u_DG8=ctypes.CDLL("basic_lib/c/mul8/mul8u_DG8.so")
mul8u_GJM=ctypes.CDLL("basic_lib/c/mul8/mul8u_GJM.so")
mul8u_GTR=ctypes.CDLL("basic_lib/c/mul8/mul8u_GTR.so")
mul8u_L93=ctypes.CDLL("basic_lib/c/mul8/mul8u_L93.so")
mul8u_LK8=ctypes.CDLL("basic_lib/c/mul8/mul8u_LK8.so")
mul8u_NLX=ctypes.CDLL("basic_lib/c/mul8/mul8u_NLX.so")
mul8u_R36=ctypes.CDLL("basic_lib/c/mul8/mul8u_R36.so")
mul8u_R92=ctypes.CDLL("basic_lib/c/mul8/mul8u_R92.so")
mul8u_T83=ctypes.CDLL("basic_lib/c/mul8/mul8u_T83.so")
mul8u_TD3=ctypes.CDLL("basic_lib/c/mul8/mul8u_TD3.so")
mul8u_XFM=ctypes.CDLL("basic_lib/c/mul8/mul8u_XFM.so")
mul8u_Z9D=ctypes.CDLL("basic_lib/c/mul8/mul8u_Z9D.so")
mul8u_ZB3=ctypes.CDLL("basic_lib/c/mul8/mul8u_ZB3.so")
mul8u_ZDF=ctypes.CDLL("basic_lib/c/mul8/mul8u_ZDF.so")
mul8u_uint_lib={
                "mul8u_0AB":mul8u_0AB,
                "mul8u_1A0M":mul8u_1A0M,
                "mul8u_1DMU":mul8u_1DMU,
                "mul8u_1JJQ":mul8u_1JJQ,
                "mul8u_1SX":mul8u_1SX,
                "mul8u_2NDH":mul8u_2NDH,
                "mul8u_2V0":mul8u_2V0,
                "mul8u_4TF":mul8u_4TF,
                "mul8u_4X5":mul8u_4X5,
                "mul8u_8U3":mul8u_8U3,
                "mul8u_12KA":mul8u_12KA,
                "mul8u_12YX":mul8u_12YX,
                "mul8u_17C8":mul8u_17C8,
                "mul8u_17MJ":mul8u_17MJ,
                "mul8u_17MN":mul8u_17MN,
                "mul8u_17R6":mul8u_17R6,
                "mul8u_18UH":mul8u_18UH,
                "mul8u_19XF":mul8u_19XF,
                "mul8u_27Y":mul8u_27Y,
                "mul8u_197B":mul8u_197B,
                "mul8u_874":mul8u_874,
                "mul8u_BG1":mul8u_BG1,
                "mul8u_C67":mul8u_C67,
                "mul8u_DG8":mul8u_DG8,
                "mul8u_GJM":mul8u_GJM,
                "mul8u_GTR":mul8u_GTR,
                "mul8u_L93":mul8u_L93,
                "mul8u_LK8":mul8u_LK8,
                "mul8u_NLX":mul8u_NLX,
                "mul8u_R36":mul8u_R36,
                "mul8u_R92":mul8u_R92,
                "mul8u_T83":mul8u_T83,
                "mul8u_TD3":mul8u_TD3,
                "mul8u_XFM":mul8u_XFM,
                "mul8u_Z9D":mul8u_Z9D,
                "mul8u_ZB3":mul8u_ZB3,
                "mul8u_ZDF":mul8u_ZDF,
                }
mul8x4u_0C9=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_0C9.so")
mul8x4u_0S7=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_0S7.so")
mul8x4u_1K7=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_1K7.so")
mul8x4u_1L6=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_1L6.so")
mul8x4u_2CC=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_2CC.so")
mul8x4u_2DB=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_2DB.so")
mul8x4u_2DH=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_2DH.so")
mul8x4u_2G2=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_2G2.so")
mul8x4u_2G5=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_2G5.so")
mul8x4u_2GR=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_2GR.so")
mul8x4u_2L5=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_2L5.so")
mul8x4u_2TZ=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_2TZ.so")
mul8x4u_3BB=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_3BB.so")
mul8x4u_3BP=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_3BP.so")
mul8x4u_3CY=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_3CY.so")
mul8x4u_3N3=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_3N3.so")
mul8x4u_3NP=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_3NP.so")
mul8x4u_3RR=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_3RR.so")
mul8x4u_3UF=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_3UF.so")
mul8x4u_03J=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_03J.so")
mul8x4u_04E=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_04E.so")
mul8x4u_29A=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_29A.so")
mul8x4u_29C=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_29C.so")
mul8x4u_42Z=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_42Z.so")
mul8x4u_49L=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_49L.so")
mul8x4u_167=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_167.so")
mul8x4u_291=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_291.so")
mul8x4u_409=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_409.so")
mul8x4u_579=ctypes.CDLL("basic_lib/c/mul8_4/mul8x4u_579.so")
mul8x4u_uint_lib={
    "mul8x4u_0C9":mul8x4u_0C9,
    "mul8x4u_0S7":mul8x4u_0S7,
    "mul8x4u_1K7":mul8x4u_1K7 ,
    "mul8x4u_1L6": mul8x4u_1L6,
    "mul8x4u_2CC":mul8x4u_2CC,
    "mul8x4u_2DB":mul8x4u_2DB,
    "mul8x4u_2DH":mul8x4u_2DH,
    "mul8x4u_2G2":mul8x4u_2G2,
    "mul8x4u_2G5":mul8x4u_2G5,
    "mul8x4u_2GR":mul8x4u_2GR,
    "mul8x4u_2L5":mul8x4u_2L5,
    "mul8x4u_2TZ":mul8x4u_2TZ,
    "mul8x4u_3BB":mul8x4u_3BB,
    "mul8x4u_3BP":mul8x4u_3BP,
    "mul8x4u_3CY":mul8x4u_3CY,
    "mul8x4u_3N3":mul8x4u_3N3,
    "mul8x4u_3NP":mul8x4u_3NP,
    "mul8x4u_3RR":mul8x4u_3RR,
    "mul8x4u_3UF":mul8x4u_3UF,
    "mul8x4u_03J":mul8x4u_03J,
    "mul8x4u_04E":mul8x4u_04E,
    "mul8x4u_29A":mul8x4u_29A,
    "mul8x4u_29C":mul8x4u_29C,
    "mul8x4u_42Z":mul8x4u_42Z,
    "mul8x4u_49L":mul8x4u_49L,
    "mul8x4u_167":mul8x4u_167,
    "mul8x4u_291":mul8x4u_291,
    "mul8x4u_409":mul8x4u_409,
    "mul8x4u_579":mul8x4u_579,
}
sub2_8bit5=ctypes.CDLL("basic_lib/c/sub8/sub2_8bit5.so")
sub2_8bit10=ctypes.CDLL("basic_lib/c/sub8/sub2_8bit10.so")
sub2_8bit15=ctypes.CDLL("basic_lib/c/sub8/sub2_8bit15.so")
sub2_8bit20=ctypes.CDLL("basic_lib/c/sub8/sub2_8bit20.so")
sub2_8bit25=ctypes.CDLL("basic_lib/c/sub8/sub2_8bit25.so")
sub2_8bit30=ctypes.CDLL("basic_lib/c/sub8/sub2_8bit30.so")
sub2_8bit35=ctypes.CDLL("basic_lib/c/sub8/sub2_8bit35.so")
sub2_8bit40=ctypes.CDLL("basic_lib/c/sub8/sub2_8bit40.so")
sub2_8bit45=ctypes.CDLL("basic_lib/c/sub8/sub2_8bit45.so")
sub2_8bit85=ctypes.CDLL("basic_lib/c/sub8/sub2_8bit85.so")
sub2_8bit90=ctypes.CDLL("basic_lib/c/sub8/sub2_8bit90.so")
sub2_8bit100=ctypes.CDLL("basic_lib/c/sub8/sub2_8bit100.so")
sub_8bit5=ctypes.CDLL("basic_lib/c/sub8/sub_8bit5.so")
sub_8bit10=ctypes.CDLL("basic_lib/c/sub8/sub_8bit10.so")
sub_8bit15=ctypes.CDLL("basic_lib/c/sub8/sub_8bit15.so")
sub_8bit20=ctypes.CDLL("basic_lib/c/sub8/sub_8bit20.so")
sub_8bit25=ctypes.CDLL("basic_lib/c/sub8/sub_8bit25.so")
sub_8bit30=ctypes.CDLL("basic_lib/c/sub8/sub_8bit30.so")
sub_8bit35=ctypes.CDLL("basic_lib/c/sub8/sub_8bit35.so")
sub_8bit40=ctypes.CDLL("basic_lib/c/sub8/sub_8bit40.so")
sub_8bit45=ctypes.CDLL("basic_lib/c/sub8/sub_8bit45.so")
sub_8bit70=ctypes.CDLL("basic_lib/c/sub8/sub_8bit70.so")
sub_8bit85=ctypes.CDLL("basic_lib/c/sub8/sub_8bit85.so")
sub_8bit130=ctypes.CDLL("basic_lib/c/sub8/sub_8bit130.so")
sub8bit_lib={
"sub2_8bit5":sub2_8bit5,
"sub2_8bit10":sub2_8bit10,
"sub2_8bit15":sub2_8bit15,
"sub2_8bit20":sub2_8bit20,
"sub2_8bit25":sub2_8bit25,
"sub2_8bit30":sub2_8bit30,
"sub2_8bit35":sub2_8bit35,
"sub2_8bit40":sub2_8bit40,
"sub2_8bit45":sub2_8bit45,
"sub2_8bit85":sub2_8bit85,
"sub2_8bit90":sub2_8bit90,
"sub2_8bit100":sub2_8bit100,
"sub_8bit5":sub_8bit5,
"sub_8bit10":sub_8bit10,
"sub_8bit15":sub_8bit15,
"sub_8bit20":sub_8bit20,
"sub_8bit25":sub_8bit25,
"sub_8bit30":sub_8bit30,
"sub_8bit35":sub_8bit35,
"sub_8bit40":sub_8bit40,
"sub_8bit45":sub_8bit45,
"sub_8bit70":sub_8bit70,
"sub_8bit85":sub_8bit85,
"sub_8bit130":sub_8bit130,
}
def txt_to_dictkey(path):
    dict={}
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            dict[key] =value
    return dict
#The purpose of this function is to evaluate the WMED value of a single operator
#need : operator name
def wmed_add8(opt1):
    wmed_all=[]
    for input_a in range(0, 256):
        for input_b in range(0, 256):
            #print(input_a,input_b)
            acc = input_a + input_b
            approx = getattr(add8_uint_lib[opt1[:-3]],opt1[:-3])(ctypes.c_int64(int(input_a)), ctypes.c_int64(int(input_b)))
            error=abs(acc-approx)
            wmed_all.append(error)
    wmed_ave = sum(wmed_all) / len(wmed_all)
    return wmed_ave

def wmed_sub8(opt1):
    wmed_all=[]
    for input_a in range(0, 256):
        for input_b in range(0, 256):
            #print(input_a,input_b)
            acc = input_a - input_b
            approx = getattr(sub8bit_lib[opt1[:-3]],opt1[:-3])(ctypes.c_int64(int(input_a)), ctypes.c_int64(int(input_b)))
            error=abs(acc-approx)
            wmed_all.append(error)
    wmed_ave = sum(wmed_all) / len(wmed_all)
    return wmed_ave
def wmed_add12(opt1):
    wmed_all=[]
    for input_a in range(0, 4096):
        for input_b in range(0, 4096):
            #print(input_a,input_b)
            acc = input_a + input_b
            approx = getattr(add12u_uint_lib[opt1[:-3]],opt1[:-3])(ctypes.c_int64(int(input_a)), ctypes.c_int64(int(input_b)))
            error=abs(acc-approx)
            wmed_all.append(error)
    wmed_ave = sum(wmed_all) / len(wmed_all)
    #print(opt1)
    return wmed_ave
def wmed_add16(opt1):
    print(opt1)
    wmed_all=[]
    for idx in range(2000000):
        input_a=random.randint(0,65535)
        input_b = random.randint(0, 65535)
        acc = input_a + input_b
        approx = getattr(add16_uint_lib[opt1[:-3]],opt1[:-3])(ctypes.c_int64(int(input_a)), ctypes.c_int64(int(input_b)))
        error=abs(acc-approx)
        wmed_all.append(error)
    wmed_ave = sum(wmed_all) / len(wmed_all)
    return wmed_ave
def wmed_sub10(opt1):
    wmed_all=[]
    for input_a in range(0, 1024):
        for input_b in range(0, 1024):
            if input_a>input_b:
                acc = input_a - input_b
                approx = getattr(sub10_uint_lib[opt1[:-3]],opt1[:-3])(ctypes.c_int64(int(input_a)), ctypes.c_int64(int(input_b)))
            else:
                acc = input_b - input_a
                approx = getattr(sub10_uint_lib[opt1[:-3]],opt1[:-3])(ctypes.c_int64(int(input_b)), ctypes.c_int64(int(input_a)))
            error=abs(acc-approx)
            wmed_all.append(error)
    wmed_ave = sum(wmed_all) / len(wmed_all)
    return wmed_ave
def wmed_mul8(opt1):
    print(opt1)
    wmed_all=[]
    for input_a in range(0, 256):
        for input_b in range(0, 256):
            print(input_a,input_b)
            acc = input_a * input_b
            approx = getattr(mul8u_uint_lib[opt1[:-3]],opt1[:-3])(ctypes.c_int64(int(input_a)), ctypes.c_int64(int(input_b)))
            print(acc,approx)
            error=abs(acc-approx)
            wmed_all.append(error)
    wmed_ave = sum(wmed_all) / len(wmed_all)
    return wmed_ave
def wmed_mul8_4(opt1):
    wmed_all=[]
    for input_a in range(0, 256):
        for input_b in range(0, 16):
            #print("in",input_a,input_b)
            acc = input_a * input_b
            approx = getattr(mul8x4u_uint_lib[opt1[:-3]],opt1[:-3])(ctypes.c_int64(int(input_a)), ctypes.c_int64(int(input_b)))
            #print("out",acc,approx)
            error=abs(acc-approx)
            wmed_all.append(error)
    wmed_ave = sum(wmed_all) / len(wmed_all)
    return wmed_ave
#The role of this function is to generate the PPA of init_lib individual operators and form a dictionary
#need The path where the evaluation unit is located
def hardware_parameters(path):
    area_path=path+"area/"
    power_path=path+"power/"
    latency_path=path+"latency/"
    data_dict={}
    for filename in os.listdir(area_path):
        file_path = os.path.join(area_path, filename)
        # 确保遍历到的是文件而不是子文件夹
        if os.path.isfile(file_path):
            # 打开文件
            with open(file_path, 'r') as file:
                # 读取文件的特定行，例如第一行，可以根据需要修改
                for line in file:
                    if  area_character in line:
                        area_parameters=line.strip().split(" ")
                        break
                data_dict[filename[:-6]] = [float(area_parameters[-1])]
    for filename in os.listdir(power_path):
        file_path = os.path.join(power_path, filename)
        # 确保遍历到的是文件而不是子文件夹
        if os.path.isfile(file_path):
            # 打开文件
            with open(file_path, 'r') as file:
                # 读取文件的特定行，例如第一行，可以根据需要修改
                for line in file:
                    if power_character in line:
                        power_parameters = line.strip().split(" ")
                        #print(power_parameters[-13:-3])
                        #exit(0)
                        break
                data_dict[filename[:-6]].append(float(power_parameters[-2]))
    for filename in os.listdir(latency_path):
        file_path = os.path.join(latency_path, filename)
        # 确保遍历到的是文件而不是子文件夹
        if os.path.isfile(file_path):
            # 打开文件
            with open(file_path, 'r') as file:
                # 读取文件的特定行，例如第一行，可以根据需要修改
                for line in file:
                    if  latency_character in line:
                        latency_parameters=line.strip().split(" ")
                        break
                data_dict[filename[:-6]].append(float(latency_parameters[-1]))
    return data_dict
#The function of this function is to add the WMED specification of each arithmetic unit to the dictionary of the corresponding hardware indicator,All indicators that make up the required measurement unit
#need:the .so path of the operator
def wmed_add_dict(name):
    if name=="add8":
        path="basic_lib/c/add8"
        hardware_path = "basic_lib/report/add8/"
        hardware_dict=hardware_parameters(hardware_path)
        so_files = [file for file in os.listdir(path) if file.endswith(".so")]
        # 打印找到的.so文件
        for so_file in so_files:
            wmed_value_add8=wmed_add8(so_file)
            hardware_dict[so_file[:-3]].extend([float(wmed_value_add8)])
        return hardware_dict
            #print(so_file,wmed_value,hardware_dict)
            #exit(0)
    elif name=="sub10":
        path="basic_lib/c/sub10"
        hardware_path = "basic_lib/report/sub10/"
        hardware_dict = hardware_parameters(hardware_path)
        so_files = [file for file in os.listdir(path) if file.endswith(".so")]
        # 打印找到的.so文件
        for so_file in so_files:
            wmed_value_sub10= wmed_sub10(so_file)
            hardware_dict[so_file[:-3]].extend([float(wmed_value_sub10)])
        #print(sub10_circuit_parameters)
        return hardware_dict
    elif name=="add12":
        path="basic_lib/c/add12"
        hardware_path = "basic_lib/report/add12/"
        hardware_dict=hardware_parameters(hardware_path)
        so_files = [file for file in os.listdir(path) if file.endswith(".so")]
        # 打印找到的.so文件
        for so_file in so_files:
            print(so_file)
            wmed_value_add12=wmed_add12(so_file)
            hardware_dict[so_file[:-3]].extend([float(wmed_value_add12)])
        return hardware_dict
    elif name == "add16":
        path = "basic_lib/c/add16u"
        hardware_path = "basic_lib/report/add16/"
        hardware_dict = hardware_parameters(hardware_path)
        print("hardware end")
        so_files = [file for file in os.listdir(path) if file.endswith(".so")]
        # 打印找到的.so文件
        for so_file in so_files:
            wmed_value = wmed_add16(so_file)
            hardware_dict[so_file[:-3]].append(float(wmed_value))
        return hardware_dict
    elif name == "mul8_4":
        path = "basic_lib/c/mul8_4"
        hardware_path = "basic_lib/report/mul8_4/"
        hardware_dict = hardware_parameters(hardware_path)
        print(hardware_dict)
        so_files = [file for file in os.listdir(path) if file.endswith(".so")]
        # 打印找到的.so文件
        for so_file in so_files:
            wmed_value = wmed_mul8_4(so_file)
            hardware_dict[so_file[:-3]].append(float(wmed_value))
        return hardware_dict
    elif name == "mul8":
        path = "basic_lib/c/mul8"
        hardware_path = "basic_lib/report/mul8/"
        hardware_dict = hardware_parameters(hardware_path)
        print(hardware_dict)
        so_files = [file for file in os.listdir(path) if file.endswith(".so")]
        # 打印找到的.so文件
        for so_file in so_files:
            wmed_value = wmed_mul8(so_file)
            hardware_dict[so_file[:-3]].append(float(wmed_value))
        return hardware_dict
    elif name == "sub8":
        path = "basic_lib/c/sub8"
        hardware_path = "basic_lib/report/sub8/"
        hardware_dict = hardware_parameters(hardware_path)
        print(hardware_dict)
        so_files = [file for file in os.listdir(path) if file.endswith(".so")]
        # 打印找到的.so文件
        for so_file in so_files:
            print(so_file)
            wmed_value = wmed_sub8(so_file)
            hardware_dict[so_file[:-3]].append(float(wmed_value))
        return hardware_dict
def basic_lib_pruning(all_dict):
    area = np.empty((0,))
    power = np.empty((0,))
    latency = np.empty((0,))
    wmed = np.empty((0,))
    del_lib = np.empty((0,))

    for value in all_dict.values():
        #print(value)
        area=np.append(area,value[0])
        power=np.append(power,value[1])
        latency=np.append(latency,value[2])
        wmed=np.append(wmed,value[3])
    for area_single,power_single,latency_single,wmed_single in zip(area,power,latency,wmed):
        idx_area=np.where(area>area_single)
        idx_power = np.where(power > power_single)
        idx_latency = np.where(latency > latency_single)
        idx_wmed = np.where(wmed > wmed_single)
        del_num=reduce(np.intersect1d,[idx_wmed,idx_latency,idx_power,idx_area])
        #print(del_num)
        #print(area_single,power_single,latency_single,wmed_single)
        del_lib=np.union1d(del_num,del_lib)
        print(del_lib)
    #table=tabulate(all_dict,headers="keys",tablefmt="grid")
    #print(table)
    if len(del_lib)!=0:
        del_lib=np.around(del_lib).astype(int).tolist()
        all_name=list(all_dict.keys())
        for index in del_lib:
            if 0 <= index < len(all_name):
                del_key = all_name[index]
                #print(del_key)
                del all_dict[del_key]
            else:
                print("Invalid index")
        return all_dict
    else :
        return all_dict
area_character="Total cell area:"
power_character="Total             "
latency_character="data arrival time"
test_uint="sub8"
unit_lib="pruning_lib/uint_lib/pruning/pre_pruning_sub8.txt"
all_uint_lib="pruning_lib/uint_lib/all/pre_pruning_sub8.txt"
#all_dict=wmed_add_dict(test_uint)
#with open(all_uint_lib,"w")as file:
#    for key, value in all_dict.items():
#        file.write(f'{key}: {value}\n')
all_dict=txt_to_dictkey(all_uint_lib)
pruning_dict=basic_lib_pruning(all_dict)
with open(unit_lib, 'w') as file:
    # 遍历字典的键值对，并将其写入文件
    for key, value in pruning_dict.items():
        file.write(f'{key}: {value}\n')

