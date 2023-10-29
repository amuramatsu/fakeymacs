﻿# -*- mode: python; coding: utf-8-with-signature-dos -*-

# 本ファイルは、config_personal.py というファイル名にすることで個人設定ファイルとして機能します。
# 本ファイルの設定には [] で括られたセクション名が定義されており、その単位で config.py の中に設定
# が取り込まれ、exec関数により実行されます。config.py ファイル内の exec関数をコールしているところ
# を検索すると、何のセクションがどこで読み込まれるかが分かると思います。

# 本ファイルはサンプルファイルです。本ファイルに記載のない設定でも、_config_parameter.py から設定を
# 取り込み、カスタマイズして利用することができます。

####################################################################################################
## 初期設定
####################################################################################################
# [section-init] -----------------------------------------------------------------------------------

print(startupString())

keymap.editor = r"notepad.exe"
keymap.setFont("ＭＳ ゴシック", 12)

####################################################################################################
## 機能オプションの選択
####################################################################################################
# [section-options] --------------------------------------------------------------------------------

# IMEの設定（次の設定のいずれかを有効にする）
# fc.ime = "old_Microsoft_IME"
# fc.ime = "new_Microsoft_IME"
# fc.ime = "Google_IME"
fc.ime = None

# 日本語キーボード設定をした OS 上で英語キーボードを利用するかどうかを指定する
# （True: 使う、False: 使わない）
# （False に設定した場合でも、OS の設定が日本語キーボードになっていれば、ランチャーメニュー
#   の一番最後に表示されるメニューからキーボード種別を切り替えることができます）
fc.use_usjis_keyboard_conversion = False

# IME の状態をテキスト カーソル インジケーターの色で表現するかどうかを指定する
# （True: 表現する、False: 表現しない）
# （テキスト カーソル インジケーターを利用するには、次のページを参考とし設定を行ってください
#   https://faq.nec-lavie.jp/qasearch/1007/app/servlet/relatedqa?QID=022081）
fc.use_ime_status_cursor_color = False

# IME が ON のときのテキスト カーソル インジケーターの色を指定する
fc.ime_on_cursor_color = 0x00C800 # 濃い緑

# IME が OFF のときのテキスト カーソル インジケーターの色を指定する
fc.ime_off_cursor_color = 0x0000FF # 赤

# 追加機能オプションの設定
fc.use_clipboardList = False
fc.use_lancherList = False
fc.use_edit_mode = False
fc.use_real_emacs = False
fc.use_change_keyboard = False

# 追加オプション
fc.use_usjp_hack = False
import platform, os
nodename = platform.uname()[1]
if re.match(r"^VPC-[A-Z]\d\d[A-Z]\d+$", nodename):
    if os_keyboard_type == "JP" and os.getenv("ViewClient_Keyboard.Type") == "4":
        fc.use_usjis_keyboard_conversion = True

####################################################################################################
## 基本設定
####################################################################################################
# [section-base-1] ---------------------------------------------------------------------------------

# すべてのキーマップを透過（スルー）するアプリケーションソフトを指定する（全ての設定に優先する）
# （keymap_base、keymap_global を含むすべてのキーマップをスルーします）
fc.transparent_target  += [
    "Game.exe",            # Some games...
    "retroarch.exe",       # RetroArch
    "np2w.exe",            # NekoProject II/w
    "np21w.exe",           # NekoProject 21/w
    "NP2kai_windows.exe",  # NekoProject II kai
    "NP21kai_windows.exe", # NekoProject 21 kai
                          ]

# すべてのキーマップを透過（スルー）するウィンドウのクラスネームを指定する（全ての設定に優先する）
# （keymap_base、keymap_global を含むすべてのキーマップをスルーします）
fc.transparent_target_class += []

# Emacs のキーバインドにするウィンドウのクラスネームを指定する（fc.not_emacs_target の設定より優先する）
fc.emacs_target_class   = []                   # 機能を無効にする

# Emacs のキーバインドに“したくない”アプリケーションソフトを指定する
# （Keyhac のメニューから「内部ログ」を ON にすると processname や classname を確認することができます）
fc.not_emacs_target    += [
    "TurboVNC.exe",        # TurboVNC
    "mstsc.exe",           # Remote Desktop
    "vmware-view.exe",     # VMware Horizon 
    "wfica32.exe",         # Citrix Receiver
    "VirtualBox.exe",      # VirtualBox
    "np2w.exe",            # NekoProject II/w
    "np21w.exe",           # NekoProject 21/w
    "NP2kai_windows.exe",  # NekoProject II kai
    "NP21kai_windows.exe", # NekoProject 21 kai
    "SL9821.exe",          # SL9821
    "xm6i.exe",            # XM6i
    "XM8.exe",             # XM8
    "BasiliskII.exe",      # BasiliskII
    "SheepShaver.exe",     # SheepShaver
    "Game.exe",            # Some games...
    "retroarch.exe",       # RetroArch
    "Fusion.exe",          # Kega Fusion
                          ]

# IME の切り替え“のみをしたい”アプリケーションソフトを指定する
# （指定できるアプリケーションソフトは、not_emacs_target で（除外）指定したものからのみとなります）
fc.ime_target          += [
    "AFXW.EXE",            # AFXw
    "WINWORD.EXE",         # Word
    "POWERPNT.EXE",        # PowerPoint
    "EXCEL.EXE",           # Excel
    "VISIO.EXE",           # Visio
    "wpa.exe",             # WPS office (Writer)
    "et.exe",              # WPS office (Spredsheet)
    "wpp.exe",             # WPSOffice (Presentation)
    "cmd.exe",             # cmd
    "mintty.exe",          # mintty
    "ckw.exe",             # ckw
    "ConEmu.exe",          # ConEmu2
    "ConEmu64.exe",        # ConEmu2 (64bit)
    "RLogin.exe",          # RLogin
    "nyaos.exe",           # nyaos.exe
    "nyagos.exe",          # nyagos.exe
    "gvim.exe",            # GVim
    "eclipse.exe",         # Eclipse
    "VCExpress.exe",       # VC++ 2008 Express
    "VCSExpress.exe",      # VC# 2008 Express
    "studio.exe",          # Android Studio
    "studio64.exe",        # Android Studio (64bit)
    "idea.exe",            # IntelliJ
    "idea64.exe",          # IntelliJ (64bit)
    "netbeans.exe",        # NetBeans
    "netbeans64.exe",      # NetBeans (64bit)
    "inkscape.exe",        # Inkscape
    "gimp.exe",            # Gimp
    "yEd.exe",             # yEd Graph Editor
    "eeschema.exe",        # KiCAD
    "pcbnew.exe",          # KiCAD
    "cvpcb.exe",           # KiCAD
    "pcb_calculator.exe",  # KiCAD
    "gerbview.exe",        # KiCAD
    "Capture.exe",         # OrCAD
    "JabRef.exe",          # JabRef
    "scad3.exe",           # LTspice IV
    "XVIIx86.exe",         # LTspice XVII
    "XVIIx64.exe",         # LTspice XVII (64bit)
    "bsch3v.exe",          # BSch3V
    "LCoV.exe",            # BSch3V
                          ]
for t in fc.ime_target:
    if t not in fc.not_emacs_target:
        fc.not_emacs_target += [ t ]

# Ctrl-m 等のみを書き換える特殊マップを使うアプリを指定する。
fc.ctrlm_target = [
    "firefox.exe",         # Firefox
]
for t in fc.ctrlm_target:
    if t not in fc.not_emacs_target:
        fc.not_emacs_target += [ t ]

# キーマップ毎にキー設定をスキップするキーを指定する
# （リストに指定するキーは、define_key の第二引数に指定する記法のキーとしてください。"A-v" や "C-v"
#   のような指定の他に、"M-f" や "Ctl-x d" などの指定も可能です。"M-g*" のようにワイルドカードも
#   利用することができます。ワイルドカード文字をエスケープしたい場合は、[] で括ってください。）
# （ここで指定したキーに新たに別のキー設定をしたいときには、「-2」が付くセクション内で define_key2
#   関数を利用して定義してください）
fc.skip_settings_key    = {"keymap_base"      : ["*W-g"], # ベース Keymap
                           "keymap_global"    : [],       # グローバル Keymap
                           "keymap_emacs"     : [],       # Emacs キーバインド対象アプリ用 Keymap
                           "keymap_vscode"    : [],       # Emacs キーバインド VSCode 拡張用 Keymap
                           "keymap_ime"       : [],       # IME 切り替え専用アプリ用 Keymap
                           "keymap_ei"        : [
                               "C-b", "C-f", "C-p", "C-n", "C-a", "C-e",
                               "Back", "C-h", "Delete", "C-d",
                               "Enter", "C-m", "Tab",
                           ],                             # Emacs 日本語入力モード用 Keymap
                           "keymap_tsw"       : [],       # タスク切り替え画面用 Keymap
                           "keymap_lw"        : [],       # リストウィンドウ用 Keymap
                           }

# Emacs のキーバインドにするアプリケーションソフトで、Emacs キーバインドから除外するキーを指定する
# （リストに指定するキーは、Keyhac で指定可能なマルチストロークではないキーとしてください。
#   Fakeymacs の記法の "M-f" や "Ctl-x d" などの指定はできません。"A-v"、"C-v" などが指定可能です。）
# （ここで指定しなくとも、左右のモディファイアキーを使い分けることで入力することは可能です）
fc.emacs_exclusion_key  = {"chrome.exe"       : ["C-l", "C-t"],
                           "msedge.exe"       : ["C-l", "C-t"],
                           "firefox.exe"      : ["C-l", "C-t"],
                           "Code.exe"         : ["C-S-b", "C-S-f", "C-S-p", "C-S-n", "C-S-a", "C-S-e"],
                           "OUTLOOK.EXE"      : ["C-k"], # complete of address
                           }

# 左右どちらの Ctrl キーを使うかを指定する（"L": 左、"R": 右）
fc.side_of_ctrl_key = "L"
# fc.side_of_ctrl_key = "R"

# C-i キーを Tab キーとして使うかどうかを指定する（True: 使う、False: 使わない）
fc.use_ctrl_i_as_tab = True

# Esc キーを Meta キーとして使うかどうかを指定する（True: 使う、False: 使わない）
# （True（Meta キーとして使う）に設定されている場合、ESC の二回押下で ESC が入力されます）
fc.use_esc_as_meta = True

# C-[ キーを Meta キーとして使うかどうかを指定する（True: 使う、False: 使わない）
# （True（Meta キーとして使う）に設定されている場合、C-[ の二回押下で ESC が入力されます）
fc.use_ctrl_openbracket_as_meta = True

# Ctl-x プレフィックスキーに使うキーを指定する
# （Ctl-x プレフィックスキーのモディファイアキーは、Ctrl または Alt のいずれかから指定してください）
fc.ctl_x_prefix_key = "C-x"
# fc.ctl_x_prefix_key = "A-x"

# スクロールに使うキーの組み合わせ（Up、Down の順）を指定する
# fc.scroll_key = None # PageUp、PageDown キーのみを利用する
fc.scroll_key = ["M-v", "C-v"]

# Emacs 日本語入力モードを使うかどうかを指定する（True: 使う、False: 使わない）
fc.use_emacs_ime_mode = True

# Emacs 日本語入力モードが有効なときに表示するバルーンメッセージを指定する
# fc.emacs_ime_mode_balloon_message = None
fc.emacs_ime_mode_balloon_message = "▲"

# IME の状態を表示するバルーンメッセージを表示するかどうかを指定する（True: 表示する、False: 表示しない）
fc.use_ime_status_balloon = True

# IME をトグルで切り替えるキーを指定する（複数指定可）
fc.toggle_input_method_key = [
    "A-S-Space",
    "A-C-Space",
    "W-Space",
    "W-(127)",
]

#---------------------------------------------------------------------------------------------------
# IME を切り替えるキーの組み合わせ（disable、enable の順）を指定する（複数指定可）
# （toggle_input_method_key のキー設定より優先します）
fc.set_input_method_key = []

## 日本語キーボードを利用している場合、<無変換> キーで英数入力、<変換> キーで日本語入力となる
#fc.set_input_method_key += [["(29)", "(28)"]]

## 日本語キーボードを利用している場合、<Ａ> キーで英数入力、<あ> キーで日本語入力となる
## （https://docs.microsoft.com/ja-jp/windows-hardware/design/component-guidelines/keyboard-japan-ime）
# fc.set_input_method_key += [["(26)", "(22)"]]

## LAlt の単押しで英数入力、RAlt の単押しで日本語入力となる
## （JetBrains 製の IDE でこの設定を利用するためには、ツールボタンをオンにする必要があるようです。
##   設定は、View -> Appearance -> Tool Window Bars を有効にしてください。）
# fc.set_input_method_key += [["O-LAlt", "O-RAlt"]]

## C-j や C-j C-j で 英数入力となる（toggle_input_method_key の設定と併せ、C-j C-o で日本語入力となる）
# fc.set_input_method_key += [["C-j", None]]

## C-j で英数入力、C-o で日本語入力となる（toggle_input_method_key の設定より優先）
# fc.set_input_method_key += [["C-j", "C-o"]]

## C-j で英数入力、C-i で日本語入力となる（C-i が Tab として利用できなくなるが、トグルキー C-o との併用可）
# fc.set_input_method_key += [["C-j", "C-i"]]
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Emacs 日本語入力モードを利用する際に、IME のショートカットを置き換えるキーの組み合わせ
# （置き換え先、置き換え元）を指定する
# （「ことえり」のキーバインドを利用するための設定例です。Google 日本語入力で「ことえり」の
#   キー設定になっている場合には不要ですが、設定を行っていても問題はありません。）
fc.emacs_ime_mode_key = []
#fc.emacs_ime_mode_key += [["C-s", "Left"],    # 文節を縮める
#                          ["C-d", "Right"],   # 文節を伸ばす
#                          ["C-j", "F6"],      # ひらがなに変換
#                          ["C-k", "F7"],      # 全角カタカナに変換
#                          ["C-l", "F9"],      # 全角英数に表示切替
#                          ["C-;", "F8"]]      # 半角に変換

#if is_japanese_keyboard:
#    fc.emacs_ime_mode_key += [["C-:", "F10"]] # 半角英数に表示切替
#else:
#    fc.emacs_ime_mode_key += [["C-'", "F10"]] # 半角英数に表示切替

## IME の「単語登録」プログラムを起動するキーを指定する
fc.word_register_key = None

if is_japanese_keyboard:
    keymap.replaceKey("(28)", "Space")
    keymap.replaceKey("(29)", "Space")
    keymap.replaceKey("(242)", "Space")
    keymap.replaceKey("Apps", "RAlt")
#---------------------------------------------------------------------------------------------------

# アプリケーションキーとして利用するキーを指定する
# （修飾キーに Alt は使えないようです）
fc.application_key = None
# fc.application_key = "O-RCtrl"

# 数引数の指定に Ctrl+数字キーを使うかを指定する（True: 使う、False: 使わない）
# （False に指定しても、C-u 数字キーで数引数を指定することができます）
fc.use_ctrl_digit_key_for_digit_argument = False

# 表示しているウィンドウの中で、一番最近までフォーカスがあったウィンドウに移動するキーを指定する
fc.other_window_key = "A-o"

# アクティブウィンドウを切り替えるキーの組み合わせ（前、後 の順）を指定する（複数指定可）
# （A-Esc キーの動作とは異なり、仮想デスクトップを跨ぎ、最小化されていないウィンドウを順に切り替え
#   ます。初期設定は ["A-p", "A-n"] としていますが、Emacs の shell-mode のキーバインドなどと設定が
#   被る場合には、["A-S-p", "A-S-n"] などの異なる設定とするか、Emacs 側に次の設定を入れて、Emacs 側
#   のキーの設定を置き換えてご利用ください。
#     (define-key key-translation-map (kbd "M-S-p") (kbd "M-p"))
#     (define-key key-translation-map (kbd "M-S-n") (kbd "M-n"))
#  ）
fc.window_switching_key = []
fc.window_switching_key += [["A-p", "A-n"]]
# fc.window_switching_key += [["A-S-p", "A-S-n"]]
# fc.window_switching_key += [["A-Up", "A-Down"]]

# クリップボードリストを起動するキーを指定する
fc.clipboardList_key = "A-y"

# ランチャーリストを起動するキーを指定する
fc.lancherList_key = "A-l"

# Microsoft Excel のセル内で改行を選択可能かを指定する（True: 選択可、False: 選択不可）
# （kill_line 関数の挙動を変えるための変数です。Microsoft Excel 2019 以降では True にして
#   ください。）
fc.is_newline_selectable_in_Excel = True

# ゲームなど、キーバインドの設定を極力行いたくないアプリケーションソフト（プロセス名称と
# クラス名称の組み合わせ（ワイルドカード指定可））を指定する
# （keymap_global 以外のすべてのキーマップをスルーします。ゲームなど、Keyhac によるキー設定と
#   相性が悪いアプリケーションソフトを指定してください。keymap_base の設定もスルーするため、
#   英語 -> 日本語キーボード変換の機能が働かなくなることにご留意ください。）
# （msrdc.exe の行の有効化の必要性については、次のコミットの説明を参照してください。
#   https://github.com/smzht/fakeymacs/commit/5ceb921bd754ce348f9cd79b6606086916520945）
fc.game_app_list        = [["ffxiv_dx11.exe", "*"],            # FINAL FANTASY XIV
                           # ["msrdc.exe",      "RAIL_WINDOW"],  # WSLg
                           ]

# [section-base-2] ---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# logicool keyboard for iPad
keymap.replaceKey("(172)", "Escape")
keymap.replaceKey("(170)", "(163)")

# emacs ime keymap
if fc.use_emacs_ime_mode:
    ## 「IME の切り替え」のキー設定
    for key in fc.toggle_input_method_key:
        define_key(keymap_ei, key, ei_disable_input_method)
    ## 「IME の切り替え」のキー設定
    for disable_key, _ in fc.set_input_method_key:
        if disable_key:
            define_key(keymap_ei, disable_key, ei_disable_input_method)

#---------------------------------------------------------------------------------------------------
# CTRL-m keymap

# input method と ctrl-h/j/mの切り替え"のみをしたい"アプリケーションソフトを指定する（True を返す）
def is_ctrlm_target(wnd, fc=fc):
    if wnd.getProcessName() in fc.ctrlm_target:
        return True
    return False
if fc.use_emacs_ime_mode:
    def is_ctrlm_target_wo_ime(wnd, fc=fc,
                               is_emacs_ime_mode=is_emacs_ime_mode,
                               is_ctrlm_target=is_ctrlm_target):
        if is_emacs_ime_mode(wnd):
            return False
        return is_ctrlm_target(wnd)
    keymap_ctrlm = keymap.defineWindowKeymap(check_func=is_ctrlm_target_wo_ime)
else:
    keymap_ctrlm = keymap.defineWindowKeymap(check_func=is_ctrlm_target)

## 数字キーの設定
for key in range(10):
    s_key = str(key)
    define_key(keymap_ctrlm,        s_key, self_insert_command2(       s_key))
    define_key(keymap_ctrlm, "S-" + s_key, self_insert_command2("S-" + s_key))

## アルファベットキーの設定
for vkey in range(VK_A, VK_Z + 1):
    s_vkey = "({})".format(vkey)
    define_key(keymap_ctrlm,        s_vkey, self_insert_command2(       s_vkey))
    define_key(keymap_ctrlm, "S-" + s_vkey, self_insert_command2("S-" + s_vkey))

## 特殊文字キーの設定
for vkey in [VK_OEM_MINUS, VK_OEM_PLUS, VK_OEM_COMMA, VK_OEM_PERIOD,
             VK_OEM_1, VK_OEM_2, VK_OEM_3, VK_OEM_4, VK_OEM_5, VK_OEM_6, VK_OEM_7, VK_OEM_102]:
    s_vkey = "({})".format(vkey)
    define_key(keymap_ctrlm,        s_vkey, self_insert_command2(       s_vkey))
    define_key(keymap_ctrlm, "S-" + s_vkey, self_insert_command2("S-" + s_vkey))

## 「IME の切り替え」のキー設定
define_key(keymap_emacs, "(243)",  toggle_input_method)
define_key(keymap_emacs, "(244)",  toggle_input_method)
define_key(keymap_ime,   "(243)",  toggle_input_method)
define_key(keymap_ime,   "(244)",  toggle_input_method)
define_key(keymap_ctrlm, "(243)",  toggle_input_method)
define_key(keymap_ctrlm, "(244)",  toggle_input_method)

define_key(keymap_emacs, "A-(25)", toggle_input_method)
define_key(keymap_ime,   "A-(25)", toggle_input_method)
define_key(keymap_ctrlm, "A-(25)", toggle_input_method)
    
## 「カーソル移動」のキー設定
define_key(keymap_ctrlm, "C-p",   reset_search(reset_undo(reset_counter(mark(repeat(previous_line), False)))))
define_key(keymap_ctrlm, "C-n",   reset_search(reset_undo(reset_counter(mark(repeat(next_line), False)))))

## 「カット / コピー / 削除 / アンドゥ」のキー設定
define_key(keymap_ctrlm, "C-h",   reset_search(reset_undo(reset_counter(reset_mark(repeat2(delete_backward_char))))))
define_key(keymap_ctrlm, "C-d",   reset_search(reset_undo(reset_counter(reset_mark(repeat2(delete_char))))))

## 「その他」のキー設定
define_key(keymap_ctrlm, "C-m",   reset_undo(reset_counter(reset_mark(repeat(newline)))))
define_key(keymap_ctrlm, "C-j",   reset_undo(reset_counter(reset_mark(newline_and_indent))))

## 「IME の切り替え」のキー設定（上書きされないように再度設定する）
if fc.toggle_input_method_key:
    for key in fc.toggle_input_method_key:
        define_key(keymap_emacs, key, toggle_input_method)
        define_key(keymap_ime,   key, toggle_input_method)
        define_key(keymap_ctrlm, key, toggle_input_method)

#---------------------------------------------------------------------------------------------------
####################################################################################################
## クリップボードリストの設定
####################################################################################################
# [section-clipboardList-1] ------------------------------------------------------------------------

# [section-clipboardList-2] ------------------------------------------------------------------------

####################################################################################################
## ランチャーリストの設定
####################################################################################################
# [section-lancherList-1] --------------------------------------------------------------------------

# [section-lancherList-2] --------------------------------------------------------------------------

####################################################################################################
## 拡張機能の設定
####################################################################################################
# [section-extensions] -----------------------------------------------------------------------------

# https://github.com/smzht/fakeymacs/blob/master/fakeymacs_manuals/extensions.org

# --------------------------------------------------------------------------------------------------

# Chrome 系ブラウザで Ctl-x C-b を入力した際、Chrome の拡張機能 Quick Tabs を起動する
if 0:
    fc.chrome_list= ["chrome.exe",
                     "msedge.exe"]
    fc.quick_tabs_shortcut_key = "A-q"
    exec(readConfigExtension(r"chrome_quick_tabs\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# Emacs の shell-command-on-region の機能をサポートする
if 0:
    fc.unix_tool = "WSL"
    # fc.unix_tool = "MSYS2"
    # fc.unix_tool = "Cygwin"
    # fc.unix_tool = "BusyBox"
    # fc.bash_options = []
    fc.bash_options = ["-l"]
    exec(readConfigExtension(r"shell_command_on_region\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# VSCode 用のキーの設定を行う
if 0:
    fc.vscode_target  = ["Code.exe"]
    fc.vscode_target += ["chrome.exe",
                         "msedge.exe",
                         "firefox.exe",
                         ]

    # fc.vscode_prefix_key = [["C-;", "C-A-;"]]
    fc.use_ctrl_atmark_for_mark = False
    fc.use_direct_input_in_vscode_terminal = False
    fc.esc_mode_in_keyboard_quit = 1

    # VSCode Extension 用のキーの設定を行う
    fc.vscode_dired = False
    fc.vscode_recenter = False
    fc.vscode_recenter2 = False
    fc.vscode_occur = False
    fc.vscode_quick_select = True
    fc.vscode_input_sequence = True
    fc.vscode_insert_numbers = True
    fc.vscode_keyboard_macro = False
    fc.vscode_filter_text = False

    exec(readConfigExtension(r"vscode_key\config.py"), dict(globals(), **locals()))
    # vscode_extensions\config.py は、vscode_key\config.py 内部から呼ばれている

# --------------------------------------------------------------------------------------------------

# Everything を起動するキーを指定する
if 0:
    exec(readConfigExtension(r"everything\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# ブラウザをポップアップしてから、ブラウザのショートカットキーを入力するキーを設定する
if 0:
    fc.browser_list= ["chrome.exe",
                      "msedge.exe",
                      "firefox.exe"]
    exec(readConfigExtension(r"browser_key\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 指定したアプリケーションソフトに F2（編集モード移行）を割り当てるキーを設定する
if 0:
    exec(readConfigExtension(r"edit_mode\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# Emacs の場合、IME 切り替え用のキーを C-\ に置き換える
if 0:
    exec(readConfigExtension(r"real_emacs\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 英語キーボード設定をした OS 上で日本語キーボードを利用する場合の設定を行う
if 0:
    fc.change_keyboard_startup = "US"
    # fc.change_keyboard_startup = "JP"
    exec(readConfigExtension(r"change_keyboard\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 日本語キーボード設定をした OS 上で日本語キーボードを英語配列で利用する場合の設定を行う
if 0:
    fc.change_keyboard2_startup = "US"
    # fc.change_keyboard2_startup = "JP"
    exec(readConfigExtension(r"change_keyboard2\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# クリップボードに格納したファイルもしくはフォルダのパスを emacsclient で開く
if 0:
    fc.emacsclient_name = r"<emacsclient プログラムをインストールしている Windows のパス>\wslclient-n.exe"
    exec(readConfigExtension(r"emacsclient\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 指定したキーを押下したときに IME の状態を表示する
if 0:
    fc.pop_ime_balloon_key = ["C-;"]
    # fc.pop_ime_balloon_key = ["O-" + fc.side_of_ctrl_key + "Ctrl"] # Ctrl キーの単押し
    exec(readConfigExtension(r"pop_ime_balloon\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 60% US キーボードのキー不足（Delete キー、Backquote キー不足）の対策を行う
if 0:
    exec(readConfigExtension(r"compact_keyboard\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 半角と全角の入力を間違えた際、入力モードの切り替えと入力文字の変換を行う
if 0:
    exec(readConfigExtension(r"zenkaku_hankaku\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# Emacs キーバインドを利用しない設定のアプリで、メニューの操作用の Emacs キーバインドを設定する
if 0:
    fc.menu_target= ["ttermpro.exe", # TeraTerm
                     ]
    exec(readConfigExtension(r"menu_key\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 現在アクティブなウィンドウと同じプロセスのウィンドウを順に切り替えるキーを設定する
if 0:
    exec(readConfigExtension(r"window_switching_key\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# YouTube で Space による停止、再生が正しく機能しないことの暫定的な対策を行う
# （次にある SpaceFN の拡張機能を有効にする場合は、本拡張機能は OFF としてください）
if 1:
    exec(readConfigExtension(r"youtube_space_key\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------
# SpaceFN を実現する設定を行う
# （本機能を有効にする場合は、上記の YouTube の対策の拡張機能は OFF としてください）
if 0:
    fc.space_fn_key = "Space"
    # fc.space_fn_key = "(29)" # 「無変換」キー
    # fc.space_fn_window_keymap_list = [keymap_emacs, keymap_ime]
    # fc.space_fn_window_keymap_list += [keymap_ei]
    # fc.space_fn_window_keymap_list += [fakeymacs.keymap_vscode]
    exec(readConfigExtension(r"space_fn\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------
