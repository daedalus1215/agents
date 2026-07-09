import asyncio
import os
import requests
from dotenv import load_dotenv
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner, trace, function_tool, SQLiteSession
load_dotenv(override=True)

async def main():
    agent = Agent(name="Jokester", instructions="You are a joke teller", model="gpt-5.4-mini")
    with trace("Telling a joke"):
        result = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
    print(result.final_output)
    print(result.to_input_list())
    
    result = Runner.run_streamed(agent, input="Please tell me 5 jokes about AI Agents.")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

asyncio.run(main())