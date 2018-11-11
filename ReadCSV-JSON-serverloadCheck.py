from flask import request
import json
import csv as csv
import hashlib
import requests
import json
import csv as csv
import hashlib
import requests

# @app.route('/todo/api/v1.0/tasks', methods=['POST'])

ip=[5000,5001,5002,5003]
hashIpvalue={}
finaldatalist=[]


def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

def read_csv(file, json_file, format):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        write_json(csv_rows, json_file, format)


def hashing(datas):
    global finaldatalist
    global hashIpvalue

    destPort=0
    for data in datas:
        list=[]
        for d in data.values():
            list.append(d)

        ourhash=findHash(list)
        for i,has in hashIpvalue:
            if int(has)>int(ourhash) :
                destPort=hashIpvalue[has]
                final="/users/data"
                url="http://127.0.0.1:"+ destPort+final
                year = list[0]
                allCauses = list[1]
                causeName = list[2]
                state = list[3]
                death = list[4]
                ageAdjustedDeath = list[5]

                r=requests.post(url,data={})





        year = list[0]
        allCauses = list[1]
        causeName = list[2]
        state = list[3]
        death = list[4]
        ageAdjustedDeath = list[5]

        res = year + ',' + allCauses + ',' + causeName + ',' + state + ',' + death + ',' + ageAdjustedDeath
        dic[hash.hexdigest()] = res
        finaldatalist.append(dic)

    print(finaldatalist)



def findHash(list):
    dic={}
    list1=[]
    year=list[0]
    allCauses=list[1]
    causeName=list[2]
    state=list[3]
    death=list[4]
    ageAdjustedDeath=list[5]
    hash=hashlib.sha1()
    hash.update(year.encode("utf-8"))
    hash.update(causeName.encode("utf-8"))
    hash.update(state.encode("utf-8"))
    res=year+','+allCauses+','+causeName+','+state+','+death+','+ageAdjustedDeath
    return hash.hexdigest()
    #
    # print(dic)
    # print("the isps arae")

    # return dic




def hashIps():
    global ip
    global hashIpvalue
    hash = hashlib.md5()
    for ips in ip:
        hash.update(str(ips).encode("utf-8"))
        hashValue=hash.hexdigest()
        hashIpvalue[ips]=hashValue
    # print(hashIpvalue)


# not needed
def findrightServer():
    hashIps()
    global hashIpvalue
    global finaldatalist
    print("final server")
    # print(finaldatalist)
    # print(hashIpvalue)
    for singlerecord in finaldatalist:
        print(singlerecord)






#Convert csv data into json and write it
def write_json(data, json_file, format):
    with open(json_file, "w") as f:
        hashedData=hashing(data)
        if format == "pretty":
            f.write(json.dumps(hashedData))
        else:
            f.write(json.dumps(hashedData))

#             , sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False





def start():
    source = "cod.csv"
    destination = "causes-of-death1.json"
    read_csv(source, destination, "pretty")
    hashIps()
    # findrightServer()



if __name__ == '__main__':
    # app.run()
    start()


