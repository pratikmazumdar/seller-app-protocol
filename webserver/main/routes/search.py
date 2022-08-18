from flask import g
from flask_expects_json import expects_json
from flask_restx import Namespace, Resource, reqparse
from jsonschema import validate

from main import constant
from main.repository.ack_response import get_ack_response
from main.service.common import send_message_to_queue_for_given_request
from main.utils.schema_utils import get_json_schema_for_given_path, get_json_schema_for_response

search_namespace = Namespace('search', description='Search Namespace')


@search_namespace.route("/v1/search")
class SearchCatalogues(Resource):
    path_schema = get_json_schema_for_given_path('/search')

    @expects_json(path_schema)
    def post(self):
        response_schema = get_json_schema_for_response('/search')
        resp = get_ack_response(ack=True)
        send_message_to_queue_for_given_request('search', g.data)
        validate(resp, response_schema)
        return resp

