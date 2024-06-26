from flask import *
import pandas as pd
import json, time
import pickle
import re
import os
from flask_cors import CORS

import warnings
warnings.filterwarnings('ignore')



app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def home_page():
    return render_template('index.html')


if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
