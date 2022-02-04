使用 python 的 opencv 识别并用 win32 api 来模拟键盘敲击。
之前一直是 pc 上缩放到最小做的，也不想改了，看能不能混个参与奖。
大致原理是第一次首先用 opencv 可以大致确定游戏需要截图的区域，然后在当前大小下截取要识别的小玛丽头像。
在循环中，截屏并识别所有的小玛丽并根据位置确定敲击的按键，使用默认 dfjk。
使用 sleep 来避免过快的循环导致的截屏错误，sleep 的时间可以微调并影响最后成绩。
![result](https://github.com/risinyoung/involutehell.github.io/blob/main/contest/risinyoung/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202022-01-27%20152422.png?raw=true)
