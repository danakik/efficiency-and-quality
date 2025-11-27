from typing import List

class FormMediator:
    def __init__(self):
        self.elements = []

    def register(self, element):
        self.elements.append(element)
        element.mediator = self

    def notify(self, sender, event):
        if isinstance(sender, DateSelector):
            sender.update_available_times()
        elif isinstance(sender, OtherRecipientCheckbox):
            for e in self.elements:
                if isinstance(e, (NameField, PhoneField)):
                    e.active = sender.checked
                    print(f"{e.name} active: {e.active}")
        elif isinstance(sender, SelfPickupCheckbox):
            for e in self.elements:
                if isinstance(e, (DateSelector, TimeSelector, OtherRecipientCheckbox, NameField, PhoneField)):
                    e.active = not sender.checked
                    print(f"{e.name} active: {e.active}")

class FormElement:
    def __init__(self, name):
        self.name = name
        self.mediator: FormMediator = None
        self.active = True

class DateSelector(FormElement):
    def __init__(self, name="Delivery Date"):
        super().__init__(name)
        self.date = None
        self.available_times = []

    def select_date(self, date):
        if not self.active:
            print(f"{self.name} is inactive")
            return
        self.date = date
        print(f"Selected date: {self.date}")
        self.mediator.notify(self, "date_changed")

    def update_available_times(self):
        if self.date == "2025-11-28":
            self.available_times = ["10:00-12:00", "12:00-14:00"]
        else:
            self.available_times = ["14:00-16:00", "16:00-18:00"]
        print(f"Available time slots for {self.date}: {self.available_times}")

class TimeSelector(FormElement):
    def __init__(self, name="Delivery Time"):
        super().__init__(name)
        self.time = None

    def select_time(self, time):
        if not self.active:
            print(f"{self.name} is inactive")
            return
        self.time = time
        print(f"Selected time: {self.time}")

class OtherRecipientCheckbox(FormElement):
    def __init__(self, name="Other Recipient"):
        super().__init__(name)
        self.checked = False

    def toggle(self, value: bool):
        if not self.active:
            print(f"{self.name} is inactive")
            return
        self.checked = value
        print(f"{self.name} = {self.checked}")
        self.mediator.notify(self, "checkbox_changed")

class NameField(FormElement):
    def __init__(self, name="Name"):
        super().__init__(name)
        self.value = ""

class PhoneField(FormElement):
    def __init__(self, name="Phone"):
        super().__init__(name)
        self.value = ""

class SelfPickupCheckbox(FormElement):
    def __init__(self, name="Self Pickup"):
        super().__init__(name)
        self.checked = False

    def toggle(self, value: bool):
        self.checked = value
        print(f"{self.name} = {self.checked}")
        self.mediator.notify(self, "self_pickup_changed")

mediator = FormMediator()

date_selector = DateSelector()
time_selector = TimeSelector()
other_recipient = OtherRecipientCheckbox()
name_field = NameField()
phone_field = PhoneField()
self_pickup = SelfPickupCheckbox()

for elem in [date_selector, time_selector, other_recipient, name_field, phone_field, self_pickup]:
    mediator.register(elem)

date_selector.select_date("2025-11-28")
other_recipient.toggle(True)
self_pickup.toggle(True)
self_pickup.toggle(False)
