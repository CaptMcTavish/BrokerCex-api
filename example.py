import swagger_client
from BrokerAPIKeyAuthenticator import generate_signature

apiKey = "S6CMGtVkR44EYv7y"
apiSecret = "Fj23XdyMzmtdbr4yTxnryxywMpZnN"

api = swagger_client.OperationsApi(swagger_client.ApiClient(swagger_client.Configuration()))

# GET ACCOUNT METRICS
acc_metrics_req_body = swagger_client.Body1()
acc_metrics_req_body.include_positions = True

message = api.api_client.sanitize_for_serialization(acc_metrics_req_body)

api.api_client.configuration.api_key = {"broAuth": "{},{}".format(apiKey, generate_signature(apiSecret, message))}

api.get_account_metrics(**{"body": {"data": {"include_positions": True}}})


# PLACE ORDER
place_order_req_body = swagger_client.Body4()
place_order_req_body.order_code = "0000000009"  # must be unique for every new order
place_order_req_body.type = "LIMIT"
place_order_req_body.instrument = "BTC/USD"
place_order_req_body.quantity = 1
place_order_req_body.position_effect = "OPEN"
place_order_req_body.side = "BUY"
place_order_req_body.limit_price = 17750.50
place_order_req_body.tif = "GTC"

message = api.api_client.sanitize_for_serialization(place_order_req_body)

api.api_client.configuration.api_key = {"broAuth": "{},{}".format(apiKey, generate_signature(apiSecret, message))}
api.open_account_order(**{"body": {"data": place_order_req_body}})
