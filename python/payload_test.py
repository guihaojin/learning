class BasicConfig(object):
    def payload(self):
        raise NotImplementedError

class CoolConfig(BasicConfig):
    def payload(self):
        return {"cool": 1}

config = CoolConfig()

def config_payload(config: BasicConfig):
    return {
        "id": "config_payload",
        **config.payload()
    }

print(config_payload(config))
