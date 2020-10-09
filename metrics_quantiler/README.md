1.将grafana导出文件放置在此目录
2.导出时Date Time Format选择为：YYYYMMDD_HHmm
3.导出完毕后使用编辑器打开csv，删除第一行的“sep=;”保存
4.分离工作日
```grep -Ev "2020011._(00|01|02|03|04|05|06|07|08|09|22|23)" grafana_data_export_A9.csv > A9_weekday.csv```


* grafana查询超时解决思路：
PromQL查询单个指标时，每value视为一个series，每个label也视为一个series
假设每 instance 有32核心，即32 labels
单次查询node_cpu_seconds_total{location="A9",mode="idle",instance="X"}，series为32
prometheus默认抓取间隔为15s
A9共108台instance，则
查询一个小时metric需要的series为
60*60/15*108*32=829440
查询五天范围内所需要的series为
829440*24*5=99,532,800
将query.max-samples默认的50,000,000修改为100,000,000，即可解决。
