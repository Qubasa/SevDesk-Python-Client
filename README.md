# A simplified Python-Client for SevDesk
This Python Package aims to simplify work with the SevDesk API. 
The package is under development and will support the Contact and Invoice API. 

## OpenAPI
The client uses the SevDesk OpenAPI specifification. 
However, the specification seems to have several issues and misses several functionalities which have been fixed or added during development.
The great `openapi-python-client` package is used to to generate the python API client which is then used by the package.

## Design Goals
The design aims to integrate Shopify Webhooks with SevDesk. 
The package implies several limitations and abstractions to make usage of the SevDesk API easier. 

## Features
- Create, update and delete contacts with invoice address, delivery address, e-mail, and phone number

## Planned Features
- Create invoices
- Create vouchers
