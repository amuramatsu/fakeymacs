﻿# -*- mode: python; coding: utf-8-with-signature-dos -*-

####################################################################################################
## Emacs の場合、IME 切り替え用のキーを C-\ に置き換える
####################################################################################################

try:
    # 設定されているか？
    fc.x_window_apps
except:
    # X Windows アプリケーションソフトのプログラム名称を指定する
    fc.x_window_apps = ["mstsc.exe",              # WSLg
                        "msrdc.exe",              # WSLg
                        "XWin.exe",               # Cygwin/X
                        "XWin_MobaX.exe",         # MobaXterm/X
                        "XWin_MobaX_1.16.3.exe",  # MobaXterm/X
                        "XWin_Cygwin_1.14.5.exe", # MobaXterm/X
                        "XWin_Cygwin_1.16.3.exe", # MobaXterm/X
                        "Xming.exe",              # Xming
                        "vcxsrv.exe",             # VcXsrv
                        "GWSL_vcxsrv.exe",        # GWSL
                        "GWSL_vcxsrv_lowdpi.exe", # GWSL
                        "X410.exe",               # X410
                        "Xpra-Launcher.exe",      # Xpra
                        ]

def is_real_emacs(window):
    if (window.getClassName() == "Emacs" or
        (window.getProcessName() in fc.x_window_apps and
         # ウィンドウのタイトルを検索する正規表現を指定する
         # Emacs を起動しているウィンドウを検索できるように、Emacs の frame-title-format 変数を
         # 次のように設定するなどして、識別できるようにする
         # (setq frame-title-format (format "emacs-%s - %%b " emacs-version))
         # （別途公開している sglstart コマンドを利用している場合、%%b の後のスペースは必要）
         re.search(r"^emacs-", window.getText()))):
        return True
    else:
        return False

keymap_real_emacs = keymap.defineWindowKeymap(check_func=is_real_emacs)

# IME 切り替え用のキーの置き換え
# （Emacs 側での C-F1 と C-F2 の設定については、次のページを参照してください。
#   https://w.atwiki.jp/ntemacs/pages/48.html ）
define_key(keymap_real_emacs, "A-(25)", self_insert_command("C-Yen")) # Alt-` キー

if is_japanese_keyboard:
    define_key(keymap_real_emacs, "(243)", self_insert_command("C-Yen")) # <半角／全角> キー
    define_key(keymap_real_emacs, "(244)", self_insert_command("C-Yen")) # <半角／全角> キー

define_key(keymap_real_emacs, "(29)",   self_insert_command("C-F1")) # <無変換> キー
define_key(keymap_real_emacs, "(28)",   self_insert_command("C-F2")) # <変換> キー
# define_key(keymap_real_emacs, "O-LAlt", self_insert_command("C-F1")) # 左 Altキーの単押し
# define_key(keymap_real_emacs, "O-RAlt", self_insert_command("C-F2")) # 右 Altキーの単押し
