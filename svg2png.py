import cairosvg
from PIL import Image

def svg_to_multiple_pngs_and_ico(svg_file_path, output_base_name):
    """
    SVGファイルを128px, 256px, 512px, 1024pxのサイズでPNGに変換し、
    ICOファイルも作成する関数。

    :param svg_file_path: SVGファイルのパス
    :param output_base_name: 出力するファイルのベース名 (例: "output" と指定すると "output_128.png" や "output.ico" になる)
    """
    sizes = [128, 192, 256, 512, 1024]  # 出力するサイズのリスト
    png_files = []  # ICOファイル作成用に生成したPNGファイルを保持

    # PNGファイルの生成
    with open(svg_file_path, "rb") as svg_file:
        svg_data = svg_file.read()  # SVGデータを読み込み

        for size in sizes:
            output_png_path = f"{output_base_name}_{size}px.png"
            cairosvg.svg2png(
                bytestring=svg_data, write_to=output_png_path, output_width=size, output_height=size
            )
            png_files.append(output_png_path)  # ICO用にPNGファイルをリストに保存
            print(f"{output_png_path} にPNGが保存されました。")

    # ICOファイルの生成（128px, 256px のサイズでICOファイルを作成）
    ico_output_path = f"{output_base_name}.ico"
    with Image.open(png_files[0]) as img_128:  # 128px PNG
        img_128.save(ico_output_path, format='ICO', sizes=[(128, 128), (256, 256)])
        print(f"{ico_output_path} にICOファイルが保存されました。")

# 例: 複数サイズでPNGを出力
svg_file = "takoyaki3.svg"
output_base = "takoyaki3"  # 出力ファイルのベース名
svg_to_multiple_pngs_and_ico(svg_file, output_base)
