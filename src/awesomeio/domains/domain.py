DOMAIN = {}


def domain():

    def result(cls):
        assert "name" in cls.__dict__, "'name' field is required!"
        assert "domain" in cls.__dict__, "'domain' field is required!"
        DOMAIN[cls.name] = cls.domain
        return cls

    return result
