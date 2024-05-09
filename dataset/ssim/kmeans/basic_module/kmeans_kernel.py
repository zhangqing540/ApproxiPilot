import math
import numpy as np
import ctypes
import os
import random
import numpy as np
sub2_8bit5=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub2_8bit5.so")
sub2_8bit10=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub2_8bit10.so")
sub2_8bit15=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub2_8bit15.so")
sub2_8bit20=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub2_8bit20.so")
sub2_8bit25=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub2_8bit25.so")
sub2_8bit30=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub2_8bit30.so")
sub2_8bit35=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub2_8bit35.so")
sub2_8bit40=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub2_8bit40.so")
sub2_8bit45=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub2_8bit45.so")
sub2_8bit85=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub2_8bit85.so")
sub2_8bit90=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub2_8bit90.so")
sub2_8bit100=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub2_8bit100.so")
sub_8bit5=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub_8bit5.so")
sub_8bit10=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub_8bit10.so")
sub_8bit15=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub_8bit15.so")
sub_8bit20=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub_8bit20.so")
sub_8bit25=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub_8bit25.so")
sub_8bit30=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub_8bit30.so")
sub_8bit35=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub_8bit35.so")
sub_8bit40=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub_8bit40.so")
sub_8bit45=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub_8bit45.so")
sub_8bit70=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub_8bit70.so")
sub_8bit85=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub_8bit85.so")
sub_8bit130=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/sub8/sub_8bit130.so")
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
add16u_0BC = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0BC.so")
add16u_0C8 = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0C8.so")
add16u_0EZ = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0EZ.so")
add16u_0GN = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0GN.so")
add16u_0GX = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0GX.so")
add16u_0HE = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0HE.so")
add16u_0HK = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0HK.so")
add16u_0J3 = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0J3.so")
add16u_0K3 = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0K3.so")
add16u_0KG = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0KG.so")
add16u_0KU = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0KU.so")
add16u_0NL = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0NL.so")
add16u_0NT = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0NT.so")
add16u_0P8 = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0P8.so")
add16u_0PT = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0PT.so")
add16u_0RH = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0RH.so")
add16u_0RJ = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0RJ.so")
add16u_0SD = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0SD.so")
add16u_0SL = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0SL.so")
add16u_0TA = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0TA.so")
add16u_0U8 = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0U8.so")
add16u_0UV = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0UV.so")
add16u_0VA = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_0VA.so")
add16u_1A5 = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_1A5.so")
add16u_07T = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_07T.so")
add16u_08V = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_08V.so")
add16u_15Q = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_15Q.so")
add16u_067 = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_067.so")
add16u_110 = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_110.so")
add16u_126 = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_126.so")
add16u_162 = ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/add16u/add16u_162.so")
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
mul8u_0AB=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_0AB.so")
mul8u_1A0M=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_1A0M.so")
mul8u_1DMU=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_1DMU.so")
mul8u_1JJQ=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_1JJQ.so")
mul8u_1SX=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_1SX.so")
mul8u_2NDH=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_2NDH.so")
mul8u_2V0=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_2V0.so")
mul8u_4TF=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_4TF.so")
mul8u_4X5=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_4X5.so")
mul8u_8U3=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_8U3.so")
mul8u_12KA=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_12KA.so")
mul8u_12YX=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_12YX.so")
mul8u_17C8=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_17C8.so")
mul8u_17MJ=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_17MJ.so")
mul8u_17MN=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_17MN.so")
mul8u_17R6=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_17R6.so")
mul8u_18UH=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_18UH.so")
mul8u_19XF=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_19XF.so")
mul8u_27Y=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_27Y.so")
mul8u_197B=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_197B.so")
mul8u_874=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_874.so")
mul8u_BG1=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_BG1.so")
mul8u_C67=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_C67.so")
mul8u_DG8=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_DG8.so")
mul8u_GJM=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_GJM.so")
mul8u_GTR=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_GTR.so")
mul8u_L93=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_L93.so")
mul8u_LK8=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_LK8.so")
mul8u_NLX=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_NLX.so")
mul8u_R36=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_R36.so")
mul8u_R92=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_R92.so")
mul8u_T83=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_T83.so")
mul8u_TD3=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_TD3.so")
mul8u_XFM=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_XFM.so")
mul8u_Z9D=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_Z9D.so")
mul8u_ZB3=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_ZB3.so")
mul8u_ZDF=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul8/mul8u_ZDF.so")
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
mul11u_00H=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul11/mul11u_00H.so")
mul11u_00K=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul11/mul11u_00K.so")
mul11u_01Z=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul11/mul11u_01Z.so")
mul11u_03N=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul11/mul11u_03N.so")
mul11u_003=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul11/mul11u_003.so")
mul11u_05D=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul11/mul11u_05D.so")
mul11u_09Z=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul11/mul11u_09Z.so")
mul11u_024=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul11/mul11u_024.so")
mul11u_041=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul11/mul11u_041.so")
mul11u_067=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul11/mul11u_067.so")
mul11u_097=ctypes.CDLL("/home/zhangqing/approximate_opt/sim/kmeans/uint_lib/mul11/mul11u_097.so")
mul11u_uint_lib={"mul11u_00H":mul11u_00H,
                 "mul11u_00K":mul11u_00K,
                 "mul11u_01Z":mul11u_01Z,
                 "mul11u_03N":mul11u_03N,
                 "mul11u_003":mul11u_003,
                 "mul11u_05D":mul11u_05D,
                 "mul11u_09Z":mul11u_09Z,
                 "mul11u_024":mul11u_024,
                 "mul11u_041":mul11u_041,
                 "mul11u_067":mul11u_067,
                 "mul11u_097":mul11u_097,}
def sqrt_model(input,opt):
    mul91=getattr(mul11u_uint_lib[opt],opt)(ctypes.c_int64(int(256)),ctypes.c_int64(int(256)))
    #mul91=256*256
    single1=1 if input>=mul91 else 0

    input2=single1*(2**8)+2**7
    mul9_2=getattr(mul11u_uint_lib[opt],opt)(ctypes.c_int64(int(input2)),ctypes.c_int64(int(input2)))
    #mul9_2=input2*input2
    single2=1 if input>=mul9_2 else 0

    input3=single1*(2**8)+single2**7+2**6
    #mul9_3=input3*input3
    mul9_3=getattr(mul11u_uint_lib[opt],opt)(ctypes.c_int64(int(input3)),ctypes.c_int64(int(input3)))
    single3=1 if input>=mul9_3 else 0

    input4=single1*(2**8)+single2*(2**7)+single3*(2**6)+2**5
    #mul9_4=input4*input4
    mul9_4=getattr(mul11u_uint_lib[opt],opt)(ctypes.c_int64(int(input4)),ctypes.c_int64(int(input4)))
    single4=1 if input>=mul9_4 else 0

    input5=single1*(2**8)+single2*(2**7)+single3*(2**6)+single4*2**5+2**4
    #mul9_5=input5*input5
    mul9_5=getattr(mul11u_uint_lib[opt],opt)(ctypes.c_int64(int(input5)),ctypes.c_int64(int(input5)))
    single5=1 if input>=mul9_5 else 0

    input6=single1*(2**8)+single2*(2**7)+single3*(2**6)+single4*(2**5)+single5*(2**4)+2**3
    #mul9_6=input6*input6
    mul9_6=getattr(mul11u_uint_lib[opt],opt)(ctypes.c_int64(int(input6)),ctypes.c_int64(int(input6)))
    single6=1 if input>=mul9_6 else 0

    input7=single1*(2**8)+single2*(2**7)+single3*(2**6)+single4*(2**5)+single5*(2**4)+single6*(2**3)+2**2
    #mul9_7=input7*input7
    mul9_7=getattr(mul11u_uint_lib[opt],opt)(ctypes.c_int64(int(input7)),ctypes.c_int64(int(input7)))
    single7=1 if input>=mul9_7 else 0

    input8=single1*(2**8)+single2*(2**7)+single3*(2**6)+single4*(2**5)+single5*(2**4)+single6*(2**3)+single7*2**2+2**1
    #mul9_8=input8*input8
    mul9_8=getattr(mul11u_uint_lib[opt],opt)(ctypes.c_int64(int(input8)),ctypes.c_int64(int(input8)))
    single8=1 if input>=mul9_8 else 0

    input9=single1*(2**8)+single2*(2**7)+single3*(2**6)+single4*(2**5)+single5*(2**4)+single6*(2**3)+single7*(2**2)+single8*(2**1)+1
    #mul9_9=input9*input9
    mul9_9=getattr(mul11u_uint_lib[opt],opt)(ctypes.c_int64(int(input9)),ctypes.c_int64(int(input9)))
    single9=1 if input>=mul9_9 else 0
    result=single1*(2**8)+single2*(2**7)+single3*(2**6)+single4*(2**5)+single5*(2**4)+single6*(2**3)+single7*(2**2)+single8*(2**1)+single9
    return int(result)
def compute_dis_core1(xi,Z,opt_list):
    sub81 = getattr(sub8bit_lib[opt_list[0]], opt_list[0])(ctypes.c_int64(int(xi[0])), ctypes.c_int64(int(Z[0][0])))
    sub82 = getattr(sub8bit_lib[opt_list[1]], opt_list[1])(ctypes.c_int64(int(xi[1])), ctypes.c_int64(int(Z[0][1])))
    sub83 = getattr(sub8bit_lib[opt_list[2]], opt_list[2])(ctypes.c_int64(int(xi[2])), ctypes.c_int64(int(Z[0][2])))
    mul81 = getattr(mul8u_uint_lib[opt_list[3]], opt_list[3])(ctypes.c_int64(int(sub81)), ctypes.c_int64(int(sub81)))
    mul82 = getattr(mul8u_uint_lib[opt_list[4]], opt_list[4])(ctypes.c_int64(int(sub82)), ctypes.c_int64(int(sub82)))
    mul83 = getattr(mul8u_uint_lib[opt_list[5]], opt_list[5])(ctypes.c_int64(int(sub83)), ctypes.c_int64(int(sub83)))
    add16 = getattr(add16_uint_lib[opt_list[6]], opt_list[6])(ctypes.c_int64(int(mul81)), ctypes.c_int64(int(mul82)))
    add17=mul83+add16
    distance =sqrt_model(add17,opt_list[8])
    #distance=np.sqrt((xi[0]-Z[0][0])**2+(xi[1]-Z[0][1])**2+(xi[2]-Z[0][2])**2)
    return distance
def compute_dis_core2(xi,Z,opt_list):
    sub81 = getattr(sub8bit_lib[opt_list[0]], opt_list[0])(ctypes.c_int64(int(xi[0])), ctypes.c_int64(int(Z[1][0])))
    sub82 = getattr(sub8bit_lib[opt_list[1]], opt_list[1])(ctypes.c_int64(int(xi[1])), ctypes.c_int64(int(Z[1][1])))
    sub83 = getattr(sub8bit_lib[opt_list[2]], opt_list[2])(ctypes.c_int64(int(xi[2])), ctypes.c_int64(int(Z[1][2])))
    mul81 = getattr(mul8u_uint_lib[opt_list[3]], opt_list[3])(ctypes.c_int64(int(sub81)), ctypes.c_int64(int(sub81)))
    mul82 = getattr(mul8u_uint_lib[opt_list[4]], opt_list[4])(ctypes.c_int64(int(sub82)), ctypes.c_int64(int(sub82)))
    mul83 = getattr(mul8u_uint_lib[opt_list[5]], opt_list[5])(ctypes.c_int64(int(sub83)), ctypes.c_int64(int(sub83)))
    add16 = getattr(add16_uint_lib[opt_list[6]], opt_list[6])(ctypes.c_int64(int(mul81)), ctypes.c_int64(int(mul82)))
    add17 = mul83 + add16
    distance = sqrt_model(add17,opt_list[8])
    return distance

def find_ci_approx(xi,Z,opt_list):
    distance_center1 =compute_dis_core1(xi,Z,opt_list[0*9:9])
    distance_center2 =compute_dis_core2(xi,Z,opt_list[9:2*9])
    all_distance=np.array([distance_center1,distance_center2])
    min_center=np.argmin(all_distance)
    return  min_center
def find_ci(xi,Z,opt_list):
    #print(Z)
    distance_center1 =int(np.sqrt((int(xi[0])-int(Z[0][0]))**2+(int(xi[1])-int(Z[0][1]))**2+(int(xi[2])-int(Z[0][2]))**2))
    distance_center2 =int(np.sqrt((int(xi[0])-int(Z[1][0]))**2+(int(xi[1])-int(Z[1][1]))**2+(int(xi[2])-int(Z[1][2]))**2))
    all_distance=np.array([distance_center1,distance_center2])
    min_center=np.argmin(all_distance)
    return  min_center