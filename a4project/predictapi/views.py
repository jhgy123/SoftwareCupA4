# Create your views here.
import sys

from django.views.decorators.csrf import csrf_exempt

sys.path.append("../PaddleRS")
import paddlers
from django.http import JsonResponse

# 检测需要的全部包： By柿子
from paddlers.deploy import Predictor
import numpy as np
import cv2
import base64
from paddlers.tasks.utils.visualize import visualize_detection


# Base64处理

def base64_cv2(base64_str, cvt_type):
    img_string = base64.b64decode(base64_str)
    np_arr = np.fromstring(img_string, np.uint8)
    image = cv2.imdecode(np_arr, cvt_type)
    return image


def cv2_base64(image):
    base64_str = cv2.imencode('.jpg', image)[1].tostring()
    base64_str = base64.b64encode(base64_str)
    return base64_str


# 目标提取颜色转换数组
def get_lut():
    lut = np.zeros((256, 3), dtype=np.uint8)
    lut[0] = [255, 0, 0]
    lut[1] = [30, 255, 142]
    lut[2] = [60, 0, 255]
    lut[3] = [255, 222, 0]
    lut[4] = [255, 255, 255]
    return lut


# 预先加载模型
model_dir = "deploy_model"  # 模型的相对路径

cdPredictor = Predictor(model_dir + "/cd", use_gpu=True)
segPredictor = Predictor(model_dir + "/seg", use_gpu=True)
tePredictor = Predictor(model_dir + "/te", use_gpu=True)
odPredictor = Predictor(model_dir + "/od", use_gpu=True)


# 变化检测
'''
接收POST，获取前端ajax请求发送的b64image1，b64image2(base64形式),
进行模型推理，返回结果图片的base64编码

'''

def change_detection_api(request):
    if request.method == 'POST':
        # 获取两张处理图的base64
        # image1 = request.POST.get('b64image1')
        # image2 = request.POST.get('b64image2')
        # image1 = bytes(image1, 'utf-8')
        # image2 = bytes(image2, 'utf-8')

        image1 = cv2.imread("E:/myProjects/new/software-cup-a4/a4project/demo_data/cd/A.png")
        image2 = cv2.imread("E:/myProjects/new/software-cup-a4/a4project/demo_data/cd/B.png")
        image1 = str(cv2_base64(image1),'utf-8')
        image2 = str(cv2_base64(image2),'utf-8')
        image1=bytes(image1,'utf-8')
        image2 = bytes(image2,'utf-8')


        ##########此处进行图片预处理与模型推理#############
        image1 = base64_cv2(image1, cv2.IMREAD_COLOR)
        image2 = base64_cv2(image2, cv2.IMREAD_COLOR)
        result = cdPredictor.predict((image1, image2))

        result = result['label_map'] * 255

        result = result.astype('uint8')

        outputimagebs64 = cv2_base64(result)
        #############################################
        # outputimagebs64:处理后输出图片base64

        data = {}
        data['status'] = 'success'  # 处理成功状态信息
        data['result'] = 'data:image/png;base64,'+str(outputimagebs64,'utf-8')#增加data:image/png;base64,才能在浏览器显示
        return JsonResponse(data)  # 向前端返回处理后图片的data数据


# 目标检测
'''
接收POST，获取前端ajax请求发送的b64image1(base64形式),
进行模型推理，返回结果图片的base64编码

'''
def object_detection_api(request):
    if request.method == 'POST':
        # 获取处理图的base64
        image1 = request.POST.get('b64image1')
        image1 = bytes(image1, 'utf-8')

        # image1 = cv2.imread("E:/myProjects/new/software-cup-a4/a4project/demo_data/od/playground_30.jpg")
        # image1 = str(cv2_base64(image1), 'utf-8')
        # image1 = bytes(image1, 'utf-8')
        ##########此处进行图片预处理与模型推理#############

        threshold = 0.2  # 检测阈值

        color = np.asarray([[0, 255, 0]], dtype=np.uint8)  # 检测结果框的颜色

        image1 = base64_cv2(image1, cv2.IMREAD_COLOR)

        result = odPredictor.predict(image1)

        result = visualize_detection(image=image1, result=result, threshold=threshold, save_dir=None, color=color)

        outputimagebs64 = cv2_base64(result)
        #############################################
        # outputimagebs64:处理后输出图片base64

        data = {}
        data['status'] = 'success'  # 处理成功状态信息
        data['result'] = 'data:image/png;base64,'+str(outputimagebs64,'utf-8')#增加data:image/png;base64,才能在浏览器显示
        return JsonResponse(data)  # 向前端返回处理后图片的data数据


# 目标提取
'''
接收POST，获取前端ajax请求发送的b64image1(base64形式),
进行模型推理，返回结果图片的base64编码

'''
def target_extraction_api(request):
    if request.method == 'POST':
        # 获取处理图的base64
        image1 = request.POST.get('b64image1')
        image1 = bytes(image1, 'utf-8')

        # image1 = cv2.imread("E:/myProjects/new/software-cup-a4/a4project/demo_data/te/input_1.png")
        # image1 = str(cv2_base64(image1), 'utf-8')
        # image1 = bytes(image1, 'utf-8')

        ##########此处进行图片预处理与模型推理#############

        image1 = base64_cv2(image1, cv2.IMREAD_COLOR)

        result = tePredictor.predict(image1)

        result = result['label_map'] * 255

        result = result.astype('uint8')

        outputimagebs64 = cv2_base64(result)
        #############################################
        # outputimagebs64:处理后输出图片base64

        data = {}
        data['status'] = 'success'  # 处理成功状态信息
        data['result'] = 'data:image/png;base64,'+str(outputimagebs64,'utf-8')#增加data:image/png;base64,才能在浏览器显示
        return JsonResponse(data)  # 向前端返回处理后图片的data数据


# 地物分类
'''
接收POST，获取前端ajax请求发送的b64image1(base64形式),
进行模型推理，返回结果图片的base64编码

'''
def classification_of_features_api(request):
    if request.method == 'POST':
        # 获取处理图的base64
        image1 = request.POST.get('b64image1')
        image1 = bytes(image1, 'utf-8')


        # image1 = cv2.imread("E:/myProjects/new/software-cup-a4/a4project/demo_data/seg/A_6.jpg")
        # image1 = str(cv2_base64(image1), 'utf-8')
        # image1 = bytes(image1, 'utf-8')

        ##########此处进行图片预处理与模型推理#############

        image1 = base64_cv2(image1, cv2.IMREAD_COLOR)

        result = segPredictor.predict(image1)

        result = result['label_map']

        lut = get_lut()

        result = lut[result]
        result=cv2.cvtColor(result,cv2.COLOR_BGR2RGB)

        outputimagebs64 = cv2_base64(result)
        #############################################
        # outputimagebs64:处理后输出图片base64

        data = {}
        data['status'] = 'success'  # 处理成功状态信息
        data['result'] = 'data:image/png;base64,'+str(outputimagebs64,'utf-8')#增加data:image/png;base64,才能在浏览器显示
        return JsonResponse(data)  # 向前端返回处理后图片的data数据


# @csrf_exempt
def ajax(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        id = request.POST.get('id')
        print(name)
        print(id)
        # 用户名和密码错误
        data = {}
        data['name'] = 'www'
        data['age'] = '11'
        return JsonResponse(data)
