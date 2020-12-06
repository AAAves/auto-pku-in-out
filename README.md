# auto-pku-in-out
by selenium


## 12.6 更新

保持电脑不关机的情况下，可以自动备案的版本。

会在每天6-10点之间的某个时间备案一次

优化了一些细节

## 使用方法

1.打开python文件把以下内容换成自己的：

```{python}
# 学号
id_card = '1901xxxxx'
# 密码
pswd = 'pswd'
# 出校事由
chu_shiyou = '实习'
# 出校轨迹
chu_guiji = '南门'
# 入校事由
ru_shiyou = '回宿舍'
# 居住地所在区
ru_district = '海淀'
# 入校街道
ru_jiedao = '北京大学'

#所在校区默认燕园
#入校前居住地默认北京
#默认14日在京
```

2.安装selenium

```{python}
pip install selenium
```

3.运行

有自动弹框 不用管

打印出success说明成功备案