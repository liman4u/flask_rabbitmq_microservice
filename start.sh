#!/bin/bash

docker-compose down

docker-compose up -d --build

>&2 echo "Waiting for application to run. Please wait....."
sleep 10
>&2 echo "Application started :)"

exit 0