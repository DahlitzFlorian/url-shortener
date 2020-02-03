import datetime

import sqlalchemy as sa

from app.data.modelbase import SqlAlchemyBase


class Link(SqlAlchemyBase):
    __tablename__ = "links"
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    short_link = sa.Column(sa.String, nullable=False)
    destination = sa.Column(sa.String, nullable=False)

    def __repr__(self):
        return '<Link {} --> {}>'.format(self.short_link, self.destination)
