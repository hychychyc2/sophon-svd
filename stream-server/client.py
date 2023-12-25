from flask import Flask, request, jsonify
import json
import io
from io import BytesIO
import base64
import requests
import argparse

app = Flask(__name__)
infos={}
last_frame_id=0
in_thresh=3
out_thresh=5
idx=0
url = "http://0.0.0.0:8001"
result_url=""
url_len=0
result_list=[]
task_id=0
Type=0
# 定义请求头（如果有的话）
headers = {
    "Content-Type": "application/json"
}

@app.route('/flask_test/<string:task_id>', methods=['POST'])
def receive_request6(task_id):
    global Type,idx
    json_data = request.json
    results={}
    frame_id=int(json_data["mFrame"]["mFrameId"])
    results["FrameIndex"]=frame_id
        # print(json_data.keys())
    if("mSubObjectMetadatas" in json_data.keys()):
            # print(json_data["mSubObjectMetadatas"][0]["mRecognizedObjectMetadatas"][0]["mLabelName"])
        names=[str(i["mRecognizedObjectMetadatas"][0]["mLabelName"]) for i in json_data["mSubObjectMetadatas"]]
    else:
        names=[]
    src_base64=json_data["mFrame"]["mSpData"]
    results["SceneImageBase64"]=src_base64
    results["AnalyzeEvents"]=[]
    results["TaskID"]=str(task_id)
        # save_base64_image(src_base64,'gg3.jpg')
    base64s=[]
    up_list=[]
    for name in names:
            # print(name)
            # print(infos.keys())
        print(infos)
        if name in infos.keys():
            infos[name]["in"]+=1
            # print(infos[name]["in"])
            if infos[name]["in"]==in_thresh:
                up_list.append(name)      
        else :
            infos[name]={}
            infos[name]["in"]=1
            if infos[name]["in"]==in_thresh:
                up_list.append(name)
    # print(names)
        
    boxes=[]
    if("mSubObjectMetadatas" in json_data.keys()):
        for indx in range(len(json_data["mDetectedObjectMetadatas"])):
            tmp=json_data["mDetectedObjectMetadatas"][indx]
            tmp2=json_data["mSubObjectMetadatas"][indx]
            if tmp2["mRecognizedObjectMetadatas"][0]["mLabelName"] in up_list:
                result={}
                x1,y1=tmp["mBox"]["mX"],tmp["mBox"]["mY"]
                x2=x1+tmp["mBox"]["mWidth"]
                y2=y1+tmp["mBox"]["mHeight"]
                boxes.append((x1,y1,x2,y2))
                    # print(tmp2["mFrame"]["mSpData"])
                    # save_base64_image(tmp2["mFrame"]["mSpData"],'gg.jpg')
                    # result["ImageBase64"]=crop_image_base64(src_base64, (x1,y1,x2,y2))
                result["ImageBase64"]=tmp2["mFrame"]["mSpData"]
                # print(result["ImageBase64"])
                # save_base64_image(result["ImageBase64"],'gg2.jpg')

                result["Box"]={"LeftTopY": y1,
                                "RightBtmY": y2,
                                "LeftTopX": x1,
                                "RightBtmX": x2 }
                result["Type"]=Type
                result["Extend"]={}
                result["Extend"]["VehicleLicense"]=tmp2["mRecognizedObjectMetadatas"][0]["mLabelName"]
                results["AnalyzeEvents"].append(result)
    rm_list=[]
    print(infos)
    for key in infos.keys():
        if key not in names:
            if "out" in infos[key].keys():
                infos[key]["out"]+=1
                if infos[key]["out"]>=out_thresh:
                    rm_list.append(key)          
            else:
                infos[key]["out"]=1
    
    for key in rm_list:
        del infos[key]
    print(infos)
    print(up_list)

    if(len(up_list)):
        # print(idx)
        # print(url_len)
        # print(idx%url_len)
        response = requests.post(result_list[idx%url_len], json=[results], headers=headers)
        idx+=1
        idx%=url_len
        print(response)
        with open("results/"+str(task_id)+'_'+frame_id+".json", 'w') as file:
            json.dump([results], file, indent=2)
    # print(json_data)
    return jsonify({"message": "Request received and processed successfully", "response": 1})

def argsparser():
    parser = argparse.ArgumentParser(prog=__file__)
    parser.add_argument('--task_id', type=str, default="0", help='id of task')
    parser.add_argument('--type', type=int, default=0, help='type of algorithm')
    parser.add_argument('--host', type=str, default="0.0.0.0", help='ip of host')
    parser.add_argument('--port', type=int, default=11100, help='port of host')
    parser.add_argument('--url', type=str, default="", help='report url')
    args = parser.parse_args()
    return args
if __name__=="__main__":
    args = argsparser()
    task_id=args.task_id
    Type=args.type
    url="http://"+args.host+":"+str(args.port)
    result_url=args.url
    result_list=eval(result_url)
    url_len=len(result_list)
    app.run(debug=False, host='0.0.0.0', port=args.port)


