from enum import Enum

from common.environ.settings_class import EnvironSettings
from dotenv import load_dotenv

load_dotenv()


class MembershipChangingStrategyType(Enum):
    Transactional = "Transactional"
    Detailed = "Detailed"


class CaesarSettings(EnvironSettings):
    MEMBERSHIP_CHANGING_STRATEGY: MembershipChangingStrategyType = (
        MembershipChangingStrategyType.Transactional
    )


MEMBERSHIP_CHANGING_STRATEGY = CaesarSettings().MEMBERSHIP_CHANGING_STRATEGY
