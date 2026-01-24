from clickhouse_connect import get_async_client
from typing import Optional


class AnalyticsDB:
    def __init__(self, host: str, port: int, username: str, password: str):
        self._host = host
        self._port = port
        self._username = username
        self._password = password

    
    async def select(self, query: str, parameters: Optional[dict] = None, column_oriented: bool = True):
        client = await get_async_client(host=self._host, port=self._port, username=self._username, password=self._password)
        result = await client.query(
            query,
            parameters=parameters,
            column_oriented=column_oriented
        )

        formatted_result: dict = dict(zip(result.column_names, result.result_rows))
        return formatted_result

