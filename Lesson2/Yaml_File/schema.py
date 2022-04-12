SCHEMA =     {
        "name": "",
        "description": "",
        "version": "",
        "author": "",
        "license": "",
        "posts":  [
        {
            "title": "",
            "date": "",
            "content": ""
        }
        ]
    }

class SchemaFile:

    def __init__(self, value=SCHEMA):
        self.value = value


    def set_values(self, values):
        
        with open("test-this.json", "w") as file_name:
            file_name.write(json.dumps(input_values))