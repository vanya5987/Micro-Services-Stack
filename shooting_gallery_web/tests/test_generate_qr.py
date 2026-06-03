from app.services.qr_services.qr_image_saver import QrImageSaver
from shared.configs.core_configs.qr_config import QrConfig
from app.utils.qr_utils.qr_binary_calculator import QrBinaryHandler

class TestGenerateQr:
    @staticmethod
    def test_generate_qr():
        save_qr_image = QrImageSaver()

        for file_name, value in QrConfig.TARGET_TYPES.items():
            save_qr_image.save_qr_image(file_name, QrBinaryHandler.encode_number_with_markers(value))