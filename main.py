import json
from openai import OpenAI
from dotenv import load_dotenv

from llm import TOOLS
from tools import *

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

tool_map = {
    "list_files": list_files,
    "read_file": read_file,
    "create_file": create_file
}

while True:
    user_input = input(">>> ")

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ],
        tools=TOOLS
    )

    message = response.choices[0].message

    if message.tool_calls:
        for tool_call in message.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            print(f"\n[TOOL CALL] {name}({args})")

            result = tool_map[name](**args)

            print("\n[RESULT]")
            print(result)

    else:
        print(message.content)
