"""Module of wrapper classes."""
from slimgym import error
from slimgym.wrappers.autoreset import AutoResetWrapper
from slimgym.wrappers.clip_action import ClipAction
from slimgym.wrappers.filter_observation import FilterObservation
from slimgym.wrappers.flatten_observation import FlattenObservation
from slimgym.wrappers.frame_stack import FrameStack, LazyFrames
from slimgym.wrappers.gray_scale_observation import GrayScaleObservation
from slimgym.wrappers.human_rendering import HumanRendering
from slimgym.wrappers.normalize import NormalizeObservation, NormalizeReward
from slimgym.wrappers.order_enforcing import OrderEnforcing
from slimgym.wrappers.record_episode_statistics import RecordEpisodeStatistics
from slimgym.wrappers.render_collection import RenderCollection
from slimgym.wrappers.rescale_action import RescaleAction
from slimgym.wrappers.resize_observation import ResizeObservation
from slimgym.wrappers.time_aware_observation import TimeAwareObservation
from slimgym.wrappers.time_limit import TimeLimit
from slimgym.wrappers.transform_observation import TransformObservation
from slimgym.wrappers.transform_reward import TransformReward
from slimgym.wrappers.vector_list_info import VectorListInfo
