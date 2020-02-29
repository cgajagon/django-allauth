from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse, TestCase

from .provider import QuestradeProvider


class QuestradeTests(OAuth2TestsMixin, TestCase):
    provider_id = QuestradeProvider.id

    def get_mocked_response(self):
        return MockedResponse(200, """
        {
            "accounts":
                {
                    "type": "Margin",
                    "number": "26598145",
                    "status": "Active",
                    "isPrimary": true,
                    "isBilling": true,
                    "clientAccountType": "Individual"
                }
        }
        """)
