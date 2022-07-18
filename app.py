from flask import Flask, jsonify, request
from flask_cors import CORS
import controller
from db import create_table

app = Flask(__name__) 
CORS(app)

@app.route('/ping', methods=["GET"])                       ### End point for fetching server status
def server_status():
    return jsonify({'success':True})


"""
Api : Fetch todo list
Method: GET
Response: JSON object containing the list of todos
"""
@app.route('/todo/getall',methods=['GET'])
def getTasks():
    todos = controller.get_todos()
    return jsonify(todos)

"""
Api : Insert todo 
Method: POST
Response: Message and Status (true/false)
"""    
@app.route('/todo/create',methods=['POST'])
def createTask():
    task_details = request.get_json()
            
    task = task_details["task"]
    status = task_details["status"]    
    if task == "" or status == "":
        resp = jsonify({'message' : 'One or more required fields is missing.'})
        resp.status_code = 415
        return resp
    else:  


        result = controller.insert_todo(task, status)
        resp = jsonify({'message' : 'Successfully added to task to TODO List.'})
        resp.status_code = 200
        return resp 

"""
Api : Update todo
Method: PUT
Accept-type: Json-object 
Response: Message and Status (true/false)
"""
@app.route('/todo/update',methods=['PUT'])
def updateTask():
    task_details = request.get_json()
    id = task_details["id"]
    status = task_details["status"]    
    if id =="" or status=="":
       
        resp = jsonify({'message' : 'One or more required fields is missing.'})
        resp.status_code = 415
        return resp
    else:          

        result = controller.update_task(id, status)
        resp = jsonify({'message' : 'Successfully added to task to TODO List.'})
        resp.status_code = 200
        return resp        
        

@app.route('/todo/delete/<id>',methods=['DELETE'])
def deleteTask(id):
    result = controller.delete_todo(id)
    resp = jsonify({'message' : 'Successfully deleted the task.'})
    resp.status_code = 200
    return resp

@app.route("/todo/filter/<status>", methods=["GET"])
def getTodoByStatus(status):
    todos = controller.filter_todo(status)
    return jsonify(todos), 200    

@app.route("/todo/search/<query>", methods=["GET"])
def getTodoByQuery(query):
    todos = controller.search_todo(query)
    return jsonify(todos), 200   

@app.errorhandler(404)                                       ### handler for Page not found error
def page_not_found(e):
    msg = f"The requested URL path {request.path} was not found on the server."
    return jsonify(error=msg), 404
    

@app.errorhandler(405)                                     ### handler for invalid http methods
def method_not_allowed(e):
    msg=f"Specified HTTP method not allowed."
    return jsonify(error=msg), 405  

if __name__ == "__main__":
    create_table()

    app.run(debug=True)
    