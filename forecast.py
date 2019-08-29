"""妙啊天气预报桌面系统"""
#导入相关模块
import io
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
import requests
 
 
def resize( w_box, h_box, pil_image):
    """调整图片大小,适应窗体大小"""
    """arg:: w_box:new width h_box:new height pil_image:img"""
    w, h = pil_image.size #获取图像的原始大小
    f1 = 1.0*w_box/w
    f2 = 1.0*h_box/h
    factor = min([f1, f2])
    width = int(w*factor)
    height = int(h*factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)
 
def cherishCallBack():
    """祝福语"""
    messagebox.showinfo("欢迎小娇贵","你好啊，美女，早上好！")
 
def searchWeather():
    """查询天气"""
    if txt_city.get() == '':
        messagebox.showinfo("提示","你要先输入城市哦~~小娇贵")
        return
    inputcity = txt_city.get()  #得到输入框的文字
    url = "http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?"%inputcity   #完善url
    respnse = requests.get(url) #访问并接收数据
    weather_result = respnse.json() #返回json数据
    #解析数据
    curdate ="当前日期:" + weather_result['date']  #得到当前日期
    weather_detail = weather_result['results']
    basicdata = weather_detail[0]
    city = "城市:" + basicdata['currentCity']  #得到当前城市
    pm = "当前pm:" + basicdata['pm25']   #得到pm2.5数值
    result1 = weather_detail[0]
    weather_data = result1['weather_data']
    data = weather_data[0]
    wind = "今日风向:" + data['wind']      #得到风向
    weather = "天气状况:" + data['weather']     #得到天气
    tempdata =data['temperature']
    tempmax = tempdata[0:2] #得到最高温度
    tempmin = tempdata[5:7] #得到最低温度
    temperature = "当前温度:" + data['temperature']  #得到温度
    weather_data_list = [curdate,city,pm,temperature,wind,weather]  #将这些信息放进list里面
    tmpmax = int(tempmax)
    tmpmin = int(tempmin)
    if 20 < tmpmax <30 and 15 <tmpmin < 20:
        tip = "tip:今天很舒服~ 不冷"
    else:
        tip = "tip:今天冷了，多穿衣服啊"
    #将内容显示在窗体上
    weatherlistbox = tkinter.Listbox(root,height=len(weather_data_list) + 1,SelectionMode=None)
    i = 0
    for item in weather_data_list:
        weatherlistbox.insert(i,item)
        i = i + 1
    weatherlistbox.insert(6,tip)
    weatherlistbox.place(x = 250 ,y = 220)
 
#初始化窗体
root = tkinter.Tk()
root.geometry("600x500") #设置窗口大小
root.resizable(width=False,height=False)#设置不可拉伸
root.title("妙啊专属天气预报")#设置标题
 
#添加背景图片
canvas = tkinter.Canvas(root,width = 600,height = 500,bg='white') #设置canvas
pil_image = Image.open('background.jpg') #打开背景图片
pil_image_resize = resize(600,500,pil_image) #将它放大保存
im = ImageTk.PhotoImage(pil_image_resize)
canvas.create_image(300,250,image = im) #将图片加载到canvas来
canvas.place(x=0,y=0,width=600,height=500)#放到屏幕当中
 
#添加按钮:
btn_welcome = tkinter.Button(text="点我看看",command = cherishCallBack)
btn_welcome.place(x = 270,y = 30, width = 60, height = 30)
btn_search = tkinter.Button(text="查询一下天气咯",command = searchWeather)
btn_search.place(x = 420,y = 150, width = 90, height = 30)
 
#添加文字：
lbl_welcome = tkinter.Label(root,text="欢迎来到这儿!") #label使用方法
lbl_welcome.place(x = 260,y = 90,width = 80,height = 30)
lbl_weather = tkinter.Label(root,text="请输入你的城市：")
lbl_weather.place(x = 60,y = 150,width = 100,height = 30)
 
#添加文本框
txt_city = tkinter.Entry(root)
txt_city.place(x = 250,y = 150,width = 100,height = 30)
 
root.mainloop()