from docutils.nodes import danger
import json
import csv as csv
import hashlib
import requests
import operator
from flask import Flask,jsonify
# import urllib
# import urllib2


ip=[5000,5001,5002,5003]
hashIpvalue={}
finaldatalist=[]
count=0






def read_csv(file, json_file, format):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        write_json(csv_rows, json_file, format)


#Convert csv data into json and write it
def write_json(data, json_file, format):
    with open(json_file, "w") as f:
        hashedData=hashing(data)
        if format == "pretty":
            f.write(json.dumps(hashedData))
        else:
            f.write(json.dumps(hashedData))







def hashing(datas):
    global finaldatalist
    global hashIpvalue
    print(datas)
    for data in datas:
        list = []
        for d in data.values():
            list.append(d)
        portHashList=getPort(list)
        dataToBePosted,port=prepareData(portHashList,list)
        print(" ------------------------------------------Data To be posted=================================================")
        print(portHashList)
        print("the data is s       =================================================")
        print(dataToBePosted)
        print(port)
        url='http://127.0.0.1:'+str(port)+'/users/data'


        r = requests.post(url, json=dataToBePosted)

        # url = 'http://127.0.0.1:5000/users/data'
        # data = urllib.urlencode({'login': 'MyLogin', 'password': 'MyPassword'})
        # req = urllib2.Request(url, data)
        # response = urllib2.urlopen(req)
        # d = response.read()
        print( r.status_code)
        print(count)



def prepareData(portHashList,list):
    dic={}
    year = list[0]
    allCauses = list[1]
    causeName = list[2]
    state = list[3]
    death = list[4]
    ageAdjustedDeath = list[5]
    res = year + ',' + allCauses + ',' + causeName + ',' + state + ',' + death + ',' + ageAdjustedDeath
    port=0
    hash=0
    for val in portHashList:
        if val>5050:
            hash=val
        else:
            port=val
    dic[str(hash)] = res
    global count
    count=count+1
    return dic,port



def getPort(list):
    year = list[0]
    allCauses = list[1]
    causeName = list[2]
    state = list[3]
    death = list[4]
    ageAdjustedDeath = list[5]
    hash = hashlib.sha1()
    maxval={}
    for ipv in ip:
        hash.update(str(ipv).encode("utf-8"))
        hash.update(year.encode("utf-8"))
        hash.update(causeName.encode("utf-8"))
        hash.update(state.encode("utf-8"))
        maxval[int(hash.hexdigest(),16)]=ipv

    print(maxval)
    # sorted_x = sorted(maxval.items(), key=operator.itemgetter(1),reverse=True)
    sorted_x = sorted(maxval.items(), reverse=True)
    print("the hashed max valeuare ar")
    print(sorted_x)
    ipHashList=[]
    for i in sorted_x:
        ipHashList.append(i)
        break
    # print(ipHashList)
    a=0
    final=[]
    for k in ipHashList:
        for f in k:
            a=f
            final.append(f)

    # print(final)
    return final










# reding the csv file
def start():
    source = "causes-of-death.csv"
    destination = "causes-of-death.json"
    read_csv(source, destination, "pretty")



if __name__ == '__main__':
    # app.run()
    start()
