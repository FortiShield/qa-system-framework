"""
Module to wrapp the Fortishield API requests. Normally, the developers should not use this class but FortishieldAPI one. This class
is used by FortishieldAPI to make and send the API requests.

This module contains the following:

- FortishieldAPIRequest:
    - send
"""
import json
import requests

from fortishield_qa_framework.generic_modules.request.request import Request
from fortishield_qa_framework.generic_modules.exceptions.exceptions import ConnectionError
from fortishield_qa_framework.fortishield.github.ioponents.api.fortishield_api_response import FortishieldAPIResponse


class FortishieldAPIRequest:
    """Wrapper class to manage requests to the Fortishield API.

    Args:
        endpoint (str): Target API endpoint.
        method (str): Request method (GET, POST, PUT, DELETE).
        payload (dict): Request data.
        headers (dict): Request headers.
        verify (boolean): False for ignore making insecure requests, False otherwise.

    Attributes:
        endpoint (str): Target API endpoint.
        method (str): Request method (GET, POST, PUT, DELETE).
        payload (dict): Request data.
        headers (dict): Request headers.
        verify (boolean): False for ignore making insecure requests, False otherwise.
    """
    def __init__(self, endpoint, method, payload=None, headers=None, verify=False):
        self.endpoint = endpoint
        self.method = method.upper()
        self.payload = payload
        self.headers = headers
        self.verify = verify

    def __get_request_parameters(self, fortishield_api_object):
        """Build the request parameters.

        Args:
            fortishield_api_object (FortishieldAPI): Fortishield API object.
        """
        # Get the token if we have not got it before.
        if fortishield_api_object.token is None:
            fortishield_api_object.token = fortishield_api_object.get_token()

        self.headers = {} if self.headers is None else self.headers
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {fortishield_api_object.token}'
        })

        request_args = {
            'method': self.method,
            'url': f"{fortishield_api_object.url}{self.endpoint}",
            'headers': self.headers,
            'verify': self.verify
        }

        if self.payload is not None:
            request_args['payload'] = self.payload

        return request_args

    def __call__(self, func):
        """Perform directly the Fortishield API call and add the response object to the function parameters. Useful to run
        the request using only a python decorator.

        Args:
            func (function): Function object.
        """
        def wrapper(obj, *args, **kwargs):
            kwargs['response'] = self.send(obj)

            return func(obj, *args, **kwargs)

        return wrapper

    def __str__(self):
        """Overwrite the print object representation"""
        return json.dumps(self.__dict__)

    def send(self, fortishield_api_object):
        """Send the API request.

        Args:
            fortishield_api_object (FortishieldAPI): Fortishield API object.

        Returns:
            FortishieldAPIResponse: Fortishield API response object.

        Raises:
            exceptions.RuntimeError: Cannot establish connection with the API.
        """
        request_parameters = self.__get_request_parameters(fortishield_api_object)

        try:
            return FortishieldAPIResponse(Request(**request_parameters).send())
        except requests.exceptions.ConnectionError as exception:
            raise ConnectionError(f"Cannot establish connection with {fortishield_api_object.url}") from exception
