cwd="$PWD"
cmd=""

# Create or update the contact-client API
cd ./sevdesk/contact/

if [ -d "client" ]; then
    cmd="update"
else 
    cmd="generate"
fi 

openapi-python-client $cmd --path $cwd/openAPI/openAPI-Contact.json --custom-template-path $cwd/openAPI/templates --config $cwd/openAPI/config-contact.yaml --meta none
cd $cwd

# Copy client to common as the client-code is shared between all instances
cp $cwd/sevdesk/contact/client/client.py $cwd/sevdesk/

# Create or update the invoice-client API
cd ./sevdesk/invoice/

if [ -d "client" ]; then
    cmd="update"
else 
    cmd="generate"
fi 

openapi-python-client $cmd --path $cwd/openAPI/openAPI-Invoice.json --custom-template-path $cwd/openAPI/templates --config $cwd/openAPI/config-invoice.yaml --meta none
cd $cwd
