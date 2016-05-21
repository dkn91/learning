#!/home/dpishe/anaconda2/envs/py27/bin/python
from flask import Flask, jsonify
from cidras import *

import logging
logging.basicConfig(filename="/home/dpishe/log/asnapi.log",level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/asn/api/v1.0/<as_num>', methods=['GET'])
def get_tasks(as_num):
	data = {}
	as_num = str(as_num)
	asnlist = as_num.split('-')
	for i in asnlist:
		data[i] = fetch_asn(i)
	return jsonify(data)


@app.errorhandler(404)
def not_found(error):
	return jsonify({'error': 'Not found'})

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')

