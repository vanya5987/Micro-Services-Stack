from app.api.database_api.DataStorageGetter import DataStorageGetter
from app.api.database_api.DbCreator import EncryptedData

class EncryptedDataRepository:
    def __init__(self, connection: DataStorageGetter):
        self.connection: DataStorageGetter = connection

    def create_encrypted_data(self, first_data_value: str, second_data_value: str) -> bool:
        try:
            self.connection.session.add(EncryptedData(FirstColumn=first_data_value, SecondColumn=second_data_value))
            self.connection.session.commit()
            return True
        except:
            self.connection.session.rollback()
            return False

    def get_encrypted_pass_key(self, object_id: int = 495) -> str:
        write = self.connection.session.query(EncryptedData.FirstColumn).filter(EncryptedData.ID == object_id).first()

        return write[0]

    def update_pass_key(self, new_key: str, object_id: int = 495) -> bool:
        try:
            self.connection.session.query(EncryptedData).filter(EncryptedData.ID == object_id).update(
                {"FirstColumn": new_key})

            self.connection.session.commit()
            return True
        except Exception:
            return False

    def delete_row(self, row_id: int):
        try:
            self.connection.session.query(EncryptedData).filter(EncryptedData.ID == row_id).delete()
            self.connection.session.commit()
            return True
        except:
            self.connection.session.rollback()
            return False
