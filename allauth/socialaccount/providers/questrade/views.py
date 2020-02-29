import requests

from allauth.socialaccount import app_settings
from allauth.socialaccount.providers.questrade.provider import QuestradeProvider
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

class QuestradeOAuth2Adapter(OAuth2Adapter):
    provider_id = QuestradeProvider.id
    access_token_url = "https://login.questrade.com/oauth2/token"
    authorize_url = "https://login.questrade.com/oauth2/authorize"

    def parse_token(self, data):
        token = super(QuestradeOAuth2Adapter, self).parse_token(data)
        token.api_url = data.get('api_url', '')
        return token

    def complete_login(self, request, app, token, **kwargs):

        headers = {
            'access_token': token.token,
            'token_type': "Bearer",
            }

        #headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(token.api_url, headers=headers)
        resp.raise_for_status()
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(
            request, extra_data
        )


oauth2_login = OAuth2LoginView.adapter_view(QuestradeOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(QuestradeOAuth2Adapter)
