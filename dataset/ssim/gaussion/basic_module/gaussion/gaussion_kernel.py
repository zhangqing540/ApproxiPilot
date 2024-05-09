import numpy as np
import ctypes
#4比特数的取值范围[0,15]
#5bit数的取值范围[0,31]
#6bit数的取值范围[0,63]
#4个4*8的乘法器，4个5*8bit的乘法器，1个6*8bit的乘法器
from ctypes import *
#12_unsigned
add16u_0BC = ctypes.CDLL("uint_lib/add16u/add16u_0BC.so")
add16u_0C8 = ctypes.CDLL("uint_lib/add16u/add16u_0C8.so")
add16u_0EZ = ctypes.CDLL("uint_lib/add16u/add16u_0EZ.so")
add16u_0GN = ctypes.CDLL("uint_lib/add16u/add16u_0GN.so")
add16u_0GX = ctypes.CDLL("uint_lib/add16u/add16u_0GX.so")
add16u_0HE = ctypes.CDLL("uint_lib/add16u/add16u_0HE.so")
add16u_0HK = ctypes.CDLL("uint_lib/add16u/add16u_0HK.so")
add16u_0J3 = ctypes.CDLL("uint_lib/add16u/add16u_0J3.so")
add16u_0K3 = ctypes.CDLL("uint_lib/add16u/add16u_0K3.so")
add16u_0KG = ctypes.CDLL("uint_lib/add16u/add16u_0KG.so")
add16u_0KU = ctypes.CDLL("uint_lib/add16u/add16u_0KU.so")
add16u_0NL = ctypes.CDLL("uint_lib/add16u/add16u_0NL.so")
add16u_0NT = ctypes.CDLL("uint_lib/add16u/add16u_0NT.so")
add16u_0P8 = ctypes.CDLL("uint_lib/add16u/add16u_0P8.so")
add16u_0PT = ctypes.CDLL("uint_lib/add16u/add16u_0PT.so")
add16u_0RH = ctypes.CDLL("uint_lib/add16u/add16u_0RH.so")
add16u_0RJ = ctypes.CDLL("uint_lib/add16u/add16u_0RJ.so")
add16u_0SD = ctypes.CDLL("uint_lib/add16u/add16u_0SD.so")
add16u_0SL = ctypes.CDLL("uint_lib/add16u/add16u_0SL.so")
add16u_0TA = ctypes.CDLL("uint_lib/add16u/add16u_0TA.so")
add16u_0U8 = ctypes.CDLL("uint_lib/add16u/add16u_0U8.so")
add16u_0UV = ctypes.CDLL("uint_lib/add16u/add16u_0UV.so")
add16u_0VA = ctypes.CDLL("uint_lib/add16u/add16u_0VA.so")
add16u_1A5 = ctypes.CDLL("uint_lib/add16u/add16u_1A5.so")
add16u_07T = ctypes.CDLL("uint_lib/add16u/add16u_07T.so")
add16u_08V = ctypes.CDLL("uint_lib/add16u/add16u_08V.so")
add16u_15Q = ctypes.CDLL("uint_lib/add16u/add16u_15Q.so")
add16u_067 = ctypes.CDLL("uint_lib/add16u/add16u_067.so")
add16u_110 = ctypes.CDLL("uint_lib/add16u/add16u_110.so")
add16u_126 = ctypes.CDLL("uint_lib/add16u/add16u_126.so")
add16u_162 = ctypes.CDLL("uint_lib/add16u/add16u_162.so")
#mul8
mul8u_0AB = ctypes.CDLL("uint_lib/mul8/mul8u_0AB.so")
mul8u_1A0M= ctypes.CDLL("uint_lib/mul8/mul8u_1A0M.so")
mul8u_1DMU= ctypes.CDLL("uint_lib/mul8/mul8u_1DMU.so")
mul8u_1JJQ= ctypes.CDLL("uint_lib/mul8/mul8u_1JJQ.so")
mul8u_1SX= ctypes.CDLL("uint_lib/mul8/mul8u_1SX.so")
mul8u_2NDH= ctypes.CDLL("uint_lib/mul8/mul8u_2NDH.so")
mul8u_2V0= ctypes.CDLL("uint_lib/mul8/mul8u_2V0.so")
mul8u_4TF= ctypes.CDLL("uint_lib/mul8/mul8u_4TF.so")
mul8u_4X5= ctypes.CDLL("uint_lib/mul8/mul8u_4X5.so")
mul8u_8U3= ctypes.CDLL("uint_lib/mul8/mul8u_8U3.so")
mul8u_12KA= ctypes.CDLL("uint_lib/mul8/mul8u_12KA.so")
mul8u_12YX= ctypes.CDLL("uint_lib/mul8/mul8u_12YX.so")
mul8u_17C8= ctypes.CDLL("uint_lib/mul8/mul8u_17C8.so")
mul8u_17MJ= ctypes.CDLL("uint_lib/mul8/mul8u_17MJ.so")
mul8u_17MN= ctypes.CDLL("uint_lib/mul8/mul8u_17MN.so")
mul8u_17R6= ctypes.CDLL("uint_lib/mul8/mul8u_17R6.so")
mul8u_18UH= ctypes.CDLL("uint_lib/mul8/mul8u_18UH.so")
mul8u_19XF= ctypes.CDLL("uint_lib/mul8/mul8u_19XF.so")
mul8u_27Y= ctypes.CDLL("uint_lib/mul8/mul8u_27Y.so")
mul8u_197B= ctypes.CDLL("uint_lib/mul8/mul8u_197B.so")
mul8u_874= ctypes.CDLL("uint_lib/mul8/mul8u_874.so")
mul8u_BG1= ctypes.CDLL("uint_lib/mul8/mul8u_BG1.so")
mul8u_C67= ctypes.CDLL("uint_lib/mul8/mul8u_C67.so")
mul8u_DG8= ctypes.CDLL("uint_lib/mul8/mul8u_DG8.so")
mul8u_GJM= ctypes.CDLL("uint_lib/mul8/mul8u_GJM.so")
mul8u_GTR= ctypes.CDLL("uint_lib/mul8/mul8u_GTR.so")
mul8u_L93= ctypes.CDLL("uint_lib/mul8/mul8u_L93.so")
mul8u_LK8= ctypes.CDLL("uint_lib/mul8/mul8u_LK8.so")
mul8u_NLX= ctypes.CDLL("uint_lib/mul8/mul8u_NLX.so")
mul8u_R36= ctypes.CDLL("uint_lib/mul8/mul8u_R36.so")
mul8u_R92= ctypes.CDLL("uint_lib/mul8/mul8u_R92.so")
mul8u_T83= ctypes.CDLL("uint_lib/mul8/mul8u_T83.so")
mul8u_TD3= ctypes.CDLL("uint_lib/mul8/mul8u_TD3.so")
mul8u_XFM= ctypes.CDLL("uint_lib/mul8/mul8u_XFM.so")
mul8u_Z9D= ctypes.CDLL("uint_lib/mul8/mul8u_Z9D.so")
mul8u_ZB3= ctypes.CDLL("uint_lib/mul8/mul8u_ZB3.so")
mul8u_ZDF= ctypes.CDLL("uint_lib/mul8/mul8u_ZDF.so")
# 将它们放入adders字典
add16= {
    "add16u_0BC": add16u_0BC,
    "add16u_0C8": add16u_0C8,
    "add16u_0EZ": add16u_0EZ,
    "add16u_0GN": add16u_0GN,
    "add16u_0GX": add16u_0GX,
    "add16u_0HE": add16u_0HE,
    "add16u_0HK": add16u_0HK,
    "add16u_0J3": add16u_0J3,
    "add16u_0K3": add16u_0K3,
    "add16u_0KG": add16u_0KG,
    "add16u_0KU": add16u_0KU,
    "add16u_0NL": add16u_0NL,
    "add16u_0NT": add16u_0NT,
    "add16u_0P8": add16u_0P8,
    "add16u_0PT": add16u_0PT,
    "add16u_0RH": add16u_0RH,
    "add16u_0RJ": add16u_0RJ,
    "add16u_0SD": add16u_0SD,
    "add16u_0SL": add16u_0SL,
    "add16u_0TA": add16u_0TA,
    "add16u_0U8": add16u_0U8,
    "add16u_0UV": add16u_0UV,
    "add16u_0VA": add16u_0VA,
    "add16u_1A5": add16u_1A5,
    "add16u_07T": add16u_07T,
    "add16u_08V": add16u_08V,
    "add16u_15Q": add16u_15Q,
    "add16u_067": add16u_067,
    "add16u_110": add16u_110,
    "add16u_126": add16u_126,
    "add16u_162": add16u_162,
}
mul8_8={
    "mul8u_0AB":mul8u_0AB,
    "mul8u_1A0M": mul8u_1A0M,
    "mul8u_1DMU": mul8u_1DMU,
    "mul8u_1JJQ": mul8u_1JJQ,
    "mul8u_1SX": mul8u_1SX,
    "mul8u_2NDH": mul8u_2NDH,
    "mul8u_2V0":mul8u_2V0,
    "mul8u_4TF": mul8u_4TF,
    "mul8u_4X5": mul8u_4X5,
    "mul8u_8U3": mul8u_8U3,
    "mul8u_12KA": mul8u_12KA,
    "mul8u_12YX": mul8u_12YX,
    "mul8u_17C8": mul8u_17C8,
    "mul8u_17MJ": mul8u_17MJ,
    "mul8u_17MN": mul8u_17MN,
    "mul8u_17R6": mul8u_17R6,
    "mul8u_18UH": mul8u_18UH,
    "mul8u_19XF": mul8u_19XF,
    "mul8u_27Y": mul8u_27Y,
    "mul8u_197B": mul8u_197B,
    "mul8u_874": mul8u_874,
    "mul8u_BG1": mul8u_BG1,
    "mul8u_C67": mul8u_C67,
    "mul8u_DG8": mul8u_DG8,
    "mul8u_GJM": mul8u_GJM,
    "mul8u_GTR": mul8u_GTR,
    "mul8u_L93": mul8u_L93,
    "mul8u_LK8": mul8u_LK8,
    "mul8u_NLX": mul8u_NLX,
    "mul8u_R36": mul8u_R36,
    "mul8u_R92": mul8u_R92,
    "mul8u_T83": mul8u_T83,
    "mul8u_TD3": mul8u_TD3,
    "mul8u_XFM": mul8u_XFM,
    "mul8u_Z9D": mul8u_Z9D,
    "mul8u_ZB3": mul8u_ZB3,
    "mul8u_ZDF": mul8u_ZDF,
}
add16_lib=["add16u_0BC","add16u_0C8","add16u_0EZ","add16u_0GN","add16u_0GX","add16u_0HE","add16u_0HK","add16u_0J3","add16u_0K3","add16u_0KG","add16u_0KU","add16u_0NL","add16u_0NT","add16u_0P8","add16u_0PT","add16u_0RH","add16u_0RJ","add16u_0SD","add16u_0SL","add16u_0TA","add16u_0U8","add16u_0UV","add16u_0VA","add16u_1A5","add16u_07T","add16u_08V","add16u_15Q","add16u_067","add16u_110","add16u_126","add16u_162"]
mul8u_lib=["mul8u_0AB","mul8u_1A0M","mul8u_1DMU","mul8u_1JJQ","mul8u_1SX","mul8u_2NDH","mul8u_2V0","mul8u_4TF","mul8u_4X5","mul8u_8U3","mul8u_12KA","mul8u_12YX","mul8u_17C8","mul8u_17MJ","mul8u_17MN","mul8u_17R6","mul8u_18UH","mul8u_19XF","mul8u_27Y","mul8u_197B","mul8u_874","mul8u_BG1","mul8u_C67","mul8u_DG8","mul8u_GJM","mul8u_GTR","mul8u_L93","mul8u_LK8","mul8u_NLX","mul8u_R36","mul8u_R92","mul8u_T83","mul8u_TD3","mul8u_XFM","mul8u_Z9D","mul8u_ZB3","mul8u_ZDF"]

def gauian_kernel(k,mul_81,mul_82,mul_83,mul_84,mul_85,mul_86,mul_87,mul_88,mul_89,add161,add162,add163,add164,add165,add166,add167,add168):
    '''
    gaussion_kernel=np.array([[0.07511361 0.1238414  0.07511361]
 [0.1238414  0.20417996 0.1238414 ]
 [0.07511361 0.1238414  0.07511361]])

    sum=np.sum(k*gaussion_kernel)

    '''
    #第一级 四个4*8的乘法器和4个5*8的乘法器
    mul_81=getattr(mul8_8[mul_81],mul_81)(ctypes.c_int64(int(k[0,0])), ctypes.c_int64(8))
    mul_82=getattr(mul8_8[mul_82],mul_82)(ctypes.c_int64(int(k[0,2])), ctypes.c_int64(8))
    mul_83 = getattr(mul8_8[mul_83], mul_83)(ctypes.c_int64(int(k[2, 0])), ctypes.c_int64(8))
    mul_84 = getattr(mul8_8[mul_84], mul_84)(ctypes.c_int64(int(k[2, 2])), ctypes.c_int64(8))
    mul_85 = getattr(mul8_8[mul_85], mul_85)(ctypes.c_int64(int(k[0, 1])), ctypes.c_int64(12))
    mul_86 = getattr(mul8_8[mul_86], mul_86)(ctypes.c_int64(int(k[1, 0])), ctypes.c_int64(12))
    mul_87 = getattr(mul8_8[mul_87], mul_87)(ctypes.c_int64(int(k[1, 2])), ctypes.c_int64(12))
    mul_88 = getattr(mul8_8[mul_88], mul_88)(ctypes.c_int64(int(k[2, 1])), ctypes.c_int64(12))
    mul_89 = getattr(mul8_8[mul_89], mul_89)(ctypes.c_int64(int(k[1, 1])), ctypes.c_int64(20 ))
    #第二级 两个12比特的加法器和两个13比特的加法器
    add16_1 = getattr(add16[add161],add161)(ctypes.c_int64(mul_81), ctypes.c_int64(mul_82))
    add16_2 = getattr(add16[add162], add162)(ctypes.c_int64(mul_83), ctypes.c_int64(mul_84))
    add16_3 = getattr(add16[add163], add163)(ctypes.c_int64(mul_85), ctypes.c_int64(mul_86))
    add16_4 = getattr(add16[add164], add164)(ctypes.c_int64(mul_88), ctypes.c_int64(mul_87))
    add16_5 = getattr(add16[add165], add165)(ctypes.c_int64(add16_1), ctypes.c_int64(add16_2))
    add16_6 = getattr(add16[add166], add166)(ctypes.c_int64(add16_3), ctypes.c_int64(add16_4))
    add16_7 = getattr(add16[add167], add167)(ctypes.c_int64(add16_5), ctypes.c_int64(add16_6))
    sum = getattr(add16[add168], add168)(ctypes.c_int64(add16_7), ctypes.c_int64(mul_89))

    return sum/100
