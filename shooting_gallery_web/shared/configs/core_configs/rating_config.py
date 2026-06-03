from typing import List, Dict

class RatingConfig:
    def __init__(self):
        self.rating_comparable_map: Dict[str, List[int]] = {"Упражнение №1 5m": [13, 20, 25], "Упражнение №2 10m": [18, 25, 30],
                                            "Упражнение начальных стрельб №1": [15, 20, 25], "Упражнение учебных стрельб №1": [18, 21, 25]}

        for _, value in self.rating_comparable_map.items():
            value.sort() #Сортировка нужна, что бы гарантировать что значения оценки будут строго в порядке возрастания,
            # если в дальнейшем будет добавлена иная система по получению значений оценки.

        self.rating_result = ["плохо", "удовлетворительно", "хорошо", "отлично"]
        self.none_rating_header = "отсутствует"