# CapMonster Cloud Python client

[![PyPI version](https://img.shields.io/pypi/v/capmonstercloudclient)](https://pypi.org/project/capmonstercloudclient/)

Official Python client for creating CAPTCHA tasks and receiving solutions from the CapMonster Cloud API.

## Links

- Package: [capmonstercloudclient on PyPI](https://pypi.org/project/capmonstercloudclient/)
- Documentation: [docs.capmonster.cloud](https://docs.capmonster.cloud/)
- Dashboard / API key: [dash.capmonster.cloud](https://dash.capmonster.cloud/)

Need to test before depositing? Contact support and we’ll add trial credits to your account.

## Installation

```bash
python3 -m pip install capmonstercloudclient
```

## Minimal example

```python
import asyncio

from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaV2ProxylessRequest

client_options = ClientOptions(api_key="<YOUR_API_KEY>")
cap_monster_client = CapMonsterClient(options=client_options)

recaptcha2request = RecaptchaV2ProxylessRequest(
    websiteUrl="https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high",
    websiteKey="6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd",
)

async def solve_captcha():
    return await cap_monster_client.solve_captcha(recaptcha2request)

response = asyncio.run(solve_captcha())
print(response)
```

Supported task families include reCAPTCHA, GeeTest, Turnstile, image-to-text, and additional task types documented in the public docs.

Supported request classes:

- [GeeTestProxylessRequest](https://zenno.link/doc-geetest-en)
- [GeeTestRequest](https://zenno.link/doc-geetest-proxy-en)
- [ImageToTextRequest](https://zenno.link/doc-ImageToTextTask-en)
- [RecaptchaV2ProxylessRequest](https://zenno.link/doc-recaptcha2-en)
- [RecaptchaV2Request](https://zenno.link/doc-recaptcha2-proxy-en)
- [RecaptchaV3ProxylessRequest](https://zenno.link/doc-recaptcha3-en)
- [RecaptchaV2EnterpriseProxylessRequest](https://zenno.link/doc-recaptcha2e-en)
- [RecaptchaV2EnterpriseRequest](https://zenno.link/doc-recaptcha2e-proxy-en)
- [TurnstileProxylessRequest](https://zenno.link/doc-turnstile-en)
- [TurnstileRequest](https://zenno.link/doc-turnstile-proxy-en)
- [RecaptchaComplexImageTaskRequest](https://zenno.link/doc-complextask-rc-en)
- [DataDomeCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/datadome)
- [TenDiCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/tendi)
- [BasiliskCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/Basilisk-task)
- [AmazonWafRequest](https://docs.capmonster.cloud/docs/captchas/amazon-task)
- [BinanceTaskRequest](https://docs.capmonster.cloud/docs/captchas/binance)
- [BinanceTaskProxylessRequest](https://docs.capmonster.cloud/docs/captchas/binance)
- [ImpervaCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/incapsula)
- [ImpervaCustomTaskProxylessRequest](https://docs.capmonster.cloud/docs/captchas/incapsula)
