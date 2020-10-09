#!/bin/bash
# pull api spec
SPEC_URL='https://api.esper.io/openapi.yaml'
SPEC_PATH='esper-api-spec.yaml'
curl --progress-bar $SPEC_URL -o $SPEC_PATH

git clone git@bitbucket.org:shoonyacloud/esper-sdk-config.git
cd esper-sdk-config
wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.2.1/swagger-codegen-cli-2.2.1.jar
java -jar swagger-codegen-cli.jar generate -i ./esper-api-spec.yaml -l python -c ./sdk-config/python-config.json --template-dir ./sdk-templates/python/ -o esperclient 
# git add esperclient
# upgrade version
# commit and puh
