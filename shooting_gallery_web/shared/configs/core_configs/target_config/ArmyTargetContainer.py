class ArmyTargetContainer:
    TOP_ARMY_CUT_SCALE: float = 0.1 #Срез фигуры на 40% от ширины.
    BOTTOM_ARMY_CUT_SCALE: float = 0.0 #Срез фигуры на 10% от ширины.

    LOG_ARMY_SCALE_WIDTH: float = 5.0 #Коэффициент масштабирования для ширины.
    LOG_ARMY_SCALE_HEIGHT: float = 4.5 #Коэффициент масштабирования для высоты.

    ARMY_HEAD_WIDTH: int = 26 #Скейл ширины головы.
    ARMY_HEAD_HEIGHT: int = 100 #Скейл высоты головы.
    ARMY_TRAPEZOID_SCALE_TO_HEAD: int = 28 #Скейл посадки трапеции ближе к шее.
    ARMY_TRAPEZOID_LENGTH: int = 17 #Скейл длины трапеции.
    ARMY_SHOULDER_HEIGHT: int = 20 #Скейл посадки плечей.

    ARMY_TARGET_DRAWER_SCALE: float = 4.50 #Скейл коррекции отрисовки.