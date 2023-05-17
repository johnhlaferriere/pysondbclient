
from concurrent.futures import thread

import socket, sys
from threading import Thread
import time
import zlib
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from typing import List
from typing import Optional
from typing import Union
from typing import Dict
from pysondb.utils import Crypt

from pysondb.db_types import DBSchemaType
from pysondb.db_types import IdGeneratorType
from pysondb.db_types import NewKeyValidTypes
from pysondb.db_types import SingleDataType
from pysondb.db_types import ReturnWithIdType
from pysondb.db_types import QueryType

from pysondb.errors import IdDoesNotExistError
from pysondb.errors import SchemaTypeError
from pysondb.errors import UnknownKeyError
from pysondb.errors import SectionNotFoundError
from pysondb.errors import SectionAlreadExistsError
from pysondb.errors import DatabaseNotFoundError
from pysondb.errors import MalformedQueryError
from pysondb.errors import InvalidUserError


try:
    import ujson as json
except ImportError:
    import json as json


class PysonDBClient:
    def __init__(self, host, port, wait=1):
        super().__init__
        self._sock = None
        self._host = host
        self._port = port
        self._connected = False
        self._wait = wait
        self._dbname = None
        self._section = None
        self._auth = None
        self._user = None
        self._passwd = None
        self._encrypt = True
        self._crypt = Crypt()

    def _check_error(self, val):
        if val["error"] == "NoError":
            return val["data"]
        else:
            raise getattr(
                getattr(__import__("pysondb.errors"), "errors"), val["error"]
            )(val["data"])

    def _check_section(self, s) -> str:
        if s == None and self._section == None:
            raise (SectionNotFoundError("There is no section selected."))
        return s if s != None else self._section

    def _recvall(self):
        MAX_BUF = 1024
        data = bytearray()
        len = int.from_bytes(self._sock.recv(8), "big")
        loop = len // MAX_BUF
        while loop > 0:
            data += self._sock.recv(MAX_BUF)
            loop -= 1
        data += self._sock.recv(len % MAX_BUF)
        if self._encrypt:
            data = self._crypt.password_decrypt(data, self._passwd)
        return data

    def _send(self, data: object, check: bool = True, auth=True) -> str:
        if self._connected:
            if check and self._dbname == None:
                raise Exception("No database has been selected.")
            if auth and self._auth == None:
                raise InvalidUserError("Missing username and password.")
            data["auth"] = self._auth
            d = json.dumps(data).encode()
            if self._auth == None:
                d = self.obscure(d)
            else:
                if self._encrypt:
                    d = self._crypt.password_encrypt(d, self._passwd)
            self._sock.sendall(len(d).to_bytes(8, "big"))
            self._sock.sendall(d)
            return json.loads(self._recvall())
        else:
            raise Exception("No Cennection")

    def add(
        self, data: object, ignore_missing_key: bool = False, section: str = None
    ) -> str:
        return self._check_error(
            self._send(
                {
                    "cmd": "ADD",
                    "payload": {
                        "section": self._check_section(section),
                        "ignore_missing_key": ignore_missing_key,
                        "data": data,
                    },
                }
            )
        )

    def add_many(
        self,
        data: object,
        ignore_missing_key: bool = False,
        json_response: bool = True,
        section: str = None,
    ):
        return self._check_error(
            self._send(
                {
                    "cmd": "ADD_MANY",
                    "payload": {
                        "section": self._check_section(section),
                        "data": data,
                        "json_response": json_response,
                        "ignore_missing_key": ignore_missing_key,
                    },
                }
            )
        )

    def add_new_key(
        self, key: str, default: Optional[NewKeyValidTypes] = None, section: str = None
    ):
        return self._check_error(
            self._send(
                {
                    "cmd": "ADD_NEW_KEY",
                    "payload": {
                        "section": self._check_section(section),
                        "key": key,
                        "default": default,
                    },
                }
            )
        )

    def add_section(self, section: str = None, use: bool = True):
        retval = self._check_error(
            self._send(
                {
                    "cmd": "ADD_SECTION",
                    "payload": {
                        "section": self._check_section(section),
                        "use": use,
                    },
                }
            )
        )
        if use:
            self._section = retval
        return retval

    def close(self) -> None:
        self._sock.shutdown(socket.SHUT_RDWR)
        self._sock.close()
        self._connected = False

    def obscure(self, data: bytes) -> bytes:
        return b64e(zlib.compress(data, 9))

    def unobscure(self, obscured: bytes) -> bytes:
        return zlib.decompress(b64d(obscured))

    def connect(
        self, username: str, password: str, encrypt: bool = True, retries=5
    ) -> bool:
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not self._connected:
            rCount = 0
        while not self._connected and rCount < retries:
            try:
                self._sock.connect((self._host, self._port))
                self._connected = True
            except:
                time.sleep(self._wait)
                rCount += 1
        if self._connected:
            self._user = username
            self._passwd = password
            self._encrypt = encrypt
            enc = str(
                self.obscure(json.dumps({"u": username, "p": password}).encode("utf-8"))
            )
            self._auth = self._check_error(
                self._send(
                    {
                        "cmd": "AUTH",
                        "payload": {
                            "credentials": enc,
                            "encrypt": encrypt,
                        },
                    },
                    False,
                    False,
                )
            )

        return self._connected

    def create_db(self, dbname: str, use: bool = True, force: bool = False):
        retval = self._check_error(
            self._send(
                {
                    "cmd": "CREATE_DB",
                    "payload": {
                        "dbname": dbname,
                        "use": use,
                        "force": force,
                    },
                },
                False,
            )
        )
        self._dbname = dbname
        return retval

    def delete_by_id(self, id: str, section: str = None):
        return self._check_error(
            self._send(
                {
                    "cmd": "DELETE_BY_ID",
                    "payload": {
                        "section": self._check_section(section),
                        "id": id,
                    },
                }
            )
        )

    def delete_by_query(self, query, section: str = None):
        return self._check_error(
            self._send(
                {
                    "cmd": "DELETE_BY_QUERY",
                    "payload": {
                        "section": self._check_section(section),
                        "query": query,
                    },
                }
            )
        )

    def get_all(self) -> str:
        return self._check_error(self._send({"cmd": "GET_ALL", "payload": ""}))

    def get_all_by_section(self, section: str = None) -> str:
        return self._check_error(
            self._send(
                {
                    "cmd": "GET_ALL_BY_SECTION",
                    "payload": {"section": self._check_section(section)},
                }
            )
        )

    def get_by_id(self, id: str, section: str = None):
        return self._check_error(
            self._send(
                {
                    "cmd": "GET_BY_ID",
                    "payload": {"section": self._check_section(section), "id": id},
                }
            )
        )

    def get_by_query(self, query: str, section: str = None):
        return self._check_error(
            self._send(
                {
                    "cmd": "GET_BY_QUERY",
                    "payload": {
                        "section": self._check_section(section),
                        "query": query,
                    },
                }
            )
        )

    def purge(self, section: str = None):
        return self._check_error(
            self._send(
                {"cmd": "PURGE", "payload": {"section": self._check_section(section)}}
            )
        )

    def purge_all(self):
        return self._check_error(self._send({"cmd": "PURGE_ALL", "payload": ""}))

    def set_id_generator(self, fn: any):
        return self._check_error(
            self._send({"cmd": "SET_ID_GENERATOR", "payload": {"fn": fn}})
        )

    def update_by_id(self, id: str, new_data: object, section: str = None):
        return self._check_error(
            self._send(
                {
                    "cmd": "UPDATE_BY_ID",
                    "payload": {
                        "section": self._check_section(section),
                        "id": id,
                        "data": new_data,
                    },
                }
            )
        )

    def update_by_query(self, query: str, new_data: object, section: str = None):
        return self._check_error(
            self._send(
                {
                    "cmd": "UPDATE_BY_QUERY",
                    "payload": {
                        "section": self._check_section(section),
                        "query": query,
                        "data": new_data,
                    },
                }
            )
        )

    def use_db(self, dbname: str, section: str = None):
        retval = self._check_error(
            self._send(
                {"cmd": "USE_DB", "payload": {"dbname": dbname, "section": section}},
                False,
            )
        )
        self._dbname = dbname
        if section != None:
            self._section = section

    def use_section(self, section: str):
        if section == self._section:
            return
        retval = self._check_error(
            self._send({"cmd": "USE_SECTION", "payload": {"section": section}})
        )
        self._section = section
        return section
