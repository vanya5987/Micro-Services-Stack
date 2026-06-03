import cv2


class VisionCalibrationUtils:
    BASE_DISTANCE_M = 2.0
    BASE_AREA = 54712.5
    COEF = 100
    ALPHA = 180

    @staticmethod
    def _calculate_distance_m(contour) -> float:
        area = cv2.contourArea(contour)

        return (
            VisionCalibrationUtils.BASE_DISTANCE_M *
            VisionCalibrationUtils.BASE_AREA /
            area
        )

    @staticmethod
    def get_distance(contour) -> float:
        raw = VisionCalibrationUtils._calculate_distance_m(contour)

        data = raw * VisionCalibrationUtils.COEF * (VisionCalibrationUtils.COEF * 2) // VisionCalibrationUtils.ALPHA

        return data