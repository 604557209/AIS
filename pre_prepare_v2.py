# -*- coding: utf-8 -*-

import csv
import os
import datetime
import random
import json


#把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d-%H")

#把字符串转成datetime
def string_toDatetime(string):
    return datetime.datetime.strptime(string, "%Y/%m/%d %H:%M")

#把字符串转成时间戳形式
def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())

#把时间戳转成字符串形式
def timestamp_toString(stamp):
    return time.strftime("%Y-%m-%d-%H", tiem.localtime(stamp))

#把datetime类型转外时间戳形式
def datetime_toTimestamp(dateTim):
    return time.mktime(dateTim.timetuple())


def fork_data(parentdir,filename):
    abs_dir = os.path.join(parentdir,filename)
    out = open(abs_dir,"w",newline="")
    csv_writer = csv.writer(out,dialect='excel')

    record_title = ['运单ID', '地址', '经纬度', '任务开始时间', '任务结束时间', '单元区域', '工号', '班次']
    csv_writer.writerow(record_title)

    address_prefix = "广东省深圳市罗湖区太宁路喜荟城一楼"
    address_suffix = "号"


    for i in range(1000):
        waybill_ID = "123"
        number = random.randint(1,150)
        address = address_prefix+str(number)+address_suffix
        lon = random.uniform(114.330, 113.340)
        lon = round(lon,6)
        lat = random.uniform(23.340, 23.350)
        lat = round(lat,6)

        lon_lat = str(lon)+","+str(lat)

        day = random.randint(1,200)

        now=datetime.datetime.now()
        delta=datetime.timedelta(days=day)
        n_days=now+delta
        time_string = n_days.strftime('%Y/%m/%d %H:%M')
        unit_area = "755XY"+str(random.randint(100,200))

        work_number = str(random.randint(61000,62000))

        shift = str(random.randint(1000,1100))

        record = [waybill_ID,address,lon_lat,time_string,time_string,unit_area,work_number,shift]

        csv_writer.writerow(record)

def write_statistic_data(Unit_area,courier):

    if not os.path.exists("./unit_area"):
        os.makedirs("./unit_area") 
    if not os.path.exists("./courier"):
        os.makedirs("./courier") 


    pre_dir = os.getcwd()
    concorrent_pwd = pre_dir+"/unit_area"
    
    for item in Unit_area:

        parentdir = concorrent_pwd+"/"+item

        if not os.path.exists(parentdir):
            os.makedirs(parentdir)

        os.chdir(parentdir)               
        day_amount=sorted(Unit_area[item].items(),key=lambda abs:abs[0],reverse=False)
        for day in day_amount:
            # print(day[1])
            day[1]["courier"] = list(day[1]["courier"])
            str_json = json.dumps(day[1],ensure_ascii=False)

            filename = ("").join([item for item in day[0].split("/")])+".json"

            with open(filename,'w') as json_file:
                json_file.write(str_json)

    concorrent_pwd = pre_dir+"/courier"
    for item in courier:

        parentdir = concorrent_pwd+"/"+item

        if not os.path.exists(parentdir):
            os.makedirs(parentdir)

        os.chdir(parentdir)



        day_amount=sorted(courier[item].items(),key=lambda abs:abs[0],reverse=False)
        for day in day_amount:
            # print(day[1])
            day[1]["Unit_area"] = list(day[1]["Unit_area"])
            str_json = json.dumps(day[1],ensure_ascii=False)

            filename = ("").join([item for item in day[0].split("/")])+".json"

            with open(filename,'w') as json_file:
                json_file.write(str_json)
def read_data(parentdir,filename):

    abs_dir = os.path.join(parentdir,filename)
    csv_file = csv.reader(open(abs_dir,"r"))

    flag = 0
    Unit_area = {}
    courier = {}
    address_unit = {}

    for record in csv_file:
        if flag == 0:
            print(record)
            flag = 1
            continue

        lon_lat = [float(item) for item in record[2].split(",")]
        date = [item for item in record[4].split(" ")][0]

        if record[5] not in Unit_area:
            Unit_area[record[5]] = {}

        if date not in Unit_area[record[5]]:
            Unit_area[record[5]][date] = {}
            Unit_area[record[5]][date]["courier"] = set()
            Unit_area[record[5]][date]["lon_lat"] = []
            Unit_area[record[5]][date]["ad_ll"] = []
            Unit_area[record[5]][date]["count"] = 0

        Unit_area[record[5]][date]["courier"].add(record[-2])
        Unit_area[record[5]][date]["lon_lat"].append(lon_lat)
        temp = [record[1]]
        temp.extend(lon_lat)
        Unit_area[record[5]][date]["ad_ll"].append(temp)
        Unit_area[record[5]][date]["count"] += 1



        if record[-2] not in courier:
            courier[record[-2]] = {}
        if date not in courier[record[-2]]:

            courier[record[-2]][date] = {}
            courier[record[-2]][date]["Unit_area"] = set()
            courier[record[-2]][date]["lon_lat"] = []
            courier[record[-2]][date]["ad_ll"] = []
            courier[record[-2]][date]["count"] = 0


        courier[record[-2]][date]["Unit_area"].add(record[5])
        courier[record[-2]][date]["lon_lat"].append(lon_lat)
        temp = [record[1]]
        temp.extend(lon_lat)
        courier[record[-2]][date]["ad_ll"].append(temp)
        courier[record[-2]][date]["count"] += 1


    # for item in Unit_area:
    #     print(item,Unit_area)


    write_statistic_data(Unit_area,courier)
    # write_statistic_data(Unit_area,courier,address_unit)
 



if __name__ == '__main__':
    # fork_data("C:/Users/18735/Desktop/0721项目","test.csv")
    read_data("C:/Users/18735/Desktop/0721项目","test.csv")
