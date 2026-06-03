from shared.configs.core_configs.decode_config import DecodeConfig

class LicenceGenerator:
    KEY: str = "fdbc1d5b78aa"

print(DecodeConfig().CreateStrippedHash(LicenceGenerator.KEY))