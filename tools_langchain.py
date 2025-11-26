from langchain.tools import Tool
from tools import get_order_status, get_delivery_time, get_cancellation_policy, get_delivery_partner_info, get_restaurant_info

order_status_tool = Tool(
    name="OrderStatus",
    func=lambda user_id: get_order_status(user_id),
    description="Use this to answer questions about the status of the user's order."
)

delivery_time_tool = Tool(
    name="DeliveryTime",
    func=lambda user_id: get_delivery_time(user_id),
    description="Use this to answer questions about how long the order will take."
)

cancellation_policy_tool = Tool(
    name="CancellationPolicy",
    func=lambda user_id: get_cancellation_policy(user_id),
    description="Use this to answer questions about order cancellation policies."
)

delivery_partner_tool = Tool(
    name="DeliveryPartner",
    func=lambda user_id: get_delivery_partner_info(user_id),
    description="Use this to provide information about the delivery partner."
)

restaurant_info_tool = Tool(
    name="RestaurantInfo",
    func=lambda order_id: get_restaurant_info(order_id),
    description="Use this to answer questions about the restaurant for a given order."
)

tools = [
    order_status_tool,
    delivery_time_tool,
    cancellation_policy_tool,
    delivery_partner_tool,
    restaurant_info_tool
]
