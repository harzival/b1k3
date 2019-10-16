converted_mountain_bike_part_list = [
    "existing-mountain-bike",
    "hub-motor",
    "battery-box",
    "speed-sensor",
    "throttle",
    "e-brake-levers",
    "logic-display",
    "logic-box",
    "spoke-replacements",
    "battery-box-mounting-mechanism",
    "logic-box-mounting-mechanism",
]

class Product:
    def __init__(
        self, name, url, price, ammount, part_list=[]
    ):
        self.name = name
        self.url = url
        self.price = price
        self.ammount = ammount
        self.part_list = part_list

existing_mountain_bike_product_list = []
ebike_kit_product_list = []
hub_motor_product_list = []
battery_box_product_list = []
speed_sensor_product_list = []
throttle_product_list = []
e_brake_levers_product_list = []
logic_display_product_list = []
logic_box_product_list = []
spoke_replacement_product_list = []
battery_box_mounting_mechanism_product_list = []
logic_box_mounting_mechanism = []

all_products = (
    []
    .extend(existing_mountain_bike_product_list)
    .extend(ebike_kit_product_list)
    .extend(hub_motor_product_list)
    .extend(battery_box_product_list)
    .extend(speed_sensor_product_list)
    .extend(throttle_product_list)
    .extend(e_brake_levers_product_list)
    .extend(logic_display_product_list)
    .extend(logic_box_product_list)
    .extend(spoke_replacement_product_list)
    .extend(battery_box_mounting_mechanism_product_list)
    .extend(logic_box_mounting_mechanism)
)

