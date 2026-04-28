import os
import asyncio

from capmonstercloudclient.requests import AlibabaCustomTaskRequest, ProxyInfo
from capmonstercloudclient import ClientOptions, CapMonsterClient


async def main():
    client_options = ClientOptions(api_key=os.getenv('API_KEY'))
    cap_monster_client = CapMonsterClient(options=client_options)

    # Proxyless (basic parameters)
    request_proxyless = AlibabaCustomTaskRequest(
        websiteUrl="https://www.example.com",
        userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        metadata={
            "sceneId": "1ww7426c4",
            "prefix": "dlw3kug",
        },
    )
    response = await cap_monster_client.solve_captcha(request_proxyless)
    print(f"Solution (proxyless): {response}")

    # Proxyless with extended metadata parameters
    request_extended = AlibabaCustomTaskRequest(
        websiteUrl="https://www.example.com",
        userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        metadata={
            "sceneId": "1ww7426c4",
            "prefix": "dlw3kug",
            "userId": "HpadJlQnz2zSKcSmjXBaqQvjYUvP4jMJIk/ZwGNDNiM=",
            "userUserId": "/uSXKkVFuuwxXA21/MpXGxpLStWBEup1B3jjlMUWwNE=",
            "verifyType": "1.0",
            "region": "sgp",
            "UserCertifyId": "0a03e59417757735511105780e2a5e",
            "apiGetLib": "https://o.example.com/captcha-frontend/aliyunCaptcha/AliyunCaptcha.js?t=2041",
        },
    )
    response = await cap_monster_client.solve_captcha(request_extended)
    print(f"Solution (extended metadata): {response}")

    # With proxy
    proxy = ProxyInfo(
        proxyType="http",
        proxyAddress="8.8.8.8",
        proxyPort=8080,
        proxyLogin="proxyLoginHere",
        proxyPassword="proxyPasswordHere",
    )
    request_with_proxy = AlibabaCustomTaskRequest(
        websiteUrl="https://www.example.com",
        userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        metadata={
            "sceneId": "1ww7426c4",
            "prefix": "dlw3kug",
        },
        proxy=proxy,
    )
    response = await cap_monster_client.solve_captcha(request_with_proxy)
    print(f"Solution (with proxy): {response}")


if __name__ == "__main__":
    asyncio.run(main())
