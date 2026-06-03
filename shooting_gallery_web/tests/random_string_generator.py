import random
import string

class RandomStringGenerator:
    @staticmethod
    def generate_random_string() -> str:
        chars = string.ascii_letters + string.digits + "+-_/="
        length = random.randint(8, 24)
        return ''.join(random.choice(chars) for _ in range(length))