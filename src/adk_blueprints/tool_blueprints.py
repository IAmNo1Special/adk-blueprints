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
from google.genai import types
from google import genai
from typing import List

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
        Returns a list of all the SqlDbTool's tools.
        '''
        return [self.info_tool, self.list_tool, self.query_checker_tool, self.query_tool]

class ImagenTool:
    """
    A class for generating images using the Imagen model.
    """
    
    def __init__(self):
        """
        Initialize the ImagenTool with the necessary client.
        """
        load_dotenv()
        self.genai_client = genai.Client()
    
    def generate_images(self, image_prompt: str, num_of_images: int = 1, model: str = 'imagen-3.0-generate-002') -> List[types.GeneratedImage] | str:
        """
        Generate a number of images based on the provided prompt.
        
        Args:
            image_prompt (str): The prompt to base the images on.
            num_of_images (int): Number of images to generate. Default: 1.
            model (str): The model to use for image generation. Default: "imagen-3.0-generate-002".
        
        Returns:
            List[types.GeneratedImage]: A list of generated images if successful.
            str: Error message if no images are generated.
        """
        try:
            response = self.genai_client.models.generate_images(
                model=model,
                prompt=image_prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=num_of_images,
                )
            )
        except Exception as e:
            print(f"Error generating images: {e}")
            return f"Error generating images: {e}"

        if response.generated_images:
            for generated_image in response.generated_images:
                generated_image.image.show()
            return response.generated_images
        else:
            print(f"No images generated: {response}")
            return f"No images generated: {response}"

    def list_tools(self):
        '''
        Returns a list of all the ImagenTool's tools.
        '''
        return [self.generate_images]

