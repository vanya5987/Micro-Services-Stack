from shared.pathings.path_config import PathConfig
from app.utils.os_system_utils.get_system_type import SystemTypeGetter
import subprocess
import os


class ExplorerOpener:
    @staticmethod
    def open_pdf_folder(filePath: str = PathConfig.REPORT_DIRECTORY_PATH):
        if SystemTypeGetter.system_is_windows():
            try:
                subprocess.Popen(['explorer', filePath])
            except:
                raise

        else:
            managers = [
                ['nautilus', filePath],
                ['dolphin', filePath]
            ]

            for manager in managers:
                try:
                    result = subprocess.run(['which', manager[0]],
                                            capture_output=True, text=True)
                    if result.returncode == 0:
                        clean_env = ExplorerOpener._get_clean_environment()
                        subprocess.Popen(manager,
                                         stdout=subprocess.DEVNULL,
                                         stderr=subprocess.DEVNULL,
                                         env=clean_env)
                        return True
                except:
                    raise

            try:
                clean_env = ExplorerOpener._get_clean_environment()
                subprocess.Popen(['xdg-open', filePath],
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL,
                                 env=clean_env)
                return True
            except:
                raise

    @staticmethod
    def _get_clean_environment():
        env = os.environ.copy()

        conflict_vars = [
            'PYTHONPATH', 'PYTHONHOME', 'QT_PLUGIN_PATH',
            'LD_LIBRARY_PATH', 'VIRTUAL_ENV'
        ]

        for var in conflict_vars:
            env.pop(var, None)

        if 'PATH' in env:
            paths = env['PATH'].split(':')
            clean_paths = [p for p in paths if not any(x in p for x in ['.venv', 'virtualenv', 'venv'])]
            env['PATH'] = ':'.join(clean_paths)

        return env
