import  numpy as np
from basic_module.gaussion.gaussion_kernel import *
'''
3*3 simga=0.8的取整模板
[[11  25 11 ]
 [25 54  25]
 [11  25 11 ]]/200
'''
def gaussian_filter(img,mul_81,mul_82,mul_83,mul_84,mul_85,mul_86,mul_87,mul_88,mul_89,add161,add162,add163,add164,add165,add166,add167,add168 ,K_size=3):
    img = np.asarray(np.uint8(img))
    if len(img.shape) == 3:
        H, W, C = img.shape
    else:
        img = np.expand_dims(img, axis=-1)
        H, W, C = img.shape

    ## Zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(float)

    tmp = out.copy()
    # filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                part=tmp[y: y + K_size, x: x + K_size, c]
                out[pad + y, pad + x, c] = gauian_kernel(part,mul_81,mul_82,mul_83,mul_84,mul_85,mul_86,mul_87,mul_88,mul_89,add161,add162,add163,add164,add165,add166,add167,add168)
    out = np.clip(out, 0, 255)
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)
    return out


def gaussian_original(img, K_size=3, sigma=1.0):
    img = np.asarray(np.uint8(img))
    if len(img.shape) == 3:
        H, W, C = img.shape
    else:
        img = np.expand_dims(img, axis=-1)
        H, W, C = img.shape

    ## Zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(float)

    K = np.array([[0.07511361,0.1238414,0.07511361],[0.1238414,0.20417996,0.1238414],[0.07511361,0.1238414,0.07511361]])
    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y, pad + x, c] = np.sum(K * tmp[y: y + K_size, x: x + K_size, c])
    out = np.clip(out, 0, 255)
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)
    return out


