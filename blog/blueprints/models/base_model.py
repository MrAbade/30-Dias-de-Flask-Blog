from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
from datetime import timezone

from . import db


class BaseModel(db.Model):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return f'{cls._domain_name.title()}{cls.__name__.title()}'

    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def before_save(self):
        return

    def after_save(self):
        return

    def save(self, auto_commit: bool = True):
        self.before_save()

        db.session.add(self)

        if auto_commit:
            try:
                db.session.commit()
            except Exception as error:
                db.session.rollback()
                raise error

        self.after_save()
