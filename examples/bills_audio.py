import os
import asyncio
import base64

from capmonstercloudclient.requests import RecognitionComplexImageTaskRequest
from capmonstercloudclient import ClientOptions, CapMonsterClient


async def main():
    client_options = ClientOptions(api_key=os.getenv('API_KEY'))
    cap_monster_client = CapMonsterClient(options=client_options)

    with open("/path/to/audio.wav", "rb") as f:
        audio_base64 = base64.b64encode(f.read()).decode("utf-8")

    request = RecognitionComplexImageTaskRequest(
        imagesBase64=[audio_base64],
        metadata={
            "Task": "bills_audio",
            "PayloadType": "Audio",
        },
    )

    response = await cap_monster_client.solve_captcha(request)
    # response["answer"] contains the digits heard in the audio, e.g. [6, 8, 4, 1, 2, 3]
    print(f"Solution: {response}")


if __name__ == "__main__":
    asyncio.run(main())
