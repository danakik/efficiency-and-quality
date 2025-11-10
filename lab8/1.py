from abc import ABC, abstractmethod


class UpdateEntityTemplate(ABC):

    def update(self, entity_data: dict) -> dict:
        entity = self.get_entity(entity_data["id"])
        if not self.validate(entity_data):
            self.on_validation_failed(entity_data) 
            return {"status": "error", "code": 400}

        request_payload = self.build_save_request(entity_data)
        self.send_to_api(request_payload)
        return self.build_response(entity)            


    @abstractmethod
    def get_entity(self, entity_id: int) -> dict:
        pass

    @abstractmethod
    def validate(self, entity_data: dict) -> bool:
        pass

    @abstractmethod
    def build_save_request(self, entity_data: dict) -> dict:
        pass

    @abstractmethod
    def send_to_api(self, payload: dict):
        pass

    def on_validation_failed(self, entity_data: dict):
        pass

    def build_response(self, entity: dict) -> dict:
        return {"status": "ok", "code": 200}


class ProductUpdater(UpdateEntityTemplate):

    def get_entity(self, entity_id: int) -> dict:
        return {"id": entity_id, "name": "Vodka Premium"}

    def validate(self, entity_data: dict) -> bool:
        return entity_data.get("price", 0) > 0

    def build_save_request(self, entity_data: dict) -> dict:
        return {"action": "update_product", "payload": entity_data}

    def send_to_api(self, payload: dict):
        print("API: product saved")

    def on_validation_failed(self, entity_data: dict):
        print("!!! send message to admin messenger - PRODUCT VALIDATION FAIL !!!")

class UserUpdater(UpdateEntityTemplate):

    def get_entity(self, entity_id: int) -> dict:
        return {"id": entity_id, "email": "test@site.com"}

    def validate(self, entity_data: dict) -> bool:
        if "email" in entity_data:
            return False
        return True

    def build_save_request(self, entity_data: dict) -> dict:
        return {"action": "update_user", "payload": entity_data}

    def send_to_api(self, payload: dict):
        print("API: user saved")


class OrderUpdater(UpdateEntityTemplate):

    def get_entity(self, entity_id: int) -> dict:
        return {"id": entity_id, "status": "processing", "sum": 99.9}

    def validate(self, entity_data: dict) -> bool:
        return True

    def build_save_request(self, entity_data: dict) -> dict:
        return {"action": "update_order", "payload": entity_data}

    def send_to_api(self, payload: dict):
        print("API: order saved")

    def build_response(self, entity: dict) -> dict:
        return {"status": "ok", "code": 200, "order": entity}


if __name__ == "__main__":

    product_updater = ProductUpdater()
    print(product_updater.update({"id": 1, "price": -10}))

    user_updater = UserUpdater()
    print(user_updater.update({"id": 22, "email": "qwerty@gmail.com"}))

    order_updater = OrderUpdater()
    print(order_updater.update({"id": 55, "status": "delivered"}))
