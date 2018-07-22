import csv
import os
import datetime
import random

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


    for i in range(10000):
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

def write_statistic_data(Unit_area,courier,address_unit):

    if not os.path.exists("./unit_area"):
        os.makedirs("./unit_area") 
    if not os.path.exists("./courier"):
        os.makedirs("./courier") 
    if not os.path.exists("./address_unit"):
        os.makedirs("./address_unit") 

    concorrent_pwd = os.getcwd()
    os.chdir(concorrent_pwd+"/unit_area")

    for item in Unit_area:
        # print(os.getcwd())
        # print(item,Unit_area[item])
        filename = item+"_"+"Delivery_volume_day.txt"
        day_amount=sorted(Unit_area[item]["Delivery_volume_day"].items(),key=lambda abs:abs[0],reverse=False)

        writer = open(filename,"w")

        for amount in day_amount:
            string = amount[0]+"\t"+str(amount[1])+"\n"
            writer.write(string)

        filename = item+"_"+"courier.txt"
        writer = open(filename,"w")

        for courier_id in Unit_area[item]["courier"]:
            string = courier_id+"\n"
            writer.write(string)

        filename = item+"_"+"lon_lat.txt"
        writer = open(filename,"w")

        for lon_lat in Unit_area[item]["lon_lat"]:
            string = str(lon_lat[0])+"\t"+str(lon_lat[1])+"\n"
            writer.write(string)



    os.chdir(concorrent_pwd+"/courier")
    for item in courier:
        # print(item,courier[item])
        filename = item+"_"+"Delivery_volume_day.txt"
        day_amount=sorted(courier[item]["Delivery_volume_day"].items(),key=lambda abs:abs[0],reverse=False)

        writer = open(filename,"w")

        for amount in day_amount:
            string = amount[0]+"\t"+str(amount[1])+"\n"
            writer.write(string)

        filename = item+"_"+"Unit_area.txt"
        writer = open(filename,"w")

        for Unit_area in courier[item]["Unit_area"]:
            string = Unit_area+"\n"
            writer.write(string)

        filename = item+"_"+"lon_lat.txt"
        writer = open(filename,"w")

        for lon_lat in courier[item]["lon_lat"]:
            string = str(lon_lat[0])+"\t"+str(lon_lat[1])+"\n"
            writer.write(string)

    os.chdir(concorrent_pwd+"/address_unit")
    for item in address_unit:
        # print(item,address_unit[item])
        filename = item+"_"+"address.txt"
        writer = open(filename,"w")

        for address in address_unit[item]["address"]:
            string = address+"\n"
            writer.write(string)

        filename = item+"_"+"lon_lat.txt"
        writer = open(filename,"w")

        for lon_lat in address_unit[item]["lon_lat"]:
            string = str(lon_lat[0])+"\t"+str(lon_lat[1])+"\n"
            writer.write(string)


        filename = item+"_"+"addr_lon_lat.txt"
        writer = open(filename,"w")

        for entire_addr in address_unit[item]["ad_ll"]:
            string = str(entire_addr[0])+"\t"+str(entire_addr[1])+"\t"+str(entire_addr[1])+"\n"
            writer.write(string)



def read_data_v1(parentdir,filename):
    abs_dir = os.path.join(parentdir,filename)
    csv_file = csv.reader(open(abs_dir,"r"))
    flag = 0
    Unit_area = {}
    courier = {}
    address_unit = {}

    for record in csv_file:
        if flag == 0:
            flag = 1
            continue

        lon_lat = [float(item) for item in record[2].split(",")]
        # print(lon_lat)

        if record[5] not in Unit_area:
            Unit_area[record[5]] = {}
            Unit_area[record[5]]["Delivery_volume_day"] = {}
            Unit_area[record[5]]["courier"] = set()
            Unit_area[record[5]]["lon_lat"] = []

        if record[-2] not in courier:
            courier[record[-2]] = {}
            courier[record[-2]]["Delivery_volume_day"] = {}
            courier[record[-2]]["Unit_area"] = set()
            courier[record[-2]]["lon_lat"] = []
            courier[record[-2]]["lon_lat"] = []

        if record[5] not in address_unit:
            address_unit[record[5]] = {}
            address_unit[record[5]]["address"] = []
            address_unit[record[5]]["lon_lat"] = []
            address_unit[record[5]]["ad_ll"] = []


        date = [item for item in record[4].split(" ")][0]

        if date not in Unit_area[record[5]]["Delivery_volume_day"]:
            Unit_area[record[5]]["Delivery_volume_day"][date] = 0
        Unit_area[record[5]]["courier"].add(record[-2])
        Unit_area[record[5]]["lon_lat"].append(lon_lat)
        Unit_area[record[5]]["Delivery_volume_day"][date] += 1

        if date not in courier[record[-2]]["Delivery_volume_day"]:
            courier[record[-2]]["Delivery_volume_day"][date] = 0

        courier[record[-2]]["Unit_area"].add(record[5])
        courier[record[-2]]["lon_lat"].append(lon_lat)
        courier[record[-2]]["Delivery_volume_day"][date] += 1

        address_unit[record[5]]["address"].append(record[1])
        address_unit[record[5]]["lon_lat"].append(lon_lat)
        address_unit[record[5]]["ad_ll"].append([record[1],lon_lat[0],lon_lat[1]])

    write_statistic_data(Unit_area,courier,address_unit)




if __name__ == '__main__':
    fork_data("C:/Users/18735/Desktop/0721项目","test.csv")
    read_data("C:/Users/18735/Desktop/0721项目","test.csv")
