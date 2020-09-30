```
╔═╗────────╔╗╔╗────╔═╗
║╬╠╦╦═╦══╦═╣╚╣╚╦═╦╦╣═╣
║╔╣╔╣╬║║║║╩╣╔╣║║╩╣║╠═║
╚╝╚╝╚═╩╩╩╩═╩═╩╩╩═╩═╩═╝
```
## IT_Prmetheus
在此记录IT-Promtheus常用的service及配置文件

#### 07/21/20
* 增加SNMP_Exporter
* 增加target: A9、 B11 Core Switches.
* 从`if_mib`中提取部分metrics,新建为`simple_switch module`,从而减少交换机walk&get的性能开支.

#### 09/04/20
* 增加Blackbox_Exporter
* 增加target: 南京、北京、郑州、周浦IDC Core Switches & IPsec.

#### 09/30/20
* 增加dell idrac监控，对IT服务器进行温度监控
* 增加alertmanager，接入企业微信和企业邮箱告警
