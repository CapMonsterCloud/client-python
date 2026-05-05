✅ CapMonster.Cloud — Fast, Reliable CAPTCHA Solving for Automation & Scraping

[![CapMonster Cloud](https://help.zennolab.com/upload/u/e4/e4bc15839b25.png)](https://capmonster.cloud/en/?utm_source=github&utm_campaign=cmcrep)

# CapMonster Cloud Python SDK

[![PyPI version](https://img.shields.io/pypi/v/capmonstercloudclient)](https://pypi.org/project/capmonstercloudclient/)

Official Python SDK for the CapMonster Cloud API.
Use this package when you want to create tasks and retrieve solutions from Python applications or scripts.

## Links

- Package: [capmonstercloudclient on PyPI](https://pypi.org/project/capmonstercloudclient/)
- Documentation: [docs.capmonster.cloud](https://docs.capmonster.cloud/?utm_source=github&utm_campaign=cmcrep)
- Dashboard / API key: [dash.capmonster.cloud](https://dash.capmonster.cloud/?utm_source=github&utm_campaign=cmcrep)

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

- [AltchaCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/altcha-task?utm_source=github&utm_campaign=cmcrep)
- [AlibabaCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/alibaba-task?utm_source=github&utm_campaign=cmcrep)
- [AmazonWafRequest](https://docs.capmonster.cloud/docs/captchas/amazon-task?utm_source=github&utm_campaign=cmcrep)
- [BasiliskCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/Basilisk-task?utm_source=github&utm_campaign=cmcrep)
- [BinanceTaskRequest](https://docs.capmonster.cloud/docs/captchas/binance?utm_source=github&utm_campaign=cmcrep)
- [CastleCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/castle-task?utm_source=github&utm_campaign=cmcrep)
- [DataDomeCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/datadome?utm_source=github&utm_campaign=cmcrep)
- [FriendlyCaptchaRequest](https://docs.capmonster.cloud/docs/captchas/friendly-task?utm_source=github&utm_campaign=cmcrep)
- [FuncaptchaRequest](https://docs.capmonster.cloud/docs/captchas/funcaptcha-task?utm_source=github&utm_campaign=cmcrep)
- [FunCaptchaComplexImageTaskRequest](https://docs.capmonster.cloud/docs/captchas/ComplexImageTask-Recognition?utm_source=github&utm_campaign=cmcrep)
- [GeetestRequest](https://docs.capmonster.cloud/docs/captchas/geetest-task?utm_source=github&utm_campaign=cmcrep)
- [HuntCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/hunt-task?utm_source=github&utm_campaign=cmcrep)
- [ImageToTextRequest](https://docs.capmonster.cloud/docs/captchas/image-to-text?utm_source=github&utm_campaign=cmcrep)
- [ImpervaCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/incapsula?utm_source=github&utm_campaign=cmcrep)
- [MTCaptchaRequest](https://docs.capmonster.cloud/docs/captchas/mtcaptcha-task?utm_source=github&utm_campaign=cmcrep)
- [ProsopoTaskRequest](https://docs.capmonster.cloud/docs/captchas/prosopo-task?utm_source=github&utm_campaign=cmcrep)
- [RecognitionComplexImageTaskRequest](https://docs.capmonster.cloud/docs/captchas/ComplexImageTask-Recognition?utm_source=github&utm_campaign=cmcrep)
- [RecaptchaComplexImageTaskRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-click?utm_source=github&utm_campaign=cmcrep)
- [RecaptchaV2EnterpriseRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-v2-enterprise-task?utm_source=github&utm_campaign=cmcrep)
- [RecaptchaV2Request](https://docs.capmonster.cloud/docs/captchas/no-captcha-task?utm_source=github&utm_campaign=cmcrep)
- [RecaptchaV3EnterpriseRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-v3-enterprise-task?utm_source=github&utm_campaign=cmcrep)
- [RecaptchaV3ProxylessRequest](https://docs.capmonster.cloud/docs/captchas/recaptcha-v3-task?utm_source=github&utm_campaign=cmcrep)
- [TemuCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/temu-task?utm_source=github&utm_campaign=cmcrep)
- [TenDiCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/tendi?utm_source=github&utm_campaign=cmcrep)
- [TspdCustomTaskRequest](https://docs.capmonster.cloud/docs/captchas/tspd-task?utm_source=github&utm_campaign=cmcrep)
- [TurnstileRequest](https://docs.capmonster.cloud/docs/captchas/turnstile-task?utm_source=github&utm_campaign=cmcrep)
- [YidunRequest](https://docs.capmonster.cloud/docs/captchas/yidun-task?utm_source=github&utm_campaign=cmcrep)


:star:️ If you find this project useful, please give it a star on GitHub!
