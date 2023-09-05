#! /bin/bash

for id in $(sudo docker ps -q)
do
    if [[ $(sudo docker "${id}") == *"${1}"* ]];then
        echo "Found on container on port 80, proceeding to stop it"
        sudo docker kill ${id}
        sleep 2
        if [[ $? == 0 ]];then
            echo "${id} container stopped"
        else 
            echo "It was taking too long, check it manually if deployment shows an error"
        fi
    fi
done