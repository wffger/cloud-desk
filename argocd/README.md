# 运行
修改helm参数值：
```
kubectl apploy -f application.yaml

alias kk="kubectl -n cloudesk"
kk port-forward service/cloudesk-cloud-desk 8080:80 --address 0.0.0.0
```

到集群8080端口使用应用。

# 排查故障
```
alias kk="kubectl -n cloudesk"
kk get secret cloudesk-secret -o jsonpath='{.data}'
```