#!/bin/bash

echo "Build frontend image"
#npm --prefix ./frontend run build || exit 1
docker build -t ondinhk/vm-manager-frontend ./frontend || exit 1
docker push ondinhk/vm-manager-frontend

##
echo "Build backend image"
docker build -t ondinhk/vm-manager-backend ./backend || exit 1
docker push ondinhk/vm-manager-backend

##
echo "Build worker image"
docker build -t ondinhk/vm-manager-worker -f ./vms/Dockerfile.worker ./vms/ || exit 1
docker push ondinhk/vm-manager-worker

##
echo "Build master image"
docker build -t ondinhk/vm-manager-master -f ./vms/Dockerfile.master ./vms/ || exit 1
docker push ondinhk/vm-manager-master
