from shared.pathings.path_config import PathConfig

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#from app.api.database_api.DbCreator import Base
#import app.api.database_api.DbCreator

class DataStorageGetter:
    def __init__(self):
        dataUrl = f"sqlite:///{PathConfig.DATA_BASE_PATH}"
        engine = create_engine(dataUrl, echo=False)

        #Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine) #Ссылка на бд.
        self.session = Session() #Глобальная копия для работы.