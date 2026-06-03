from app.entitys.processing_entity.draw_processing_entity import DrawShootingProcessing
from app.utils.draw_utils.contour_drawer import ContourDrawer


class CircleDrawer:
    @staticmethod
    def permanent_circle_drawer(shooting_session: DrawShootingProcessing):
        if shooting_session.shooting_mods.circle_state == True and len(shooting_session.sorted_contours) == len(
                shooting_session.centers):
            for player_id in range(1, len(shooting_session.centers) + 1):
                if player_id in shooting_session.valid_contour_matrix:
                    if shooting_session.valid_contour_matrix[player_id] and len(shooting_session.radii) > 0:
                        ContourDrawer.draw_circle(shooting_session.contour_image, shooting_session.centers[player_id],
                                                  int(min(shooting_session.radii) / shooting_session.target_scale[1]))
