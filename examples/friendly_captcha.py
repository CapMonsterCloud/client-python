import os
import asyncio

from capmonstercloudclient.requests import FriendlyCaptchaRequest, ProxyInfo
from capmonstercloudclient import ClientOptions, CapMonsterClient


async def main():
    client_options = ClientOptions(api_key=os.getenv('API_KEY'))
    cap_monster_client = CapMonsterClient(options=client_options)

    # Proxyless example (V1)
    request_proxyless = FriendlyCaptchaRequest(
        websiteUrl="https://example.com",
        websiteKey="FFMGEMAD2K3JJ35P",
        userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        metadata={
            "apiGetLib": "https://cdn.jsdelivr.net/npm/friendly-challenge@0.9.19/widget.module.min.js"
        },
    )
    response = await cap_monster_client.solve_captcha(request_proxyless)
    print(f"Solution (proxyless V1): {response}")

    # With proxy example (V2)
    proxy = ProxyInfo(
        proxyType="http",
        proxyAddress="8.8.8.8",
        proxyPort=8080,
        proxyLogin="proxyLoginHere",
        proxyPassword="proxyPasswordHere",
    )
    request_with_proxy = FriendlyCaptchaRequest(
        websiteUrl="https://example.com",
        websiteKey="FFMGEMAD2K3JJ35P",
        userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        metadata={
            "apiGetLib": "https://example.com/wp-content/plugins/friendly-captcha/public/vendor/v2/site.min.js"
        },
        proxy=proxy,
    )
    response = await cap_monster_client.solve_captcha(request_with_proxy)
    print(f"Solution (with proxy V2): {response}")


if __name__ == "__main__":
    asyncio.run(main())
