# Python 和 FastAPI 学习项目

从一个可运行的 FastAPI 应用开始，逐步学习 Python 后端开发。当前业务方向是企业安全生产管理，后续模块设计见 [后端架构](docs/architecture.md)。

## 运行项目

项目使用 Python 3.13.16、uv、FastAPI 和 Uvicorn。第一次运行前请准备好 [uv](https://docs.astral.sh/uv/getting-started/installation/)。

在项目根目录打开 PowerShell，运行以下命令。

```powershell
uv sync --locked
uv run uvicorn app.main:app --reload
```

`uv sync --locked` 按 `uv.lock` 准备项目环境。`app.main:app` 表示 Uvicorn 加载 `app/main.py` 中名为 `app` 的对象。`--reload` 会在修改代码后重启服务，按 Ctrl+C 停止服务。

也可以在 VS Code 打开根目录，选择「FastAPI：启动后端」后按 F5。

应用代码只定义了 `GET /api/v1/health`，返回 `{"status":"ok"}`。FastAPI 自动生成交互式接口文档。[健康接口](http://127.0.0.1:8000/api/v1/health) · [交互式接口文档](http://127.0.0.1:8000/docs)

## 从入口开始读代码

1. 打开 `app/main.py`，了解 `FastAPI()` 如何创建应用。
2. 看 `@app.get(...)` 如何把 URL 和 GET 方法绑定到 `health()` 函数。
3. 在 `/docs` 里调用接口，观察 Python 字典如何变成 JSON 响应。

编辑代码后，可用 Ruff 检查代码和格式。

```powershell
uv run ruff check .
uv run ruff format --check .
```
