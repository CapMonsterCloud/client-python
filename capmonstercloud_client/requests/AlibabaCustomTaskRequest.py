from typing import Dict, Union
from pydantic import Field, validator

from .CustomTaskRequestBase import CustomTaskRequestBase


class AlibabaCustomTaskRequest(CustomTaskRequestBase):
    captchaClass: str = Field(default='alibaba')
    metadata: Dict[str, str]

    @validator('metadata')
    def validate_metadata(cls, value):
        allowed_keys = {'sceneId', 'prefix', 'userId', 'userUserId', 'verifyType',
                        'region', 'UserCertifyId', 'apiGetLib'}
        unknown = set(value.keys()) - allowed_keys
        if unknown:
            raise TypeError(f'Unexpected metadata keys: {unknown}. Allowed: {allowed_keys}')
        for key in ['sceneId', 'prefix']:
            if value.get(key) is None:
                raise TypeError(f'Expect that {key} will be defined.')
            if not isinstance(value[key], str):
                raise TypeError(f'Expect that {key} will be str.')
        for key in ['userId', 'userUserId', 'verifyType', 'region', 'UserCertifyId', 'apiGetLib']:
            if key in value and not isinstance(value[key], str):
                raise TypeError(f'Expect that {key} will be str.')
        return value

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.type
        task['class'] = self.captchaClass
        task['websiteURL'] = self.websiteUrl
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
