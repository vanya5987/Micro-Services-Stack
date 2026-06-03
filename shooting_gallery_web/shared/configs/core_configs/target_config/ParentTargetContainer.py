from app.utils.target_utils.target_data_creator import TargetDataCreator
from shared.configs.keys_configs.target_name_keys import TargetNameKeys

from typing import *


class ParentTargetContainer:
    PHYSICAL_TARGET_SIZE: int = 560
    FRAME_DISTANCE: int = 0.4
    MAX_CIRCLE_DIAMETER: int = 4.2

    MAX_RADII_COUNT: int = 10
    MIN_RADII_COUNT: int = 0

    LOG_SCALE_WIDTH: float = 3.5  # Коэффициент масштабирования для ширины мишеней.
    LOG_SCALE_HEIGHT: float = 6.2  # Коэффициент масштабирования для высоты мишеней.
    LOG_BASE: float = 1.53  # Основание логарифма, чем выше значение тем медленее изменения мишеней.

    REDUCTION: int = 1000  # Коэфицент сокращения нулей для более простого числового результата.
    POSITION_SCALE: int = 2  # Коэфицент позиционирования точек.

    SCALED_TARGET_WIDTH: int = 206
    SCALED_TARGET_HEIGHT: int = 274

    def __init__(self):
        # Формат таблицы: (Имя, cкелирование поинтов, (Для круглых мишеней, радиус - флаг, IPDA - мод, Army - мод)).
        self.PISTOL_25: Tuple[str, List[float], List[bool]] = (TargetNameKeys.PISTOL_25_KEY, [4.6, 2.0, 0.0],
                                                               TargetDataCreator.SetPistolStates())
        self.PISTOL_50: Tuple[str, List[float], List[bool]] = (TargetNameKeys.PISTOL_50_KEY, [2.5, 4.0, 0.0],
                                                               TargetDataCreator.SetPistolStates())
        self.PISTOL_75: Tuple[str, List[float], List[bool]] = (TargetNameKeys.PISTOL_75_KEY, [1.6, 6.0, 0.0],
                                                               TargetDataCreator.SetPistolStates())
        self.PISTOL_100: Tuple[str, List[float], List[bool]] = (TargetNameKeys.PISTOL_100_KEY, [1.0, 8.0, 0.0],
                                                                TargetDataCreator.SetPistolStates())

        self.GTO_5: Tuple[str, List[float], List[bool]] = (TargetNameKeys.GTO_5_KEY, [1.9, 4.2, 0.0],
                                                           TargetDataCreator.SetGtoStates())
        self.GTO_10: Tuple[str, List[float], List[bool]] = (TargetNameKeys.GTO_10_KEY, [0.85, 8.2, 0.0],
                                                            TargetDataCreator.SetGtoStates())

        self.IDPA_25: Tuple[str, List[float], List[bool]] = (TargetNameKeys.IDPA_25_KEY, [2.0, 1.0, 0.0],
                                                             TargetDataCreator.SetIdpaStates())
        self.IDPA_50: Tuple[str, List[float], List[bool]] = (TargetNameKeys.IDPA_50_KEY, [1.0, 0.5, 0.0],
                                                             TargetDataCreator.SetIdpaStates())
        self.IDPA_100: Tuple[str, List[float], List[bool]] = (TargetNameKeys.IDPA_100_KEY, [0.50, 0.25, 0.0],
                                                              TargetDataCreator.SetIdpaStates())
        self.IDPA_150: Tuple[str, List[float], List[bool]] = (TargetNameKeys.IDPA_150_KEY, [0.375, 0.1875, 0.0],
                                                              TargetDataCreator.SetIdpaStates())
        self.IDPA_200: Tuple[str, List[float], List[bool]] = (TargetNameKeys.IDPA_200_KEY, [0.25, 0.125, 0.0],
                                                              TargetDataCreator.SetIdpaStates())
        self.IDPA_500: Tuple[str, List[float], List[bool]] = (TargetNameKeys.IDPA_500_KEY, [0.25, 0.125, 0.0],
                                                              TargetDataCreator.SetIdpaStates())

        self.ARMY_25: Tuple[str, List[float], List[bool]] = (TargetNameKeys.ARMY_25_KEY, [10.0, 1.0, 0.0],
                                                             TargetDataCreator.SetArmyStates())
        self.ARMY_50: Tuple[str, List[float], List[bool]] = (TargetNameKeys.ARMY_50_KEY, [5.0, 2.0, 0.0],
                                                             TargetDataCreator.SetArmyStates())
        self.ARMY_75: Tuple[str, List[float], List[bool]] = (TargetNameKeys.ARMY_75_KEY, [3.2, 3.0, 0.0],
                                                             TargetDataCreator.SetArmyStates())
        self.ARMY_100: Tuple[str, List[float], List[bool]] = (TargetNameKeys.ARMY_100_KEY, [2.5, 4.0, 0.0],
                                                              TargetDataCreator.SetArmyStates())

        self.GAME_25: Tuple[str, List[float], List[bool]] = (TargetNameKeys.GAME_25_KEY, [10.0, 5.0, 1.0],
                                                             TargetDataCreator.set_game_mode_states())
        self.GAME_50: Tuple[str, List[float], List[bool]] = (TargetNameKeys.GAME_50_KEY, [5.0, 2.5, 2.0],
                                                             TargetDataCreator.set_game_mode_states())
        # Формат таблицы: (Имя, Scale point, (Для круглых мишеней, радиус - флаг, IPDA - мод, Army - мод)).

        self.targetList: List[Tuple[str, List[float], List[bool]]] = \
            [self.PISTOL_25, self.PISTOL_50, self.PISTOL_75, self.PISTOL_100,
             self.GTO_5, self.GTO_10,
             self.IDPA_25, self.IDPA_50, self.IDPA_100, self.IDPA_150, self.IDPA_200, self.IDPA_500,
             self.ARMY_25, self.ARMY_50, self.ARMY_75, self.ARMY_100,
             self.GAME_25, self.GAME_50]

    # Создает список по индексу.
    def GetTargetParametresByIndex(self, collection: List[any], index: int) -> List[any]:
        return [item[index] for item in collection]

    # Создает словарь с коэфицентами мишеней.
    def CreateCoefDict(self) -> Dict[str, List[float]]:
        return TargetDataCreator.target_dict_creator(self.GetTargetParametresByIndex(self.targetList, 0),
                                                     self.GetTargetParametresByIndex(self.targetList, 1))

    # Создает словарь с модом (RadiusMode).
    def CreateRadiusModeDict(self) -> Dict[str, bool]:
        return self.ConfigureTargetDict(0)

    # Создает словарь с модом (CircleState).
    def CreateCircleStateDict(self) -> Dict[str, bool]:
        return self.ConfigureTargetDict(1)

    # Создает словарь с модом (IdpaMode).
    def CreateIdpaModeDict(self) -> Dict[str, bool]:
        return self.ConfigureTargetDict(2)

    # Создает словарь с модом (ArmyMode).
    def CreateArmyModeDict(self) -> Dict[str, bool]:
        return self.ConfigureTargetDict(3)

    def CreateGameModeDict(self) -> Dict[str, bool]:
        return self.ConfigureTargetDict(4)

    def ConfigureTargetDict(self, index):
        states: List[bool] = self.GetTargetParametresByIndex(self.targetList, 2)
        return TargetDataCreator.target_dict_creator(self.GetTargetParametresByIndex(self.targetList, 0),
                                                     self.GetTargetParametresByIndex(states, index))
