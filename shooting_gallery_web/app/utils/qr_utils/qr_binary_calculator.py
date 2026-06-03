from shared.configs.core_configs.qr_config import QrConfig

from typing import List

class QrBinaryHandler:
    # Кодирует число в бинарный код.
    @staticmethod
    def encode_number_with_markers(num: int) -> List[List[bool]]:
        if num < QrConfig.MIN_MATRIX_VALUE or num > QrConfig.MAX_MATRIX_VALUE:
            raise ValueError(f"Number must be between {QrConfig.MIN_MATRIX_VALUE} and {QrConfig.MAX_MATRIX_VALUE}")

        matrix: List[List[bool]] = [[False for _ in range(QrConfig.MATRIX_SIZE)]
                                    for _ in range(QrConfig.MATRIX_SIZE)]

        bit_string = format(num, f'0{QrConfig.BIT_COUNT}b')

        bit_index = 0
        for y in range(QrConfig.MATRIX_SIZE):
            for x in range(QrConfig.MATRIX_SIZE):
                if QrConfig.OUTLINE_INDEXES[y][x]:
                    continue
                if bit_index < QrConfig.BIT_COUNT:
                    matrix[y][x] = (bit_string[bit_index] == '1')
                    bit_index += 1

        return matrix

    #Декодирует бинарный код.
    @staticmethod #Декодер инвертирован.
    def decode_with_markers(matrix: List[List[bool]]) -> int: #Приходит matrix с контуром и высчитывает тоже с контуром.
        bit_string = ""
        bit_count = 0

        for y in range(QrConfig.MATRIX_SIZE):
            for x in range(QrConfig.MATRIX_SIZE):
                if QrConfig.OUTLINE_INDEXES[y][x]:
                    continue
                if bit_count < QrConfig.BIT_COUNT:
                    bit_string += '1' if matrix[y][x] else '0'
                    bit_count += 1

        return abs(int(bit_string, 2) - QrConfig.MAX_MATRIX_VALUE) #Инвертируем результат.