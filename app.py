
from flask import Flask, jsonify ,request


app = Flask(__name__)

tasks= [
    {
       'id':1,
        'title':'techskills',
        'description':'c,html,java',
        
  
    },
    {
        'id':2,
        'title':'students',
        'discription':'ankita,mehak,riya',
    }
]

@app.route("/")
def hi():
    return "Hi!" 

@app.route("/add-data",methods=["POST"])
def add_data():
    
    
    task = {
       'id':tasks[-1]['id'] + 1,
       'title':request.json['title'],
       'discription': request.json['discription']
    

    }
    tasks.append(task)
    return jsonify({
       "status":"success",
       "message":"data has been added"
    })

@app.route("/get-data")
def get_data():
    return jsonify({
        "data": tasks
    })

if  (__name__== "__main__"):
    app.run(debug=True)  