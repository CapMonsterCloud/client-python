import unittest

from pydantic.error_wrappers import ValidationError
from capmonstercloudclient.requests import FriendlyCaptchaRequest, ProxyInfo


class FriendlyCaptchaRequestTest(unittest.TestCase):
    websiteUrlExample = "https://example.com"
    websiteKeyExample = "FFMGEMAD2K3JJ35P"
    userAgentExample = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    metadataV1Example = {
        "apiGetLib": "https://cdn.jsdelivr.net/npm/friendly-challenge@0.9.19/widget.module.min.js"
    }
    metadataV2Example = {
        "apiGetLib": "https://example.com/wp-content/plugins/friendly-captcha/public/vendor/v2/site.min.js"
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
        required_fields = ["type", "class", "websiteURL", "websiteKey", "metadata"]
        request = FriendlyCaptchaRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            metadata=self.metadataV1Example,
        )
        task_dict = request.getTaskDict()
        for f in required_fields:
            self.assertIn(f, task_dict, msg=f'Required field "{f}" missing from task dict.')
        self.assertEqual(task_dict["class"], "friendly")
        self.assertEqual(task_dict["type"], "CustomTask")
        self.assertIn("apiGetLib", task_dict["metadata"])

    def test_required_fields_with_proxy(self):
        proxy_fields = ["proxyType", "proxyAddress", "proxyPort", "proxyLogin", "proxyPassword"]
        request = FriendlyCaptchaRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            metadata=self.metadataV1Example,
            proxy=self.proxy,
        )
        task_dict = request.getTaskDict()
        for f in proxy_fields:
            self.assertIn(f, task_dict, msg=f'Proxy field "{f}" missing from task dict.')

    def test_proxy_fields_not_sent_when_none(self):
        request = FriendlyCaptchaRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            metadata=self.metadataV1Example,
        )
        task_dict = request.getTaskDict()
        self.assertNotIn("proxyType", task_dict)
        self.assertNotIn("proxyAddress", task_dict)

    def test_user_agent_included_when_provided(self):
        request = FriendlyCaptchaRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            metadata=self.metadataV1Example,
            userAgent=self.userAgentExample,
        )
        task_dict = request.getTaskDict()
        self.assertEqual(task_dict["userAgent"], self.userAgentExample)

    def test_user_agent_not_sent_when_none(self):
        request = FriendlyCaptchaRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            metadata=self.metadataV1Example,
        )
        task_dict = request.getTaskDict()
        self.assertNotIn("userAgent", task_dict)

    def test_metadata_missing_api_get_lib(self):
        self.assertRaises(
            TypeError,
            FriendlyCaptchaRequest,
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            metadata={},
        )

    def test_metadata_api_get_lib_must_be_str(self):
        with self.assertRaises((TypeError, ValidationError)):
            FriendlyCaptchaRequest(
                websiteUrl=self.websiteUrlExample,
                websiteKey=self.websiteKeyExample,
                metadata={"apiGetLib": 123},
            )

    def test_missing_required_constructor_fields(self):
        self.assertRaises(ValidationError, FriendlyCaptchaRequest)
        self.assertRaises(
            ValidationError,
            FriendlyCaptchaRequest,
            websiteUrl=self.websiteUrlExample,
        )
        self.assertRaises(
            ValidationError,
            FriendlyCaptchaRequest,
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
        )

    def test_v2_metadata(self):
        request = FriendlyCaptchaRequest(
            websiteUrl=self.websiteUrlExample,
            websiteKey=self.websiteKeyExample,
            metadata=self.metadataV2Example,
        )
        task_dict = request.getTaskDict()
        self.assertEqual(task_dict["metadata"]["apiGetLib"], self.metadataV2Example["apiGetLib"])


if __name__ == "__main__":
    unittest.main()
