from core.repository.base import DBOperations
from edusmart.role.db_table import Role


class DBRole(DBOperations):
    pass


db_role = DBRole(Role)
