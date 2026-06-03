from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Shooters(Base):
    __tablename__ = 'Shooters'

    ID = Column(Integer, primary_key=True)
    PlayerName = Column(String(24)) #Имя игрока.
    PlayerSurname = Column(String(24)) #Фамилия игрока.
    GroupID = Column(Integer, ForeignKey('Group.ID')) #ID группы.

    GroupRelation = relationship("Group", back_populates="ShootersRelation")
    ShootingRelation = relationship("Shooting", back_populates="ShootersRelation")

class Group(Base):
    __tablename__ = "Group"

    ID = Column(Integer, primary_key=True)
    GroupName = Column(String(24)) #Наименование группы.

    ShootersRelation = relationship("Shooters", back_populates="GroupRelation")

class Targets(Base):
    __tablename__ = 'Targets'

    ID = Column(Integer, primary_key=True)
    NameTarget = Column(String(24)) #Имя мишени.
    FileTarget = Column(String(48)) #Имя файла мишени.

    ExerciseRelation = relationship("Exercise", back_populates="TargetsRelation")

class Exercise(Base):
    __tablename__ = 'Exercise'

    ID = Column(Integer, primary_key=True)
    ExerciseName = Column(String(48)) #Название упражнения.
    ShootersCount = Column(Integer) #Колличество стрелков.
    ShotsCount = Column(Integer) #Колличество выстрелов.
    TargetID = Column(Integer, ForeignKey("Targets.ID")) #ID мишени.
    ExerciseDescription = Column(String(500)) #Описание упражнения.
    ExerciseType = Column(Integer) #Тип упражнения.
    ExerciseTime = Column(String(24)) #Время на выполнения упражнения.
    WeaponType = Column(Integer)

    TargetsRelation = relationship("Targets", back_populates="ExerciseRelation")
    ShootingRelation = relationship("Shooting", back_populates="ExerciseRelation")

class Shooting(Base):
    __tablename__ = "Shooting"

    ID = Column(Integer, primary_key=True)
    ShootersID = Column(Integer, ForeignKey("Shooters.ID")) #ID стрелка.
    ExerciseID = Column(Integer, ForeignKey("Exercise.ID")) #ID упражнения.
    SumPoints = Column(Integer) #Результат стрельбы в поинтах.
    ShootingDate = Column(String(24)) #Дата и время стрельб.
    BulletSpentShooting = Column(Integer) #Кол-во выстрелянных патрон.
    TimeSpentShooting = Column(String(24)) #Время затраченное на упражнение.
    PdfFileName = Column(String(48)) #Имя pdf файла.

    ShootersRelation = relationship("Shooters", back_populates="ShootingRelation")
    ExerciseRelation = relationship("Exercise", back_populates="ShootingRelation")
    ShootsRelation = relationship("Shoots", back_populates="ShootingRelation")

class Shoots(Base):
    __tablename__ = "Shoots"

    ID = Column(Integer, primary_key=True)
    BulletNumber = Column(Integer) #Номер выстрела.
    PointsForBullet = Column(Integer) #Баллы за выстрел.
    ShootingStartTime = Column(String(24)) #Время от начала стрельбы.
    ShootingID = Column(Integer, ForeignKey("Shooting.ID")) #ID стрельбы.
    LaserX = Column(Integer)
    LaserY = Column(Integer)

    ShootingRelation = relationship("Shooting", back_populates="ShootsRelation")

class EncryptedData(Base):
    __tablename__ = "kfij3oi2oirkk"

    ID = Column(Integer, primary_key=True)
    FirstColumn = Column(String)
    SecondColumn = Column(String)