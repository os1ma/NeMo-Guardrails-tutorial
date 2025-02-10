from dotenv import load_dotenv
from nemoguardrails import LLMRails, RailsConfig

load_dotenv(override=True)

config = RailsConfig.from_path("./config")

rails = LLMRails(config)

response = rails.generate(
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        },
    ],
)
print(response)
