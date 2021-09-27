# suds-sanity

Simple demonstration of data/action manipulation through use of _Python 3_ `suds-community` [<sup>[1]</sup>](https://github.com/suds-community/suds) SOAP client.  
The demo covers work with `WSDL` [<sup>[2]</sup>](https://www.w3.org/TR/wsdl.html) file obtained from [_SoapUI's tutorial_](https://www.soapui.org/docs/soap-and-wsdl/).

Client's service imitates a calculator tool, providing few different operations:
* addition,
* subtraction,
* multiplication and
* division.

## Prerequisites

The scripts were built using:
* [Python v3.8.10](https://www.python.org/downloads/release/python-3810/)
* [suds-community v0.8.5](https://pypi.org/project/suds-community/0.8.5/)

## Running the scripts

* [install Python](https://www.python.org/downloads/)
* **optional:** create a project-specific _venv_ ([How To?](https://realpython.com/python-virtual-environments-a-primer/))
* install libraries from `requirements.txt` file (command: `pip install -r requirements.txt`)
* run `main.py`

## References

* [SoapUI: SOAP and WSDL - Getting Started](https://www.soapui.org/docs/soap-and-wsdl/)
* [SUDS - Library Overview](https://docs.inductiveautomation.com/display/DOC79/SUDS+-+Library+Overview)
