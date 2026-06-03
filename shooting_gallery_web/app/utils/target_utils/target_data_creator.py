from typing import *

class TargetDataCreator:
    @staticmethod
    def get_dict_value(dictSearcher: Dict[str, Union[List[float], bool]], inputName: str) -> Union[float, bool]:
        if TargetDataCreator.get_values_by_name(dictSearcher, inputName):
            value: Union[float, bool] = TargetDataCreator.get_values_by_name(dictSearcher, inputName)

            return value

    @staticmethod
    def get_values_by_name(collections: Dict[str, int], inputName: str) -> int:
        value: int = 0

        for targetName in collections:
            if targetName == inputName:
                value = collections[targetName]

        if value is None:
            raise Exception(f"Value by name is not contains! {collections}")

        return value

    @staticmethod
    def target_dict_creator(targetNames: List[str], valueList: List[any]) -> Dict[str, any]:
        targetDict: Dict[str, any] = {}

        if len(targetNames) != len(valueList):
            print("Targets names count != valueList items in file ParentTargetContainer/target_dict_creator!")

        for i, name in enumerate(targetNames):
            targetDict[name] = valueList[i]

        return targetDict

    @staticmethod
    def SetPistolStates() -> List[bool]:
        return [True, True, False, False, False]

    @staticmethod
    def SetGtoStates() -> List[bool]:
        return [True, True, False, False, False]

    @staticmethod
    def SetIdpaStates() -> List[bool]:
        return [False, False, True, False, False]

    @staticmethod
    def SetArmyStates() -> List[bool]:
        return [False, False, False, True, False]

    @staticmethod
    def set_game_mode_states() -> List[bool]:
        return [False, False, False, False, True]