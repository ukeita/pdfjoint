#psthlobモジュールでファイル・ディレクトリ(フォルダ)のパスをオブジェクトとして処理できる
from pathlib import Path
import PyPDF2

# フォルダ内のPDFファイル一覧
pdf_dir = Path("./pdf_files")
pdf_files = sorted(pdf_dir.glob("*.pdf"))

# １つのPDFファイルにまとめる
pdf_writer = PyPDF2.PdfFileWriter()
for pdf_file in pdf_files:
    pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
    for i in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(i))

# 保存ファイル名（先頭と末尾のファイル名で作成）
merged_file = pdf_files[0].stem + "-" + pdf_files[-1].stem + ".pdf"

# 保存
with open(merged_file, "wb") as f:
    pdf_writer.write(f)
