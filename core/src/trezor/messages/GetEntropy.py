# Automatically generated by pb2py
# fmt: off
import protobuf as p


class GetEntropy(p.MessageType):
    MESSAGE_WIRE_TYPE = 9

    def __init__(
        self,
        size: int = None,
    ) -> None:
        self.size = size

    @classmethod
    def get_fields(cls):
        return {
            1: ('size', p.UVarintType, 0),  # required
        }