"""Helpers for doing U2F with bitbox02"""

from typing import Tuple
import binascii
import struct

import communication
from communication import Bitbox02Exception

from communication.devices import get_device, BITBOX02MULTI, DeviceInfo
from . import u2f


def get_bitbox02_u2f_device() -> DeviceInfo:
    return get_device(BITBOX02MULTI, 1)


class BitBox02U2F:
    """Interact with a bitbox for u2f purposes"""

    def __init__(self, transport: communication.TransportLayer):
        self._transport = transport
        # 0 and 0xffffffff are reserved
        self._cid = self._transport.generate_cid()
        self.debug = False

    def close(self) -> None:
        self._transport.close()

    def _query(self, cid: int, cmd: int, msg: bytes) -> bytes:
        """
        Sends msg bytes and retrieves response bytes.
        """
        if self.debug:
            print(f"msg: {msg}, cid: {cid}, cmd: {cmd}")
        self._transport.write(msg, cmd, cid)
        response_bytes = self._transport.read(cmd, cid)
        if self.debug:
            print(f"response {len(response_bytes)}: {binascii.hexlify(bytes(response_bytes))}")
        return bytes(response_bytes)

    @staticmethod
    def _maybe_error(response_bytes: bytes, cmd: int) -> None:
        if cmd == 0x80 + 0x3F:
            raise Bitbox02Exception(response_bytes[0], "U2F error discovered")

    @staticmethod
    def _parse_u2f_init_response(response_bytes: bytes) -> u2f.InitResponse:
        return u2f.InitResponse(
            response_bytes[0:8],
            response_bytes[8:12],
            response_bytes[12:13],
            response_bytes[13:14],
            response_bytes[14:15],
            response_bytes[15:16],
            response_bytes[16:17],
        )

    def u2fhid_init(self, allocate: bool) -> None:
        """Set allocate to ask the device to choose CID"""
        nonce = bytes([1, 2, 3, 4, 5, 6, 7, 8])
        cid = self._cid
        if allocate:
            cid = communication.u2fhid.CID_BROADCAST
        response_bytes = self._query(cid, communication.u2fhid.INIT, nonce)
        init_response = self._parse_u2f_init_response(response_bytes)
        self._cid = init_response.cid

    def u2fhid_ping(self, msg: bytes) -> bytes:
        return self._query(self._cid, communication.u2fhid.PING, msg)

    def u2fhid_wink(self) -> bool:
        _response_bytes = self._query(self._cid, communication.u2fhid.WINK, bytes("", "utf-8"))
        return True

    def u2fhid_msg(self, msg: bytes) -> bytes:
        return self._query(self._cid, communication.u2fhid.MSG, msg)

    def u2f_register(self, appid: str) -> Tuple[bytes, bytes]:
        self.u2fhid_init(True)
        req = u2f.RegistrationRequest(appid)
        response = req.send(self)
        if not response.verify():
            raise Exception("Did not verify")
        return (response.ec_public_key, response.key_handle)

    def u2f_authenticate(self, appid: str, key_handle: bytes, pub_key: bytes) -> bool:
        self.u2fhid_init(True)
        req = u2f.AuthenticationRequest(appid, key_handle)
        response = req.send(self)
        if self.debug:
            counter = struct.unpack(">L", response.ctr)[0]
            print(f"Counter is: {counter}")
        return response.verify(pub_key)

    def u2f_register_bogus(self, vendor: str) -> None:
        self.u2fhid_init(True)
        req = u2f.RegistrationRequest("", vendor)
        response = req.send(self)
        if not response.verify():
            raise Exception("Did not verify")
