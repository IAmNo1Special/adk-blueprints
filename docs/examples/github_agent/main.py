import asyncio
import json
from dotenv import load_dotenv

from google.genai import types 
from google.adk.runners import Runner
from google.adk.memory import InMemoryMemoryService
from google.adk.sessions import InMemorySessionService

from adk_blueprints import GithubAgent


load_dotenv()


async def call_agent_async(runner: Runner, user_id: str, session_id: str, prompt: str):
    '''
    Sends the query to the agent and returns the response.
    '''
    content = types.Content(
        role='user',
        parts=[
            types.Part(text=prompt),
        ]
    )
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        if not event.content:
            print(f'<<< [{event.author}]: {event}')
            return
            
        author = event.author
        parts = event.content.parts
        
        for part in parts:
            if part.text:
                text = part.text
                # Truncate long text to 200 characters
                if len(text) > 200:
                    text = text[:197] + '...'
                print(f'<<< [{author}]: {text}')
            elif part.function_call:
                func_call = part.function_call
                print(f'<<< [{author}]: Function call: {func_call.name}')
                # Truncate args if too long
                args = json.dumps(func_call.args)
                if len(args) > 100:
                    args = args[:97] + '...'
                print(f'   ^^^ Args: {args}')
            elif part.function_response:
                func_response = part.function_response
                print(f'<<< [{author}]: Function response: {func_response.name}')
                # Truncate response if too long
                response = json.dumps(func_response.response)
                if len(response) > 100:
                    response = response[:97] + '...'
                print(f'^^^ Response: {response}')

async def main():
    '''
    Main function to run the github agent.
    '''
    try:
        APP_NAME = 'github_agent_example'
        USER_ID = 'user_id'
        SESSION_ID = 'session_id'

        github_agent = GithubAgent(model='gemini-2.5-flash')

        session_service = InMemorySessionService()
        memory_service = InMemoryMemoryService()
        runner = Runner(app_name=APP_NAME, agent=github_agent, session_service=session_service, memory_service=memory_service)
        await runner.session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=SESSION_ID,
            state={}
        )
    except Exception as e:
        print(f'Error creating session: {e}')
        return
    while True:
        prompt = input('>>> [User Query]: ')
        if not prompt:
            break
        await call_agent_async(runner, USER_ID, SESSION_ID, prompt)

if __name__ == '__main__':
    asyncio.run(main())
