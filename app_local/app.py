import pandas as pd  
from flask import Flask
from flask import Response

import os

app = Flask(__name__)

@app.route('/')
def panda():
    # string values in the list   
    lst = ['Java', 'Python', 'C', 'C++',  
             'JavaScript', 'Swift', 'Go']  

    os.system(""" 
    mkdir -p app/output
    """)

    # Calling DataFrame constructor on list  
    dframe = pd.DataFrame(lst)  

    dframe.to_csv('app/output/test.csv')
    return dframe.to_html()