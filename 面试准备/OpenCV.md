# OpenCV之终极临时抱佛脚

## 大纲

当使用OpenCV库进行计算机视觉和图像处理时，以下是一些常用的API功能和大纲，包括图像处理、计算机视觉、特征检测与描述等领域。请注意，OpenCV的版本可能会影响API的具体细节，所以在查找详细信息时，请参考您使用的OpenCV版本的文档。

1. 图像读写与显示

   - `cv::imread()`：读取图像文件
   - `cv::imwrite()`：保存图像文件
   - `cv::imshow()`：显示图像窗口
   - `cv::waitKey()`：等待键盘输入
2. 基本图像操作

   - 图像创建和复制
   - 通道拆分与合并
   - 图像尺寸调整和剪裁
   - 颜色空间转换（如BGR到灰度）

   以下是OpenCV中基本图像操作部分的更详细大纲：

   1. 图像创建和加载

      - 创建空白图像：`cv::Mat`
      - 从文件加载图像：`cv::imread()`
      - 创建常量图像：`cv::Mat::zeros()`、`cv::Mat::ones()`
   2. 图像复制与赋值

      - 复制图像：`cv::Mat::clone()`
      - 赋值图像：`cv::Mat::operator=()`
      - ROI（感兴趣区域）操作：`cv::Mat::row()`、`cv::Mat::col()`
   3. 通道操作

      - 通道拆分：`cv::split()`
      - 通道合并：`cv::merge()`
   4. 图像尺寸调整和剪裁

      - 调整大小：`cv::resize()`
      - 图像剪裁：`cv::Rect` 类的使用
   5. 颜色空间转换

      - BGR到灰度：`cv::cvtColor()`
      - BGR到HSV、Lab、YUV 等其他颜色空间的转换
   6. 通道拆分与合并

      - 通道拆分：`cv::split()`
      - 通道合并：`cv::merge()`
   7. 像素访问与修改

      - 使用 `.at<>()` 方法访问和修改像素值
      - 遍历图像像素：使用循环访问每个像素
      - 使用迭代器遍历图像像素
   8. 图像类型转换

      - 数据类型转换：`cv::convertTo()`
      - 数据范围缩放：`cv::normalize()`
   9. 图像深度与通道数

      - 获取图像深度：`cv::Mat::depth()`
      - 获取通道数：`cv::Mat::channels()`
   10. 填充和掩码操作

       - 填充图像：`cv::copyMakeBorder()`
       - 使用掩码进行图像操作：`cv::bitwise_and()`

   这些是基本图像操作的核心功能。您可以根据需要进一步深入研究这些操作，并查看OpenCV文档以获取更多详细信息和示例。
3. 图像处理

   - 滤波与卷积：`cv::filter2D()`、`cv::GaussianBlur()`、`cv::medianBlur()` 等
   - 直方图均衡化：`cv::equalizeHist()`
   - 阈值处理：`cv::threshold()`、`cv::adaptiveThreshold()`
   - 边缘检测：`cv::Canny()`
   - 形态学操作：腐蚀、膨胀、开运算、闭运算等
4. 几何变换

   - 旋转、平移和缩放图像：`cv::warpAffine()`
   - 透视变换：`cv::warpPerspective()`
   - 图像仿射变换：`cv::getAffineTransform()`、`cv::getPerspectiveTransform()`
5. 特征检测与描述

   - 特征点检测：SIFT、SURF、ORB、FAST、Harris 等
   - 特征描述：计算特征点的描述符
   - 特征匹配：`cv::BFMatcher`、`cv::FlannBasedMatcher`
6. 目标检测与跟踪

   - Haar 级联检测器：用于面部检测等
   - HOG+SVM：用于行人检测
   - 单目标跟踪：KLT、BOOSTING、MIL、TLD 等
   - 多目标跟踪：SORT、DeepSORT、MOT 等
7. 形状分析与轮廓检测

   - 轮廓检测：`cv::findContours()`
   - 轮廓特征：面积、周长、凸包等
   - 形状匹配：`cv::matchShapes()`
8. 图像拼接与全景图

   - 图像拼接：`cv::Stitcher`
   - 创建全景图像
9. 摄像头与视频处理

   - 摄像头捕获：`cv::VideoCapture`
   - 视频编码与保存：`cv::VideoWriter`
10. 机器学习工具

    - 机器学习模型训练与加载
    - 图像分类、对象检测、语义分割等任务
11. 深度学习集成

    - 使用 OpenCV 的深度学习模块：`dnn`
    - 加载和执行预训练的神经网络模型
12. GUI 与用户界面

    - 创建窗口和控件
    - 处理鼠标和键盘事件
13. 并行处理与优化

    - 多线程处理：`cv::parallel_for_()`
    - 使用 SIMD 指令优化图像处理

这个大纲提供了OpenCV库的一些核心功能，但OpenCV包含了更多的功能和模块，可根据特定需求进行扩展和深入研究。您可以查阅OpenCV文档以获取更详细的信息和示例代码。

## 基本操作

imread，imwrite

$ img格式:height*width*channel$

且使用的是BGR三个通道

VideoCapture

只保留一个通道的方法：

1.把剩余通道置为0<绿色的>

2.把剩余通道置为一样的<灰色的>

```python
copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
```
### 数据结构篇

#### 常见的几种存储结构
`cv::Mat`

声明方式
```cpp
Mat(int rows, int cols, int type);
// rows and cols

Mat(Size size, int type)
//size:(cols, rows)
// 2D array size: Size(cols, rows) . In the Size() constructor, the number of rows and the number of columns go in the reverse order.
// *:The cv::Point(x,y) is f**king reversed,too.It is Point(cols, rows),but surely the same. 

Mat(Size size, int type, const Scalar& s);
// both of them can be add the argument of Scalar

Mat(int ndims, const int* sizes, int type, const Scalar& s);
// the ndim is not neccesary,and it need to fit the dim of size.
// but if you use the *size to set the size of Mat,it would be needed ti add the ndim or you will get error.
```
一些成员

```cpp
cv::Mat::step
// The length of one row in RAM.
// a pic of 1920*1080*3(channels),it will have the step of 5760.
```


## 图像处理

### HSV

色相（Hue）、饱和度（Saturation）和明度（Value）

色相：0-179(uint8)，类似于色盘的角度，0 度对应红色，120 度对应绿色，240 度对应蓝色。

饱和度：0-255
      
![1694267122525](image/OpenCV/1694267122525.png)

### Canny边缘检测

#### 做平滑处理(高斯模糊)

      卷积核的数值是符合高斯分布的，如

$$
\begin{bmatrix}
 1& 2& 1\\
 2& 4& 2\\
 1& 2& 1
\end{bmatrix}
$$

#### 计算图形梯度

$$
Sobel算子
$$

$$
S_y:
\begin{bmatrix}
 1& 2& 1\\
 0& 0& 0\\
 -1& -2& -1
\end{bmatrix}
$$

*:将索贝尔算子垂直或水平翻转后不会影响结果,计算完梯度之后会取绝对值

#### 非极大值抑制

在Canny边缘检测中，选取梯度方向上相邻的两个像素分别进行梯度计算，以确定局部最大值(更清晰的边缘?)

#### 双阈值检测

用于确定真实的和潜在的边缘

1. 高阈值（High Threshold）和低阈值（Low Threshold）：首先，用户需要选择两个阈值，通常称为高阈值和低阈值。这两个阈值的选择取决于应用的具体需求和图像的特性。通常，高阈值被设置得相对较高，低阈值被设置得较低。
2. 边缘像素分类：Canny边缘检测器会将梯度幅度图中的边缘像素分为三类：

         1. 高梯度像素：梯度幅度大于或等于高阈值的像素。
         2. 低梯度像素：梯度幅度介于低阈值和高阈值之间的像素。
         3. 非边缘像素：梯度幅度小于低阈值的像素。
3. 边缘连接：接下来，通过连接高梯度像素以形成连续的边缘，并检查低梯度像素是否与高梯度像素相邻，从而确定是否将其添加到边缘中。这通常采用连通组件分析或边缘跟踪算法来完成。高梯度像素之间的连接形成了强边缘，而与强边缘连接的低梯度像素形成了弱边缘。
4. 去除孤立的弱边缘：在连接边缘之后，可能会存在一些孤立的弱边缘像素，这些边缘通常不具有实际意义。通常，可以应用一些后处理步骤来去除这些孤立的弱边缘。

![双阈值检测](canny_5.png)
*:在该图中,A和C都会被保留,B会被舍弃

### 滤波

#### 卷积滤波
      高斯滤波
$$G_{3×3}:
      1/16*\begin{bmatrix}
      1& 2& 1\\
      2& 4& 2\\
      1& 2& 1
      \end{bmatrix}
      $$

      均值滤波

$$
1/9*\begin{bmatrix}
 1& 1& 1\\
 1& 1& 1\\
 1& 1& 1
\end{bmatrix}$$

#### 别的滤波

        中值滤波:选取排序后的中间值

### 轮廓检测

#### 常用api
```cpp
cv::findContours(grayImage, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);
// the contours have the struct of "std::vector<std::vector<cv::Point>>",which is like "No.contour/No.point/cv::Point"
cv::drawContours(contourImage, contours, contourInx, color, thickness);
// If the contourInx is -1,it will draw all the Contours.
```

## 特征匹配

### 暴力匹配

        不会考的，略过

### 随机抽样一致算法

RANSAC算法的基本思想如下：

1. 从数据集中随机选择一小部分数据点（这些点称为随机样本）来估计模型的参数。

2. 使用随机样本估计模型的参数。

3. 对于所有其他数据点，计算它们到估计模型的距离，然后将距离小于某个阈值的点视为内点（即符合模型的点），距离大于阈值的点视为外点（即异常值）。

4. 统计内点的数量。

5. 如果内点数量超过了事先定义的阈值或达到了一定的置信水平，认为估计的模型是有效的，算法结束。否则，回到步骤1，重新选择随机样本，继续估计模型。

### Harris角点检测

计算自相似性

比较两个特征值的大小(
   $\lambda_{1} \ and\ \lambda_{2}$
)

        都比较大且相当:角点
        一个显著大于另一个:边
        都很小:内部

