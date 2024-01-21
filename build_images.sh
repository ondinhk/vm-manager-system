#!/bin/bash

echo "Build frontend image"
#npm --prefix ./frontend run build || exit 1
docker build -t ondinhk/vm-manager-frontend ./frontend || exit 1

##
echo "Build backend image"
docker build -t ondinhk/vm-manager-backend ./backend || exit 1


##
echo "Build worker image"
docker build -t ondinhk/vm-manager-worker -f ./vms/Dockerfile.worker ./vms/ || exit 1

##
echo "Build master image"
docker build -t ondinhk/vm-manager-master -f ./vms/Dockerfile.master ./vms/ || exit 1

# docker push ondinhk/vm-manager-frontend
# docker push ondinhk/vm-manager-backend
# docker push ondinhk/vm-manager-worker
# docker push ondinhk/vm-manager-master
echo "save fe"
docker save ondinhk/vm-manager-frontend -o frontend.tar
echo "save be"
docker save ondinhk/vm-manager-backend -o backend.tar
echo "save worker"
docekr save ondinhk/vm-manager-worker -o worker.tar
echo "save master"
docekr save ondinhk/vm-manager-master -o master.tar

echo "import frontend"
sudo ctr -n=k8s.io images import  frontend.tar
echo "import backed"
sudo ctr -n=k8s.io images import  backend.tar
echo "import worker"
sudo ctr -n=k8s.io images import  worker.tar
echo "import master"
sudo ctr -n=k8s.io images import  master.tar

echo "remove file"
rm frontend.tar backend.tar worker.tar master.tar
echo "success"