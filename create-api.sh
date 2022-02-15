cwd="$PWD"
cmd=""

cd ./sevdesk/contact/

if [ -d "client" ]; then
    cmd="update"
else 
    cmd="generate"
fi 

openapi-python-client $cmd --path $cwd/openAPI/openAPI-Contact.json --custom-template-path $cwd/openAPI/templates --config $cwd/openAPI/config.yaml --meta none
