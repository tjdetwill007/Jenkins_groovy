#! /bin/bash
filepath='tjdetwill007/mycloudapp:latest'

sudo docker pull $filepath
sudo docker run -d -p 80:80 $filepath 
