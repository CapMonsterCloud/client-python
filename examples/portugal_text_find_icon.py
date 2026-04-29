import os
import io
import asyncio
import base64

from PIL import Image

from capmonstercloudclient.requests import RecognitionComplexImageTaskRequest
from capmonstercloudclient import ClientOptions, CapMonsterClient


async def main():
    client_options = ClientOptions(api_key=os.getenv('API_KEY'))
    cap_monster_client = CapMonsterClient(options=client_options)

    
    
    # 5 icon images must be merged horizontally in display order before sending
    with open("./images/portugal.png", "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    request = RecognitionComplexImageTaskRequest(
        imagesBase64=[image_base64],
        metadata={
            "Task": "portugal_text_find_icon",
            # Serialize non-ASCII characters as escaped Unicode, e.g.:
            # "Encontre o(a) avião." instead of "Encontre o(a) avião."
            "TaskArgument": "Encontre o(a) avi\\u00E3o.",
        },
    )

    response = await cap_monster_client.solve_captcha(request)
    # response["answer"] is a 1-based index of the matching icon, e.g. [4]
    print(f"Solution: {response}")


if __name__ == "__main__":
    asyncio.run(main())
