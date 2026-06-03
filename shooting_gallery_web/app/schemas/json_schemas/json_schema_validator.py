from shared.pathings.path_config import PathConfig
from app.presenters.json_presenter import JsonPresenter
from shared.configs.keys_configs.json_key_config import JsonKeyConfig


class JsonSchemaValidator:
    def __init__(self):
        self.json_controller = JsonPresenter.get_instance()

        cam_settings_json_path: str = PathConfig.CAM_SETTING_JSON_PATH
        licence_json_path: str = PathConfig.LICENCE_JSON_PATH
        version_json_path: str = PathConfig.VERSION_JSON_PATH
        shooting_states_json_path: str = PathConfig.SHOOTING_STATES_JSON_PATH
        program_settings_json_path: str = PathConfig.PROGRAM_SETTINGS_JSON_PATH
        developer_settings_json_path: str = PathConfig.DEVELOPER_SETTINGS

        cam_settings = (self.json_controller.read_json_file(cam_settings_json_path), cam_settings_json_path)
        licence_settings = (self.json_controller.read_json_file(licence_json_path), licence_json_path)
        version_info_settings = (self.json_controller.read_json_file(version_json_path), version_json_path)
        shooting_states = (self.json_controller.read_json_file(shooting_states_json_path), shooting_states_json_path)
        program_setting = (self.json_controller.read_json_file(program_settings_json_path), program_settings_json_path)
        developer_setting = (self.json_controller.read_json_file(developer_settings_json_path), developer_settings_json_path)

        self.all_json_settings = [cam_settings, licence_settings, version_info_settings, shooting_states,
                                  program_setting, developer_setting]
        self.all_schemas = [{key: value for (key, value) in schema} for schema in JsonKeyConfig.ALL_SCHEMAS]

    def check_valid_schemas(self):
        if len(self.all_json_settings) != len(self.all_schemas):
            raise Exception("Schemas count and data count doesn't should be different!")

        for setting_index in range(len(self.all_json_settings)):
            current_settings = self.all_json_settings[setting_index][0]
            current_schema = self.all_schemas[setting_index]

            if len(current_settings) != len(current_schema):
                self.json_controller.upload_data(self.all_json_settings[setting_index][1], current_schema)
            else:
                pass  # Схемы валидны, ничего делать не нужно!
