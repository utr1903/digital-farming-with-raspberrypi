#!/usr/bin/bash

# Datasources
cat > ./grafana/conf/provisioning/datasources/datasources.yaml <<EOF
apiVersion: 1
datasources:
  - name: Prometheus
    type: prometheus
    url: http://localhost:9090
    access: proxy
    isDefault: false
EOF

# Dashboard providers
cat > ./grafana/conf/provisioning/dashboards/dashboardproviders.yaml <<EOF
apiVersion: 1
providers:
  - name: 'digital-farming'
    orgId: 1
    folder: ''
    type: file
    updateIntervalSeconds: 10
    disableDeletion: true
    editable: true
    options:
    path: $(pwd)/dashboards
EOF
