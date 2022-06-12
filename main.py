from traceback import print_tb
from flask import Flask, request, render_template,jsonify
import flask_monitoringdashboard as dashboard
from flask_cors import CORS, cross_origin
# from flask import Response
# from application_logger.logger import App_Logger
# from logger import App_Logger


# file_obj = open("Training_Logs/Training_Main_Log.txt", 'a+')
# message = " hi i am rakesh from main hello"

# log_try = App_Logger()
# log_try.log(file_obj,message)


app = Flask(__name__)
dashboard.bind(app)
CORS(app)

@app.route("/",methods=['GET', 'POST'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train",methods = ['GET'])
@cross_origin()
def trainRouteClient():
    try:
        if request.json['folderPath'] is not None:
            path = request.json['folderPath']
            
            train_valObj = train_validation(path)

    except Exception as e:
        return Response("Error Occurred! %s" % e)
    


if __name__ == "__main__":
    #host = '0.0.0.0'
    #port = 5000
    #httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    #httpd.serve_forever()
    app.run(debug=True)
