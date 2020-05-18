'''Custom generic CloudFormation resource example'''

import json
import logging
import signal
from urllib2 import build_opener, HTTPHandler, Request

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def send_response(event, context, response_status, response_data):
    '''Send a resource manipulation status response to CloudFormation'''
    response_body = json.dumps({
        "Status": response_status,
        "Reason": "See the details in CloudWatch Log Stream: " + context.log_stream_name,
        "PhysicalResourceId": context.log_stream_name,
        "StackId": event['StackId'],
        "RequestId": event['RequestId'],
        "LogicalResourceId": event['LogicalResourceId'],
        "Data": response_data
    })


send_response(event, context, "SUCCESS", {"Message": "Resource creation successful!"})

LOGGER.info('ResponseURL: %s', event['ResponseURL'])
LOGGER.info('ResponseBody: %s', response_body)
