# Master
ENTRYPOINT ["sh","-c", "/startup.sh & sleep 20 && export DISPLAY=:1 && python /home/ubuntu/code/sync_mouse/master.py"]

# Client
ENTRYPOINT ["sh","-c", "/startup.sh & sleep 20 && export DISPLAY=:1 && python /home/ubuntu/code/sync_mouse/client.py"]

sudo crictl pull --creds ondinhk:dckr_pat_Z5rjpw0JULt8_zBgqAZDQYR7x1g ondinhk/vm-manager-worker

# Join k8s
sudo swapoff -a
sudo sed -i '/\tswap\t/d' /etc/fstab

kubeadm token create --print-join-command

kubeadm join 192.168.1.11:6443 --token kvyszm.hxcfbmje7ox6xqvi \
	--discovery-token-ca-cert-hash sha256:8b6aa6afdfd82cec416013338dcad17633b0e320d5e9ad98d119fc5f0da06ed7

# Label
kubectl label node <name> node-role.kubernetes.io/worker=worker

# Dashboard
kubectl patch svc prometheus-stack-grafana -p '{"spec": {"type": "NodePort"}}'
kubectl get secret prometheus-stack-grafana -o jsonpath="{.data.admin-password}" | base64 --decode