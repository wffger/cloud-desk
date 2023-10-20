# 使用YAML部署在k8s

## 准备环境变量

```
echo -n 'ap-southeast-1' | openssl base64 -A
echo -n 'AWS_ACCESS_KEY_ID' | openssl base64 -A
echo -n 'AWS_SECRET_ACCESS_KEY' | openssl base64 -A
echo -n 'AWS_S3_BUCKET' | openssl base64 -A
```

修改cloudesk-secret
```
  AWS_REGION_NAME: "YXAtc291dGhlYXN0LTE="
  AWS_ACCESS_KEY_ID: "xxx="
  AWS_SECRET_ACCESS_KEY: "xxx="
  AWS_S3_BUCKET: "xxx="
```

## 部署cloudesk.yaml
```
alias kk="kubectl -n cloudesk"
kk apply -f cloudesk.yaml
kubectl -n cloudesk port-forward service/cloudesk-svc 8080:8080 --address 0.0.0.0
```

## 浏览器查看服务

http://localhost:8080  
or  
https://localhost:8080  