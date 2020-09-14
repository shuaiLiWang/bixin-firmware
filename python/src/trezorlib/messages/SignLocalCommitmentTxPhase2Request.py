# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .ChannelNonce import ChannelNonce
from .CommitmentInfo import CommitmentInfo
from .NodeId import NodeId

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class SignLocalCommitmentTxPhase2Request(p.MessageType):
    MESSAGE_WIRE_TYPE = 865

    def __init__(
        self,
        node_id: NodeId = None,
        channel_nonce: ChannelNonce = None,
        commitment_info: CommitmentInfo = None,
    ) -> None:
        self.node_id = node_id
        self.channel_nonce = channel_nonce
        self.commitment_info = commitment_info

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('node_id', NodeId, 0),
            2: ('channel_nonce', ChannelNonce, 0),
            4: ('commitment_info', CommitmentInfo, 0),
        }