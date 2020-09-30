#### 增加dell idrac module
* 在dell官网获取对应服务器型号的mib文件
* 进入服务器的idrac管理界面，开启snmp服务并配置账号和group
* 执行snmpbulkwalk测试snmp连通性以及OID
```shell
snmpbulkwalk -v3 -l authPriv -u "root" -a SHA -A "Warp1234" -x AES -X "Warp1234" 172.16.19.11 1.3.6.1.4.1.674.10892.5.4.700.20.1.6
```
* git clone snmp_exporter，拿到generator并使用go编译
* 编辑generator.yml，指定OID后执行generate，拿到snmp_exporter可用的module，结束。

生成配置文件时提示OID无效，把所有dell的所有mib文件放至mibs/文件目录即可解决.
