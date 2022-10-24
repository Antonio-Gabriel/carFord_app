from datetime import datetime
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime

Base = declarative_base()


class PersonModel(Base):
    """model to person"""

    __tablename__ = "person"

    id = Column(String(200), primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    is_admin = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"PersonModel(id={self.id}, name={self.name}, \
                 email={self.email})"


class VehicleModel(Base):
    """model to vehicle"""

    __tablename__ = "vehicle"

    id = Column(String(200), primary_key=True)
    person_id = Column(String(200), ForeignKey("person.id"))
    model = Column(String(20), nullable=False)
    color = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=current_timestamp())

    person = relationship("PersonModel", foreign_keys=[person_id])

    def __repr__(self) -> str:
        return f"VehicleModel(id={self.id}, model={self.model}, \
                 color={self.color}, created_at={self.created_at}, updated_at={self.updated_at})"


class AdminModel(Base):
    """model to admin"""

    __tablename__ = "admin"

    id = Column(String(200), primary_key=True)
    person_id = Column(String(200), ForeignKey("person.id"))
    password = Column(String(100), nullable=False)

    person = relationship("PersonModel", foreign_keys=[person_id])

    def __repr__(self) -> str:
        return f"AdminModel(id={self.id}, person_id={self.person_id}, \
                 password={self.password})"
