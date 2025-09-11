import json
import logging

import aiohttp

from config import API_HOST, API_PORT

from typing import Optional, Dict, Union
from urllib.parse import unquote
from aiohttp import ClientResponse
from aiohttp.http import HTTPStatus

from common_lib.api_client.url_factory import URLFactory
from common_lib.dataclasses import FileData

class ApiClient:
    def __init__(
            self,
            token
    ):
        self.__token = token


    def get_headers_base(
            self
    ) -> Dict:
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f'Bearer {self.__token}'
        }

        return headers

    async def call_async_post(
            self,
            url: str,
            body: Union[Dict, bytes],
            params: Optional[Dict] = None,
            headers: Optional[Dict] = None
    ) -> ClientResponse:
        if headers is None:
            headers = self.get_headers_base()
        data = json.dumps(body) if isinstance(body, Dict) else body
        try:
            async with aiohttp.ClientSession() as session:

                async with session.post(
                    url=url,
                    headers=headers,
                    params=params,
                    data=data
                ) as response:

                    if response.status == HTTPStatus.INTERNAL_SERVER_ERROR or response.status == HTTPStatus.UNAUTHORIZED:
                        raise Exception(await response.text())

                    return response

        except Exception as e:
            logging.error(f'Произошла ошибка при выполнении операции POST по пути {response.url}.\nПараметры: {response.headers}.\nТекст ошибки {await response.text()}')
            raise Exception(
                f'Произошла ошибка при выполнении операции POST'
            )

    async def call_async_delete(
            self,
            url: str,
            body: Union[Dict, bytes],
            params: Optional[Dict] = None,
            headers: Optional[Dict] = None
    ):
        if headers is None:
            headers = self.get_headers_base()

        try:
            async with aiohttp.ClientSession() as session:

                async with session.post(
                        url=url,
                        headers=headers,
                        params=params,
                        body=body
                ) as response:
                    if response == HTTPStatus.INTERNAL_SERVER_ERROR:
                        raise Exception(await response.text())

                    response_data = await response.text()
                    return json.loads(response_data) if isinstance(response_data, str) else response_data


        except Exception:
            logging.error(
                f'Произошла ошибка при выполнении операции DELETE по пути {response.url}.\nПараметры: {response.headers}.\nТекст ошибки {await response.text()}')
            raise Exception(
                f'Произошла ошибка при выполнении операции DELETE'
            )

    async def call_async_put(
            self,
            url: str,
            body: Union[Dict, bytes],
            params: Optional[Dict] = None,
            headers: Optional[Dict] = None
    ):
        if headers is None:
            headers = self.get_headers_base()

        try:
            async with aiohttp.ClientSession() as session:

                async with session.post(
                        url=url,
                        headers=headers,
                        params=params,
                        body=body
                ) as response:
                    if response == HTTPStatus.INTERNAL_SERVER_ERROR:
                        pass

                    response_data = await response.text()
                    return json.loads(response_data) if isinstance(response_data, str) else response_data


        except Exception:
            logging.error(
                f'Произошла ошибка при выполнении операции PUT по пути {response.url}.\nПараметры: {response.headers}.\nТекст ошибки {await response.text()}')
            raise Exception(
                f'Произошла ошибка при выполнении операции PUT'
            )

    async def call_async_get(
            self,
            url: str,
            params: Optional[Dict] = None,
            headers: Optional[Dict] = None
    ) -> ClientResponse:
        if headers is None:
            headers = self.get_headers_base()

        try:
            async with aiohttp.ClientSession() as session:

                async with session.get(
                        url=url,
                        headers=headers,
                        params=params,
                ) as response:
                    if response.status == HTTPStatus.INTERNAL_SERVER_ERROR or response.status == HTTPStatus.UNAUTHORIZED:
                        raise Exception(await response.text())

                    if response.status == HTTPStatus.OK:
                        if response.headers.get('content-type') == 'application/json':
                            response_data = await response.json()
                            return response_data

        except Exception as e:
            logging.error(
                f'Произошла ошибка при выполнении операции GET по пути {url}.\nПараметры: {headers}.\nТекст ошибки {e}')
            raise Exception(
                f'Произошла ошибка при выполнении операции GET'
            )

    async def get_file(
            self,
            url: str,
            params: Optional[Dict] = None,
            headers: Optional[Dict] = None
    ) -> Optional[FileData]:

        if headers is None:
            headers = self.get_headers_base()

        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=url,
                headers=headers,
                params=params
            ) as response:

                if response.status == HTTPStatus.INTERNAL_SERVER_ERROR:
                    raise
                if response.status == HTTPStatus.NOT_FOUND:
                    return None

                filename = unquote(response.headers.get('filename'))
                file_type = response.headers.get('file_type')
                file_data = await response.content.read()

        return FileData(
            filename=filename,
            file_type=file_type,
            data=file_data
        )

api_client = ApiClient(
    token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzA5OTMwMDcsInN1YmplY3QiOnsibG9naW4iOiJzdHJpbmciLCJlbWFpbCI6InN0cmluZyJ9fQ.9zxK19zFhaD0KwqewVWkARybd00ecs6XWVEYcjHiP0Q'
)

url_f = URLFactory(
    host=API_HOST,
    port=API_PORT
)
