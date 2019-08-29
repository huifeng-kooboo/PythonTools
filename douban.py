'''爬取豆瓣图书前250名'''
#author :ytouch
#date:2019/4/29
 
import requests
import random
from lxml import etree
 
'''Func:爬取豆瓣信息'''
def getBookInfo(i):
    #param1:页数
    url = 'https://book.douban.com/top250?start={}'.format(i*25) #输入对应的url
    data = requests.get(url).text #获取页面html信息
    info = etree.HTML(data) #解析Html
    cur_books = info.xpath('/html/body/div[3]/div[1]/div/div[1]/div/table')
    record_file = open('E:/record{}.txt'.format(i + 1), 'w',encoding='utf-8') #新建txt文件，用于写入爬虫信息
    for div in cur_books:
        name = div.xpath('./tr/td[2]/div[1]/a/@title')[0]     #图书名
        book_name = str(name) #得到图书名
        author_info = div.xpath('./tr/td[2]/p[1]/text()')[0]        #作者信息
        author_info_msg = str(author_info) #强制类型转换str：用于方便写入到txt文件当中
        info_list = author_info_msg.split('/')
        cur_count = len(info_list) #获得count长度
        cur_price = info_list[cur_count-1] #获得当前价格
        publish_date = info_list[cur_count-2] #获得出版时间
        publish_type = info_list[cur_count-3] #获得出版社信息
        writer_name = '' #作者姓名
        nums_book = random.randint(3,10)#产生册数（利用随机数）
        book_num_str = str(nums_book)
        for j in range(0,cur_count-3): #由于前面作者数量不确定，故采取遍历形式
            writer_name += info_list[j]
        #写入信息到txt文本
        record_file.write('图书名:'+ book_name +' 作者:'+ writer_name + ' 出版社:'+publish_type +' 出版日期:'+publish_date + ' 册数：'+book_num_str+' 价格:'+cur_price) #记录信息
        record_file.write('\n') #换行输入
    record_file.close() #使用后一定要关闭文件
 
 
if __name__ == '__main__':
    for j in range(0,10): #遍历 因为有10页
        getBookInfo(j)