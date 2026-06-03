from shared.configs.core_configs.target_config.ParentTargetContainer import ParentTargetContainer
from app.utils.target_utils.target_data_creator import TargetDataCreator

from typing import *

class ValidParentTargetValues:
    def __init__(self):
        self.parentTargetContainer: ParentTargetContainer = ParentTargetContainer()

#Вычисляет валидные знаечние и состояния ля текущей цели.
    def CalculateValidTargetValues(self, inputName: str) -> List[Union[float, bool]]:
        coefDict: Dict[str, List[float]] = self.parentTargetContainer.CreateCoefDict()
        radiusModeDict: Dict[str, bool] = self.parentTargetContainer.CreateRadiusModeDict()
        circleStateDict: Dict[str, bool] = self.parentTargetContainer.CreateCircleStateDict()
        idpaModeDict: Dict[str, bool] = self.parentTargetContainer.CreateIdpaModeDict()
        armyModeDict: Dict[str, bool] = self.parentTargetContainer.CreateArmyModeDict()
        gameModeDict: Dict[str, bool] = self.parentTargetContainer.CreateGameModeDict()

        coef: float = TargetDataCreator.get_dict_value(coefDict, inputName) #Ошибка в коллекции
        radiusMode: bool = TargetDataCreator.get_dict_value(radiusModeDict, inputName)
        circleState: bool = TargetDataCreator.get_dict_value(circleStateDict, inputName)
        idpaMode: bool = TargetDataCreator.get_dict_value(idpaModeDict, inputName)
        armyMode: bool = TargetDataCreator.get_dict_value(armyModeDict, inputName)
        gameMode: bool = TargetDataCreator.get_dict_value(gameModeDict, inputName)

        return [coef, radiusMode, circleState, idpaMode, armyMode, gameMode]