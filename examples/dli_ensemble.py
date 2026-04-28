import os
import asyncio
import base64

from capmonstercloudclient.requests import RecognitionComplexImageTaskRequest
from capmonstercloudclient import ClientOptions, CapMonsterClient


async def main():
    client_options = ClientOptions(api_key=os.getenv('API_KEY'))
    cap_monster_client = CapMonsterClient(options=client_options)

    with open("./images/dli.jpg", "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    request = RecognitionComplexImageTaskRequest(
        imagesBase64=[image_base64],
        metadata={
            "Task": "dli",
        },
    )

    response = await cap_monster_client.solve_captcha(request)
    # response["answer"] is the computed result as a string, e.g. "1"
    print(f"Solution: {response}")


if __name__ == "__main__":
    asyncio.run(main())
