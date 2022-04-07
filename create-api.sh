cwd="$PWD"
cmd=""

# Build final OpenAPI document
swagger-cli bundle $cwd/openAPI/specification/openapi.json --outfile $cwd/build/openapi.json --type json

cd ./sevdesk/

if [ -d "client" ]; then
    cmd="update"
else 
    cmd="generate"
fi 

# Create python-client using templates and config
openapi-python-client $cmd --path $cwd/build/openapi.json --custom-template-path $cwd/openAPI/templates --config $cwd/openAPI/configuration/client.yaml --meta none
