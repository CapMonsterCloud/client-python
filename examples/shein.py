import os
import asyncio
import base64

from capmonstercloudclient.requests import RecognitionComplexImageTaskRequest
from capmonstercloudclient import ClientOptions, CapMonsterClient


async def main():
    client_options = ClientOptions(api_key=os.getenv('API_KEY'))
    cap_monster_client = CapMonsterClient(options=client_options)

    with open("./images/shein.png", "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    request = RecognitionComplexImageTaskRequest(
        imagesBase64=[image_base64],
        metadata={
            "Task": "shein",
        },
    )

    response = await cap_monster_client.solve_captcha(request)
    # response["answer"] contains click coordinates, e.g.:
    # [{"X": 69.0, "Y": 201.9}, {"X": 128.0, "Y": 281.5}, {"X": 181.0, "Y": 49.9}]
    print(f"Solution: {response}")


if __name__ == "__main__":
    asyncio.run(main())
