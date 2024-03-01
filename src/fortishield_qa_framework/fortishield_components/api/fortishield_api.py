"""
Module to wrapp the main Fortishield API calls. This module contains the following:

- FortishieldAPI:
    - get_token
    - set_token_expiration
    - get_api_info
    - list_agents
    - restart_agent
"""
from base64 import b64encode
from http import HTTPStatus
import requests

from fortishield_qa_framework.fortishield.github.ioponents.api.fortishield_api_request import FortishieldAPIRequest
from fortishield_qa_framework.generic_modules.request.request import GetRequest
from fortishield_qa_framework.generic_modules.exceptions.exceptions import ConnectionError, RuntimeError


DEFAULT_USER = 'fortishield'
DEFAULT_PASSOWRD = 'fortishield'
DEFAULT_PORT = 55000
DEFAULT_ADDRESS = 'localhost'
DEFAULT_PROTOCOL = 'https'
DEFAULT_TOKEN_EXPIRATION = 900


class FortishieldAPI:
    """Class to manage the Fortishield API via requests.

    Args:
        user (str): Fortishield API user.
        password (str): Fortishield API password.
        port (int): Fortishield API port connection.
        address (str): Fortishield API address.
        protocol (str): Fortishield API protocol.
        auto_auth (boolean): True for getting the API auth token automatically, False otherwise.
        token_expiration (int): Number of seconds to set to the token expiration.

    Attributes:
        user (str): Fortishield API user.
        password (str): Fortishield API password.
        port (int): Fortishield API port connection.
        address (str): Fortishield API address.
        protocol (str): Fortishield API protocol.
        token (str): Fortishield API auth token.
        token_expiration (int): Number of seconds to set to the token expiration.
    """
    def __init__(self, user=DEFAULT_USER, password=DEFAULT_PASSOWRD, port=DEFAULT_PORT, address=DEFAULT_ADDRESS,
                 protocol=DEFAULT_PROTOCOL, auto_auth=True, token_expiration=DEFAULT_TOKEN_EXPIRATION):
        self.user = user
        self.password = password
        self.port = port
        self.address = address
        self.protocol = protocol
        self.url = f"{protocol}://{address}:{port}"
        self.token_expiration = token_expiration
        self.token = self.get_token() if auto_auth else None

        if token_expiration != DEFAULT_TOKEN_EXPIRATION:
            self.set_token_expiration(token_expiration)
            self.token = self.get_token()

    def get_token(self):
        """Get the auth API token.

        Returns:
            str: API auth token.

        Raises:
            exceptions.RuntimeError: If there are any error when obtaining the login token.
            exceptions.RuntimeError: Cannot establish connection with API.
        """
        basic_auth = f"{self.user}:{self.password}".encode()
        auth_header = {'Content-Type': 'application/json', 'Authorization': f'Basic {b64encode(basic_auth).decode()}'}

        try:
            response = GetRequest(f"{self.url}/security/user/authenticate?raw=true", headers=auth_header).send()

            if response.status_code == HTTPStatus.OK:
                return response.text

            raise RuntimeError(f"Error obtaining login token: {response.json()}")

        except requests.exceptions.ConnectionError as exception:
            raise ConnectionError(f"Cannot establish connection with {self.url}") from exception

    def set_token_expiration(self, num_seconds):
        """Set the Fortishield API token expiration.

        Returns:
            FortishieldAPIResponse: Operation result (response).
        """
        response = FortishieldAPIRequest(method='PUT', endpoint='/security/config',
                                   payload={'auth_token_exp_timeout': num_seconds}).send(self)
        return response

    @FortishieldAPIRequest(method='GET', endpoint='/')
    def get_api_info(self, response):
        """Get the Fortishield API info.

        Returns:
            dict: Fortishield API info.
        """
        return response.data

    @FortishieldAPIRequest(method='GET', endpoint='/agents')
    def list_agents(self, response):
        """List the fortishield agents.

        Returns:
            dict: Fortishield API info.
        """
        return response.data

    def restart_agent(self, agent_id):
        """Restart a fortishield-agent.

        Returns:
            dict: Fortishield API info.
        """
        response = FortishieldAPIRequest(method='PUT', endpoint=f"/agents/{agent_id}/restart").send(self)

        return response
