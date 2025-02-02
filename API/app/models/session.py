from app.models import Base
from app.models.base_model import BaseModel
from app.utils.countries import ALL_COUNTRIES
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from datetime import datetime, timedelta


class Session(BaseModel, Base):
    """The Session model."""

    __tablename__ = "sessions"
    expiry_time = Column(Integer, nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    def check_expiry(self):
        time_change = timedelta(seconds=self.expiry_time)
        new_time = self.created_at + time_change
        if new_time <= datetime.now():
            return False
        return True
