# CapMonster Cloud Python SDK

[![PyPI version](https://img.shields.io/pypi/v/capmonstercloudclient)](https://pypi.org/project/capmonstercloudclient/)

Official Python SDK for the CapMonster Cloud API.
Use this package when you want to create tasks and retrieve solutions from Python applications or scripts.

## Links

- Package: [capmonstercloudclient on PyPI](https://pypi.org/project/capmonstercloudclient/)
- Documentation: [docs.capmonster.cloud](https://docs.capmonster.cloud/)
- Dashboard / API key: [dash.capmonster.cloud](https://dash.capmonster.cloud/)

## Installation

```bash
python3 -m pip install capmonstercloudclient
```

Need to test before depositing? Contact support and we’ll add trial credits to your account.

## Minimal async example

```python
import asyncio

from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaV2Request

client_options = ClientOptions(api_key="<YOUR_API_KEY>")
cap_monster_client = CapMonsterClient(options=client_options)

recaptcha2request = RecaptchaV2Request(
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

- [AltchaCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/altcha-task)
- [AlibabaCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/alibaba-task)
- [AmazonWafRequest](https://docs.capmonster.cloud/docs/captchas/amazon-task)
- [BasiliskCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/Basilisk-task)
- [BinanceTaskRequest](https://docs.capmonster.cloud/docs/captchas/binance)
- [CastleCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/castle-task)
- [DataDomeCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/datadome)
- [FriendlyCaptchaRequest](https://docs.capmonster.cloud/docs/captchas/friendly-task)
- [FuncaptchaRequest](https://docs.capmonster.cloud/docs/captchas/funcaptcha-task)
- [FunCaptchaComplexImageTaskRequest](https://docs.capmonster.cloud/docs/captchas/ComplexImageTask-Recognition)
- [GeetestRequest](https://docs.capmonster.cloud/docs/captchas/geetest-task)
- [HuntCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/hunt-task)
- [ImageToTextRequest](https://docs.capmonster.cloud/docs/captchas/image-to-text)
- [ImpervaCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/incapsula)
- [MTCaptchaRequest](https://docs.capmonster.cloud/docs/captchas/mtcaptcha-task)
- [ProsopoTaskRequest](https://docs.capmonster.cloud/docs/captchas/prosopo-task)
- [RecognitionComplexImageTaskRequest](https://docs.capmonster.cloud/docs/captchas/ComplexImageTask-Recognition)
- [RecaptchaComplexImageTaskRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-click)
- [RecaptchaV2EnterpriseRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-v2-enterprise-task)
- [RecaptchaV2Request](https://docs.capmonster.cloud/docs/captchas/no-captcha-task)
- [RecaptchaV3EnterpriseRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-v3-enterprise-task)
- [RecaptchaV3ProxylessRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-v3-task)
- [TemuCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/temu-task)
- [TenDiCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/tendi)
- [TspdCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/tspd-task)
- [TurnstileRequest](https://docs.capmonster.cloud/docs/captchas/turnstile-task)
- [YidunRequest](https://docs.capmonster.cloud/docs/captchas/yidun-task)
