from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class ServiceRequest(Base):
    __tablename__ = "service_requests"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String, default="pending", nullable=False) # حالة الطلب (قيد الانتظار، معتمد، مرفوض...)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # الربط مع جدول المستخدمين
    user = relationship("User", backref="service_requests")