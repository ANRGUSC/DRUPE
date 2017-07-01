'''
 * Copyright (c) 2017, Autonomous Networks Research Group. All rights reserved.
 *     contributor: Jiatong Wang, Bhaskar Krishnamachari
 *     Read license file in main directory for more details
'''

from flask import Flask
import psutil
import json
app = Flask(__name__)

@app.route('/') #web route url
def performance():
    response = {} #create a response json object
    response["memory"]=psutil.virtual_memory().percent 
    response["cpu"]=psutil.cpu_percent() 
    return json.dumps(response) 

if __name__ == '__main__':
    app.run(host='0.0.0.0') #run this web application on 0.0.0.0 and default port is 5000
