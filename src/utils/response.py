

class Response():
    
    def default_response_message(self, data, metadata, message_id, error):
        return {
            "data":data, "metadata": metadata, "message_id": message_id, "error": error
        }
    
    def response(self, status_code, data={}, metadata={}, message_id="", error=False, exception="", traceback=""):
        response = self.default_response_message(data, metadata, message_id, error)
        
        print('resposta', response)
        
        if status_code >= 400:
            print(traceback)
            
        try:
            print(exception)
        except Exception as e:
            print("Tracker logger: ", e)
            
        response["traceback"] = traceback
        
        return response, status_code