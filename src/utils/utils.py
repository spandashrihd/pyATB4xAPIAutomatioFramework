
class Utils():
    def common_headers_json(self):
        headers={
            "Content_Type" : "application/json"
        }
        return headers
    
    def common_headers_xml(self):
        headers={
            "Content_Type" : "application/xml"
        }
        return headers

    def common_headers_put_patch_delete_basic_auth(self, basic_auth_value):
        headers={
            "Content_Type" : "application/json",
            "Authorization" : "Basic"+ str(basic_auth_value)
        }
        return headers

    def common_headers_put_patch_delete_cookie(self, token):
        headers={
            "Content_Type" : "application/json",
            "cookie" : "token=" + str(token)
        }
        return headers

    #in future we can add below utility also
    def read_csv(self):
        pass

    def read_envfile(self):
        pass

    def read_database(self):
        pass
