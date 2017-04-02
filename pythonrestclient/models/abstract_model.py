from collection_class import CollectionClass
from pythonrestclient.service_factory import ServiceFactory


class AbstractModel:
    def __init__(self, attributes = None):
        self.attributes = attributes

    def attributes(self):
        return self.attributes

    @classmethod
    def all(cls):
        response = ServiceFactory.api_client.get_resources(cls.resources_name())
        items = list(map(lambda attributes: cls(attributes), response))
        return CollectionClass(items)

    @classmethod
    def get(cls, resource_id):
        response = ServiceFactory.api_client.get(cls.resources_name(), resource_id)
        return cls(response)

    @classmethod
    def create(cls, attributes):
        cls._validate_presence_of_required_attributes(attributes)
        response = ServiceFactory.api_client.post(cls.resources_name(), attributes)
        if response['id']:
            merged_attributes = cls.merge_two_dicts(response, attributes)
            return cls(merged_attributes)
        else:
            return None

    # TODO: create two methods static and for instance
    def update(self, resource_id, attributes):
        response = ServiceFactory.api_client.put(self.resources_name(), resource_id, attributes)
        return response['id'] == resource_id

    def delete(self):
        # TODO: check ID
        return self.__class__.delete_by_id(self.attributes['id'])

    @classmethod
    def delete_by_id(cls, resource_id):
        response = ServiceFactory.api_client.delete(cls.resources_name(), resource_id)
        return response == {}

    @classmethod
    def resources_name(cls):
        raise NotImplementedError("AbstractModel does not have _resources_name!")

    @classmethod
    def _validate_presence_of_required_attributes(cls, attributes):
        # TODO: implement _validate_presence_of_required_params
        pass

    @staticmethod
    def merge_two_dicts(x, y):
        z = x.copy()
        z.update(y)
        return z
