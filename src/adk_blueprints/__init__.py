'''
ADK Blueprints - A collection of reusable components to use with the google-adk framework.
'''

__version__ = '0.1.0'

from .agent_blueprints import SqlDbAgent, ImagenPaidAgent, GmailAgent, GithubAgent, RedditSearchAgent
from .tool_blueprints import SqlDbTools, ImagenPaidTool, GmailTools, RedditSearchTool
from .description_blueprints import sqldb_agent_description, imagen_paid_agent_description, gmail_agent_description, github_agent_description, redditsearch_agent_description
from .instruction_blueprints import sqldb_tool_instruction, imagen_paid_tool_instruction, gmail_tool_instruction, github_tool_instruction, redditsearch_tool_instruction

__all__ = [
    'SqlDbAgent',
    'SqlDbTools',
    'sqldb_agent_description',
    'sqldb_tool_instruction',
    'ImagenPaidAgent',
    'ImagenPaidTool',
    'imagen_paid_agent_description',
    'imagen_paid_tool_instruction',
    'GmailAgent',
    'GmailTools',
    'gmail_agent_description',
    'gmail_tool_instruction',
    'GithubAgent',
    'GithubTools',
    'github_agent_description',
    'github_tool_instruction',
    'RedditSearchAgent',
    'RedditSearchTool',
    'redditsearch_agent_description',
    'redditsearch_tool_instruction'
    '__version__',
]

                                                       