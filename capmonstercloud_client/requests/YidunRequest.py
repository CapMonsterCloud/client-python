from typing import Dict, Optional, Union
from pydantic import Field
from .baseRequestWithProxy import BaseRequestWithProxy


class YidunRequest(BaseRequestWithProxy):
    type: str = Field(default="YidunTask")
    websiteUrl: str
    websiteKey: str
    userAgent: Optional[str] = Field(default=None)
    yidunGetLib: Optional[str] = Field(default=None)
    yidunApiServerSubdomain: Optional[str] = Field(default=None)
    challenge: Optional[str] = Field(default=None)
    hcg: Optional[str] = Field(default=None)
    hct: Optional[int] = Field(default=None)

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task["type"] = self.type
        task["websiteURL"] = self.websiteUrl
        task["websiteKey"] = self.websiteKey
        if self.userAgent is not None:
            task["userAgent"] = self.userAgent
        if self.yidunGetLib is not None:
            task["yidunGetLib"] = self.yidunGetLib
        if self.yidunApiServerSubdomain is not None:
            task["yidunApiServerSubdomain"] = self.yidunApiServerSubdomain
        if self.challenge is not None:
            task["challenge"] = self.challenge
        if self.hcg is not None:
            task["hcg"] = self.hcg
        if self.hct is not None:
            task["hct"] = self.hct
        if self.proxy:
            task["proxyType"] = self.proxy.proxyType
            task["proxyAddress"] = self.proxy.proxyAddress
            task["proxyPort"] = self.proxy.proxyPort
            task["proxyLogin"] = self.proxy.proxyLogin
            task["proxyPassword"] = self.proxy.proxyPassword

        return task
