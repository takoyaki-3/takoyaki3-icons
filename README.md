# SVGからPNGとICOに変換するツール

このツールは、指定したSVGファイルを、複数のサイズ（128px, 192px, 256px, 512px, 1024px）のPNG画像に変換し、さらにICOファイルを作成します。

## 特徴

- SVGファイルをPNG画像に変換
- 指定した複数のサイズでPNG画像を出力
- ICOファイルを作成
- シンプルなPythonスクリプトで動作


## インストール

このツールはPythonで記述されており、以下のライブラリが必要です。

- cairosvg
- Pillow

インストールには、pipを使用します。

```bash
pip install cairosvg Pillow
```


## 使い方

1. **`svg2png.py` を実行**

   `svg2png.py` スクリプトを実行します。スクリプトには、SVGファイルのパスと出力ファイルのベース名を指定します。

   ```bash
   python svg2png.py
   ```

1. **出力ファイル**

   指定した出力ファイルのベース名に基づいて、以下のファイルが生成されます。

   - `takoyaki3_128px.png`
   - `takoyaki3_192px.png`
   - `takoyaki3_256px.png`
   - `takoyaki3_512px.png`
   - `takoyaki3_1024px.png`
   - `takoyaki3.ico`

## ファイル構成

```
├── svg2png.py             # メインのPythonスクリプト
├── takoyaki3.ico          # 生成されるICOファイル (サンプル)
├── takoyaki3.svg          # サンプルのSVGファイル
├── takoyaki3_1024px.png    # 生成されるPNGファイル (サンプル)
├── takoyaki3_128px.png    # 生成されるPNGファイル (サンプル)
├── takoyaki3_192px.png    # 生成されるPNGファイル (サンプル)
├── takoyaki3_256px.png    # 生成されるPNGファイル (サンプル)
├── takoyaki3_512px.png    # 生成されるPNGファイル (サンプル)
```
