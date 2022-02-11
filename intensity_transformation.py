import numpy as np

def inverse_image(input):
    '''
    Image Negatives
    反色变换，可增强暗色背景图像中的明亮区域
    '''
    max_value = np.max(input)
    output = max_value - input
    return output

def log_image(input):
    '''
    Log Transformation
    对数变换，压缩图像矩阵值域的动态范围，可以显示更多的图像细节
    '''
    return np.log(1+input)

def gamma_trans(input, gamma=2, eps=0):
    '''
    Gamma/Power-Law Transformation
    伽马/幂指变换
    '''
    return 255. * (((input+eps)/255) ** gamma)