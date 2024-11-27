class NameResolver:
    def __init__(self):
        self.records={
            "example.com": "33.423.243.24",
            "openai.com": "12.233.32.44",
            "google.com": "54.234.678.98"
        }
        self.cache ={}
    def resolve(self, hostname):
        if hostname in self.cache:
            return self.cache[hostname]
        ip_address= self.records.get(hostname)
        if ip_address:
            self.cache[hostname]= ip_address
            return ip_address
        else:
            return False  
resolver=NameResolver()
userinput=input("Enter the domain name:")
output=resolver.resolve(userinput)
if output:
    print("Mapped Ip for your domain",output)
else:
    print("No such domain mapping found")
