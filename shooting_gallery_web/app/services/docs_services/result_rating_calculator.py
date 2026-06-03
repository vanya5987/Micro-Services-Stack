from shared.configs.core_configs.rating_config import RatingConfig


class ResultRatingCalculator:
    def __init__(self, result_rating_container: RatingConfig):
        self.result_rating_container = result_rating_container

    def get_rating_by_score(self, current_exercise_name: str, player_score_result: int):
        last_comparable_index: int = 0

        if not current_exercise_name in self.result_rating_container.rating_comparable_map:
            return self.result_rating_container.none_rating_header

        if player_score_result and current_exercise_name:  # Валидация входных данных.
            for target_name, rating_thresholds in self.result_rating_container.rating_comparable_map.items():
                if len(rating_thresholds) != len(self.result_rating_container.rating_result) - 1:
                    raise Exception("Кол-во порогов или оценок указаны некорректно!")

                if target_name == current_exercise_name:
                    for rating_value in rating_thresholds:
                        if player_score_result >= rating_value:
                            last_comparable_index += 1
                    break

        return self.result_rating_container.rating_result[last_comparable_index]
