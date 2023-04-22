"""Root __init__ of the gym module setting the __all__ of gym modules."""
# isort: skip_file

from slimgym import error
from slimgym.version import VERSION as __version__

from slimgym.core import (
    Env,
    Wrapper,
    ObservationWrapper,
    ActionWrapper,
    RewardWrapper,
)
from slimgym.spaces import Space
from slimgym import logger
from slimgym import vector
from slimgym import wrappers
import os
import sys

__all__ = ["Env", "Space", "Wrapper"]
