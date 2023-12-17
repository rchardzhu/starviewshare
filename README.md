# starviewshare
观星量化--开源金融量化数据接口

[starviewshare](https://github.com/rchardzhu/starviewshare) 中文名为观星量化， 是一个用于获取股票、ETF、期货数据的免费开源 Python 库。

特点：
* 只需一行代码，可以自由切换底层数据源
* 基于akshare、efinance、miniqmt打造
* 免费开源

欢迎关注微信公众号"Python量化实战"，与您分享更多资源和信息。关注后回复加群可以与小伙伴们一起讨论问题、贡献代码


## Installation

- 通过 `pip` 安装

```bash
pip install starviewshare
```

- 通过 `pip` 更新

```bash
pip install starviewshare --upgrade
```

## Examples

- 验证安装是否成功：输出starviewshare版本

```python
import starviewshare as svs
print(svs.__version__)
```

### stock

- 股票龙虎榜
```python
import starviewshare as svs
svs.stock.get_daily_billboard()
start_date = '2023-12-08'
end_date = '2023-12-17'
svs.stock.get_daily_billboard(start_date=start_date,end_date=end_date)
```