from python_graphql_client import GraphqlClient
from requests.auth import HTTPBasicAuth

from buycoins.exceptions import QueryError

class BuyCoinsClient:
    def __init__(self, auth_key: str):
        self.__endpoint = "https://backend.buycoins.tech/api/graphql"
        self.__username = ""
        self.__password = ""
        self.auth_key = auth_key

    def _split_auth_key(self):
        self.__username, self.__password = self.auth_key.split(":")

    def _initiate_client(self):
        self._split_auth_key()
        self.auth = HTTPBasicAuth(self.__username, self.__password)
        self.client = GraphqlClient(self.__endpoint, auth=self.auth)
        return self.client

    def _execute_request(self, query: str, variables: dict= {}):
        if not query or query == "":
            raise QueryError("Invalid query passed!")

        self._initiate_client()
        return self.client.execute(query=query, variables=variables)
