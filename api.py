import logging
import sys

from flask import Blueprint, request, abort, Response

from utility import guess_number

api = Blueprint('api', __name__)

logger = logging.getLogger(__name__)

handler = logging.StreamHandler(stream=sys.stdout)
logging.basicConfig(format='[%(asctime)s %(levelname)s]:%(message)s', handlers=[handler], level=logging.DEBUG)


@api.route("/guess")
def process_guess():
    # JSON is like {"number": int}
    try:
        try:
            data = request.get_json()
        except Exception as ex:
            return abort(Response(str(ex), 400))
        try:
            number = int(data["number"])
        except KeyError as ex:
            raise Exception(f"'{ex.args[0]}' is required")
        except ValueError:
            raise Exception("There should be integer!")
    except Exception as ex:
        return abort(Response(str(ex), 400))

    if number >= 100 or number < 0:
        return abort(Response("Number should be in range [0,100) ", 400))

    answer = guess_number(number)

    return {"answer": answer}
