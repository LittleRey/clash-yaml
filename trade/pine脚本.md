

```markdown
# Pine Script Cheatsheet

## Types
**array**
  关键词用于声明数组类型
**bool**
  关键词用于声明布尔类型
**box**
  关键词用于声明盒子类型
**chart.point**
  关键词用于声明图表点类型
**color**
  关键词用于声明颜色类型
**const**
  `const` 关键词用于声明常量
**float**
  关键词用于声明浮点数类型
**int**
  关键词用于声明整数类型
**label**
  关键词用于声明标签类型
**line**
  关键词用于声明线条类型
**linefill**
  关键词用于声明线段填充类型
**map**
  关键词用于声明映射类型
**matrix**
  关键词用于声明矩阵类型
**polyline**
  关键词用于声明折线类型
**series**
  `series` 关键词用于声明序列类型
**simple**
  `simple` 关键词用于声明简单类型
**string**
  关键词用于声明字符串类型
**table**
  关键词用于声明表格类型

## Operators
**-**
  减法或一元负号
**-=**
  减法赋值
**:=**
  重新赋值运算符
**!=**
  不等于。适用于所有类型
**?:**
  三元条件运算符
**[]**
  系列下标。用于访问系列数据
**\***
  乘法。适用于数值类型
**\*=**
  乘法赋值
**/**
  除法。适用于数值类型
**/=**
  除法赋值
**%**
  取模（整数余数）
**%=**
  取模赋值
**+**
  加法或一元正号
**+=**
  加法赋值
**<**
  小于。适用于数值类型
**<=**
  小于或等于
**==**
  等于。适用于所有类型
**=>**
  `=>` 运算符用于函数定义
**>**
  大于。适用于数值类型
**>=**
  大于或等于

## Strings
**str.contains()**
  如果字符串包含子字符串则返回 true
**str.endswith()**
  如果字符串以指定后缀结尾则返回 true
**str.format_time()**
  将 `time` 转换为格式化时间字符串
**str.format()**
  格式化字符串
**str.length()**
  返回字符串长度（整数）
**str.lower()**
  返回小写形式的新字符串
**str.match()**
  返回匹配后的新子字符串
**str.pos()**
  返回子字符串的位置
**str.repeat()**
  构造重复多次的新字符串
**str.replace_all()**
  替换所有出现的子字符串
**str.replace()**
  返回替换后的新字符串
**str.split()**
  将字符串分割为数组
**str.startswith()**
  如果字符串以指定前缀开头则返回 true
**str.substring()**
  返回子字符串的新字符串
**str.tonumber()**
  将值转换为数字
**str.tostring()**
  转换为字符串
**str.trim()**
  构造去除空白的新字符串
**str.upper()**
  返回大写形式的新字符串
**strategy.close_all()**
  创建订单以平仓所有头寸
**string()**
  将 NA 转换为字符串

## Maths
**math.abs()**
  `n` 的绝对值
**math.acos()**
  反余弦函数
**math.asin()**
  反正弦函数
**math.atan()**
  反正切函数
**math.avg()**
  计算平均值
**math.ceil()**
  向上取整
**math.cos()**
  余弦函数
**math.e**
  数学常数 e
**math.exp()**
  指数函数
**math.floor()**
  向下取整
**math.log()**
  自然对数
**math.log10()**
  以 10 为底的对数
**math.max()**
  返回最大值
**math.min()**
  返回最小值
**math.phi**
  黄金分割比例常数
**math.pi**
  圆周率常数
**math.pow()**
  幂函数
**math.random()**
  返回伪随机数
**math.round_to_mintick()**
  按最小刻度四舍五入
**math.round()**
  四舍五入
**math.rphi**
  黄金分割比例的倒数
**math.sign()**
  符号函数
**math.sin()**
  正弦函数
**math.sqrt()**
  平方根
**math.sum()**
  求和函数
**math.tan()**
  正切函数
**math.todegrees()**
  弧度转角度
**math.toradians()**
  角度转弧度
**na**
  表示缺失值的关键词

## Bar State
**barstate.isconfirmed**
  如果当前柱已确认则返回 true
**barstate.isfirst**
  如果是当前图表的第一个柱则返回 true
**barstate.ishistory**
  如果是历史柱则返回 true
**barstate.islast**
  如果是当前图表的最后一个柱则返回 true
**barstate.islastconfirmedhistory**
  如果脚本执行时当前柱是最后一个确认的历史柱则返回 true
**barstate.isnew**
  如果是新柱则返回 true
**barstate.isrealtime**
  如果是实时柱则返回 true

## Plotting
**barcolor()**
  设置柱状图颜色
**bgcolor()**
  填充背景
**display.all**
  显示所有内容
**display.data_window**
  仅显示数据窗口
**display.none**
  不显示
**display.pane**
  仅显示当前面板
**display.price_scale**
  仅显示价格轴
**display.status_line**
  仅显示状态栏
**fill()**
  填充背景区域
**hline.style_dashed**
  水平线样式：虚线
**hline.style_dotted**
  水平线样式：点线
**hline.style_solid**
  水平线样式：实线
**hline()**
  绘制水平线
**plot.style_area**
  面积图样式
**plot.style_areabr**
  面积柱状图样式
**plot.style_circles**
  圆点样式
**plot.style_columns**
  柱状图样式
**plot.style_cross**
  十字交叉样式
**plot.style_histogram**
  直方图样式
**plot.style_line**
  折线图样式
**plot.style_linebr**
  断线样式
**plot.style_stepline**
  阶梯线样式
**plot.style_stepline_diamond**
  钻石阶梯线样式
**plot.style_steplinebr**
  阶梯断线样式
**plot()**
  绘制数据系列
**plotarrow()**
  绘制上下箭头
**plotbar()**
  在图表上绘制 OHLC 柱状图
**plotcandle()**
  在图表上绘制蜡烛图
**plotchar()**
  绘制视觉形状
**plotshape()**
  绘制视觉形状
**shape.arrowdown**
  箭头向下形状
**shape.arrowup**
  箭头向上形状
**shape.circle**
  圆形形状
**shape.cross**
  十字形形状
**shape.diamond**
  菱形形状
**shape.flag**
  旗帜形状
**shape.labeldown**
  向下标签形状
**shape.labelup**
  向上标签形状
**shape.square**
  方形形状
**shape.triangledown**
  三角形向下形状
**shape.triangleup**
  三角形向上形状
**shape.xcross**
  X 形交叉形状

## Indicators
**ta.accdist**
  累积/派发指标
**ta.alma()**
  阿尔诺·勒格克斯移动平均线
**ta.atr()**
  平均真实波幅函数
**ta.barssince()**
  计算自条件满足以来的柱数
**ta.bb()**
  布林带。技术分析指标
**ta.bbw()**
  布林带宽度
**ta.cci()**
  商品通道指数
**ta.change()**
  比较当前值与前一值的变化
**ta.cmo()**
  钱德动量振荡器
**ta.cog()**
  重心指标
**ta.correlation()**
  相关系数
**ta.cross()**
  
**ta.crossover()**
  当 `source1` 系列上穿 `source2` 系列时返回 true
**ta.crossunder()**
  当 `source1` 系列下穿 `source2` 系列时返回 true
**ta.cum()**
  累积（总计）值
**ta.dev()**
  差异度量
**ta.dmi()**
  DMI 函数返回方向移动指标
**ta.ema()**
  EMA 函数返回指数移动平均线
**ta.falling()**
  测试 `source` 是否正在下跌
**ta.highest()**
  指定周期内的最高值
**ta.highestbars()**
  指定周期内最高值的偏移量
**ta.hma()**
  HMA 函数返回哈拉尔移动平均线
**ta.iii**
  盘中强度指标
**ta.kc()**
  凯尔特纳通道。技术分析指标
**ta.kcw()**
  凯尔特纳通道宽度
**ta.linreg()**
  线性回归曲线
**ta.lowest()**
  指定周期内的最低值
**ta.lowestbars()**
  指定周期内最低值的偏移量
**ta.macd()**
  MACD（移动平均线收敛/发散）
**ta.max()**
  返回历史最高值
**ta.median()**
  返回中位数
**ta.mfi()**
  资金流量指标
**ta.min()**
  返回历史最低值
**ta.mode()**
  返回[众数]
**ta.mom()**
  `source` 的动量
**ta.nvi**
  负成交量指标
**ta.obv**
  能量潮指标
**ta.percentile_linear_interpolation()**
  计算百分位数（线性插值）
**ta.percentile_nearest_rank()**
  计算百分位数（最近排名）
**ta.percentrank()**
  百分位排名是值的排名在数据集中所占的百分比
**ta.pivot_point_levels()**
  计算枢轴点水平
**ta.pivothigh()**
  该函数返回枢轴高点
**ta.pivotlow()**
  该函数返回枢轴低点
**ta.pvi**
  正成交量指标
**ta.pvt**
  价格-成交量趋势
**ta.range()**
  返回 `high` 与 `low` 之间的差值
**ta.rci()**
  计算秩相关指数
**ta.rising()**
  测试 `source` 是否正在上涨
**ta.rma()**
  移动平均线，用于计算 RSI
**ta.roc()**
  计算百分比变化率
**ta.rsi()**
  相对强弱指数
**ta.sar()**
  抛物线 SAR（抛物线转向指标）
**ta.sma()**
  SMA 函数返回简单移动平均线
**ta.stdev()**
  
**ta.stoch()**
  随机指标。它是一种动量指标
**ta.supertrend()**
  超级趋势指标
**ta.swma()**
  对称加权移动平均线
**ta.tr**
  真实波幅，等同于
**ta.tr()**
  计算当前真实波幅
**ta.tsi()**
  真实强度指数
**ta.valuewhen()**
  返回 `source` 在 `condition` 为 true 时的值
**ta.variance()**
  方差是期望的平方差
**ta.vwap**
  成交量加权平均价格
**ta.vwap()**
  成交量加权平均价格
**ta.vwma()**
  VWMA 函数返回成交量加权移动平均线
**ta.wad**
  威廉姆斯累积/派发指标
**ta.wma()**
  WMA 函数返回加权移动平均线
**ta.wpr()**
  威廉姆斯 %R。振荡器
**ta.wvad**
  威廉姆斯可变累积/派发指标
**table.all**
  返回填充了表引用 ID 的数组
**table.cell_set_bgcolor()**
  该函数设置单元格背景颜色
**table.cell_set_height()**
  该函数设置单元格高度
**table.cell_set_text_color()**
  该函数设置单元格文本颜色
**table.cell_set_text_font_family()**
  该函数设置单元格文本字体
**table.cell_set_text_formatting()**
  设置单元格文本格式
**table.cell_set_text_halign()**
  该函数设置单元格文本水平对齐方式
**table.cell_set_text_size()**
  该函数设置单元格文本大小
**table.cell_set_text_valign()**
  该函数设置单元格文本垂直对齐方式
**table.cell_set_text()**
  该函数设置单元格文本
**table.cell_set_tooltip()**
  该函数设置单元格工具提示
**table.cell_set_width()**
  该函数设置单元格宽度
**table.cell()**
  该函数定义单元格
**table.clear()**
  该函数移除表中的所有单元格
**table.delete()**
  该函数删除表
**table.merge_cells()**
  该函数合并单元格
**table.new()**
  该函数创建新表
**table.set_bgcolor()**
  该函数设置表背景颜色
**table.set_border_color()**
  该函数设置表边框颜色
**table.set_border_width()**
  该函数设置表边框宽度
**table.set_frame_color()**
  该函数设置表框架颜色
**table.set_frame_width()**
  该函数设置表框架宽度
**table.set_position()**
  该函数设置表位置
**table()**
  将 NA 转换为表格

## Inputs
**input.bool()**
  添加布尔输入到脚本
**input.color()**
  添加颜色输入到脚本
**input.enum()**
  添加枚举输入到脚本
**input.float()**
  添加浮点数输入到脚本
**input.int()**
  添加整数输入到脚本
**input.price()**
  添加价格输入到脚本
**input.session()**
  添加会话输入到脚本
**input.source()**
  添加源输入到脚本
**input.string()**
  添加字符串输入到脚本
**input.symbol()**
  添加符号输入到脚本
**input.text_area()**
  添加文本区域输入到脚本
**input.time()**
  添加时间输入到脚本
**input.timeframe()**
  添加时间框架输入到脚本
**input()**
  添加输入到脚本

## Polylines
**polyline.all**
  返回包含所有多边形 ID 的数组
**polyline.delete()**
  删除指定的多边形
**polyline.new()**
  创建新的[多边形]

## Alerts
**alert.freq_all**
  每次脚本执行时都触发警报
**alert.freq_once_per_bar**
  每个柱触发一次警报
**alert.freq_once_per_bar_close**
  在柱关闭时触发警报
**alert()**
  创建警报触发器
**alertcondition()**
  创建警报条件

## Sessions
**session.extended**
  扩展会话的常量
**session.isfirstbar**
  如果当前柱是第一个扩展会话柱则返回 [true](#const)
**session.isfirstbar_regular**
  如果当前柱是第一个常规会话柱则返回 [true](#const)
**session.islastbar**
  如果当前柱是最后一个扩展会话柱则返回 [true](#const)
**session.islastbar_regular**
  如果当前柱是最后一个常规会话柱则返回 [true](#const)
**session.ismarket**
  如果当前柱在常规交易时段内则返回 [true](#const)
**session.ispostmarket**
  如果当前柱在盘后交易时段则返回 [true](#const)
**session.ispremarket**
  如果当前柱在盘前交易时段则返回 [true](#const)
**session.regular**
  常规会话的常量

## Timeframe
**timeframe.change()**
  检测时间框架变化
**timeframe.from_seconds()**
  将秒数转换为时间框架
**timeframe.in_seconds()**
  将时间框架转换为秒数
**timeframe.isdaily**
  如果当前时间框架是日线则返回 true
**timeframe.isdwm**
  如果当前时间框架是日/周/月则返回 true
**timeframe.isintraday**
  如果当前时间框架是分钟线则返回 true
**timeframe.isminutes**
  如果当前时间框架是分钟线则返回 true
**timeframe.ismonthly**
  如果当前时间框架是月线则返回 true
**timeframe.isseconds**
  如果当前时间框架是秒线则返回 true
**timeframe.isticks**
  如果当前时间框架是 ticks 则返回 true
**timeframe.isweekly**
  如果当前时间框架是周线则返回 true
**timeframe.main_period**
  主要周期的字符串表示
**timeframe.multiplier**
  分辨率的乘数
**timeframe.period**
  时间段的字符串表示

## Annotations
**@description**
  设置自定义描述
**@enum**
  如果放置在枚举上方
**@field**
  如果放置在[表格单元格](#表格)上方
**@function**
  如果放置在函数上方
**@param**
  如果放置在函数参数上方
**@returns**
  如果放置在函数返回值上方
**@strategy_alert_message**
  如果在[策略](#策略)中用于为警报添加自定义消息
**@type**
  如果放置在类型声明上方
**@variable**
  如果放置在变量声明上方
**@version=**
  指定 Pine Script 版本

## Bar Data
**bar_index**
  当前柱的索引。数值类型
**close**
  当前柱的收盘价
**high**
  当前柱的最高价
**low**
  当前柱的最低价
**open**
  当前柱的开盘价
**volume**
  当前柱的成交量

## Arrays
**array.abs()**
  返回包含数组元素绝对值的新数组
**array.avg()**
  该函数返回数组元素的平均值
**array.binary_search_leftmost()**
  该函数返回使用二分搜索找到最左匹配项的索引
**array.binary_search_rightmost()**
  该函数返回使用二分搜索找到最右匹配项的索引
**array.binary_search()**
  该函数返回使用二分搜索找到匹配项的索引
**array.clear()**
  该函数移除数组中的所有元素
**array.concat()**
  该函数用于合并多个数组
**array.copy()**
  该函数创建数组的副本
**array.covariance()**
  该函数返回数组元素的协方差
**array.every()**
  如果数组中所有元素都满足条件则返回 [true](#const)
**array.fill()**
  该函数设置数组元素的值
**array.first()**
  返回数组的第一个元素
**array.from()**
  该函数从值列表创建数组
**array.get()**
  该函数返回数组元素
**array.includes()**
  该函数返回数组是否包含指定元素
**array.indexof()**
  该函数返回数组中第一个匹配项的索引
**array.insert()**
  该函数更改数组
**array.join()**
  该函数创建由数组元素连接而成的新字符串
**array.last()**
  返回数组的最后一个元素
**array.lastindexof()**
  该函数返回数组中最后一个匹配项的索引
**array.max()**
  该函数返回数组元素的最大值
**array.median()**
  该函数返回数组元素的中位数
**array.min()**
  该函数返回数组元素的最小值
**array.mode()**
  该函数返回数组元素的[众数]
**array.new_bool()**
  该函数创建布尔数组
**array.new_box()**
  该函数创建盒子数组
**array.new_color()**
  该函数创建颜色数组
**array.new_float()**
  该函数创建浮点数数组
**array.new_int()**
  该函数创建整数数组
**array.new_label()**
  该函数创建标签数组
**array.new_line()**
  该函数创建线条数组
**array.new_linefill()**
  该函数创建线段填充数组
**array.new_string()**
  该函数创建字符串数组
**array.new_table()**
  该函数创建表格数组
**array.new<type>()**
  该函数创建类型数组
**array.percentile_linear_interpolation()**
  返回线性插值的百分位数值
**array.percentile_nearest_rank()**
  返回最近排名的百分位数值
**array.percentrank()**
  返回数组元素的百分位排名
**array.pop()**
  该函数移除数组的最后一个元素
**array.push()**
  该函数向数组末尾添加元素
**array.range()**
  该函数返回数组元素的范围
**array.remove()**
  该函数更改数组
**array.reverse()**
  该函数反转数组
**array.set()**
  该函数设置数组元素的值
**array.shift()**
  该函数移除数组的第一个元素
**array.size()**
  该函数返回数组长度
**array.slice()**
  该函数创建数组的子数组
**array.some()**
  如果数组中至少有一个元素满足条件则返回 [true](#const)
**array.sort_indices()**
  返回按元素值排序后的索引数组
**array.sort()**
  该函数对数组进行排序
**array.standardize()**
  该函数返回数组元素的标准化值
**array.stdev()**
  该函数返回数组元素的标准差
**array.sum()**
  该函数返回数组元素的总和
**array.unshift()**
  该函数向数组开头添加元素
**array.variance()**
  该函数返回数组元素的方差

## Matrixes
**matrix.add_col()**
  该函数添加列
**matrix.add_row()**
  该函数添加行
**matrix.avg()**
  该函数计算平均值
**matrix.col()**
  该函数创建列向量
**matrix.columns()**
  该函数返回列数
**matrix.concat()**
  该函数追加矩阵
**matrix.copy()**
  该函数创建副本
**matrix.det()**
  该函数返回行列式
**matrix.diff()**
  该函数返回差分
**matrix.eigenvalues()**
  该函数返回特征值
**matrix.eigenvectors()**
  返回特征向量矩阵
**matrix.elements_count()**
  该函数返回元素总数
**matrix.fill()**
  该函数填充矩阵
**matrix.get()**
  该函数返回元素
**matrix.inv()**
  该函数返回逆矩阵
**matrix.is_antidiagonal()**
  该函数判断是否为反对对角矩阵
**matrix.is_antisymmetric()**
  该函数判断是否为反对称矩阵
**matrix.is_binary()**
  该函数判断是否为二进制矩阵
**matrix.is_diagonal()**
  该函数判断是否为对角矩阵
**matrix.is_identity()**
  该函数判断是否为单元矩阵
**matrix.is_square()**
  该函数判断是否为方阵
**matrix.is_stochastic()**
  该函数判断是否为随机矩阵
**matrix.is_symmetric()**
  该函数判断是否为对称矩阵
**matrix.is_triangular()**
  该函数判断是否为三角矩阵
**matrix.is_zero()**
  该函数判断是否为零矩阵
**matrix.kron()**
  该函数返回克罗内克积
**matrix.max()**
  该函数返回最大值
**matrix.median()**
  该函数计算中位数
**matrix.min()**
  该函数返回最小值
**matrix.mode()**
  该函数计算众数
**matrix.mult()**
  该函数返回乘积
**matrix.new<type>()**
  该函数创建类型矩阵
**matrix.pinv()**
  该函数返回伪逆矩阵
**matrix.pow()**
  该函数计算幂
**matrix.rank()**
  该函数计算秩
**matrix.remove_col()**
  该函数移除列
**matrix.remove_row()**
  该函数移除行
**matrix.reshape()**
  该函数重建矩阵形状
**matrix.reverse()**
  该函数反转矩阵
**matrix.row()**
  该函数创建行向量
**matrix.rows()**
  该函数返回行数
**matrix.set()**
  该函数赋值元素
**matrix.sort()**
  该函数重新排列矩阵
**matrix.submatrix()**
  该函数提取子矩阵
**matrix.sum()**
  该函数返回总和
**matrix.swap_columns()**
  该函数交换列
**matrix.swap_rows()**
  该函数交换行
**matrix.trace()**
  该函数计算迹
**matrix.transpose()**
  该函数创建转置矩阵

## Datetime
**dayofmonth**
  当前柱的日期。数值类型
**dayofmonth()**
**dayofweek**
  当前柱的星期几。数值类型
**dayofweek.friday**
  常量，星期五
**dayofweek.monday**
  常量，星期一
**dayofweek.saturday**
  常量，星期六
**dayofweek.sunday**
  常量，星期日
**dayofweek.thursday**
  常量，星期四
**dayofweek.tuesday**
  常量，星期二
**dayofweek.wednesday**
  常量，星期三
**dayofweek()**
**hour**
  当前柱的小时。数值类型
**hour()**
**minute**
  当前柱的分钟。数值类型
**minute()**
**month**
  当前柱的月份。数值类型
**month()**
**second**
  当前柱的秒。数值类型
**second()**
**time**
  当前柱的时间（UNIX 时间戳）。数值类型
**time_close**
  当前柱的收盘时间
**time_tradingday**
  当前交易日的开始时间
**timenow**
  当前时间（UNIX 时间戳）。数值类型
**weekofyear**
  当前柱的周数。数值类型
**weekofyear()**
**year**
  当前柱的年份。数值类型
**year()**

## Labels
**label.all**
  返回包含所有标签 ID 的数组
**label.copy()**
  克隆标签对象
**label.delete()**
  删除指定标签
**label.get_text()**
  返回标签文本
**label.get_x()**
  返回 UNIX 时间或柱索引
**label.get_y()**
  返回此标签的价格
**label.new()**
  创建新的标签对象
**label.set_color()**
  设置标签边框和文本颜色
**label.set_point()**
  设置标签位置
**label.set_size()**
  设置箭头和文本大小
**label.set_style()**
  设置标签样式
**label.set_text_font_family()**
  该函数设置标签文本字体
**label.set_text_formatting()**
  设置文本格式
**label.set_text()**
  设置标签文本
**label.set_textalign()**
  设置文本对齐方式
**label.set_textcolor()**
  设置标签文本颜色
**label.set_tooltip()**
  设置工具提示文本
**label.set_x()**
  设置柱索引或时间
**label.set_xloc()**
  设置 x 位置和显示方式
**label.set_xy()**
  设置柱索引/时间与价格
**label.set_y()**
  设置标签价格
**label.set_yloc()**
  设置新的 y 位置
**label.style_arrowdown**
  [标签](#标签)样式：向下箭头
**label.style_arrowup**
  [标签](#标签)样式：向上箭头
**label.style_circle**
  [标签](#标签)样式：圆形
**label.style_cross**
  [标签](#标签)样式：十字形
**label.style_diamond**
  [标签](#标签)样式：菱形
**label.style_flag**
  [标签](#标签)样式：旗帜
**label.style_label_center**
  [标签](#标签)样式：居中标签
**label.style_label_down**
  [标签](#标签)样式：向下标签
**label.style_label_left**
  [标签](#标签)样式：向左标签
**label.style_label_lower_left**
  [标签](#标签)样式：左下标签
**label.style_label_lower_right**
  [标签](#标签)样式：右下标签
**label.style_label_right**
  [标签](#标签)样式：向右标签
**label.style_label_up**
  [标签](#标签)样式：向上标签
**label.style_label_upper_left**
  [标签](#标签)样式：左上标签
**label.style_label_upper_right**
  [标签](#标签)样式：右上标签
**label.style_none**
  [标签](#标签)样式：无
**label.style_square**
  [标签](#标签)样式：方形
**label.style_text_outline**
  [标签](#标签)样式：文本轮廓
**label.style_triangledown**
  [标签](#标签)样式：向下三角形
**label.style_triangleup**
  [标签](#标签)样式：向上三角形
**label.style_xcross**
  [标签](#标签)样式：X 形交叉
**label()**
  将 NA 转换为标签
**yloc.abovebar**
  位于柱上方的命名常量
**yloc.belowbar**
  位于柱下方的命名常量
**yloc.price**
  位于价格轴上的命名常量

## Lines
**line.all**
  返回包含所有线条 ID 的数组
**line.copy()**
  克隆线条对象
**line.delete()**
  删除指定线条
**line.get_price()**
  返回价格水平
**line.get_x1()**
  返回 UNIX 时间或柱索引
**line.get_x2()**
  返回 UNIX 时间或柱索引
**line.get_y1()**
  返回线条起点价格
**line.get_y2()**
  返回线条终点价格
**line.new()**
  创建新的线条对象
**line.set_color()**
  设置线条颜色
**line.set_extend()**
  设置延伸类型
**line.set_first_point()**
  设置第一个点
**line.set_second_point()**
  设置第二个点
**line.set_style()**
  设置线条样式
**line.set_width()**
  设置线条宽度
**line.set_x1()**
  设置柱索引或时间
**line.set_x2()**
  设置柱索引或时间
**line.set_xloc()**
  设置 x 位置和显示方式
**line.set_xy1()**
  设置柱索引/时间与价格
**line.set_xy2()**
  设置柱索引/时间与价格
**line.set_y1()**
  设置线条起点价格
**line.set_y2()**
  设置线条终点价格
**line.style_arrow_both**
  [线条](#线条)样式：两端箭头
**line.style_arrow_left**
  [线条](#线条)样式：左箭头
**line.style_arrow_right**
  [线条](#线条)样式：右箭头
**line.style_dashed**
  [线条](#线条)样式：虚线
**line.style_dotted**
  [线条](#线条)样式：点线
**line.style_solid**
  [线条](#线条)样式：实线
**line()**
  将 NA 转换为线条
**linefill.all**
  返回包含所有线段填充 ID 的数组
**linefill.delete()**
  删除指定线段填充
**linefill.get_line1()**
  返回第一条线的 ID
**linefill.get_line2()**
  返回第二条线的 ID
**linefill.new()**
  创建新的线段填充
**linefill.set_color()**
  该函数设置线段填充颜色
**linefill()**
  将 NA 转换为线段填充

## Boxes
**box.all**
  返回包含所有盒子 ID 的数组
**box.copy()**
  克隆盒子对象
**box.delete()**
  删除指定盒子
**box.get_bottom()**
  返回价格值
**box.get_left()**
  返回柱索引
**box.get_right()**
  返回柱索引
**box.get_top()**
  返回价格值
**box.new()**
  创建新的盒子对象
**box.set_bgcolor()**
  设置背景颜色
**box.set_border_color()**
  设置边框颜色
**box.set_border_style()**
  设置边框样式
**box.set_border_width()**
  设置边框宽度
**box.set_bottom_right_point()**
  设置右下角点
**box.set_bottom()**
  设置底部坐标
**box.set_extend()**
  设置延伸类型
**box.set_left()**
  设置左侧坐标
**box.set_lefttop()**
  设置左侧和顶部坐标
**box.set_right()**
  设置右侧坐标
**box.set_rightbottom()**
  设置右侧和底部坐标
**box.set_text_color()**
  该函数设置文本颜色
**box.set_text_font_family()**
  该函数设置文本字体
**box.set_text_formatting()**
  设置文本格式
**box.set_text_halign()**
  该函数设置文本水平对齐方式
**box.set_text_size()**
  该函数设置文本大小
**box.set_text_valign()**
  该函数设置文本垂直对齐方式
**box.set_text_wrap()**
  该函数设置文本换行方式
**box.set_text()**
  该函数设置文本
**box.set_top_left_point()**
  设置左上角点
**box.set_top()**
  设置顶部坐标
**box()**
  将 NA 转换为盒子

## Keywords
**and**
  逻辑与。适用于所有类型
**as**
  
**break**
  
**by**
  
**continue**
  
**else**
  
**enum**
  该关键词允许定义枚举类型
**export**
  在库中使用以导出函数或变量
**for**
  `for` 结构用于循环
**for...in**
  `for...in` 结构用于遍历集合
**if**
  If 语句定义条件逻辑
**import**
  用于加载外部库
**in**
  
**method**
  该关键词用于定义类方法
**not**
  逻辑非（NOT）
**or**
  逻辑或。适用于所有类型
**switch**
  switch 运算符
**to**
  
**type**
  该关键词允许定义新类型
**var**
  **var** 是声明变量的关键词
**varip**
  **varip** (var intra-bar) 声明的变量在每个柱的实时计算中保持其值
**while**
  `while` 语句用于循环

## Colors
**color.aqua**
  命名常量
**color.b()**
  检索蓝色分量值
**color.black**
  命名常量
**color.blue**
  命名常量
**color.from_gradient()**
  基于相对位置在两种颜色之间插值
**color.fuchsia**
  命名常量
**color.g()**
  检索绿色分量值
**color.gray**
  命名常量
**color.green**
  命名常量
**color.lime**
  命名常量
**color.maroon**
  命名常量
**color.navy**
  命名常量
**color.new()**
  颜色应用函数
**color.olive**
  命名常量
**color.orange**
  命名常量
**color.purple**
  命名常量
**color.r()**
  检索红色分量值
**color.red**
  命名常量
**color.rgb()**
  创建新颜色
**color.silver**
  命名常量
**color.t()**
  检索颜色的透明度分量
**color.teal**
  命名常量
**color.white**
  命名常量
**color.yellow**
  命名常量
**color()**
  将 NA 转换为颜色

## Chart Types
**chart.bg_color**
  返回图表背景颜色
**chart.fg_color**
  返回前景色
**chart.is_heikinashi**
  
**chart.is_kagi**
  
**chart.is_linebreak**
  
**chart.is_pnf**
  
**chart.is_range**
  
**chart.is_renko**
  
**chart.is_standard**
  
**chart.left_visible_bar_time**
  [时间](#var_time) 的值，表示图表左边缘可见的最早柱的时间
**chart.point.copy()**
  创建 [chart.point](#chartpoint) 的副本
**chart.point.from_index()**
  返回 [chart.point](#chartpoint) 对象
**chart.point.from_time()**
  返回 [chart.point](#chartpoint) 对象
**chart.point.new()**
  创建新的 [chart.point](#chartpoint)
**chart.point.now()**
  返回 [chart.point](#chartpoint) 对象
**chart.right_visible_bar_time**
  [时间](#var_time) 的值，表示图表右边缘可见的最晚柱的时间

## Currency
**currency.AUD**
  澳元
**currency.BTC**
  比特币
**currency.CAD**
  加元
**currency.CHF**
  瑞士法郎
**currency.ETH**
  以太坊
**currency.EUR**
  欧元
**currency.GBP**
  英镑
**currency.HKD**
  港币
**currency.INR**
  印度卢比
**currency.JPY**
  日元
**currency.KRW**
  韩元
**currency.MYR**
  马来西亚林吉特
**currency.NOK**
  挪威克朗
**currency.NONE**
  未指定货币
**currency.NZD**
  新西兰元
**currency.RUB**
  俄罗斯卢布
**currency.SEK**
  瑞典克朗
**currency.SGD**
  新加坡元
**currency.TRY**
  土耳其里拉
**currency.USD**
  美元
**currency.USDT**
  泰达币
**currency.ZAR**
  南非兰特

## Symbol Info
**syminfo.basecurrency**
  返回包含基础货币的字符串
**syminfo.country**
  返回两字母国家代码
**syminfo.currency**
  返回包含货币的字符串
**syminfo.description**
  标的的描述
**syminfo.employees**
  员工数量
**syminfo.expiration_date**
  UNIX 时间戳表示到期日期
**syminfo.industry**
  返回行业
**syminfo.main_tickerid**
  股票代码标识符
**syminfo.mincontract**
  最小合约数量
**syminfo.minmove**
  返回整数
**syminfo.mintick**
  标的的最小刻度值
**syminfo.pointvalue**
  标的的点值
**syminfo.prefix**
  当前标的的前缀
**syminfo.prefix()**
  返回交易所前缀
**syminfo.pricescale**
  返回整数
**syminfo.recommendations_buy**
  买入评级的分析师数量
**syminfo.recommendations_buy_strong**
  强烈买入评级的分析师数量
**syminfo.recommendations_date**
  评级起始日期
**syminfo.recommendations_hold**
  持有评级的分析师数量
**syminfo.recommendations_sell**
  卖出评级的分析师数量
**syminfo.recommendations_sell_strong**
  强烈卖出评级的分析师数量
**syminfo.recommendations_total**
  总评级数量
**syminfo.root**
  衍生品标的的根代码
**syminfo.sector**
  返回行业板块
**syminfo.session**
  标的交易时段类型
**syminfo.shareholders**
  股东数量
**syminfo.shares_outstanding_float**
  流通股本总数
**syminfo.shares_outstanding_total**
  总股本总数
**syminfo.target_price_average**
  目标价的平均值
**syminfo.target_price_date**
  目标价起始日期
**syminfo.target_price_estimates**
  最新总目标价数量
**syminfo.target_price_high**
  最高目标价
**syminfo.target_price_low**
  最低目标价
**syminfo.target_price_median**
  目标价中位数
**syminfo.ticker**
  不带交易所前缀的标的名称
**syminfo.ticker()**
  返回 `symbol` 名称
**syminfo.tickerid**
  股票代码标识符
**syminfo.timezone**
  交易所时区
**syminfo.type**
  市场类型
**syminfo.volumetype**
  标的成交量类型

## Requests
**adjustment.dividends**
  除息调整常量
**adjustment.none**
  无调整常量
**adjustment.splits**
  除权调整常量
**barmerge.gaps_off**
  请求合并策略：关闭缺口
**barmerge.gaps_on**
  请求合并策略：开启缺口
**barmerge.lookahead_off**
  请求前瞻性合并策略：关闭
**barmerge.lookahead_on**
  请求前瞻性合并策略：开启
**dividends.future_amount**
  返回未来分红金额
**dividends.future_ex_date**
  返回未来除息日
**dividends.future_pay_date**
  返回未来派息日
**dividends.gross**
  毛利的命名常量
**dividends.net**
  净利的命名常量
**earnings.actual**
  实际盈利的命名常量
**earnings.estimate**
  预估盈利的命名常量
**earnings.future_eps**
  返回未来每股收益预估
**earnings.future_period_end_time**
  检查数据
**earnings.future_revenue**
  返回收入预估
**earnings.future_time**
  返回 UNIX 时间戳
**earnings.standardized**
  标准化盈利的命名常量
**request.currency_rate()**
  提供每日汇率
**request.dividends()**
  请求分红数据
**request.earnings()**
  请求盈利数据
**request.economic()**
  请求经济数据
**request.financial()**
  请求财务数据
**request.quandl()**
  *注意：* 此函数已弃用，请改用 `request.economic()`
**request.security_lower_tf()**
  请求较低时间框架的结果
**request.security()**
  请求结果
**request.seed()**
  从种子请求数据
**request.splits()**
  请求除权数据
**splits.denominator**
  除权分母的命名常量
**splits.numerator**
  除权分子的命名常量
**ticker.heikinashi()**
  创建 Heikin-Ashi 股票代码标识符
**ticker.inherit()**
  构建股票代码
**ticker.kagi()**
  创建 Kagi 股票代码标识符
**ticker.linebreak()**
  创建 Line Break 股票代码标识符
**ticker.modify()**
  创建股票代码标识符
**ticker.new()**
  创建股票代码标识符
**ticker.pointfigure()**
  创建 Point & Figure 股票代码标识符
**ticker.renko()**
  创建 Renko 股票代码标识符
**ticker.standard()**
  创建标准股票代码

## Strategy
**strategy.account_currency**
  返回账户货币
**strategy.avg_losing_trade**
  返回亏损交易的平均结果
**strategy.avg_losing_trade_percent**
  返回亏损交易的平均百分比结果
**strategy.avg_trade**
  返回交易的平均结果
**strategy.avg_trade_percent**
  返回交易的平均百分比结果
**strategy.avg_winning_trade**
  返回盈利交易的平均结果
**strategy.avg_winning_trade_percent**
  返回盈利交易的平均百分比结果
**strategy.cancel_all()**
  取消所有挂单
**strategy.cancel()**
  取消挂单或止损单
**strategy.cash**
  这是账户属性之一
**strategy.close_all()**
  创建订单以平仓所有头寸
**strategy.close()**
  创建订单以平仓特定头寸
**strategy.closedtrades**
  已平仓交易数
**strategy.closedtrades.commission()**
  返回所有已平仓交易的佣金总和
**strategy.closedtrades.entry_bar_index()**
  返回进入交易的柱索引
**strategy.closedtrades.entry_comment()**
  返回进入交易的注释
**strategy.closedtrades.entry_id()**
  返回进入交易的 ID
**strategy.closedtrades.entry_price()**
  返回进入交易的价格
**strategy.closedtrades.entry_time()**
  返回进入交易的 UNIX 时间
**strategy.closedtrades.exit_bar_index()**
  返回退出交易的柱索引
**strategy.closedtrades.exit_comment()**
  返回退出交易的注释
**strategy.closedtrades.exit_id()**
  返回退出交易的 ID
**strategy.closedtrades.exit_price()**
  返回退出交易的价格
**strategy.closedtrades.exit_time()**
  返回退出交易的 UNIX 时间
**strategy.closedtrades.first_index**
  索引或交易编号
**strategy.closedtrades.max_drawdown_percent()**
  返回最大亏损百分比
**strategy.closedtrades.max_drawdown()**
  返回最大亏损
**strategy.closedtrades.max_runup_percent()**
  返回最大盈利百分比
**strategy.closedtrades.max_runup()**
  返回最大盈利
**strategy.closedtrades.profit_percent()**
  返回盈亏百分比
**strategy.closedtrades.profit()**
  返回盈亏
**strategy.closedtrades.size()**
  返回方向
**strategy.commission.cash_per_contract**
  按合约计算佣金的类型
**strategy.commission.cash_per_order**
  按订单计算佣金的类型
**strategy.commission.percent**
  按百分比计算佣金的类型
**strategy.convert_to_account()**
  将值转换为账户货币
**strategy.convert_to_symbol()**
  将值转换为标的货币
**strategy.default_entry_qty()**
  计算默认入场数量
**strategy.direction.all**
  允许策略在所有方向上交易
**strategy.direction.long**
  允许策略在多头方向上交易
**strategy.direction.short**
  允许策略在空头方向上交易
**strategy.entry()**
  创建新的入场订单
**strategy.equity**
  当前权益（[strategy.cash](#strategycash) + 浮动盈亏）
**strategy.eventrades**
  保本交易数
**strategy.exit()**
  创建基于价格的退出订单
**strategy.fixed**
  这是账户属性之一
**strategy.grossloss**
  总货币价值
**strategy.grossloss_percent**
  总亏损百分比
**strategy.grossprofit**
  总货币价值
**strategy.grossprofit_percent**
  总盈利百分比
**strategy.initial_capital**
  初始资金
**strategy.long**
  多头的命名常量
**strategy.losstrades**
  亏损交易数
**strategy.margin_liquidation_price**
  启用保证金时显示
**strategy.max_contracts_held_all**
  所有交易中持有的最大合约数
**strategy.max_contracts_held_long**
  多头交易中持有的最大合约数
**strategy.max_contracts_held_short**
  空头交易中持有的最大合约数
**strategy.max_drawdown**
  最大权益回撤
**strategy.max_drawdown_percent**
  最大权益回撤百分比
**strategy.max_runup**
  最大权益增长
**strategy.max_runup_percent**
  最大权益增长百分比
**strategy.netprofit**
  总货币价值
**strategy.netprofit_percent**
  总盈利百分比
**strategy.oca.cancel**
  订单组合类型：取消其他订单
**strategy.oca.none**
  订单组合类型：无
**strategy.oca.reduce**
  订单组合类型：减少其他订单
**strategy.openprofit**
  当前未实现盈亏
**strategy.openprofit_percent**
  当前未实现盈亏百分比
**strategy.opentrades**
  未平仓交易数
**strategy.opentrades.capital_held**
  返回占用资金
**strategy.opentrades.commission()**
  返回所有未平仓交易的佣金总和
**strategy.opentrades.entry_bar_index()**
  返回进入交易的柱索引
**strategy.opentrades.entry_comment()**
  返回进入交易的注释
**strategy.opentrades.entry_id()**
  返回进入交易的 ID
**strategy.opentrades.entry_price()**
  返回进入交易的价格
**strategy.opentrades.entry_time()**
  返回进入交易的 UNIX 时间
**strategy.opentrades.max_drawdown_percent()**
  返回最大回撤百分比
**strategy.opentrades.max_drawdown()**
  返回最大回撤
**strategy.opentrades.max_runup_percent()**
  返回最大盈利百分比
**strategy.opentrades.max_runup()**
  返回最大盈利
**strategy.opentrades.profit_percent()**
  返回盈亏百分比
**strategy.opentrades.profit()**
  返回盈亏
**strategy.opentrades.size()**
  返回方向
**strategy.order()**
  创建新订单
**strategy.percent_of_equity**
  这是账户属性之一
**strategy.position_avg_price**
  平均入场价格
**strategy.position_entry_name**
  导致当前头寸的订单名称
**strategy.position_size**
  头寸方向和大小
**strategy.risk.allow_entry_in()**
  此函数可用于限制策略只能在特定条件下进入交易
**strategy.risk.max_cons_loss_days()**
  此函数的目的
**strategy.risk.max_drawdown()**
  此函数的目的
**strategy.risk.max_intraday_filled_orders()**
  此函数的目的
**strategy.risk.max_intraday_loss()**
  最大亏损值
**strategy.risk.max_position_size()**
  此函数的目的
**strategy.short**
  空头的命名常量
**strategy.wintrades**
  盈利交易数
**strategy()**
  此声明开始策略的定义
``` 

此Markdown格式文档完整保留了原始手册的层级结构，并完成了所有注释部分的翻译。翻译遵循了技术文档的准确性原则，同时保持了代码关键词的原文不变，便于开发者对照查询。


```markdown
# Pine Script Cheatsheet

## Types
**array**
  关键词用于声明数组类型
**bool**
  关键词用于声明布尔类型
**box**
  关键词用于声明盒子类型
**chart.point**
  关键词用于声明图表点类型
**color**
  关键词用于声明颜色类型
**const**
  `const` 关键词用于声明常量
**float**
  关键词用于声明浮点数类型
**int**
  关键词用于声明整数类型
**label**
  关键词用于声明标签类型
**line**
  关键词用于声明线条类型
**linefill**
  关键词用于声明线段填充类型
**map**
  关键词用于声明映射类型
**matrix**
  关键词用于声明矩阵类型
**polyline**
  关键词用于声明折线类型
**series**
  `series` 关键词用于声明序列类型
**simple**
  `simple` 关键词用于声明简单类型
**string**
  关键词用于声明字符串类型
**table**
  关键词用于声明表格类型

## Operators
**-**
  减法或一元负号
**-=**
  减法赋值
**:=**
  重新赋值运算符
**!=**
  不等于。适用于所有类型
**?:**
  三元条件运算符
**[]**
  系列下标。用于访问系列数据
**\***
  乘法。适用于数值类型
**\*=**
  乘法赋值
**/**
  除法。适用于数值类型
**/=**
  除法赋值
**%**
  取模（整数余数）
**%=**
  取模赋值
**+**
  加法或一元正号
**+=**
  加法赋值
**<**
  小于。适用于数值类型
**<=**
  小于或等于
**==**
  等于。适用于所有类型
**=>**
  `=>` 运算符用于函数定义
**>**
  大于。适用于数值类型
**>=**
  大于或等于

## Strings
**str.contains()**
  如果字符串包含子字符串则返回 true
**str.endswith()**
  如果字符串以指定后缀结尾则返回 true
**str.format_time()**
  将 `time` 转换为格式化时间字符串
**str.format()**
  格式化字符串
**str.length()**
  返回字符串长度（整数）
**str.lower()**
  返回小写形式的新字符串
**str.match()**
  返回匹配后的新子字符串
**str.pos()**
  返回子字符串的位置
**str.repeat()**
  构造重复多次的新字符串
**str.replace_all()**
  替换所有出现的子字符串
**str.replace()**
  返回替换后的新字符串
**str.split()**
  将字符串分割为数组
**str.startswith()**
  如果字符串以指定前缀开头则返回 true
**str.substring()**
  返回子字符串的新字符串
**str.tonumber()**
  将值转换为数字
**str.tostring()**
  转换为字符串
**str.trim()**
  构造去除空白的新字符串
**str.upper()**
  返回大写形式的新字符串
**strategy.close_all()**
  创建订单以平仓所有头寸
**string()**
  将 NA 转换为字符串

## Maths
**math.abs()**
  `n` 的绝对值
**math.acos()**
  反余弦函数
**math.asin()**
  反正弦函数
**math.atan()**
  反正切函数
**math.avg()**
  计算平均值
**math.ceil()**
  向上取整
**math.cos()**
  余弦函数
**math.e**
  数学常数 e
**math.exp()**
  指数函数
**math.floor()**
  向下取整
**math.log()**
  自然对数
**math.log10()**
  以 10 为底的对数
**math.max()**
  返回最大值
**math.min()**
  返回最小值
**math.phi**
  黄金分割比例常数
**math.pi**
  圆周率常数
**math.pow()**
  幂函数
**math.random()**
  返回伪随机数
**math.round_to_mintick()**
  按最小刻度四舍五入
**math.round()**
  四舍五入
**math.rphi**
  黄金分割比例的倒数
**math.sign()**
  符号函数
**math.sin()**
  正弦函数
**math.sqrt()**
  平方根
**math.sum()**
  求和函数
**math.tan()**
  正切函数
**math.todegrees()**
  弧度转角度
**math.toradians()**
  角度转弧度
**na**
  表示缺失值的关键词

## Bar State
**barstate.isconfirmed**
  如果当前柱已确认则返回 true
**barstate.isfirst**
  如果是当前图表的第一个柱则返回 true
**barstate.ishistory**
  如果是历史柱则返回 true
**barstate.islast**
  如果是当前图表的最后一个柱则返回 true
**barstate.islastconfirmedhistory**
  如果脚本执行时当前柱是最后一个确认的历史柱则返回 true
**barstate.isnew**
  如果是新柱则返回 true
**barstate.isrealtime**
  如果是实时柱则返回 true

## Plotting
**barcolor()**
  设置柱状图颜色
**bgcolor()**
  填充背景
**display.all**
  显示所有内容
**display.data_window**
  仅显示数据窗口
**display.none**
  不显示
**display.pane**
  仅显示当前面板
**display.price_scale**
  仅显示价格轴
**display.status_line**
  仅显示状态栏
**fill()**
  填充背景区域
**hline.style_dashed**
  水平线样式：虚线
**hline.style_dotted**
  水平线样式：点线
**hline.style_solid**
  水平线样式：实线
**hline()**
  绘制水平线
**plot.style_area**
  面积图样式
**plot.style_areabr**
  面积柱状图样式
**plot.style_circles**
  圆点样式
**plot.style_columns**
  柱状图样式
**plot.style_cross**
  十字交叉样式
**plot.style_histogram**
  直方图样式
**plot.style_line**
  折线图样式
**plot.style_linebr**
  断线样式
**plot.style_stepline**
  阶梯线样式
**plot.style_stepline_diamond**
  钻石阶梯线样式
**plot.style_steplinebr**
  阶梯断线样式
**plot()**
  绘制数据系列
**plotarrow()**
  绘制上下箭头
**plotbar()**
  在图表上绘制 OHLC 柱状图
**plotcandle()**
  在图表上绘制蜡烛图
**plotchar()**
  绘制视觉形状
**plotshape()**
  绘制视觉形状
**shape.arrowdown**
  箭头向下形状
**shape.arrowup**
  箭头向上形状
**shape.circle**
  圆形形状
**shape.cross**
  十字形形状
**shape.diamond**
  菱形形状
**shape.flag**
  旗帜形状
**shape.labeldown**
  向下标签形状
**shape.labelup**
  向上标签形状
**shape.square**
  方形形状
**shape.triangledown**
  三角形向下形状
**shape.triangleup**
  三角形向上形状
**shape.xcross**
  X 形交叉形状

## Indicators
**ta.accdist**
  累积/派发指标
**ta.alma()**
  阿尔诺·勒格克斯移动平均线
**ta.atr()**
  平均真实波幅函数
**ta.barssince()**
  计算自条件满足以来的柱数
**ta.bb()**
  布林带。技术分析指标
**ta.bbw()**
  布林带宽度
**ta.cci()**
  商品通道指数
**ta.change()**
  比较当前值与前一值的变化
**ta.cmo()**
  钱德动量振荡器
**ta.cog()**
  重心指标
**ta.correlation()**
  相关系数
**ta.cross()**
  
**ta.crossover()**
  当 `source1` 系列上穿 `source2` 系列时返回 true
**ta.crossunder()**
  当 `source1` 系列下穿 `source2` 系列时返回 true
**ta.cum()**
  累积（总计）值
**ta.dev()**
  差异度量
**ta.dmi()**
  DMI 函数返回方向移动指标
**ta.ema()**
  EMA 函数返回指数移动平均线
**ta.falling()**
  测试 `source` 是否正在下跌
**ta.highest()**
  指定周期内的最高值
**ta.highestbars()**
  指定周期内最高值的偏移量
**ta.hma()**
  HMA 函数返回哈拉尔移动平均线
**ta.iii**
  盘中强度指标
**ta.kc()**
  凯尔特纳通道。技术分析指标
**ta.kcw()**
  凯尔特纳通道宽度
**ta.linreg()**
  线性回归曲线
**ta.lowest()**
  指定周期内的最低值
**ta.lowestbars()**
  指定周期内最低值的偏移量
**ta.macd()**
  MACD（移动平均线收敛/发散）
**ta.max()**
  返回历史最高值
**ta.median()**
  返回中位数
**ta.mfi()**
  资金流量指标
**ta.min()**
  返回历史最低值
**ta.mode()**
  返回[众数](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Type_system.html#mode)
**ta.mom()**
  `source` 的动量
**ta.nvi**
  负成交量指标
**ta.obv**
  能量潮指标
**ta.percentile_linear_interpolation()**
  计算百分位数（线性插值）
**ta.percentile_nearest_rank()**
  计算百分位数（最近排名）
**ta.percentrank()**
  百分位排名是值的排名在数据集中所占的百分比
**ta.pivot_point_levels()**
  计算枢轴点水平
**ta.pivothigh()**
  该函数返回枢轴高点
**ta.pivotlow()**
  该函数返回枢轴低点
**ta.pvi**
  正成交量指标
**ta.pvt**
  价格-成交量趋势
**ta.range()**
  返回 `high` 与 `low` 之间的差值
**ta.rci()**
  计算秩相关指数
**ta.rising()**
  测试 `source` 是否正在上涨
**ta.rma()**
  移动平均线，用于计算 RSI
**ta.roc()**
  计算百分比变化率
**ta.rsi()**
  相对强弱指数
**ta.sar()**
  抛物线 SAR（抛物线转向指标）
**ta.sma()**
  SMA 函数返回简单移动平均线
**ta.stdev()**
  
**ta.stoch()**
  随机指标。它是一种动量指标
**ta.supertrend()**
  超级趋势指标
**ta.swma()**
  对称加权移动平均线
**ta.tr**
  真实波幅，等同于
**ta.tr()**
  计算当前真实波幅
**ta.tsi()**
  真实强度指数
**ta.valuewhen()**
  返回 `source` 在 `condition` 为 true 时的值
**ta.variance()**
  方差是期望的平方差
**ta.vwap**
  成交量加权平均价格
**ta.vwap()**
  成交量加权平均价格
**ta.vwma()**
  VWMA 函数返回成交量加权移动平均线
**ta.wad**
  威廉姆斯累积/派发指标
**ta.wma()**
  WMA 函数返回加权移动平均线
**ta.wpr()**
  威廉姆斯 %R。振荡器
**ta.wvad**
  威廉姆斯可变累积/派发指标
**table.all**
  返回填充了表引用 ID 的数组
**table.cell_set_bgcolor()**
  该函数设置单元格背景颜色
**table.cell_set_height()**
  该函数设置单元格高度
**table.cell_set_text_color()**
  该函数设置单元格文本颜色
**table.cell_set_text_font_family()**
  该函数设置单元格文本字体
**table.cell_set_text_formatting()**
  设置单元格文本格式
**table.cell_set_text_halign()**
  该函数设置单元格文本水平对齐方式
**table.cell_set_text_size()**
  该函数设置单元格文本大小
**table.cell_set_text_valign()**
  该函数设置单元格文本垂直对齐方式
**table.cell_set_text()**
  该函数设置单元格文本
**table.cell_set_tooltip()**
  该函数设置单元格工具提示
**table.cell_set_width()**
  该函数设置单元格宽度
**table.cell()**
  该函数定义单元格
**table.clear()**
  该函数移除表中的所有单元格
**table.delete()**
  该函数删除表
**table.merge_cells()**
  该函数合并单元格
**table.new()**
  该函数创建新表
**table.set_bgcolor()**
  该函数设置表背景颜色
**table.set_border_color()**
  该函数设置表边框颜色
**table.set_border_width()**
  该函数设置表边框宽度
**table.set_frame_color()**
  该函数设置表框架颜色
**table.set_frame_width()**
  该函数设置表框架宽度
**table.set_position()**
  该函数设置表位置
**table()**
  将 NA 转换为表格

## Inputs
**input.bool()**
  添加布尔输入到脚本
**input.color()**
  添加颜色输入到脚本
**input.enum()**
  添加枚举输入到脚本
**input.float()**
  添加浮点数输入到脚本
**input.int()**
  添加整数输入到脚本
**input.price()**
  添加价格输入到脚本
**input.session()**
  添加会话输入到脚本
**input.source()**
  添加源输入到脚本
**input.string()**
  添加字符串输入到脚本
**input.symbol()**
  添加符号输入到脚本
**input.text_area()**
  添加文本区域输入到脚本
**input.time()**
  添加时间输入到脚本
**input.timeframe()**
  添加时间框架输入到脚本
**input()**
  添加输入到脚本

## Polylines
**polyline.all**
  返回包含所有多边形 ID 的数组
**polyline.delete()**
  删除指定的多边形
**polyline.new()**
  创建新的[多边形](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Polylines.html)

## Alerts
**alert.freq_all**
  每次脚本执行时都触发警报
**alert.freq_once_per_bar**
  每个柱触发一次警报
**alert.freq_once_per_bar_close**
  在柱关闭时触发警报
**alert()**
  创建警报触发器
**alertcondition()**
  创建警报条件

## Sessions
**session.extended**
  扩展会话的常量
**session.isfirstbar**
  如果当前柱是第一个扩展会话柱则返回 [true](#const)
**session.isfirstbar_regular**
  如果当前柱是第一个常规会话柱则返回 [true](#const)
**session.islastbar**
  如果当前柱是最后一个扩展会话柱则返回 [true](#const)
**session.islastbar_regular**
  如果当前柱是最后一个常规会话柱则返回 [true](#const)
**session.ismarket**
  如果当前柱在常规交易时段内则返回 [true](#const)
**session.ispostmarket**
  如果当前柱在盘后交易时段则返回 [true](#const)
**session.ispremarket**
  如果当前柱在盘前交易时段则返回 [true](#const)
**session.regular**
  常规会话的常量

## Timeframe
**timeframe.change()**
  检测时间框架变化
**timeframe.from_seconds()**
  将秒数转换为时间框架
**timeframe.in_seconds()**
  将时间框架转换为秒数
**timeframe.isdaily**
  如果当前时间框架是日线则返回 true
**timeframe.isdwm**
  如果当前时间框架是日/周/月则返回 true
**timeframe.isintraday**
  如果当前时间框架是分钟线则返回 true
**timeframe.isminutes**
  如果当前时间框架是分钟线则返回 true
**timeframe.ismonthly**
  如果当前时间框架是月线则返回 true
**timeframe.isseconds**
  如果当前时间框架是秒线则返回 true
**timeframe.isticks**
  如果当前时间框架是 ticks 则返回 true
**timeframe.isweekly**
  如果当前时间框架是周线则返回 true
**timeframe.main_period**
  主要周期的字符串表示
**timeframe.multiplier**
  分辨率的乘数
**timeframe.period**
  时间段的字符串表示

## Annotations
**@description**
  设置自定义描述
**@enum**
  如果放置在枚举上方
**@field**
  如果放置在[表格单元格](#表格)上方
**@function**
  如果放置在函数上方
**@param**
  如果放置在函数参数上方
**@returns**
  如果放置在函数返回值上方
**@strategy_alert_message**
  如果在[策略](#策略)中用于为警报添加自定义消息
**@type**
  如果放置在类型声明上方
**@variable**
  如果放置在变量声明上方
**@version=**
  指定 Pine Script 版本

## Bar Data
**bar_index**
  当前柱的索引。数值类型
**close**
  当前柱的收盘价
**high**
  当前柱的最高价
**low**
  当前柱的最低价
**open**
  当前柱的开盘价
**volume**
  当前柱的成交量

## Arrays
**array.abs()**
  返回包含数组元素绝对值的新数组
**array.avg()**
  该函数返回数组元素的平均值
**array.binary_search_leftmost()**
  该函数返回使用二分搜索找到最左匹配项的索引
**array.binary_search_rightmost()**
  该函数返回使用二分搜索找到最右匹配项的索引
**array.binary_search()**
  该函数返回使用二分搜索找到匹配项的索引
**array.clear()**
  该函数移除数组中的所有元素
**array.concat()**
  该函数用于合并多个数组
**array.copy()**
  该函数创建数组的副本
**array.covariance()**
  该函数返回数组元素的协方差
**array.every()**
  如果数组中所有元素都满足条件则返回 [true](#const)
**array.fill()**
  该函数设置数组元素的值
**array.first()**
  返回数组的第一个元素
**array.from()**
  该函数从值列表创建数组
**array.get()**
  该函数返回数组元素
**array.includes()**
  该函数返回数组是否包含指定元素
**array.indexof()**
  该函数返回数组中第一个匹配项的索引
**array.insert()**
  该函数更改数组
**array.join()**
  该函数创建由数组元素连接而成的新字符串
**array.last()**
  返回数组的最后一个元素
**array.lastindexof()**
  该函数返回数组中最后一个匹配项的索引
**array.max()**
  该函数返回数组元素的最大值
**array.median()**
  该函数返回数组元素的中位数
**array.min()**
  该函数返回数组元素的最小值
**array.mode()**
  该函数返回数组元素的[众数]
**array.new_bool()**
  该函数创建布尔数组
**array.new_box()**
  该函数创建盒子数组
**array.new_color()**
  该函数创建颜色数组
**array.new_float()**
  该函数创建浮点数数组
**array.new_int()**
  该函数创建整数数组
**array.new_label()**
  该函数创建标签数组
**array.new_line()**
  该函数创建线条数组
**array.new_linefill()**
  该函数创建线段填充数组
**array.new_string()**
  该函数创建字符串数组
**array.new_table()**
  该函数创建表格数组
**array.new<type>()**
  该函数创建类型数组
**array.percentile_linear_interpolation()**
  返回线性插值的百分位数值
**array.percentile_nearest_rank()**
  返回最近排名的百分位数值
**array.percentrank()**
  返回数组元素的百分位排名
**array.pop()**
  该函数移除数组的最后一个元素
**array.push()**
  该函数向数组末尾添加元素
**array.range()**
  该函数返回数组元素的范围
**array.remove()**
  该函数更改数组
**array.reverse()**
  该函数反转数组
**array.set()**
  该函数设置数组元素的值
**array.shift()**
  该函数移除数组的第一个元素
**array.size()**
  该函数返回数组长度
**array.slice()**
  该函数创建数组的子数组
**array.some()**
  如果数组中至少有一个元素满足条件则返回 [true](#const)
**array.sort_indices()**
  返回按元素值排序后的索引数组
**array.sort()**
  该函数对数组进行排序
**array.standardize()**
  该函数返回数组元素的标准化值
**array.stdev()**
  该函数返回数组元素的标准差
**array.sum()**
  该函数返回数组元素的总和
**array.unshift()**
  该函数向数组开头添加元素
**array.variance()**
  该函数返回数组元素的方差

## Matrixes
**matrix.add_col()**
  该函数添加列
**matrix.add_row()**
  该函数添加行
**matrix.avg()**
  该函数计算平均值
**matrix.col()**
  该函数创建列向量
**matrix.columns()**
  该函数返回列数
**matrix.concat()**
  该函数追加矩阵
**matrix.copy()**
  该函数创建副本
**matrix.det()**
  该函数返回行列式
**matrix.diff()**
  该函数返回差分
**matrix.eigenvalues()**
  该函数返回特征值
**matrix.eigenvectors()**
  返回特征向量矩阵
**matrix.elements_count()**
  该函数返回元素总数
**matrix.fill()**
  该函数填充矩阵
**matrix.get()**
  该函数返回元素
**matrix.inv()**
  该函数返回逆矩阵
**matrix.is_antidiagonal()**
  该函数判断是否为反方向对角矩阵
**matrix.is_antisymmetric()**
  该函数判断是否为反对称矩阵
**matrix.is_binary()**
  该函数判断是否为二进制矩阵
**matrix.is_diagonal()**
  该函数判断是否为对角矩阵
**matrix.is_identity()**
  该函数判断是否为单元矩阵
**matrix.is_square()**
  该函数判断是否为方阵
**matrix.is_stochastic()**
  该函数判断是否为随机矩阵
**matrix.is_symmetric()**
  该函数判断是否为对称矩阵
**matrix.is_triangular()**
  该函数判断是否为三角矩阵
**matrix.is_zero()**
  该函数判断是否为零矩阵
**matrix.kron()**
  该函数返回克罗内克积
**matrix.max()**
  该函数返回最大值
**matrix.median()**
  该函数计算中位数
**matrix.min()**
  该函数返回最小值
**matrix.mode()**
  该函数计算众数
**matrix.mult()**
  该函数返回乘积
**matrix.new<type>()**
  该函数创建类型矩阵
**matrix.pinv()**
  该函数返回伪逆矩阵
**matrix.pow()**
  该函数计算幂
**matrix.rank()**
  该函数计算秩
**matrix.remove_col()**
  该函数移除列
**matrix.remove_row()**
  该函数移除行
**matrix.reshape()**
  该函数重建矩阵形状
**matrix.reverse()**
  该函数反转矩阵
**matrix.row()**
  该函数创建行向量
**matrix.rows()**
  该函数返回行数
**matrix.set()**
  该函数赋值元素
**matrix.sort()**
  该函数重新排列矩阵
**matrix.submatrix()**
  该函数提取子矩阵
**matrix.sum()**
  该函数返回总和
**matrix.swap_columns()**
  该函数交换列
**matrix.swap_rows()**
  该函数交换行
**matrix.trace()**
  该函数计算迹
**matrix.transpose()**
  该函数创建转置矩阵

## Datetime
**dayofmonth**
  当前柱的日期。数值类型
**dayofmonth()**
**dayofweek**
  当前柱的星期几。数值类型
**dayofweek.friday**
  常量，星期五
**dayofweek.monday**
  常量，星期一
**dayofweek.saturday**
  常量，星期六
**dayofweek.sunday**
  常量，星期日
**dayofweek.thursday**
  常量，星期四
**dayofweek.tuesday**
  常量，星期二
**dayofweek.wednesday**
  常量，星期三
**dayofweek()**
**hour**
  当前柱的小时。数值类型
**hour()**
**minute**
  当前柱的分钟。数值类型
**minute()**
**month**
  当前柱的月份。数值类型
**month()**
**second**
  当前柱的秒。数值类型
**second()**
**time**
  当前柱的时间（UNIX 时间戳）。数值类型
**time_close**
  当前柱的收盘时间
**time_tradingday**
  当前交易日的开始时间
**timenow**
  当前时间（UNIX 时间戳）。数值类型
**weekofyear**
  当前柱的周数。数值类型
**weekofyear()**
**year**
  当前柱的年份。数值类型
**year()**

## Labels
**label.all**
  返回包含所有标签 ID 的数组
**label.copy()**
  克隆标签对象
**label.delete()**
  删除指定标签
**label.get_text()**
  返回标签文本
**label.get_x()**
  返回 UNIX 时间或柱索引
**label.get_y()**
  返回此标签的价格
**label.new()**
  创建新的标签对象
**label.set_color()**
  设置标签边框和文本颜色
**label.set_point()**
  设置标签位置
**label.set_size()**
  设置箭头和文本大小
**label.set_style()**
  设置标签样式
**label.set_text_font_family()**
  该函数设置标签文本字体
**label.set_text_formatting()**
  设置文本格式
**label.set_text()**
  设置标签文本
**label.set_textalign()**
  设置文本对齐方式
**label.set_textcolor()**
  设置标签文本颜色
**label.set_tooltip()**
  设置工具提示文本
**label.set_x()**
  设置柱索引或时间
**label.set_xloc()**
  设置 x 位置和显示方式
**label.set_xy()**
  设置柱索引/时间与价格
**label.set_y()**
  设置标签价格
**label.set_yloc()**
  设置新的 y 位置
**label.style_arrowdown**
  [标签](#标签)样式：向下箭头
**label.style_arrowup**
  [标签](#标签)样式：向上箭头
**label.style_circle**
  [标签](#标签)样式：圆形
**label.style_cross**
  [标签](#标签)样式：十字形
**label.style_diamond**
  [标签](#标签)样式：菱形
**label.style_flag**
  [标签](#标签)样式：旗帜
**label.style_label_center**
  [标签](#标签)样式：居中标签
**label.style_label_down**
  [标签](#标签)样式：向下标签
**label.style_label_left**
  [标签](#标签)样式：向左标签
**label.style_label_lower_left**
  [标签](#标签)样式：左下标签
**label.style_label_lower_right**
  [标签](#标签)样式：右下标签
**label.style_label_right**
  [标签](#标签)样式：向右标签
**label.style_label_up**
  [标签](#标签)样式：向上标签
**label.style_label_upper_left**
  [标签](#标签)样式：左上标签
**label.style_label_upper_right**
  [标签](#标签)样式：右上标签
**label.style_none**
  [标签](#标签)样式：无
**label.style_square**
  [标签](#标签)样式：方形
**label.style_text_outline**
  [标签](#标签)样式：文本轮廓
**label.style_triangledown**
  [标签](#标签)样式：向下三角形
**label.style_triangleup**
  [标签](#标签)样式：向上三角形
**label.style_xcross**
  [标签](#标签)样式：X 形交叉
**label()**
  将 NA 转换为标签
**yloc.abovebar**
  位于柱上方的命名常量
**yloc.belowbar**
  位于柱下方的命名常量
**yloc.price**
  位于价格轴上的命名常量

## Lines
**line.all**
  返回包含所有线条 ID 的数组
**line.copy()**
  克隆线条对象
**line.delete()**
  删除指定线条
**line.get_price()**
  返回价格水平
**line.get_x1()**
  返回 UNIX 时间或柱索引
**line.get_x2()**
  返回 UNIX 时间或柱索引
**line.get_y1()**
  返回线条起点价格
**line.get_y2()**
  返回线条终点价格
**line.new()**
  创建新的线条对象
**line.set_color()**
  设置线条颜色
**line.set_extend()**
  设置延伸类型
**line.set_first_point()**
  设置第一个点
**line.set_second_point()**
  设置第二个点
**line.set_style()**
  设置线条样式
**line.set_width()**
  设置线条宽度
**line.set_x1()**
  设置柱索引或时间
**line.set_x2()**
  设置柱索引或时间
**line.set_xloc()**
  设置 x 位置和显示方式
**line.set_xy1()**
  设置柱索引/时间与价格
**line.set_xy2()**
  设置柱索引/时间与价格
**line.set_y1()**
  设置线条起点价格
**line.set_y2()**
  设置线条终点价格
**line.style_arrow_both**
  [线条](#线条)样式：两端箭头
**line.style_arrow_left**
  [线条](#线条)样式：左箭头
**line.style_arrow_right**
  [线条](#线条)样式：右箭头
**line.style_dashed**
  [线条](#线条)样式：虚线
**line.style_dotted**
  [线条](#线条)样式：点线
**line.style_solid**
  [线条](#线条)样式：实线
**line()**
  将 NA 转换为线条
**linefill.all**
  返回包含所有线段填充 ID 的数组
**linefill.delete()**
  删除指定线段填充
**linefill.get_line1()**
  返回第一条线的 ID
**linefill.get_line2()**
  返回第二条线的 ID
**linefill.new()**
  创建新的线段填充
**linefill.set_color()**
  该函数设置线段填充颜色
**linefill()**
  将 NA 转换为线段填充

## Boxes
**box.all**
  返回包含所有盒子 ID 的数组
**box.copy()**
  克隆盒子对象
**box.delete()**
  删除指定盒子
**box.get_bottom()**
  返回价格值
**box.get_left()**
  返回柱索引
**box.get_right()**
  返回柱索引
**box.get_top()**
  返回价格值
**box.new()**
  创建新的盒子对象
**box.set_bgcolor()**
  设置背景颜色
**box.set_border_color()**
  设置边框颜色
**box.set_border_style()**
  设置边框样式
**box.set_border_width()**
  设置边框宽度
**box.set_bottom_right_point()**
  设置右下角点
**box.set_bottom()**
  设置底部坐标
**box.set_extend()**
  设置延伸类型
**box.set_left()**
  设置左侧坐标
**box.set_lefttop()**
  设置左侧和顶部坐标
**box.set_right()**
  设置右侧坐标
**box.set_rightbottom()**
  设置右侧和底部坐标
**box.set_text_color()**
  该函数设置文本颜色
**box.set_text_font_family()**
  该函数设置文本字体
**box.set_text_formatting()**
  设置文本格式
**box.set_text_halign()**
  该函数设置文本水平对齐方式
**box.set_text_size()**
  该函数设置文本大小
**box.set_text_valign()**
  该函数设置文本垂直对齐方式
**box.set_text_wrap()**
  该函数设置文本换行方式
**box.set_text()**
  该函数设置文本
**box.set_top_left_point()**
  设置左上角点
**box.set_top()**
  设置顶部坐标
**box()**
  将 NA 转换为盒子

## Keywords
**and**
  逻辑与。适用于所有类型
**as**
  
**break**
  
**by**
  
**continue**
  
**else**
  
**enum**
  该关键词允许定义枚举类型
**export**
  在库中使用以导出函数或变量
**for**
  `for` 结构用于循环
**for...in**
  `for...in` 结构用于遍历集合
**if**
  If 语句定义条件逻辑
**import**
  用于加载外部库
**in**
  
**method**
  该关键词用于定义类方法
**not**
  逻辑非（NOT）
**or**
  逻辑或。适用于所有类型
**switch**
  switch 运算符
**to**
  
**type**
  该关键词允许定义新类型
**var**
  **var** 是声明变量的关键词
**varip**
  **varip** (var intra-bar) 声明的变量在每个柱的实时计算中保持其值
**while**
  `while` 语句用于循环

## Colors
**color.aqua**
  命名常量
**color.b()**
  检索蓝色分量值
**color.black**
  命名常量
**color.blue**
  命名常量
**color.from_gradient()**
  基于相对位置在两种颜色之间插值
**color.fuchsia**
  命名常量
**color.g()**
  检索绿色分量值
**color.gray**
  命名常量
**color.green**
  命名常量
**color.lime**
  命名常量
**color.maroon**
  命名常量
**color.navy**
  命名常量
**color.new()**
  颜色应用函数
**color.olive**
  命名常量
**color.orange**
  命名常量
**color.purple**
  命名常量
**color.r()**
  检索红色分量值
**color.red**
  命名常量
**color.rgb()**
  创建新颜色
**color.silver**
  命名常量
**color.t()**
  检索颜色的透明度分量
**color.teal**
  命名常量
**color.white**
  命名常量
**color.yellow**
  命名常量
**color()**
  将 NA 转换为颜色

## Chart Types
**chart.bg_color**
  返回图表背景颜色
**chart.fg_color**
  返回前景色
**chart.is_heikinashi**
  
**chart.is_kagi**
  
**chart.is_linebreak**
  
**chart.is_pnf**
  
**chart.is_range**
  
**chart.is_renko**
  
**chart.is_standard**
  
**chart.left_visible_bar_time**
  [时间](#var_time) 的值，表示图表左边缘可见的最早柱的时间
**chart.point.copy()**
  创建 [chart.point](#chartpoint) 的副本
**chart.point.from_index()**
  返回 [chart.point](#chartpoint) 对象
**chart.point.from_time()**
  返回 [chart.point](#chartpoint) 对象
**chart.point.new()**
  创建新的 [chart.point](#chartpoint)
**chart.point.now()**
  返回 [chart.point](#chartpoint) 对象
**chart.right_visible_bar_time**
  [时间](#var_time) 的值，表示图表右边缘可见的最晚柱的时间

## Currency
**currency.AUD**
  澳元
**currency.BTC**
  比特币
**currency.CAD**
  加元
**currency.CHF**
  瑞士法郎
**currency.ETH**
  以太坊
**currency.EUR**
  欧元
**currency.GBP**
  英镑
**currency.HKD**
  港币
**currency.INR**
  印度卢比
**currency.JPY**
  日元
**currency.KRW**
  韩元
**currency.MYR**
  马来西亚林吉特
**currency.NOK**
  挪威克朗
**currency.NONE**
  未指定货币
**currency.NZD**
  新西兰元
**currency.RUB**
  俄罗斯卢布
**currency.SEK**
  瑞典克朗
**currency.SGD**
  新加坡元
**currency.TRY**
  土耳其里拉
**currency.USD**
  美元
**currency.USDT**
  泰达币
**currency.ZAR**
  南非兰特

## Symbol Info
**syminfo.basecurrency**
  返回包含基础货币的字符串
**syminfo.country**
  返回两字母国家代码
**syminfo.currency**
  返回包含货币的字符串
**syminfo.description**
  标的的描述
**syminfo.employees**
  员工数量
**syminfo.expiration_date**
  UNIX 时间戳表示到期日期
**syminfo.industry**
  返回行业
**syminfo.main_tickerid**
  股票代码标识符
**syminfo.mincontract**
  最小合约数量
**syminfo.minmove**
  返回整数
**syminfo.mintick**
  标的的最小刻度值
**syminfo.pointvalue**
  标的的点值
**syminfo.prefix**
  当前标的的前缀
**syminfo.prefix()**
  返回交易所前缀
**syminfo.pricescale**
  返回整数
**syminfo.recommendations_buy**
  买入评级的分析师数量
**syminfo.recommendations_buy_strong**
  强烈买入评级的分析师数量
**syminfo.recommendations_date**
  评级起始日期
**syminfo.recommendations_hold**
  持有评级的分析师数量
**syminfo.recommendations_sell**
  卖出评级的分析师数量
**syminfo.recommendations_sell_strong**
  强烈卖出评级的分析师数量
**syminfo.recommendations_total**
  总评级数量
**syminfo.root**
  衍生品标的的根代码
**syminfo.sector**
  返回行业板块
**syminfo.session**
  标的交易时段类型
**syminfo.shareholders**
  股东数量
**syminfo.shares_outstanding_float**
  流通股本总数
**syminfo.shares_outstanding_total**
  总股本总数
**syminfo.target_price_average**
  目标价的平均值
**syminfo.target_price_date**
  目标价起始日期
**syminfo.target_price_estimates**
  最新总目标价数量
**syminfo.target_price_high**
  最高目标价
**syminfo.target_price_low**
  最低目标价
**syminfo.target_price_median**
  目标价中位数
**syminfo.ticker**
  不带交易所前缀的标的名称
**syminfo.ticker()**
  返回 `symbol` 名称
**syminfo.tickerid**
  股票代码标识符
**syminfo.timezone**
  交易所时区
**syminfo.type**
  市场类型
**syminfo.volumetype**
  标的成交量类型

## Requests
**adjustment.dividends**
  除息调整常量
**adjustment.none**
  无调整常量
**adjustment.splits**
  除权调整常量
**barmerge.gaps_off**
  请求合并策略：关闭缺口
**barmerge.gaps_on**
  请求合并策略：开启缺口
**barmerge.lookahead_off**
  请求前瞻性合并策略：关闭
**barmerge.lookahead_on**
  请求前瞻性合并策略：开启
**dividends.future_amount**
  返回未来分红金额
**dividends.future_ex_date**
  返回未来除息日
**dividends.future_pay_date**
  返回未来派息日
**dividends.gross**
  毛利的命名常量
**dividends.net**
  净利的命名常量
**earnings.actual**
  实际盈利的命名常量
**earnings.estimate**
  预估盈利的命名常量
**earnings.future_eps**
  返回未来每股收益预估
**earnings.future_period_end_time**
  检查数据
**earnings.future_revenue**
  返回收入预估
**earnings.future_time**
  返回 UNIX 时间戳
**earnings.standardized**
  标准化盈利的命名常量
**request.currency_rate()**
  提供每日汇率
**request.dividends()**
  请求分红数据
**request.earnings()**
  请求盈利数据
**request.economic()**
  请求经济数据
**request.financial()**
  请求财务数据
**request.quandl()**
  *注意：* 此函数已弃用，请改用 `request.economic()`
**request.security_lower_tf()**
  请求较低时间框架的结果
**request.security()**
  请求结果
**request.seed()**
  从种子请求数据
**request.splits()**
  请求除权数据
**splits.denominator**
  除权分母的命名常量
**splits.numerator**
  除权分子的命名常量
**ticker.heikinashi()**
  创建 Heikin-Ashi 股票代码标识符
**ticker.inherit()**
  构建股票代码
**ticker.kagi()**
  创建 Kagi 股票代码标识符
**ticker.linebreak()**
  创建 Line Break 股票代码标识符
**ticker.modify()**
  创建股票代码标识符
**ticker.new()**
  创建股票代码标识符
**ticker.pointfigure()**
  创建 Point & Figure 股票代码标识符
**ticker.renko()**
  创建 Renko 股票代码标识符
**ticker.standard()**
  创建标准股票代码

## Strategy
**strategy.account_currency**
  返回账户货币
**strategy.avg_losing_trade**
  返回亏损交易的平均结果
**strategy.avg_losing_trade_percent**
  返回亏损交易的平均百分比结果
**strategy.avg_trade**
  返回交易的平均结果
**strategy.avg_trade_percent**
  返回交易的平均百分比结果
**strategy.avg_winning_trade**
  返回盈利交易的平均结果
**strategy.avg_winning_trade_percent**
  返回盈利交易的平均百分比结果
**strategy.cancel_all()**
  取消所有挂单
**strategy.cancel()**
  取消挂单或止损单
**strategy.cash**
  这是账户属性之一
**strategy.close_all()**
  创建订单以平仓所有头寸
**strategy.close()**
  创建订单以平仓特定头寸
**strategy.closedtrades**
  已平仓交易数
**strategy.closedtrades.commission()**
  返回所有已平仓交易的佣金总和
**strategy.closedtrades.entry_bar_index()**
  返回进入交易的柱索引
**strategy.closedtrades.entry_comment()**
  返回进入交易的注释
**strategy.closedtrades.entry_id()**
  返回进入交易的 ID
**strategy.closedtrades.entry_price()**
  返回进入交易的价格
**strategy.closedtrades.entry_time()**
  返回进入交易的 UNIX 时间
**strategy.closedtrades.exit_bar_index()**
  返回退出交易的柱索引
**strategy.closedtrades.exit_comment()**
  返回退出交易的注释
**strategy.closedtrades.exit_id()**
  返回退出交易的 ID
**strategy.closedtrades.exit_price()**
  返回退出交易的价格
**strategy.closedtrades.exit_time()**
  返回退出交易的 UNIX 时间
**strategy.closedtrades.first_index**
  索引或交易编号
**strategy.closedtrades.max_drawdown_percent()**
  返回最大亏损百分比
**strategy.closedtrades.max_drawdown()**
  返回最大亏损
**strategy.closedtrades.max_runup_percent()**
  返回最大盈利百分比
**strategy.closedtrades.max_runup()**
  返回最大盈利
**strategy.closedtrades.profit_percent()**
  返回盈亏百分比
**strategy.closedtrades.profit()**
  返回盈亏
**strategy.closedtrades.size()**
  返回方向
**strategy.commission.cash_per_contract**
  按合约计算佣金的类型
**strategy.commission.cash_per_order**
  按订单计算佣金的类型
**strategy.commission.percent**
  按百分比计算佣金的类型
**strategy.convert_to_account()**
  将值转换为账户货币
**strategy.convert_to_symbol()**
  将值转换为标的货币
**strategy.default_entry_qty()**
  计算默认入场数量
**strategy.direction.all**
  允许策略在所有方向上交易
**strategy.direction.long**
  允许策略在多头方向上交易
**strategy.direction.short**
  允许策略在空头方向上交易
**strategy.entry()**
  创建新的入场订单
**strategy.equity**
  当前权益（[strategy.cash](#strategycash) + 浮动盈亏）
**strategy.eventrades**
  保本交易数
**strategy.exit()**
  创建基于价格的退出订单
**strategy.fixed**
  这是账户属性之一
**strategy.grossloss**
  总货币价值
**strategy.grossloss_percent**
  总亏损百分比
**strategy.grossprofit**
  总货币价值
**strategy.grossprofit_percent**
  总盈利百分比
**strategy.initial_capital**
  初始资金
**strategy.long**
  多头的命名常量
**strategy.losstrades**
  亏损交易数
**strategy.margin_liquidation_price**
  启用保证金时显示
**strategy.max_contracts_held_all**
  所有交易中持有的最大合约数
**strategy.max_contracts_held_long**
  多头交易中持有的最大合约数
**strategy.max_contracts_held_short**
  空头交易中持有的最大合约数
**strategy.max_drawdown**
  最大权益回撤
**strategy.max_drawdown_percent**
  最大权益回撤百分比
**strategy.max_runup**
  最大权益增长
**strategy.max_runup_percent**
  最大权益增长百分比
**strategy.netprofit**
  总货币价值
**strategy.netprofit_percent**
  总盈利百分比
**strategy.oca.cancel**
  订单组合类型：取消其他订单
**strategy.oca.none**
  订单组合类型：无
**strategy.oca.reduce**
  订单组合类型：减少其他订单
**strategy.openprofit**
  当前未实现盈亏
**strategy.openprofit_percent**
  当前未实现盈亏百分比
**strategy.opentrades**
  未平仓交易数
**strategy.opentrades.capital_held**
  返回占用资金
**strategy.opentrades.commission()**
  返回所有未平仓交易的佣金总和
**strategy.opentrades.entry_bar_index()**
  返回进入交易的柱索引
**strategy.opentrades.entry_comment()**
  返回进入交易的注释
**strategy.opentrades.entry_id()**
  返回进入交易的 ID
**strategy.opentrades.entry_price()**
  返回进入交易的价格
**strategy.opentrades.entry_time()**
  返回进入交易的 UNIX 时间
**strategy.opentrades.max_drawdown_percent()**
  返回最大回撤百分比
**strategy.opentrades.max_drawdown()**
  返回最大回撤
**strategy.opentrades.max_runup_percent()**
  返回最大盈利百分比
**strategy.opentrades.max_runup()**
  返回最大盈利
**strategy.opentrades.profit_percent()**
  返回盈亏百分比
**strategy.opentrades.profit()**
  返回盈亏
**strategy.opentrades.size()**
  返回方向
**strategy.order()**
  创建新订单
**strategy.percent_of_equity**
  这是账户属性之一
**strategy.position_avg_price**
  平均入场价格
**strategy.position_entry_name**
  导致当前头寸的订单名称
**strategy.position_size**
  头寸方向和大小
**strategy.risk.allow_entry_in()**
  此函数可用于限制策略只能在特定条件下进入交易
**strategy.risk.max_cons_loss_days()**
  此函数的目的
**strategy.risk.max_drawdown()**
  此函数的目的
**strategy.risk.max_intraday_filled_orders()**
  此函数的目的
**strategy.risk.max_intraday_loss()**
  最大亏损值
**strategy.risk.max_position_size()**
  此函数的目的
**strategy.short**
  空头的命名常量
**strategy.wintrades**
  盈利交易数
**strategy()**
  此声明开始策略的定义
```
