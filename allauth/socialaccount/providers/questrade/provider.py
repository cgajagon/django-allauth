from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class QuestradeAccount(ProviderAccount):
    def to_str(self):
        dflt = super(QuestradeAccount, self).to_str()
        return self.account.extra_data.get('name', dflt)

class QuestradeProvider(OAuth2Provider):
    id = 'questrade'
    name = 'Questrade'
    account_class = QuestradeAccount

    def get_default_scope(self):
        return ['profile']

    def extract_uid(self, data):
        """Extract uid ('id') and ensure it's a str."""
        return str(data['accounts']['number'])


provider_classes = [QuestradeProvider]
