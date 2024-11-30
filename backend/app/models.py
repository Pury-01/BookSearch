#!/usr/biin/env python3
"""
models for the Book search application
"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Initialize the database object
db = SQLAlchemy()


class SearchHistory(db.Model):
    """
    model for storing search history
    """
    # define tablename
    __tablename__ = 'search_history'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    search_query = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    # use user_id for users who are logged in
    user_id = db.column(db.Integer, foreign_key('user.id'), nullable=True)
    # use session_id for users who are not logged in
    session_id = db.column(db.String(255), nullable=True)

    def __repr__(self):
        """
        representation of the SearchHistory object
        """
        return f"<SearchHistory id={self.id} query={self.search_query}>"
