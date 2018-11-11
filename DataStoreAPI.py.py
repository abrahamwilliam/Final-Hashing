from flask import Flask,jsonify,request
import json
import sys

app = Flask(__name__)
list=[]

@app.route('/api/v1/entries')
def hello_world():
    global list
    list.append({'417ba95980eddc371bfe2f4ed656f92954cf70eb': '2016,Accidents (unintentional injuries) (V01-X59,Y85-Y86),Unintentional injuries,Alabama,2755,55.50'})
    list.append({'f4cfad804fc9e84f187566059ea096b86ac5ad14': '2016,Accidents (unintentional injuries) (V01-X59,Y85-Y86),Unintentional injuries,Alaska,439,63.10'})
    dic={}
    dic["entries"] = list
    dic["num_entries"] = len(list)
    return jsonify(dic)

@app.route('/users/data', methods = ['POST'])
def posted():
    global list
    print(request.json)
    list.append(request.json)


    # print(dix["f4cfad804fc9e84f187566059ea096b86ac5ad14"])
    # listNew=request.data;
    # for key,val in request.data:
    #     dix[key]=val
    # print(dix)

    # dic[num_entries]=
    # dic[entries]=list
    return "thanks",201


if __name__ == '__main__':
    pr_nb=sys.argv[1]
    app.run(debug=True,port=pr_nb)
