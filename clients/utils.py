import suds
from suds.client import Client


def create_suds_client(url):
    """
    Creates a suds client for SOAP protocol from the passed URL pointing to
    WSDL Schema file.

    :param url: URL pointing to WSDL Schema file
    :return: suds client object
    """
    return Client(url)


def execute_operation(client, operation_name, operands):
    """
    Executes specific operation of an existing suds client for given
    operands and based on its name, raises error if passed non-existing
    operation name.

    :param client: existing suds client
    :param operation_name: name of the operation to be executed
    :param operands: operands to be used within operation execution
    :return: result of executed operation
    """
    try:
        return getattr(client.service, operation_name)(
            operands[0], operands[1]
        )
    except suds.MethodNotFound:
        raise ValueError(f"Called a non-existing method of suds client!")
