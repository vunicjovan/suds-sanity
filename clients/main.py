from utils import create_suds_client, execute_operation

# WSDL Schema file used from: https://www.soapui.org/docs/soap-and-wsdl/
wsdl_url = "http://www.dneonline.com/calculator.asmx?wsdl"

client = create_suds_client(url=wsdl_url)

operands = [9, 3]
results = {
    "add": execute_operation(client, "Add", operands),
    "subtract": execute_operation(client, "Subtract", operands),
    "multiply": execute_operation(client, "Multiply", operands),
    "divide": execute_operation(client, "Divide", operands),
}

print(f"Contents of created client:\n{client}")

for (key, value) in results.items():
    print(f"Result for '{key}' operation with operands {operands}: {value}")
