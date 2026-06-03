import hashlib
import base64

class Encryptor:
    KEY = hashlib.sha256(b"asf3afqwr124125t2wegfs32dsase2").digest()

    @staticmethod
    def pass_key_sha_converter(inputString: str) -> str:
        sha256Hash = hashlib.sha256()
        sha256Hash.update(inputString.encode('utf-8'))
        return sha256Hash.hexdigest()

    @staticmethod
    def _keystream(length: int) -> bytes:
        stream = b''
        counter = 0

        while len(stream) < length:
            block = hashlib.sha256(
                Encryptor.KEY + counter.to_bytes(4, 'big')
            ).digest()
            stream += block
            counter += 1

        return stream[:length]

    @staticmethod
    def __encrypt_bytes(text: str) -> bytes:
        data = text.encode()
        ks = Encryptor._keystream(len(data))
        return bytes([a ^ b for a, b in zip(data, ks)])

    @staticmethod
    def __decrypt_bytes(data: bytes) -> str:
        ks = Encryptor._keystream(len(data))
        return bytes([a ^ b for a, b in zip(data, ks)]).decode()

    @staticmethod
    def __bytes_to_str(data: bytes) -> str:
        return base64.b64encode(data).decode('utf-8')

    @staticmethod
    def __str_to_bytes(data: str) -> bytes:
        return base64.b64decode(data.encode('utf-8'))

    @staticmethod
    def encrypt(text: str) -> str:
        encrypted = Encryptor.__encrypt_bytes(text)
        return Encryptor.__bytes_to_str(encrypted)

    @staticmethod
    def decrypt(data: str) -> str:
        raw_bytes = Encryptor.__str_to_bytes(data)
        return Encryptor.__decrypt_bytes(raw_bytes)