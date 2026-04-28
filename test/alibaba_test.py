import unittest

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import AlibabaCustomTaskRequest, ProxyInfo


class AlibabaCustomTaskRequestTest(unittest.TestCase):
    websiteUrlExample = "https://www.example.com"
    userAgentExample = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    metadataExample = {
        "sceneId": "1ww7426c4",
        "prefix": "dlw3kug",
    }
    metadataExtendedExample = {
        "sceneId": "1ww7426c4",
        "prefix": "dlw3kug",
        "userId": "HpadJlQnz2zSKcSmjXBaqQvjYUvP4jMJIk/ZwGNDNiM=",
        "userUserId": "/uSXKkVFuuwxXA21/MpXGxpLStWBEup1B3jjlMUWwNE=",
        "verifyType": "1.0",
        "region": "sgp",
        "UserCertifyId": "0a03e59417757735511105780e2a5e",
        "apiGetLib": "https://o.example.com/captcha-frontend/aliyunCaptcha/AliyunCaptcha.js?t=2041",
    }

    def setUp(self):
        self.proxy = ProxyInfo(
            proxyType="http",
            proxyAddress="8.8.8.8",
            proxyPort=8080,
            proxyLogin="proxyLoginHere",
            proxyPassword="proxyPasswordHere",
        )

    def test_required_fields_proxyless(self):
        required_fields = ["type", "class", "websiteURL", "metadata"]
        request = AlibabaCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=self.metadataExample,
        )
        task_dict = request.getTaskDict()
        for f in required_fields:
            self.assertIn(f, task_dict, msg=f'Required field "{f}" missing from task dict.')
        self.assertEqual(task_dict["class"], "alibaba")
        self.assertEqual(task_dict["type"], "CustomTask")
        self.assertIn("sceneId", task_dict["metadata"])
        self.assertIn("prefix", task_dict["metadata"])

    def test_required_fields_with_proxy(self):
        proxy_fields = ["proxyType", "proxyAddress", "proxyPort", "proxyLogin", "proxyPassword"]
        request = AlibabaCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=self.metadataExample,
            proxy=self.proxy,
        )
        task_dict = request.getTaskDict()
        for f in proxy_fields:
            self.assertIn(f, task_dict, msg=f'Proxy field "{f}" missing from task dict.')

    def test_proxy_fields_not_sent_when_none(self):
        request = AlibabaCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=self.metadataExample,
        )
        task_dict = request.getTaskDict()
        self.assertNotIn("proxyType", task_dict)
        self.assertNotIn("proxyAddress", task_dict)

    def test_user_agent_included_when_provided(self):
        request = AlibabaCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=self.metadataExample,
            userAgent=self.userAgentExample,
        )
        task_dict = request.getTaskDict()
        self.assertEqual(task_dict["userAgent"], self.userAgentExample)

    def test_user_agent_not_sent_when_none(self):
        request = AlibabaCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=self.metadataExample,
        )
        task_dict = request.getTaskDict()
        self.assertNotIn("userAgent", task_dict)

    def test_metadata_missing_scene_id(self):
        self.assertRaises(
            TypeError,
            AlibabaCustomTaskRequest,
            websiteUrl=self.websiteUrlExample,
            metadata={"prefix": "dlw3kug"},
        )

    def test_metadata_missing_prefix(self):
        self.assertRaises(
            TypeError,
            AlibabaCustomTaskRequest,
            websiteUrl=self.websiteUrlExample,
            metadata={"sceneId": "1ww7426c4"},
        )

    def test_metadata_empty(self):
        self.assertRaises(
            TypeError,
            AlibabaCustomTaskRequest,
            websiteUrl=self.websiteUrlExample,
            metadata={},
        )

    def test_extended_metadata_fields(self):
        request = AlibabaCustomTaskRequest(
            websiteUrl=self.websiteUrlExample,
            metadata=self.metadataExtendedExample,
        )
        task_dict = request.getTaskDict()
        meta = task_dict["metadata"]
        for key in ["sceneId", "prefix", "userId", "userUserId", "verifyType",
                    "region", "UserCertifyId", "apiGetLib"]:
            self.assertIn(key, meta, msg=f'Extended metadata key "{key}" missing.')

    def test_metadata_unknown_key_rejected(self):
        self.assertRaises(
            TypeError,
            AlibabaCustomTaskRequest,
            websiteUrl=self.websiteUrlExample,
            metadata={"sceneId": "1ww7426c4", "prefix": "dlw3kug", "unknownField": "value"},
        )

    def test_metadata_optional_field_wrong_type(self):
        for key in ['userId', 'userUserId', 'verifyType', 'region', 'UserCertifyId', 'apiGetLib']:
            with self.assertRaises((TypeError, ValidationError), msg=f'{key} should reject non-str'):
                AlibabaCustomTaskRequest(
                    websiteUrl=self.websiteUrlExample,
                    metadata={"sceneId": "1ww7426c4", "prefix": "dlw3kug", key: 123},
                )

    def test_missing_required_constructor_fields(self):
        self.assertRaises(ValidationError, AlibabaCustomTaskRequest)
        self.assertRaises(
            ValidationError,
            AlibabaCustomTaskRequest,
            websiteUrl=self.websiteUrlExample,
        )


if __name__ == "__main__":
    unittest.main()
