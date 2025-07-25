from dotenv import load_dotenv
from langchain_community.utilities.sql_database import SQLDatabase
from langchain.chat_models import init_chat_model
from langchain_community.tools.sql_database.tool import (
    InfoSQLDatabaseTool,
    ListSQLDatabaseTool,
    QuerySQLCheckerTool,
    QuerySQLDatabaseTool,
)
from google.adk.tools.langchain_tool import LangchainTool

class SqlDbTools:
    '''
    A class to manage SQL database tools for interacting with a SQL database.
    '''
    
    def __init__(self, db_uri: str, model: str, model_provider: str):
        '''
        Initialize the SqlDbTools with a database connection.
        
        Args:
            db_uri: The database connection URI.
            model: The model to use for the SQL database tools. Example: "gemini-2.5-flash".
            model_provider: The model provider to use for the SQL database tools. Example: "google_genai".
        '''
        load_dotenv()
        self.llm = init_chat_model(model, model_provider=model_provider)
        self.db = SQLDatabase.from_uri(db_uri)
        
        # Initialize database tools
        self.info_tool = LangchainTool(InfoSQLDatabaseTool(db=self.db))
        self.list_tool = LangchainTool(ListSQLDatabaseTool(db=self.db))
        self.query_checker_tool = LangchainTool(QuerySQLCheckerTool(db=self.db, llm=self.llm))
        self.query_tool = LangchainTool(QuerySQLDatabaseTool(db=self.db))
    
    def list_tools(self):
        '''
        Returns a list of all the SqlDbTools tools.
        '''
        return [self.info_tool, self.list_tool, self.query_checker_tool, self.query_tool]