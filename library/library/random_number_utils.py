import random
import string


class RandomUtils:
    """
    generate random IDS

    """
    @staticmethod
    def generate_random_id() -> str:
        """
        generate random IDs 6 lenght ascii uppercase

        """
        return "".join(random.choices(string.ascii_uppercase, k=6))




