import numpy as np
def conv2d(im, kernel, stride =1):    
    # 请完成本函数代码
    
    ker=kernel
    #UnboundLocalError: local variable 'ker' referenced before assignment
    #solution:把欲用的global variance(即ker) 在local context内重新赋值——ker=kernel
    
    h=len(ker)
    #h为K(卷积核)矩阵的行数（列表长度）；
    w=len(ker[0])
    #w为K（卷积核）矩阵的列数(列表中每个元素的长度)
    im_out=[]
    new_ker=np.zeros((w,h))
    for i in range(h):#1.翻转核矩阵
        for j in range(w):
            new_ker[i][j]=ker[h-i-1][w-j-1]
    #K′[i][j]=K[h−i−1][w−j−1]
    ker=new_ker
    #——————核矩阵翻转完成——————
    #print(ker)

    h=len(ker)
    w=len(ker[0])
    #h为K`(翻转卷积核)矩阵的行数（列表长度）；
    #w为K`（翻转后卷积核）矩阵的列数(列表中每个元素的长度)
    H=len(im)
    W=len(im[0])
    #H为im矩阵的行数
    #W为im矩阵的列数
    
    h1=int((H-h)/stride)+1
    #惊了我，"H--h"居然等价于"H+h"，我说怎么h1比H还大，以至于后面卷积老是出现IndexError……
    w1=int((W-w)/stride)+1
    #计算im_out的行数h1和列数w1
    #h1=floor((H-h)/垂直方向步长)+1 行
    #w1=floor((W-w)/水平方向步长)+1 列

    unit=0
    im_out=np.zeros((h1,w1))
    #构造h1行w1i列的m_out零矩阵，以便于承接卷积后（i，j）的值
    for i in range(0,h1,stride):
        for j in range(0,w1,stride):
            #从左上角开始，在图像上从左到右、从上到下滑动：每次向右滑动移动的步长为stride
            for u in range(h):
                for v in range(w):
                    unit+=im[i+u][j+v]*ker[u][v]
                    print(unit)
                    #将K′和其覆盖的im的对应位置的元素相乘并求和，作为这个位置的响应值，即unit
            im_out[i][j]=unit
            #把响应值存入im_out对应位置（i，j）
            unit=0
            #清空上个位置的响应值unit
    return im_out



im = [[1, 1, 0, 0],
             [1, 1, 0, 0],
             [0, 0, 1, 1],
             [0, 0, 1, 1]]
K = [[1, 1],
      [1, 1]]
print(conv2d(im, K, 2))