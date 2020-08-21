init python:

    import json
    import os.path
    import base64
    import os

    class base_class(renpy.python.RevertableObject):

        def __getstate__(self):
            return vars(self).copy()
        
        def __setstate__(self,new_dict):
            self.__dict__.update(new_dict)

    class player(base_class):
        ''' Player Class where we can init the player
        '''

        DEFAULT_DATA =  {"player_data":{"player_name":"Umiko","player_status":"NEW"}}

        JSONDATA = "{}/data.json".format(config.gamedir)

        def __init__(self):
            """ Init of the Player

            The following attributes will be instantiated:
            iventory
            
            """
            self.do_login = True
            self.load_data()
            self.player_name = self.local_data["player_data"]["player_name"]            
            self.inventory = inventory()
            self.health = 100
            self.actionPoints = 100

        def load_data(self):
            if os.path.exists(self.JSONDATA):
                with open(self.JSONDATA) as json_file:
                    self.local_data = json.load(json_file)
            else:
                self.save_data(self.DEFAULT_DATA)
                self.load_data()
        
        def save_data(self,input):
            with open(self.JSONDATA, "w") as outfile:
                json.dump(input, outfile)

        #def do_request(self, r_url, r_params, r_json):
            #return requests.post(r_url, params=r_params, json=r_json)

        def validate(self,passcode):
            validate_url = "{}/bunny/auth.php".format(BASE_URL)
            validate_input = {'action': 'validate'}
            validate_json= {'passcode': passcode}
            self.response = self.do_request(validate_url, validate_input, validate_json)
            validate_data = self.response.json()             
            if (validate_data["status"]=="OK"):
                self.save_data(validate_data["player_data"])
                self.load_data()
                self.do_login = False
                return True
            else:
                self.do_login = True
                return False


    class inventory(base_class):
        ''' Iventory Class where inventory is defined
        '''

        def __init__(self):
            ''' Init Iventory
                set items attribute
            '''
            self.items = []

        def addItem(self, item):
            ''' Add one item to the list
            '''
            self.items.append(item)

        def useItem(self, item):
            ''' Pop one item from the list
            
            Return the item that it's pop
            Return False if there is no item in the list
            '''
            if item in self.items:
                self.items.remove(item)
                return True
            else:
                return False

        def checkItems(self, item):
            ''' Pop one item from the list
            
            Return the item that it's pop
            Return False if there is no item in the list
            '''
            if item in self.items:            
                return True
            else:
                return False

        def listItems(self):
            ''' 
            Return All item from list
            '''
            return self.items

    class game_data(base_class):
        ''' Handle Game data
        '''

        def __init__(self):
            ''' Init Game data
            '''
            self.save_name = "gdata.save"
            self.content = None

        def enc_data(self,inputData):
            return base64.b64encode(inputData)
        
        def dec_data(self,inputData):
            return base64.b64decode(inputData)

        def load_data(self):
            with open("{}/{}".format(config.gamedir,self.save_name), 'rb') as f:
                fileData = f.read()
            self.content = json.loads(self.dec_data(fileData).decode("utf-8"))
        
        def save_data(self):
            with open(self.save_name, 'wb') as f:
                f.write(self.enc_data(self.content))     
        