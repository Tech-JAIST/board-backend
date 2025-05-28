# backend-template-python
## 開発の進め方
1. [プロジェクト作成方法](#プロジェクト作成方法)に従ってプロジェクトを作成する
2. [Tools](#Tools)のうち、必要なツールをインストール
3. [実装方法](docs/implement.md)に従って開発を進める

## プロジェクト作成方法
### GUI
右上の `Use this template` からレポジトリを作成できます。

## Tools
### エディタ(必須)
エディタはVSCode、もしくはそのフォークであるCursorを推奨しています。

拡張機能として、`Dev Containers`をインストールしてください。

[参考: DevContainerを使ってみよう](https://zenn.dev/bells17/articles/devcontainer-2024)

### Docker(必須)
[公式ページ](https://www.docker.com/)
DevContainerを立ち上げるために必要です。

インストール方法は[こちら](https://github.com/Tech-JAIST/backend-template-go/blob/main/docs/docker.md)を参考にしてください。

### uv(DevContainerに内包)
```sh
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
[ref: uv documentation](https://docs.astral.sh/uv/getting-started/features/)

### Python(DevContainerに内包)
```sh
uv python install {version}
```

## How to run
DevContainerを立ち上げると8080番ポートでサーバーが立ち上がります。
http://localhost:8080/ (API)

DevContainerを使わず手動で立ち上げたい場合、以下のコマンドを使用してください。
```
docker build -t backend_python . && docker run --rm -p 8080:8080 backend_python
```

## format
```sh
uv run ruff format .
```

## linter check
```sh
ruff check . --fix
```

## Acknowledgements

This project is based on [a5chin/python-uv](https://github.com/a5chin/python-uv/tree/main), which is licensed under the MIT License.
