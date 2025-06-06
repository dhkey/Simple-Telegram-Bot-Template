import sqlite3
from structlog.typing import FilteringBoundLogger
import structlog
from typing import Tuple, Dict, Any, Optional
import os
import logging

class Connection:
    
    def __init__(self) -> None:
        
        self.logger = logging.getLogger(__name__)
                
        self.database_name = os.getenv("DB_NAME", 'default_database.db')
        
        try:
            self.connection = sqlite3.connect(
                database = self.database_name,
                check_same_thread=False
            )
            self.connection.row_factory = sqlite3.Row
            self.logger.debug(f"Connected to [{self.database_name}] SQLite database ✅")
        except sqlite3.Error as e:
            self.logger.error(f"Error while connecting to SQLite database: {e}")
            exit(0) 

        self.cursor = self.connection.cursor()
        
    def commit(self) -> None:
        self.connection.commit()
    
    def execute(self, query, params=None) -> None:
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.commit()
    
    def fetchOne(self, query, params=None) -> Optional[Any]:
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        result = self.cursor.fetchone()

        if not result:
            return None
        elif len(result) > 1:
            return result
        elif len(result) == 1:
            return result[0]
    
    def fetchAll(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def closeConnection(self) -> None:
        self.logger.debug("Closing connection...")
        self.connection.close()
        self.logger.debug("Closed ✅")