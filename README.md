# PDF to Image Converter

PDF2Image by Geek Fujiwara (@geekfujiwara)

## Overview

A desktop application that converts PDF files to high-quality images (PNG format). It provides a simple and user-friendly GUI interface, supporting both single file conversion and batch conversion of multiple files.


https://github.com/user-attachments/assets/938bbf6a-a9e7-4c93-b641-44b129f2764c



>[!Note]
>[Distribution](https://github.com/geekfujiwara/PDF2ImageConverter/tree/main/dist) has been created. So you can use this app without install.

## Main Features

### 📄 Conversion Features
- **Single File Conversion**: Convert one PDF file to images
- **Batch Folder Conversion**: Convert all PDF files in a folder at once
- **Subfolder Support**: Include PDF files in subfolders
- **Folder Structure Preservation**: Maintain original folder structure in output

### 🎨 Quality Settings
- **Low Quality**: Lightweight and fast conversion (1.0x scale)
- **Medium Quality**: Balanced quality (1.5x scale)
- **High Quality**: High-quality image output (2.0x scale)
- **Ultra Quality**: Maximum quality image output (3.0x scale)

### 🖥️ User Interface
- **Intuitive GUI**: Easy-to-understand buttons and layout
- **DPI Support**: Compatible with high-resolution displays
- **Real-time Progress**: Display file count and page progress
- **Cancel Function**: Cancel conversion process at any time
- **Completion Notification**: Show results after conversion and option to open output folder

### 🌐 Multilingual Support
- **Language Selection**: Dropdown menu for language switching
- **Japanese**: Full Japanese interface support
- **English**: Full English interface support
- **Real-time Language Switching**: UI updates immediately when language is changed

### 🔧 Additional Features
- **4-digit Page Numbers**: Output files with 4-digit page numbers (e.g., `document_0001.png`)
- **Memory Efficient**: Stable operation even with large PDF files
- **Error Handling**: Appropriate error messages when issues occur
- **Creator Information**: Clickable credit links

## System Requirements

- **OS**: Windows 10/11
- **Python**: 3.7 or later
- **Required Libraries**:
  - PyMuPDF (fitz)
  - tkinter (standard library)

## Installation

### 1. Install Dependencies

```bash
pip install PyMuPDF
```

### 2. Run the Application

```bash
python figconvertimagefrompdf.py
```

## Usage

### Basic Usage

1. **Launch the Application**
   ```bash
   python figconvertimagefrompdf.py
   ```

2. **Select Language**
   - Choose between "日本語" (Japanese) or "English" from the Language dropdown

3. **Input Selection**
   - `[FILE] Select PDF File`: Convert a single file
   - `[FOLDER] Select Folder`: Batch convert PDF files in a folder

4. **Output Selection**
   - `[FOLDER] Select Output Folder`: Choose folder to save converted images

5. **Quality Settings**
   - Choose from Low, Medium, High, or Ultra quality

6. **Execute**
   - Click the `Execute` button to start conversion

### Progress Display

During conversion, the following information is displayed:
- Currently processing file name
- File progress (for multiple files)
- Page progress
- Cancel button

## Output Format

- **File Format**: PNG
- **File Name**: `{original_filename}_{page_number}.png`
- **Page Number**: 4-digit fixed format (e.g., 0001, 0002, 0003...)
- **Folder Structure**: Maintains original folder structure

## Technical Specifications

### Technologies Used
- **PyMuPDF**: PDF parsing and image conversion
- **tkinter**: GUI framework
- **threading**: Asynchronous processing
- **ctypes**: DPI support

### Architecture
- **Modular Design**: Each feature implemented as independent modules
- **Error Handling**: Comprehensive error processing
- **Memory Management**: Efficient memory usage and garbage collection

## Developer Information

### Code Structure

```
figconvertimagefrompdf.py
├── LanguageManager          # Multilingual support
├── make_dpi_aware()         # DPI support
├── show_completion_dialog() # Completion dialog
├── show_author_links()      # Creator links display
├── show_mode_selection()    # Main settings UI
├── convert_single_pdf()     # Single PDF conversion
├── ProgressWindow           # Progress display class
└── convert_pdf_to_images()  # Main processing
```

### Customizable Settings

```python
# Quality settings
quality_scale = {
    "low": 1.0,
    "medium": 1.5,
    "high": 2.0,
    "ultra": 3.0
}

# Output format
output_format = "png"
filename_pattern = "{prefix}_{page:04d}.{ext}"
```

## License

This project is freely available for personal and commercial use.

## Creator

**Geek Fujiwara (@geekfujiwara)**

- 🐦 Twitter/X: [@geekfujiwara](https://x.com/geekfujiwara)
- 📺 YouTube: [GeekFujiwara](https://youtube.com/geekfujiwara)
- 📝 Blog: [geekfujiwara.com](https://www.geekfujiwara.com)

## Version History

### v1.1.0
- Added multilingual support (Japanese/English)
- Real-time language switching
- Enhanced user interface

### v1.0.0
- Initial release
- Single file and folder conversion support
- Quality settings feature
- Progress display feature
- DPI support
- Completion notification feature

---

# PDF to Image Converter (日本語)

PDF2Image by Geek Fujiwara (@geekfujiwara)

https://github.com/user-attachments/assets/91e373b4-36c3-4263-bbac-7bcdbb059799

## 概要

PDFファイルを高品質な画像（PNG形式）に変換するデスクトップアプリケーションです。
シンプルで使いやすいGUIインターフェースを提供し、単一ファイルの変換から複数ファイルの一括変換まで対応しています。

>[!Note]
>[Distribution](https://github.com/geekfujiwara/PDF2ImageConverter/tree/main/dist)から`.exe`ファイルを利用することで、インストール不要ですぐに利用できます。

## 主な機能

### 📄 変換機能
- **単一ファイル変換**: 1つのPDFファイルを画像に変換
- **フォルダ一括変換**: フォルダ内のすべてのPDFファイルを一括変換
- **サブフォルダ対応**: サブフォルダ内のPDFファイルも対象に含める
- **フォルダ構造保持**: 元のフォルダ構造を維持して画像を出力

### 🎨 画質設定
- **低画質**: 軽量で高速な変換（スケール1.0x）
- **中画質**: バランスの取れた品質（スケール1.5x）
- **高画質**: 高品質な画像出力（スケール2.0x）
- **超高画質**: 最高品質の画像出力（スケール3.0x）

### 🖥️ ユーザーインターフェース
- **直感的なGUI**: 分かりやすいボタンとレイアウト
- **DPI対応**: 高解像度ディスプレイに対応
- **リアルタイム進捗表示**: ファイル数とページ数の進行状況を表示
- **キャンセル機能**: 処理中の変換をいつでも中断可能
- **完了通知**: 変換完了後に結果を表示し、出力フォルダを開く選択肢を提供

### 🌐 多言語対応
- **言語選択**: ドロップダウンメニューで言語切り替え
- **日本語**: 完全な日本語インターフェース対応
- **英語**: 完全な英語インターフェース対応
- **リアルタイム言語切り替え**: 言語変更時に即座にUI更新

### 🔧 その他の機能
- **4桁ページ番号**: 出力ファイル名に4桁固定のページ番号を付与（例: `document_0001.png`）
- **メモリ効率**: 大容量PDFファイルでも安定した動作
- **エラーハンドリング**: 問題発生時の適切なエラーメッセージ表示
- **作成者情報**: クリック可能なクレジットリンク

## システム要件

- **OS**: Windows 10/11
- **Python**: 3.7以降
- **必要なライブラリ**:
  - PyMuPDF (fitz)
  - tkinter (標準ライブラリ)

## インストール

### 1. 依存関係のインストール

```bash
pip install PyMuPDF
```

### 2. アプリケーションの実行

```bash
python figconvertimagefrompdf.py
```

## 使用方法

### 基本的な使い方

1. **アプリケーションを起動**
   ```bash
   python figconvertimagefrompdf.py
   ```

2. **言語選択**
   - Languageドロップダウンから「日本語」または「English」を選択

3. **入力の選択**
   - `[FILE] PDFファイルを選択`: 単一ファイルを変換
   - `[FOLDER] フォルダを選択`: フォルダ内のPDFファイルを一括変換

4. **出力先の選択**
   - `[FOLDER] 出力先フォルダを選択`: 変換後の画像を保存するフォルダを選択

5. **画質設定**
   - 低・中・高・超高から選択

6. **実行**
   - `実行`ボタンをクリックして変換開始

### 進捗表示

変換中は以下の情報が表示されます：
- 現在処理中のファイル名
- ファイル進行状況（複数ファイルの場合）
- ページ進行状況
- キャンセルボタン

## 出力形式

- **ファイル形式**: PNG
- **ファイル名**: `{元のファイル名}_{ページ番号}.png`
- **ページ番号**: 4桁固定（例: 0001, 0002, 0003...）
- **フォルダ構造**: 元のフォルダ構造を維持

## 技術仕様

### 使用技術
- **PyMuPDF**: PDF解析と画像変換
- **tkinter**: GUIフレームワーク
- **threading**: 非同期処理
- **ctypes**: DPI対応

### アーキテクチャ
- **モジュラー設計**: 各機能を独立したモジュールとして実装
- **エラーハンドリング**: 包括的なエラー処理
- **メモリ管理**: 効率的なメモリ使用とガベージコレクション

## 開発者向け情報

### コード構造

```
figconvertimagefrompdf.py
├── LanguageManager          # 多言語対応
├── make_dpi_aware()         # DPI対応
├── show_completion_dialog() # 完了ダイアログ
├── show_author_links()      # 作成者リンク表示
├── show_mode_selection()    # メイン設定UI
├── convert_single_pdf()     # 単一PDF変換
├── ProgressWindow           # 進捗表示クラス
└── convert_pdf_to_images()  # メイン処理
```

### カスタマイズ可能な設定

```python
# 画質設定
quality_scale = {
    "low": 1.0,
    "medium": 1.5,
    "high": 2.0,
    "ultra": 3.0
}

# 出力形式
output_format = "png"
filename_pattern = "{prefix}_{page:04d}.{ext}"
```

## ライセンス

このプロジェクトは個人利用・商用利用問わず自由に使用できます。

## 作成者

**Geek Fujiwara (@geekfujiwara)**

- 🐦 Twitter/X: [@geekfujiwara](https://x.com/geekfujiwara)
- 📺 YouTube: [GeekFujiwara](https://youtube.com/geekfujiwara)
- 📝 Blog: [geekfujiwara.com](https://www.geekfujiwara.com)

## 更新履歴

### v1.1.0
- 多言語対応を追加（日本語/英語）
- リアルタイム言語切り替え機能
- ユーザーインターフェースの改善

### v1.0.0
- 初回リリース
- 単一ファイル・フォルダ変換対応
- 画質設定機能
- 進捗表示機能
- DPI対応
- 完了通知機能

---

📝 **Note**: このアプリケーションは継続的に改善されています。問題やご要望がございましたら、お気軽にお知らせください。
