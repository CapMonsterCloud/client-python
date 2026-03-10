from typing import Dict, Union
from pydantic import Field, validator

from .CustomTaskRequestBase import CustomTaskRequestBase

class CastleCustomTaskRequest(CustomTaskRequestBase):
    captchaClass: str = Field(default='Castle')
    websiteKey: str = Field()
    metadata: Dict[str, Union[str, int]]

    @validator('metadata')
    def validate_metadata(cls, value):
        if value.get('wUrl') is None:
            raise TypeError(f'Expect that wUrl will be defined.')
        else:
            if not isinstance(value.get('wUrl'), str):
                raise TypeError(f'Expect that wUrl will be str.')
        if value.get('swUrl') is None:
            raise TypeError(f'Expect that swUrl will be defined.')
        else:
            if not isinstance(value.get('swUrl'), str):
                raise TypeError(f'Expect that swUrl will be str.')
        if value.get('count') is not None and not isinstance(value.get('count'), int):
            raise TypeError(f'Expect that count will be int.')
        return value

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
        task['websiteKey'] = self.websiteKey
        task['metadata'] = self.metadata
        if self.proxy:
            task['proxyType'] = self.proxy.proxyType
            task['proxyAddress'] = self.proxy.proxyAddress
            task['proxyPort'] = self.proxy.proxyPort
            task['proxyLogin'] = self.proxy.proxyLogin
            task['proxyPassword'] = self.proxy.proxyPassword
        if self.userAgent is not None:
            task['userAgent'] = self.userAgent
        return task
