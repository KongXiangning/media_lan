import logging
from ...core.message import (
    MessageType,
    MessageRequest,
    MessageResponse,
    MessageBody,
)

_LOGGER = logging.getLogger(__name__)


class MessageCDBase(MessageRequest):
    def __init__(self, message_type, body_type):
        super().__init__(
            device_type=0xE2,
            message_type=message_type,
            body_type=body_type
        )

    @property
    def _body(self):
        raise NotImplementedError


class MessageQuery(MessageCDBase):
    def __init__(self):
        super().__init__(
            message_type=MessageType.query,
            body_type=0x01)

    @property
    def _body(self):
        return bytearray([0x01])


class MessageGeneralSet(MessageCDBase):
    def __init__(self):
        super().__init__(
            message_type=MessageType.set,
            body_type=0x04)

    @property
    def _body(self):

        return bytearray([])


class CDGeneralMessageBody(MessageBody):
    def __init__(self, body):
        super().__init__(body)


class MessageCDResponse(MessageResponse):
    def __init__(self, message):
        super().__init__(message)
        body = message[10: -2]
        if self._message_type in [MessageType.query, MessageType.notify2]:
            self._body = CDGeneralMessageBody(body)
