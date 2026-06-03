from shared.pathings.builder_config import BuilderConfig

from typing import List
from functools import wraps
import os

def create_base_cmd_command(func):
    @wraps(func)
    def wrapper(self, builder_config: BuilderConfig, *args, **kwargs):
        cmd: List[str] = []

        for cmd_param in builder_config.command_params:
            cmd.append(cmd_param)

        cmd.append(f'--name={builder_config.start_file_name}')
        cmd.extend(func(self, builder_config, *args, **kwargs))

        cmd.append(f'--paths={builder_config.indicator_path}')
        cmd.append(os.path.join(builder_config.indicator_path, builder_config.root_file_name))

        return cmd

    return wrapper