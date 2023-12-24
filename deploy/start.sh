#!/bin/bash

case "$1" in
    "template")
        python3 /home/ubuntu/deploy/create_resource.py
        ;;
    "install")
        case "$2" in
            "--infra")
                echo "Starting infrastructure..."
                helm install infra-release /home/ubuntu/deploy/helm-chart/frontend-charts
                ;;
            "--worker")
                echo "Starting worker..."
                helm install worker-release /home/ubuntu/deploy/helm-chart/worker-chart
                ;;
            *)
                echo "Invalid start option. Use --infra or --worker."
                ;;
        esac
        ;;
    "delete")
        case "$2" in
            "--infra")
                echo "Deleting worker..."
                helm delete infra-release
                ;;
            "--worker")
                echo "Deleting worker..."
                helm delete worker-release
                ;;
            "--all")
                echo "Deleting all..."
                # Add your logic to delete all resources here
                helm delete infra-release
                helm delete worker-release
                ;;
            *)
                echo "Invalid delete option. Use --worker or --all."
                ;;
        esac
        ;;
    *)
        echo "Invalid action. Use start or delete."
        ;;
esac
