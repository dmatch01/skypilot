"""The Sky package."""
import os

# Keep this order to avoid cyclic imports
from sky import backends
from sky import clouds
from sky.clouds.service_catalog import list_accelerators
from sky.dag import Dag, DagContext
from sky.execution import launch, exec, spot_launch  # pylint: disable=redefined-builtin
from sky.resources import Resources
from sky.task import Task
from sky.optimizer import Optimizer, OptimizeTarget
from sky.data import Storage, StoreType
from sky.data.storage_utils import storage_ls, storage_delete
from sky.global_user_state import ClusterStatus
from sky.skylet.job_lib import JobStatus

__root_dir__ = os.path.dirname(os.path.abspath(__file__))

# Aliases.
AWS = clouds.AWS
Azure = clouds.Azure
GCP = clouds.GCP
optimize = Optimizer.optimize

__all__ = [
    'AWS',
    'Azure',
    'GCP',
    'Dag',
    'DagContext',
    'Optimizer',
    'OptimizeTarget',
    'Resources',
    'Task',
    'backends',
    'list_accelerators',
    '__root_dir__',
    'Storage',
    'StoreType',
    'ClusterStatus',
    'JobStatus',
    # APIs
    'launch',
    'exec',
    'spot_launch',
    'storage_ls',
    'storage_delete',
]
