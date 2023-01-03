from flask import Flask, render_template,request,redirect

app = Flask(__name__)

dic=[{"title":"This is the title 2","content":"this is the content 2","published":True,"id":2,"created_at":"2022-12-15T08:41:44.888493+05:30"},{"title":"This is the title 4","content":"this is the content 4","published":True,"id":4,"created_at":"2022-12-15T08:42:21.689495+05:30"},{"title":"This is the title 5","content":"this is the content 5","published":True,"id":5,"created_at":"2022-12-15T08:42:29.122437+05:30"},{"title":"This is the title 6","content":"this is the content 6","published":True,"id":6,"created_at":"2022-12-15T08:48:46.036579+05:30"},{"title":"This is the title 7","content":"this is the content 7","published":True,"id":7,"created_at":"2022-12-15T08:49:36.170970+05:30"},{"title":"This is the title 8","content":"this is the content 8","published":True,"id":8,"created_at":"2022-12-15T08:54:30.602010+05:30"},{"title":"hi again","content":"hello again","published":True,"id":3,"created_at":"2022-12-15T08:42:15.566597+05:30"},{"title":"This is the title 9","content":"this is the content 9","published":True,"id":9,"created_at":"2022-12-15T22:42:46.765041+05:30"},{"title":"This is the title 11","content":"this is the content 11","published":True,"id":11,"created_at":"2022-12-15T22:45:41.168004+05:30"},{"title":"This is the title 12","content":"this is the content 12","published":True,"id":12,"created_at":"2022-12-15T22:47:57.880590+05:30"},{"title":"This is the title 13","content":"this is the content 13","published":True,"id":13,"created_at":"2022-12-15T22:52:03.893427+05:30"},{"title":"This is the title 14","content":"this is the content 14","published":True,"id":14,"created_at":"2022-12-15T22:53:24.159921+05:30"},{"title":"Nineth post updated","content":"This is the content for Nineth post","published":True,"id":10,"created_at":"2022-12-15T22:45:05.874094+05:30"}]
@app.route("/",methods=['post'])
def create():
    return dic


# @app.route("/<id>",methods=["POST","GET"])
# def create_user(id):
#     name=request.json.get("name")
#     mobile=request.json.get("mobile")
#     about=request.json.get("about")
#     temp={"name":name,"mobile":mobile,"about":about}
#     id=int(id)
#     if id<len(dic)-1:
#         dic[int(id)]=temp 
#         return dic
#     else:
#         return "no index found"

@app.route("/<id>",methods=["POST","GET"])
def create_user(id):
    id=int(id)
    if id<len(dic)-1:
        dic[id]["title"]=request.json.get("title")
        dic[id]["content"]=request.json.get("content")
        dic[id]["published"]=request.json.get("published")
        dic[id]["id"]=request.json.get("id")
        dic[id]["created_at"]=request.json.get("created_at")
        return dic
    else:
        return "no index found"
        
if __name__=="__main__":
    app.run(debug=True)