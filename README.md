# botzone-local-runner
Botzone local runner for Chinese-Standard-Mahjong on UNIX-like Systems

## 食用指南

将 `runner.cpp` 中的 `bot_path` 和 `judger_path` 改成你的，然后干就完了

编译可以直接使用 `make` 编译，也许你需要把 `Makefile` 中的 `g++-9` 改成你的 `g++`

Log 文件会被存在 `log.json` 中，运行 `runner` 会输出 initdata 和最后的 output

提供 `quiet mode`，用 `./runner -q` 或 `./runner --quiet` 开启，只输出 `final_output` （JSON形式）

`statistics.py` 提供了一个运行多次统计数据的例子