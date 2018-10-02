import redis
from flask import Flask, request, jsonify
from random import randint

from flask_httpauth import HTTPBasicAuth

from .conf import WAF_REDIS_DB, USERNAME, PASSWORD

REDIS_CLIENT = redis.Redis(connection_pool=WAF_REDIS_DB)
auth = HTTPBasicAuth()

app = Flask(__name__)

MAX_CUSTOMER_ID = 1024

REDIS_USED_LIST_KEY = "SNOWFLAKE_CUSTOMER_USED_ID"

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/snowflake/customer-id', methods=['GET', 'PUT', 'DELETE'])
@auth.login_required
def snowflake_customer_id():
    if request.method == "GET":
        ret = get_customer_id()
        return jsonify(ret)
    elif request.method == "PUT":
        data = request.json
        customer_id = data.get("id")
        id_key = "{}_{}".format(REDIS_USED_LIST_KEY, customer_id)
        REDIS_CLIENT.set(id_key, customer_id, 300)
        return jsonify(
            {
                "id": customer_id
            }
        )
    elif request.method == "DELETE":
        data = request.json
        customer_id = data.get("id")
        id_key = "{}_{}".format(REDIS_USED_LIST_KEY, customer_id)
        REDIS_CLIENT.delete(id_key)
        return jsonify(
            {
                "id": customer_id
            }
        )

def get_customer_id():
    while True:
        randint_id = randint(0, MAX_CUSTOMER_ID)
        id_key = "{}_{}".format(REDIS_USED_LIST_KEY, randint_id)
        key_len = len(REDIS_CLIENT.keys("{}*".format(REDIS_USED_LIST_KEY)))
        if key_len > 1024:
            ret = {
                    "id": None
                }
            return ret

        if not REDIS_CLIENT.get(id_key):
            ret = {
                    "id": randint_id
                }
            REDIS_CLIENT.set(id_key, randint_id, 300)
            return ret


@auth.verify_password
def verify_password(username, password):
    if username == USERNAME and password == PASSWORD:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
