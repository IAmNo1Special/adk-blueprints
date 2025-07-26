from dotenv import load_dotenv
from google.adk.agents import LlmAgent

from adk_blueprints.tool_blueprints import SqlDbTools, ImagenPaidTool
from adk_blueprints.instruction_blueprints import sqldb_tool_instruction, imagen_paid_tool_instruction
from adk_blueprints.description_blueprints import sqldb_agent_description, imagen_paid_agent_description


load_dotenv()

class SqlDbAgent(LlmAgent):
    '''
    A class to manage SQL database agents for interacting with a SQL database.
    '''
    def __init__(self, db_uri: str, model: str, model_provider: str, **kwargs):
        '''
        Initialize the SqlDbAgent with a database connection.
        
        Args:
            db_uri: The database connection URI.
            model: The model to use for the SQL database agent. Example: 'gemini-2.5-flash'.
            model_provider: The model provider to use for the SQL database agent. Example: 'google_genai'.
            **kwargs: Additional keyword arguments to pass to the LlmAgent constructor. See google.adk.agents.LlmAgent constructor for more details.
        '''
        super().__init__(
            name='sqldb_agent',
            model=model,
            description=sqldb_agent_description,
            instruction=sqldb_tool_instruction,
            tools=SqlDbTools(db_uri=db_uri, model=model, model_provider=model_provider).list_tools(),
            **kwargs
        )

class ImagenPaidAgent(LlmAgent):
    '''
    A class to manage image generation agents for generating images based on a prompt.
    '''
    def __init__(self, model: str, imagen_model: str, **kwargs):
        '''
        Initialize the ImagenAgent with a model connection.
        
        Args:
            model: The model to use for image generation. Example: 'gemini-2.5-flash'.
            imagen_model: The model to use for image generation. Example: 'imagen-4.0-generate-preview-06-06'.
            **kwargs: Additional keyword arguments to pass to the LlmAgent constructor. See google.adk.agents.LlmAgent constructor for more details.
        '''
        super().__init__(
            name='imagen_agent',
            model=model,
            description=imagen_paid_agent_description,
            instruction=imagen_paid_tool_instruction,
            tools=ImagenPaidTool(model=imagen_model).list_tools(),
            **kwargs
        )

