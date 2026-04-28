import os
import asyncio
import base64

from capmonstercloudclient.requests import RecognitionComplexImageTaskRequest
from capmonstercloudclient import ClientOptions, CapMonsterClient


async def main():
    client_options = ClientOptions(api_key=os.getenv('API_KEY'))
    cap_monster_client = CapMonsterClient(options=client_options)

    image_paths = [f"./images/betpunch_{i}.png" for i in range(1, 10)]
    images_base64 = []
    for path in image_paths:
        with open(path, "rb") as f:
            images_base64.append(base64.b64encode(f.read()).decode("utf-8"))

    request = RecognitionComplexImageTaskRequest(
        imagesBase64=images_base64,
        metadata={
            "Task": "betpunch_3x3_rotate",
        },
    )

    response = await cap_monster_client.solve_captcha(request)
    # response["answer"] is a list of 9 values (1-4 per image):
    # 4 = no rotation needed; 1-3 = number of 90° CCW rotations needed
    # e.g. [4, 4, 4, 4, 4, 3, 1, 2, 2]
    print(f"Solution: {response}")


if __name__ == "__main__":
    asyncio.run(main())
