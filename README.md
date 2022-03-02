# A simplified Python-Client for SevDesk
This Python Package aims to simplify work with the SevDesk API. Instead of writing all clients by hand, the great `openapi-python-client` package is used to to generate the API client used by the package from the SevDesk OpenAPI specifications.

## Design Goals
The package tries to simplify working with the SevDesk API by introducing a level of abstraction for contacts, invoices and credit notes. These simplifications are focusing on the integration of Shopify with SevDesk. However, most of the common usecases are definitly covered. Furthermore, modern Python ensure a highly modular and extensible design.

# Features
- Create, update and delete contacts with invoice address, delivery address, e-mail, and phone number
- Create, update, download and delete simple invoices
- Create, update, download and delete invoice-specfic credit notes and booking-type credit notes

## Contacts
SevDesk offers an OpenAPI specification to handle contacts. However, the official specification has a lot of issues making code generation impossible. This package contains a version with many bug fixes and added functionality to auto-generate a client for the SevDesk API.

The python SevDesk client comes with an additional layer of abstraction, currently supporting customers (as used by Shopify). A customer can have a limited amount of addresses (invoice address, delivery address) and contact methods (E-Mail, Phone) to simplify contact management.

## Invoices
SevDesk offers an OpenAPI specification to handle invoices. However, the official specification has a lot of issues making code generation impossible. This package contains a version with many bug fixes and added functionality to auto-generate a client for the SevDesk API.

On top of the SevDesk client code, this package comes with a simplified invoice API allowing to create, downlaod and update invoices. 

## Credit-Notes
SevDesk does not offer an OpenAPI specification for the credit note API. Hence, the package includes (a far from complete or perfect) OpenAPI specification for credit notes based on the SevDesk invoice API.

The package offers a similar API as for invoices and allows to create two types of credit notes:
- _Underachievements_ are linked to invoices 
- _Booking_ are linked to a booking category

These credit notes are integrated in the API to allow a smooth integration of Shopify gift cards. For further context, the Shopify app has a detailed explanation on how to book and use credit notes to correctly integrate gift cards compliant to european law (multi-purpose gift cards - Mehrzweckgutscheine). 

## Accounting Types
The package includes some (undocumented) OpenAPI files reverse engineered from SevDesk calls to simplify working with the API. The accounting types/categories - needed by the e.g. booking-type credit notes - are an example for an added OpenAPI specification. Not all properties are covered within the specification - if needed, extension is easy. 

# Contributing
Feel free to contribute to the ongoing project. Also, if you are mising features not covered by OpenAPI, feel free to open an issue or to contribute to the OpenAPI specification of SevDesk directly. Lets help their developers fixing the bugs and completing the specification!

## Generate API
To generate the client based on the OpenAPI specifications, you need the following tools available on your path:
- swagger-cli
- openapi-python-client

Then, simply run `create-api.sh`