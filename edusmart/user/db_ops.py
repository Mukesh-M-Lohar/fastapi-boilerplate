from core.repository.base import DBOperations
from edusmart.user.db_table import User


class DBUser(DBOperations):
    pass


db_user = DBUser(User)
