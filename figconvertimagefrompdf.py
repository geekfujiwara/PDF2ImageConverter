import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import glob
import ctypes
import webbrowser
import subprocess
import sys
import threading
import time
import json

# 言語設定管理クラス
class LanguageManager:
    def __init__(self):
        self.current_language = "ja"  # デフォルトは日本語
        self.translations = {
            "ja": {
                # メイン UI
                "title": "PDF to Image Converter",
                "credit": "PDF2Image by Geek Fujiwara (@geekfujiwara)",
                "language": "Language",
                "input_selection": "入力の選択",
                "select_pdf_file": "[FILE] PDFファイルを選択",
                "select_folder": "[FOLDER] フォルダを選択",
                "not_selected": "選択されていません",
                "mode_unselected": "モード: 未選択",
                "mode_single": "モード: 単一ファイル処理",
                "mode_folder": "モード: フォルダ処理",
                "include_subfolders": "サブフォルダーも対象に含める",
                "output_selection": "出力先の選択",
                "select_output_folder": "[FOLDER] 出力先フォルダを選択",
                "quality_settings": "画質設定",
                "quality_low": "低",
                "quality_medium": "中",
                "quality_high": "高",
                "quality_ultra": "超高",
                "execute": "実行",
                "cancel": "キャンセル",
                
                # ダイアログ
                "processing": "処理中...",
                "pdf_conversion": "PDF変換中...",
                "file_progress": "ファイル進行状況:",
                "page_progress": "ページ進行状況:",
                "files_unit": "ファイル",
                "pages_unit": "ページ",
                "preparing": "準備中...",
                "processing_file": "処理中:",
                "completed": "完了",
                "completion_title": "処理完了",
                "open_folder_question": "出力先フォルダを開きますか？",
                "yes_open_folder": "はい（フォルダを開く）",
                "no": "いいえ",
                "close": "閉じる",
                
                # エラー・メッセージ
                "error": "エラー",
                "input_error": "入力エラー",
                "select_input_output": "入力元と出力先を選択してください。",
                "no_pdf_found": "指定されたフォルダにPDFファイルが見つかりませんでした。",
                "conversion_complete": "変換が完了しました。",
                "pages_created": "ページの画像が作成されました。",
                "quality": "画質:",
                "save_location": "保存先:",
                "process_complete": "処理が完了しました。",
                "processed_files": "処理したファイル数:",
                "converted_pages": "変換したページ数:",
                "errors": "エラー",
                "other_errors": "他{0}件のエラー",
                "folder_open_error": "フォルダを開けませんでした:",
                
                # ファイル選択ダイアログ
                "select_pdf_title": "PDFファイルを選択してください",
                "select_input_folder_title": "PDFファイルがあるフォルダを選択してください",
                "select_output_folder_title": "出力先フォルダを選択してください",
                
                # 作成者情報
                "about_geek_fujiwara": "ギークフジワラについて",
                "about_description": "このアプリの作成者はX、YouTube、ブログなどを執筆しています。\nどちらに遷移しますか？",
                "blog": "ブログ",
                
                # 処理エラー
                "file_processing_error": "ファイル '{0}' の処理中にエラーが発生しました: {1}"
            },
            "en": {
                # メイン UI
                "title": "PDF to Image Converter",
                "credit": "PDF2Image by Geek Fujiwara (@geekfujiwara)",
                "language": "Language",
                "input_selection": "Input Selection",
                "select_pdf_file": "[FILE] Select PDF File",
                "select_folder": "[FOLDER] Select Folder",
                "not_selected": "Not selected",
                "mode_unselected": "Mode: Unselected",
                "mode_single": "Mode: Single File Processing",
                "mode_folder": "Mode: Folder Processing",
                "include_subfolders": "Include subfolders",
                "output_selection": "Output Selection",
                "select_output_folder": "[FOLDER] Select Output Folder",
                "quality_settings": "Quality Settings",
                "quality_low": "Low",
                "quality_medium": "Medium",
                "quality_high": "High",
                "quality_ultra": "Ultra",
                "execute": "Execute",
                "cancel": "Cancel",
                
                # ダイアログ
                "processing": "Processing...",
                "pdf_conversion": "Converting PDF...",
                "file_progress": "File Progress:",
                "page_progress": "Page Progress:",
                "files_unit": "files",
                "pages_unit": "pages",
                "preparing": "Preparing...",
                "processing_file": "Processing:",
                "completed": "Completed",
                "completion_title": "Process Completed",
                "open_folder_question": "Would you like to open the output folder?",
                "yes_open_folder": "Yes (Open Folder)",
                "no": "No",
                "close": "Close",
                
                # エラー・メッセージ
                "error": "Error",
                "input_error": "Input Error",
                "select_input_output": "Please select input and output locations.",
                "no_pdf_found": "No PDF files found in the specified folder.",
                "conversion_complete": "Conversion completed.",
                "pages_created": "image pages have been created.",
                "quality": "Quality:",
                "save_location": "Save Location:",
                "process_complete": "Process completed.",
                "processed_files": "Processed Files:",
                "converted_pages": "Converted Pages:",
                "errors": "Errors",
                "other_errors": "{0} other errors",
                "folder_open_error": "Could not open folder:",
                
                # ファイル選択ダイアログ
                "select_pdf_title": "Please select a PDF file",
                "select_input_folder_title": "Please select a folder containing PDF files",
                "select_output_folder_title": "Please select an output folder",
                
                # 作成者情報
                "about_geek_fujiwara": "About Geek Fujiwara",
                "about_description": "The creator of this app writes on X, YouTube, and blog.\nWhich would you like to visit?",
                "blog": "Blog",
                
                # 処理エラー
                "file_processing_error": "An error occurred while processing file '{0}': {1}"
            }
        }
    
    def get_text(self, key, *args):
        """指定されたキーの翻訳テキストを取得"""
        text = self.translations.get(self.current_language, {}).get(key, key)
        if args:
            return text.format(*args)
        return text
    
    def set_language(self, language):
        """言語を設定"""
        if language in self.translations:
            self.current_language = language
    
    def get_languages(self):
        """利用可能な言語リストを取得"""
        return {
            "ja": "日本語",
            "en": "English"
        }

# グローバル言語マネージャー
lang_manager = LanguageManager()

def make_dpi_aware():
    """高解像度DPIに対応"""
    try:
        # Windows 8.1以降でDPI対応を有効にする
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except:
        try:
            # Windows Vista/7でDPI対応を有効にする
            ctypes.windll.user32.SetProcessDPIAware()
        except:
            pass

def show_completion_dialog(message, output_path):
    """完了ダイアログを表示し、出力先を開くかどうかを確認"""
    def open_folder():
        try:
            if sys.platform == "win32":
                os.startfile(output_path)
            elif sys.platform == "darwin":
                subprocess.run(["open", output_path])
            else:
                subprocess.run(["xdg-open", output_path])
        except Exception as e:
            messagebox.showerror(lang_manager.get_text("error"), f"{lang_manager.get_text('folder_open_error')} {str(e)}")
        completion_window.destroy()
    
    def close_only():
        completion_window.destroy()
    
    completion_window = tk.Toplevel()
    completion_window.title(lang_manager.get_text("completion_title"))
    completion_window.resizable(False, False)
    completion_window.grab_set()  # モーダルダイアログにする
    
    # 一時的なウィンドウサイズを設定
    completion_window.geometry("500x300")
    
    # 中央に配置の準備
    completion_window.transient()
    completion_window.update_idletasks()
    
    # メインフレーム
    main_frame = ttk.Frame(completion_window, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # 完了メッセージ
    message_label = ttk.Label(main_frame, text=message, 
                             font=("Arial", 10), justify=tk.LEFT, wraplength=450)
    message_label.pack(pady=(0, 20), fill=tk.X)
    
    # 質問
    question_label = ttk.Label(main_frame, text=lang_manager.get_text("open_folder_question"), 
                              font=("Arial", 11, "bold"))
    question_label.pack(pady=(0, 20))
    
    # ボタンフレーム
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill=tk.X, pady=10)
    
    # ボタンを中央に配置するためのサブフレーム
    button_subframe = ttk.Frame(button_frame)
    button_subframe.pack(anchor="center")
    
    ttk.Button(button_subframe, text=lang_manager.get_text("yes_open_folder"), 
               command=open_folder, width=20).pack(side=tk.LEFT, padx=(0, 15))
    ttk.Button(button_subframe, text=lang_manager.get_text("no"), 
               command=close_only, width=10).pack(side=tk.LEFT)
    
    # ウィンドウサイズを内容に合わせて調整
    completion_window.update_idletasks()
    
    # 必要な幅と高さを計算
    required_width = max(500, main_frame.winfo_reqwidth() + 60)
    required_height = max(300, main_frame.winfo_reqheight() + 80)
    
    # 画面中央に配置
    x = (completion_window.winfo_screenwidth() // 2) - (required_width // 2)
    y = (completion_window.winfo_screenheight() // 2) - (required_height // 2)
    completion_window.geometry(f"{required_width}x{required_height}+{x}+{y}")
    
    # ESCキーで閉じる
    completion_window.bind('<Escape>', lambda e: close_only())
    
    # ウィンドウを最前面に表示
    completion_window.lift()
    completion_window.attributes('-topmost', True)
    completion_window.after_idle(lambda: completion_window.attributes('-topmost', False))
    
    # イベントループ開始
    completion_window.mainloop()

def show_author_links():
    """作成者のリンクを表示するダイアログ"""
    def open_x():
        webbrowser.open("https://x.com/geekfujiwara")
    
    def open_youtube():
        webbrowser.open("https://youtube.com/geekfujiwara")
    
    def open_blog():
        webbrowser.open("https://www.geekfujiwara.com")
    
    def close_dialog():
        link_window.destroy()
    
    # 新しいルートウィンドウを作成
    link_window = tk.Tk()
    link_window.title(lang_manager.get_text("about_geek_fujiwara"))
    link_window.geometry("500x350")
    link_window.resizable(False, False)
    
    # 中央に配置
    link_window.eval('tk::PlaceWindow . center')
    
    # DPI対応を有効にする
    make_dpi_aware()
    
    # メインフレーム
    main_frame = ttk.Frame(link_window, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # 説明文
    desc_label = ttk.Label(main_frame, 
                          text=lang_manager.get_text("about_description"), 
                          font=("Arial", 12), justify=tk.CENTER, anchor="center", wraplength=460)
    desc_label.pack(pady=(10, 40), fill=tk.X)
    
    # ボタンフレーム
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill=tk.X, pady=20)
    
    # ボタンを中央に配置するためのサブフレーム
    button_subframe = ttk.Frame(button_frame)
    button_subframe.pack(anchor="center")
    
    ttk.Button(button_subframe, text="X", command=open_x, width=12).pack(side=tk.LEFT, padx=15)
    ttk.Button(button_subframe, text="YouTube", command=open_youtube, width=12).pack(side=tk.LEFT, padx=15)
    ttk.Button(button_subframe, text=lang_manager.get_text("blog"), command=open_blog, width=12).pack(side=tk.LEFT, padx=15)
    
    # 閉じるボタン
    ttk.Button(main_frame, text=lang_manager.get_text("close"), command=close_dialog, width=15).pack(pady=(40, 0))
    
    # ESCキーで閉じる
    link_window.bind('<Escape>', lambda e: close_dialog())
    
    # ウィンドウを最前面に表示
    link_window.lift()
    link_window.attributes('-topmost', True)
    link_window.after_idle(lambda: link_window.attributes('-topmost', False))
    
    # イベントループ開始
    link_window.mainloop()

def show_mode_selection():
    """処理モードを選択するGUIを表示"""
    result = {'mode': None, 'input_path': None, 'output_path': None, 'include_subfolders': False, 'quality': 'medium'}
    
    # UI要素の参照を保持するための辞書
    ui_elements = {}
    
    def browse_input_file():
        file_path = filedialog.askopenfilename(
            title=lang_manager.get_text("select_pdf_title"),
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if file_path:
            input_var.set(file_path)
            # 単一ファイルモードに切り替え
            mode_var.set("single")
            update_ui()
    
    def browse_input_folder():
        folder_path = filedialog.askdirectory(
            title=lang_manager.get_text("select_input_folder_title")
        )
        if folder_path:
            input_var.set(folder_path)
            # フォルダモードに切り替え
            mode_var.set("folder")
            update_ui()
    
    def browse_output_folder():
        folder_path = filedialog.askdirectory(
            title=lang_manager.get_text("select_output_folder_title"),
            initialdir=os.path.dirname(input_var.get()) if input_var.get() else None
        )
        if folder_path:
            output_var.set(folder_path)
    
    def update_ui():
        mode = mode_var.get()
        if mode == "single":
            ui_elements['mode_label'].config(text=lang_manager.get_text("mode_single"))
            ui_elements['subfolder_check'].config(state="disabled")
        elif mode == "folder":
            ui_elements['mode_label'].config(text=lang_manager.get_text("mode_folder"))
            ui_elements['subfolder_check'].config(state="normal")
        else:
            ui_elements['mode_label'].config(text=lang_manager.get_text("mode_unselected"))
            ui_elements['subfolder_check'].config(state="disabled")
        
        # 実行ボタンの有効/無効を切り替え
        if input_var.get() and output_var.get():
            ui_elements['execute_button'].config(state="normal")
        else:
            ui_elements['execute_button'].config(state="disabled")
    
    def update_language():
        """言語変更時にUIを更新"""
        # タイトルとラベルを更新
        selection_window.title(lang_manager.get_text("title"))
        ui_elements['title_label'].config(text=lang_manager.get_text("title"))
        ui_elements['credit_label'].config(text=lang_manager.get_text("credit"))
        
        # 各セクションのラベルを更新
        ui_elements['input_frame'].config(text=lang_manager.get_text("input_selection"))
        ui_elements['output_frame'].config(text=lang_manager.get_text("output_selection"))
        ui_elements['quality_frame'].config(text=lang_manager.get_text("quality_settings"))
        ui_elements['language_frame'].config(text=lang_manager.get_text("language"))
        
        # ボタンを更新
        ui_elements['file_button'].config(text=lang_manager.get_text("select_pdf_file"))
        ui_elements['folder_button'].config(text=lang_manager.get_text("select_folder"))
        ui_elements['output_button'].config(text=lang_manager.get_text("select_output_folder"))
        ui_elements['execute_button'].config(text=lang_manager.get_text("execute"))
        ui_elements['cancel_button'].config(text=lang_manager.get_text("cancel"))
        
        # チェックボックスとラジオボタンを更新
        ui_elements['subfolder_check'].config(text=lang_manager.get_text("include_subfolders"))
        ui_elements['quality_low'].config(text=lang_manager.get_text("quality_low"))
        ui_elements['quality_medium'].config(text=lang_manager.get_text("quality_medium"))
        ui_elements['quality_high'].config(text=lang_manager.get_text("quality_high"))
        ui_elements['quality_ultra'].config(text=lang_manager.get_text("quality_ultra"))
        
        # パス表示ラベルを更新
        update_input_label()
        update_output_label()
        update_ui()
    
    def on_language_change(event=None):
        """言語が変更されたときの処理"""
        selected_lang = language_var.get()
        # 言語コードを取得
        lang_code = None
        for code, name in lang_manager.get_languages().items():
            if name == selected_lang:
                lang_code = code
                break
        
        if lang_code:
            lang_manager.set_language(lang_code)
            update_language()
    
    def on_execute():
        if not input_var.get() or not output_var.get():
            messagebox.showwarning(lang_manager.get_text("input_error"), lang_manager.get_text("select_input_output"))
            return
        
        result['mode'] = mode_var.get()
        result['input_path'] = input_var.get()
        result['output_path'] = output_var.get()
        result['include_subfolders'] = subfolder_var.get()
        result['quality'] = quality_var.get()
        selection_window.destroy()
    
    def on_cancel():
        selection_window.destroy()
    
    def on_credit_click(event):
        show_author_links()
    
    # DPI対応を有効にする
    make_dpi_aware()
    
    # メインウィンドウを作成
    selection_window = tk.Tk()
    selection_window.title(lang_manager.get_text("title"))
    
    # 高解像度対応のウィンドウサイズ設定
    base_width = 520
    base_height = 520  # 言語選択分を考慮して少し高さを増加
    
    # DPIスケールを取得
    try:
        dpi_scale = selection_window.winfo_fpixels('1i') / 96.0
        width = int(base_width * min(dpi_scale, 1.5))
        height = int(base_height * min(dpi_scale, 1.5))
    except:
        width = base_width
        height = base_height
    
    selection_window.geometry(f"{width}x{height}")
    selection_window.resizable(False, False)
    
    # ウィンドウを中央に配置
    selection_window.eval('tk::PlaceWindow . center')
    
    # 変数
    mode_var = tk.StringVar()
    input_var = tk.StringVar()
    output_var = tk.StringVar()
    subfolder_var = tk.BooleanVar()
    quality_var = tk.StringVar(value="medium")
    language_var = tk.StringVar()
    
    # 現在の言語を設定
    current_lang_name = lang_manager.get_languages()[lang_manager.current_language]
    language_var.set(current_lang_name)
    
    # 変数の変更を監視
    input_var.trace('w', lambda *args: update_ui())
    output_var.trace('w', lambda *args: update_ui())
    
    # メインフレーム
    main_frame = ttk.Frame(selection_window, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # タイトル
    ui_elements['title_label'] = ttk.Label(main_frame, text=lang_manager.get_text("title"), 
                           font=("Arial", 16, "bold"))
    ui_elements['title_label'].pack(pady=(0, 5))
    
    # クレジット・署名（クリック可能）
    ui_elements['credit_label'] = ttk.Label(main_frame, text=lang_manager.get_text("credit"), 
                            font=("Arial", 10), foreground="blue", cursor="hand2")
    ui_elements['credit_label'].pack(pady=(0, 15))
    ui_elements['credit_label'].bind("<Button-1>", on_credit_click)
    
    # 言語選択セクション
    ui_elements['language_frame'] = ttk.LabelFrame(main_frame, text=lang_manager.get_text("language"), padding="10")
    ui_elements['language_frame'].pack(fill=tk.X, pady=(0, 15))
    
    language_combo = ttk.Combobox(ui_elements['language_frame'], textvariable=language_var, 
                                 values=list(lang_manager.get_languages().values()), 
                                 state="readonly", width=20)
    language_combo.pack(anchor="w")
    language_combo.bind('<<ComboboxSelected>>', on_language_change)
    
    # 入力選択セクション
    ui_elements['input_frame'] = ttk.LabelFrame(main_frame, text=lang_manager.get_text("input_selection"), padding="10")
    ui_elements['input_frame'].pack(fill=tk.X, pady=(0, 15))
    
    # 入力選択ボタン
    input_button_frame = ttk.Frame(ui_elements['input_frame'])
    input_button_frame.pack(fill=tk.X, pady=(0, 10))
    
    ui_elements['file_button'] = ttk.Button(input_button_frame, text=lang_manager.get_text("select_pdf_file"), 
               command=browse_input_file, width=22)
    ui_elements['file_button'].pack(side=tk.LEFT, padx=(0, 10))
    
    ui_elements['folder_button'] = ttk.Button(input_button_frame, text=lang_manager.get_text("select_folder"), 
               command=browse_input_folder, width=22)
    ui_elements['folder_button'].pack(side=tk.LEFT)
    
    # 選択されたパス表示
    ui_elements['input_label'] = ttk.Label(ui_elements['input_frame'], text=lang_manager.get_text("not_selected"), 
                           relief="sunken", anchor="w")
    ui_elements['input_label'].pack(fill=tk.X, pady=(0, 5))
    
    # モード表示
    ui_elements['mode_label'] = ttk.Label(ui_elements['input_frame'], text=lang_manager.get_text("mode_unselected"), 
                          font=("Arial", 9), foreground="blue")
    ui_elements['mode_label'].pack(anchor="w")
    
    # サブフォルダーオプション
    ui_elements['subfolder_check'] = ttk.Checkbutton(ui_elements['input_frame'], text=lang_manager.get_text("include_subfolders"), 
                                     variable=subfolder_var, state="disabled")
    ui_elements['subfolder_check'].pack(anchor="w", pady=(5, 0))
    
    # 出力選択セクション
    ui_elements['output_frame'] = ttk.LabelFrame(main_frame, text=lang_manager.get_text("output_selection"), padding="10")
    ui_elements['output_frame'].pack(fill=tk.X, pady=(0, 15))
    
    # 出力選択ボタン
    ui_elements['output_button'] = ttk.Button(ui_elements['output_frame'], text=lang_manager.get_text("select_output_folder"), 
               command=browse_output_folder, width=25)
    ui_elements['output_button'].pack(pady=(0, 10))
    
    # 選択されたパス表示
    ui_elements['output_label'] = ttk.Label(ui_elements['output_frame'], text=lang_manager.get_text("not_selected"), 
                            relief="sunken", anchor="w")
    ui_elements['output_label'].pack(fill=tk.X)
    
    # 画質選択セクション
    ui_elements['quality_frame'] = ttk.LabelFrame(main_frame, text=lang_manager.get_text("quality_settings"), padding="10")
    ui_elements['quality_frame'].pack(fill=tk.X, pady=(0, 15))
    
    quality_button_frame = ttk.Frame(ui_elements['quality_frame'])
    quality_button_frame.pack(fill=tk.X)
    
    ui_elements['quality_low'] = ttk.Radiobutton(quality_button_frame, text=lang_manager.get_text("quality_low"), variable=quality_var, value="low")
    ui_elements['quality_low'].pack(side=tk.LEFT, padx=(0, 15))
    
    ui_elements['quality_medium'] = ttk.Radiobutton(quality_button_frame, text=lang_manager.get_text("quality_medium"), variable=quality_var, value="medium")
    ui_elements['quality_medium'].pack(side=tk.LEFT, padx=(0, 15))
    
    ui_elements['quality_high'] = ttk.Radiobutton(quality_button_frame, text=lang_manager.get_text("quality_high"), variable=quality_var, value="high")
    ui_elements['quality_high'].pack(side=tk.LEFT, padx=(0, 15))
    
    ui_elements['quality_ultra'] = ttk.Radiobutton(quality_button_frame, text=lang_manager.get_text("quality_ultra"), variable=quality_var, value="ultra")
    ui_elements['quality_ultra'].pack(side=tk.LEFT)
    
    # 実行・キャンセルボタン
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill=tk.X, pady=(20, 0))
    
    ui_elements['execute_button'] = ttk.Button(button_frame, text=lang_manager.get_text("execute"), 
                               command=on_execute, state="disabled")
    ui_elements['execute_button'].pack(side=tk.LEFT, padx=(0, 10))
    
    ui_elements['cancel_button'] = ttk.Button(button_frame, text=lang_manager.get_text("cancel"), 
               command=on_cancel)
    ui_elements['cancel_button'].pack(side=tk.LEFT)
    
    # 入力パスの更新を監視してラベルを更新
    def update_input_label(*args):
        path = input_var.get()
        if path:
            ui_elements['input_label'].config(text=path)
        else:
            ui_elements['input_label'].config(text=lang_manager.get_text("not_selected"))
    
    def update_output_label(*args):
        path = output_var.get()
        if path:
            ui_elements['output_label'].config(text=path)
        else:
            ui_elements['output_label'].config(text=lang_manager.get_text("not_selected"))
    
    input_var.trace('w', update_input_label)
    output_var.trace('w', update_output_label)
    
    # ESCキーでキャンセル
    selection_window.bind('<Escape>', lambda e: on_cancel())
    
    # ウィンドウを最前面に表示
    selection_window.lift()
    selection_window.attributes('-topmost', True)
    selection_window.after_idle(lambda: selection_window.attributes('-topmost', False))
    
    # イベントループ開始
    selection_window.mainloop()
    
    return result

def convert_single_pdf(pdf_file, output_base_dir, input_base_dir=None, quality="medium", progress_window=None):
    """単一のPDFファイルを画像に変換"""
    doc = None
    try:
        # PDFを開く
        doc = fitz.open(pdf_file)
        
        # 元のPDFファイル名（拡張子なし）をプレフィックスとして使用
        file_prefix = os.path.splitext(os.path.basename(pdf_file))[0]
        
        # 出力先ディレクトリを決定
        if input_base_dir:
            # 相対パスを計算してフォルダ構造を保持
            rel_path = os.path.relpath(os.path.dirname(pdf_file), input_base_dir)
            output_dir = os.path.join(output_base_dir, rel_path)
        else:
            output_dir = output_base_dir
        
        # 出力ディレクトリが存在しない場合は作成
        os.makedirs(output_dir, exist_ok=True)
        
        # 画質設定に応じたスケール値を決定
        quality_scale = {
            "low": 1.0,
            "medium": 1.5,
            "high": 2.0,
            "ultra": 3.0
        }
        scale = quality_scale.get(quality, 1.5)
        
        # ページ数を取得
        page_count = len(doc)
        
        # 各ページを画像に変換
        for page_num in range(page_count):
            # キャンセルチェック
            if progress_window and progress_window.is_cancelled():
                return 0
                
            page = doc.load_page(page_num)
            
            # 画質設定に応じた変換マトリックスを作成
            mat = fitz.Matrix(scale, scale)
            pix = page.get_pixmap(matrix=mat)
            
            # 出力ファイル名を生成（4桁固定のページ番号）
            output_file = os.path.join(output_dir, f"{file_prefix}_{page_num + 1:04d}.png")
            pix.save(output_file)
            
            # プログレスバーの更新
            if progress_window:
                progress_window.update_page(1)
            
            # メモリ解放
            pix = None
            page = None
        
        return page_count
        
    except Exception as e:
        raise Exception(lang_manager.get_text("file_processing_error", pdf_file, str(e)))
    
    finally:
        # ドキュメントを確実に閉じる
        if doc is not None:
            try:
                doc.close()
            except:
                pass

class ProgressWindow:
    def __init__(self, title=None, total_files=0, total_pages=0):
        self.total_files = total_files
        self.total_pages = total_pages
        self.current_file = 0
        self.current_page = 0
        self.cancelled = False
        
        # プログレスウィンドウを作成
        self.progress_window = tk.Toplevel()
        self.progress_window.title(title or lang_manager.get_text("processing"))
        self.progress_window.resizable(False, False)
        self.progress_window.grab_set()
        
        # 一時的なウィンドウサイズを設定
        self.progress_window.geometry("500x250")
        
        # 中央に配置の準備
        self.progress_window.transient()
        self.progress_window.update_idletasks()
        
        # DPI対応
        make_dpi_aware()
        
        # メインフレーム
        main_frame = ttk.Frame(self.progress_window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 現在のファイル名表示
        self.current_file_label = ttk.Label(main_frame, text=lang_manager.get_text("preparing"), 
                                           font=("Arial", 10), wraplength=450)
        self.current_file_label.pack(pady=(0, 15), fill=tk.X)
        
        # ファイル進行状況
        if total_files > 1:
            ttk.Label(main_frame, text=lang_manager.get_text("file_progress"), 
                     font=("Arial", 9)).pack(anchor="w")
            self.file_progress = ttk.Progressbar(main_frame, length=450, mode='determinate')
            self.file_progress.pack(pady=(5, 10), fill=tk.X)
            self.file_progress['maximum'] = total_files
            
            self.file_status_label = ttk.Label(main_frame, text=f"0 / 0 {lang_manager.get_text('files_unit')}", 
                                              font=("Arial", 9))
            self.file_status_label.pack(pady=(0, 15), anchor="w")
        else:
            self.file_progress = None
            self.file_status_label = None
        
        # ページ進行状況
        ttk.Label(main_frame, text=lang_manager.get_text("page_progress"), 
                 font=("Arial", 9)).pack(anchor="w")
        self.page_progress = ttk.Progressbar(main_frame, length=450, mode='determinate')
        self.page_progress.pack(pady=(5, 10), fill=tk.X)
        self.page_progress['maximum'] = max(total_pages, 1)
        
        self.page_status_label = ttk.Label(main_frame, text=f"0 / 0 {lang_manager.get_text('pages_unit')}", 
                                          font=("Arial", 9))
        self.page_status_label.pack(pady=(0, 20), anchor="w")
        
        # キャンセルボタン
        ttk.Button(main_frame, text=lang_manager.get_text("cancel"), 
                  command=self.cancel, width=15).pack(pady=(0, 10))
        
        # ウィンドウサイズを内容に合わせて調整
        self.progress_window.update_idletasks()
        
        # 必要な幅と高さを計算
        required_width = max(500, main_frame.winfo_reqwidth() + 60)
        required_height = max(250, main_frame.winfo_reqheight() + 80)
        
        # 画面中央に配置
        x = (self.progress_window.winfo_screenwidth() // 2) - (required_width // 2)
        y = (self.progress_window.winfo_screenheight() // 2) - (required_height // 2)
        self.progress_window.geometry(f"{required_width}x{required_height}+{x}+{y}")
        
        # ウィンドウを最前面に表示
        self.progress_window.lift()
        self.progress_window.attributes('-topmost', True)
        self.progress_window.after_idle(lambda: self.progress_window.attributes('-topmost', False))
        
        # ウィンドウを閉じる際の処理
        self.progress_window.protocol("WM_DELETE_WINDOW", self.cancel)
    
    def update_file(self, file_index, filename):
        """ファイル進行状況を更新"""
        if self.cancelled:
            return
            
        self.current_file = file_index
        if isinstance(filename, str):
            display_name = os.path.basename(filename) if filename != lang_manager.get_text("completed") else filename
            self.current_file_label.config(text=f"{lang_manager.get_text('processing_file')} {display_name}")
        
        if self.file_progress:
            self.file_progress['value'] = file_index
            self.file_status_label.config(text=f"{file_index} / {self.total_files} {lang_manager.get_text('files_unit')}")
        
        self.progress_window.update_idletasks()
        self.progress_window.update()  # 強制的にGUIを更新
    
    def update_page(self, page_count):
        """ページ進行状況を更新"""
        if self.cancelled:
            return
            
        self.current_page += page_count
        self.page_progress['value'] = self.current_page
        self.page_status_label.config(text=f"{self.current_page} / {self.total_pages} {lang_manager.get_text('pages_unit')}")
        
        self.progress_window.update_idletasks()
        self.progress_window.update()  # 強制的にGUIを更新
    
    def cancel(self):
        """処理をキャンセル"""
        self.cancelled = True
        if self.progress_window and self.progress_window.winfo_exists():
            self.progress_window.destroy()
    
    def close(self):
        """ウィンドウを閉じる"""
        if self.progress_window and self.progress_window.winfo_exists():
            self.progress_window.destroy()
    
    def is_cancelled(self):
        """キャンセルされたかどうかを確認"""
        return self.cancelled

def convert_pdf_to_images():
    while True:  # 無限ループで繰り返し処理
        # 統合された設定UIを表示
        settings = show_mode_selection()
        
        if not settings['mode']:  # キャンセルが選択された場合
            break
        
        # 隠しルートウィンドウを作成（メッセージボックス用）
        root = tk.Tk()
        root.withdraw()
        
        try:
            if settings['mode'] == "single":  # 単一ファイル処理
                # 単一ファイルの場合、ページ数を事前に取得
                try:
                    temp_doc = fitz.open(settings['input_path'])
                    total_pages = len(temp_doc)
                    temp_doc.close()
                except:
                    total_pages = 1
                
                # プログレスウィンドウを作成
                progress_window = ProgressWindow(lang_manager.get_text("pdf_conversion"), total_files=1, total_pages=total_pages)
                progress_window.update_file(0, settings['input_path'])
                
                page_count = convert_single_pdf(settings['input_path'], settings['output_path'], 
                                              None, settings['quality'], progress_window)
                
                # プログレスを更新
                if not progress_window.is_cancelled():
                    progress_window.update_file(1, lang_manager.get_text("completed"))
                    time.sleep(0.5)  # 完了状態を少し表示
                
                progress_window.close()
                
                # キャンセルされた場合は次のループへ
                if progress_window.is_cancelled():
                    continue
                
                message = f"{lang_manager.get_text('conversion_complete')}\n{page_count}{lang_manager.get_text('pages_created')}\n{lang_manager.get_text('quality')} {settings['quality']}\n{lang_manager.get_text('save_location')} {settings['output_path']}"
                show_completion_dialog(message, settings['output_path'])
                
            else:  # フォルダ処理
                # PDFファイルを検索
                if settings['include_subfolders']:
                    pdf_files = glob.glob(os.path.join(settings['input_path'], "**", "*.pdf"), recursive=True)
                else:
                    pdf_files = glob.glob(os.path.join(settings['input_path'], "*.pdf"))
                
                if not pdf_files:
                    messagebox.showinfo(lang_manager.get_text("error"), lang_manager.get_text("no_pdf_found"))
                    continue
                
                # 総ページ数を事前に計算
                total_pages = 0
                for pdf_file in pdf_files:
                    try:
                        temp_doc = fitz.open(pdf_file)
                        total_pages += len(temp_doc)
                        temp_doc.close()
                    except:
                        total_pages += 1
                
                # プログレスウィンドウを作成
                progress_window = ProgressWindow(lang_manager.get_text("pdf_conversion"), total_files=len(pdf_files), total_pages=total_pages)
                
                # 各PDFファイルを処理
                total_converted_pages = 0
                processed_files = 0
                errors = []
                
                for i, pdf_file in enumerate(pdf_files):
                    if progress_window.is_cancelled():
                        break
                    
                    progress_window.update_file(i, pdf_file)
                    
                    try:
                        page_count = convert_single_pdf(pdf_file, settings['output_path'], 
                                                      settings['input_path'], settings['quality'], progress_window)
                        
                        if not progress_window.is_cancelled():
                            total_converted_pages += page_count
                            processed_files += 1
                            
                            # メモリクリーンアップ
                            import gc
                            gc.collect()
                        
                    except Exception as e:
                        errors.append(str(e))
                
                # プログレスウィンドウを閉じる
                if not progress_window.is_cancelled():
                    progress_window.update_file(len(pdf_files), lang_manager.get_text("completed"))
                    time.sleep(0.5)  # 完了状態を少し表示
                
                progress_window.close()
                
                # キャンセルされた場合は次のループへ
                if progress_window.is_cancelled():
                    continue
                
                # 結果を表示
                result_message = f"{lang_manager.get_text('process_complete')}\n" \
                                f"{lang_manager.get_text('processed_files')} {processed_files}/{len(pdf_files)}\n" \
                                f"{lang_manager.get_text('converted_pages')} {total_converted_pages}\n" \
                                f"{lang_manager.get_text('quality')} {settings['quality']}\n" \
                                f"{lang_manager.get_text('save_location')} {settings['output_path']}"
                
                if errors:
                    result_message += f"\n\n{lang_manager.get_text('errors')}({len(errors)}件):\n" + "\n".join(errors[:5])
                    if len(errors) > 5:
                        result_message += f"\n... {lang_manager.get_text('other_errors', len(errors)-5)}"
                
                show_completion_dialog(result_message, settings['output_path'])
                    
        except Exception as e:
            messagebox.showerror(lang_manager.get_text("error"), str(e))
        
        finally:
            # ルートウィンドウを閉じる
            root.destroy()

if __name__ == "__main__":
    convert_pdf_to_images()
