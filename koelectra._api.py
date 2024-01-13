import warnings
warnings.filterwarnings(action='ignore')

import json
from flask import Flask, make_response
from flask_restful import reqparse, Api, Resource

import sys
# Electra 모델 로드를 위한 경로 설정
sys.path.append('C:\\sqlite\\mysql\\code\\AI\\FINAL_project\\dialogLM\\dialogLM\\service')
from Demonstration.model.load_electra import DialogElectra 

# Flask 서버 설정
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)

# DialogElectra 모델 로드
dialog_electra = DialogElectra()

# DialogElectraAPI 클래스 정의
class DialogElectraAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('s')
        args = parser.parse_args()
        result = dialog_electra.predict(args['s'])
        print('sentence:',args['s'] )
        print('result:',result )
        return make_response(json.dumps({'answer':result}, ensure_ascii=False))

# Electra API 경로 설정
# api.add_resource(DialogElectraAPI, '/api/dialog/electra')
api.add_resource(DialogElectraAPI, '/api/wellness/dialog/electra')


# Flask 애플리케이션 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9900)
