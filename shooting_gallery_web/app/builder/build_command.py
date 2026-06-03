from shared.pathings.builder_config import BuilderConfig
from app.decorators.base_cmd_creator import create_base_cmd_command

from typing import List

class BuildCommand:
    # Команда создания .spec файла.
    @create_base_cmd_command
    def create_extend_cmd_command(self, builder_config: BuilderConfig) -> List[str]:
        cmd: List[str] = []

        # Добавляем явные пакеты библиотек.
        for package_append_command in builder_config.get_add_packages_command():
            cmd.append(package_append_command)

        return cmd

    @create_base_cmd_command
    def create_base_cmd_command(self, builder_config: BuilderConfig) -> List[str]:
        return []