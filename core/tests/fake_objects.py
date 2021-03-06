
CONFIG_SERVER = {
    'server_name': 'test.server.com',
    'base_api_url': 'https://test.server.com/ces/api',
    'oauth2_token_url': 'https://test.server.com/oauth2/token',
    'oauth2_client_id': 'test-client-id',
    'oauth2_client_password': 'test-client-password',
    'oauth2_scope': 'test-scope test-scope2',
}

SERVER_OAUTH2_RESPONSE = {
    'access_token': 'ba6a3dfa96c6f5862cc944f36e55f3e9d9a767e1',
    'expires_in': 3600, 'token_type': 'Bearer',
    'scope': 'test-scope test-scope2',
    'refresh_token': '7da4b334f3484c245206ea9ccd528548e405423c',
}


class FakeApiAccess:
    def __init__(self, config):
        self.server = config["server"]
        self.has_access = True
        self.headers = {
            'Content-Type': 'application/vnd.api+json',
            'Authorization': 'Bearer ba6a3dfa96c6f5862cc944f36e55f3e9d9a767e1'
        }
        self.user = "user@test.server.com"
        self._auth = SERVER_OAUTH2_RESPONSE


ME_RESPONSE = {'data': {'type': 'users', 'id':
'75736572-2020-4525-a671-000000000006', 'relationships': {'members': {'data':
[{'type': 'members', 'id': '6d656d62-6572-4525-a671-000000000002'}, {'type':
'members', 'id': '6d656d62-6572-4525-a671-000000000008'}]}}, 'links': {'self':
'https://demo.integralces.net/ces/api/social/users/75736572-2020-4525-a671-000000000006'}},
'included': [{'type': 'members', 'id': '6d656d62-6572-4525-a671-000000000002',
'attributes': {'code': 'NET20000', 'name': 'Fermat', 'access': 'group', 'type':
'personal', 'description': '', 'image':
'https://demo.integralces.net/sites/default/files/Fermat.jpg', 'address':
'12345, Somewhere', 'location': {'name': 'Somewhere', 'type': 'Point',
'coordinates': [0, 0]}, 'created': '2021-02-08T18:54:59+00:00', 'updated':
'2021-02-08T18:54:59+00:00'}, 'relationships': {'group': {'data': {'type':
'groups', 'id': '67726f75-7020-4525-a671-000000000002'}}, 'account': {'links':
{'related':
'https://demo.integralces.net/ces/api/accounting/NET2/accounts/NET20000'},
'data': {'type': 'accounts', 'id': 'a383a9dc-7ad4-4868-8807-069675c6ad3e',
'meta': {'external': True}}}, 'contacts': {'data': [{'type': 'contacts', 'id':
'656d6169-6c20-4525-a671-000000000006'}, {'type': 'contacts', 'id':
'70686f6e-6520-4525-a671-000000000006'}]}, 'needs': {'links': {'related':
'https://demo.integralces.net/ces/api/social/NET2/needs?filter[member]=6d656d62-6572-4525-a671-000000000002'},
'meta': {'count': '0'}}, 'offers': {'links': {'related':
'https://demo.integralces.net/ces/api/social/NET2/offers?filter[member]=6d656d62-6572-4525-a671-000000000002'},
'meta': {'count': '1'}}}, 'links': {'self':
'https://demo.integralces.net/ces/api/social/NET2/members/NET20000'}}, {'type':
'groups', 'id': '67726f75-7020-4525-a671-000000000002', 'attributes': {'code':
'NET2', 'name': 'Network 2 - Euro based', 'description': '', 'image': None,
'website': 'http://www.integralces.net', 'access': 'public', 'location':
{'name': 'Barcelona', 'type': 'Point', 'coordinates': [0, 0]}, 'created':
'2021-02-08T18:54:59+00:00', 'updated': '2021-02-08T18:54:59+00:00'},
'relationships': {'currency': {'links': {'related':
'https://demo.integralces.net/ces/api/accounting/NET2/currency'}, 'data':
{'type': 'currencies', 'id': '66130728-b248-4c8e-8d5e-b8643a68e24e', 'meta':
{'external': True}}}, 'contacts': {'data': [{'type': 'contacts', 'id':
'656d6169-6c20-4525-a671-000000000006'}]}, 'members': {'links': {'related':
'https://demo.integralces.net/ces/api/social/NET2/members'}, 'meta': {'count':
'4'}}, 'categories': {'data': [{'type': 'categories', 'id':
'63617465-676f-4525-a671-00000000000c'}, {'type': 'categories', 'id':
'63617465-676f-4525-a671-000000000008'}, {'type': 'categories', 'id':
'63617465-676f-4525-a671-000000000002'}, {'type': 'categories', 'id':
'63617465-676f-4525-a671-000000000009'}, {'type': 'categories', 'id':
'63617465-676f-4525-a671-00000000000a'}, {'type': 'categories', 'id':
'63617465-676f-4525-a671-00000000000b'}], 'meta': {'count': 6}}, 'offers':
{'links': {'related':
'https://demo.integralces.net/ces/api/social/NET2/offers'}, 'meta': {'count':
'3'}}, 'needs': {'links': {'related':
'https://demo.integralces.net/ces/api/social/NET2/needs'}, 'meta': {'count':
'0'}}}, 'links': {'self': 'https://demo.integralces.net/ces/api/social/NET2'}},
{'type': 'accounts', 'id': 'a383a9dc-7ad4-4868-8807-069675c6ad3e', 'links':
{'self':
'https://demo.integralces.net/ces/api/accounting/NET2/accounts/NET20000'},
'meta': {'external': True}}, {'type': 'members', 'id':
'6d656d62-6572-4525-a671-000000000008', 'attributes': {'code': 'NET20003',
'name': 'Fermat', 'access': 'group', 'type': 'personal', 'description': '',
'image': 'https://demo.integralces.net/sites/default/files/Fermat.jpg',
'address': '12345, Somewhere', 'location': {'name': 'Somewhere', 'type':
'Point', 'coordinates': [0, 0]}, 'created': '2021-02-08T18:54:59+00:00',
'updated': '2021-02-08T18:54:59+00:00'}, 'relationships': {'group': {'data':
{'type': 'groups', 'id': '67726f75-7020-4525-a671-000000000002'}}, 'account':
{'links': {'related':
'https://demo.integralces.net/ces/api/accounting/NET2/accounts/NET20003'},
'data': {'type': 'accounts', 'id': 'f12b9b04-13a7-4558-9b6f-ee36f8f8e6b3',
'meta': {'external': True}}}, 'contacts': {'data': [{'type': 'contacts', 'id':
'656d6169-6c20-4525-a671-000000000006'}, {'type': 'contacts', 'id':
'70686f6e-6520-4525-a671-000000000006'}]}, 'needs': {'links': {'related':
'https://demo.integralces.net/ces/api/social/NET2/needs?filter[member]=6d656d62-6572-4525-a671-000000000008'},
'meta': {'count': 0}}, 'offers': {'links': {'related':
'https://demo.integralces.net/ces/api/social/NET2/offers?filter[member]=6d656d62-6572-4525-a671-000000000008'},
'meta': {'count': 0}}}, 'links': {'self':
'https://demo.integralces.net/ces/api/social/NET2/members/NET20003'}}, {'type':
'accounts', 'id': 'f12b9b04-13a7-4558-9b6f-ee36f8f8e6b3', 'links': {'self':
'https://demo.integralces.net/ces/api/accounting/NET2/accounts/NET20003'},
'meta': {'external': True}}]}
BALANCE_RESPONSE = {'data': {'type': 'accounts', 'id':
'a383a9dc-7ad4-4868-8807-069675c6ad3e', 'attributes': {'code': 'NET20000',
'balance': 130, 'creditLimit': -1, 'debitLimit': -1}, 'relationships':
{'currency': {'data': {'type': 'currencies', 'id':
'66130728-b248-4c8e-8d5e-b8643a68e24e'}}}, 'links': {'self':
'https://demo.integralces.net/ces/api/accountingNET2//accounts/NET20000'}},
'included': [{'type': 'currencies', 'id':
'66130728-b248-4c8e-8d5e-b8643a68e24e', 'attributes': {'codeType': 'CEN',
'code': 'NET2', 'name': 'eco', 'namePlural': 'ecos', 'symbol': 'ECO',
'decimals': '2', 'scale': '2', 'value': 100000}, 'links': {'self':
'https://demo.integralces.net/ces/api/accountingNET2/currency'}}]}
STATEMENT_RESPONSE = {'links': {'next': None}, 'data': [{'type': 'transfers',
'id': 'e2f52ef0-6deb-471a-aeb3-ea10a1b187e2', 'attributes': {'amount': 130,
'meta': 'campana de gauss', 'state': 'committed', 'created':
'2021-02-09T17:57:17+00:00', 'updated': '2021-02-09T17:57:17+00:00'},
'relationships': {'payer': {'data': {'type': 'accounts', 'id':
'0c1d2b8c-cef9-4120-8675-e19d1a14c636'}}, 'payee': {'data': {'type':
'accounts', 'id': 'a383a9dc-7ad4-4868-8807-069675c6ad3e'}}, 'currency':
{'data': {'type': 'currencies', 'id':
'66130728-b248-4c8e-8d5e-b8643a68e24e'}}}, 'links': {'self':
'https://demo.integralces.net/ces/api/accountingNET2//transfers/e2f52ef0-6deb-471a-aeb3-ea10a1b187e2'}}]}
