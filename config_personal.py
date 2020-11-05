# -*- mode: python; coding: utf-8-with-signature-dos -*-

# https://stackoverflow.com/questions/2904274/globals-and-locals-in-python-exec
# https://docs.python.org/3/library/functions.html?highlight=exec%20global#exec

# 本ファイルは、config_personal.py というファイル名にすることで個人設定ファイルとして機能します。
# 本ファイルの設定には [] で括られたセクション名が定義されており、その単位で config.py の中に設定
# が取り込まれ、exec関数により実行されます。config.py ファイル内の exec関数をコールしているところ
# を検索すると、何のセクションがどこで読み込まれるかが分かると思います。

# 本ファイルはサンプルファイルです。本ファイルに記載のない設定でも、config.py から設定を取り込み、
# カスタマイズしてご利用ください。

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

# IMEの設定（３つの設定のいずれか一つを True にする）
# IMEの設定（次の設定のいずれかを有効にする）
# fc.ime = "old_Microsoft_IME"
# fc.ime = "new_Microsoft_IME"
# fc.ime = "Google_IME"
fc.ime = None

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
    if is_japanese_keyboard and os.getenv("ViewClient_Keyboard.Type") == "4":
        fc.use_usjp_hack = True

####################################################################################################
## 基本設定
####################################################################################################
# [section-base-1] ---------------------------------------------------------------------------------

# Emacs のキーバインドにするウィンドウのクラスネームを指定する（全ての設定に優先する）
fc.emacs_target_class   = []                   # 機能を無効にする

# Emacs のキーバインドに“したくない”アプリケーションソフトを指定する
# （Keyhac のメニューから「内部ログ」を ON にすると processname や classname を確認することができます）
fc.not_emacs_target    += [
    "TurboVNC.exe",        # TurboVNC
    "mstsc.exe",           # Remote Desktop
    "vmware-view.exe",     # VMware Horizon 
    "wfica32.exe",         # Citrix Receiver
    "VirtualBox.exe",      # VirtualBox
                          ]

# IME の切り替え“のみをしたい”アプリケーションソフトを指定する
# （指定できるアプリケーションソフトは、not_emacs_target で（除外）指定したものからのみとなります）
fc.ime_target          += [
    "AFXW.EXE",            # AFXw
    "WINWORD.EXE",         # Word
    "POWERPNT.EXE",        # PowerPoint
    "EXCEL.EXE",           # Excel
    "wpa.exe",             # WPS office (Writer)
    "et.exe",              # WPS office (Spredsheet)
    "wpp.exe",             # WPSOffice (Presentation)
    "cmd.exe",             # cmd
    "mintty.exe",          # mintty
    "ckw.exe",             # ckw
    "ConEmu.exe",          # ConEmu2
    "ConEmu64.exe",        # ConEmu2 (64bit)
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
    "gerbview.exe,"        # KiCAD
    "Capture.exe",         # OrCAD
    "JabRef.exe",          # JabRef
    "scad3.exe",           # LTspice IV
    "XVIIx86.exe",         # LTspice XVII
    "XVIIx64.exe",         # LTspice XVII (64bit)
    "bsch3v.exe",          # BSch3V
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
#   のような指定の他に、"M-f" や "Ctl-x d" などの指定も可能です。）
# （ここで指定したキーに新たに別のキー設定をしたいときには、「-2」が付くセクション内で define_key2
#   関数を利用して定義してください）
fc.skip_settings_key    = {"keymap_global"    : [],
                           "keymap_emacs"     : [],
                           "keymap_ime"       : [],
                           "keymap_ei"        : [
                               "C-b", "C-f", "C-p", "C-n", "C-a", "C-e",
                               "Back", "C-h", "Delete", "C-d",
                               "Enter", "C-m", "Tab",
                           ],
                           "keymap_tsw"       : [],
                           "keymap_lw"        : [],
                          }

# Emacs のキーバインドにするアプリケーションソフトで、Emacs キーバインドから除外するキーを指定する
# （リストに指定するキーは、Keyhac で指定可能なマルチストロークではないキーとしてください。
#   Fakeymacs の記法の "M-f" や "Ctl-x d" などの指定はできません。"A-v"、"C-v" などが指定可能です。）
fc.emacs_exclusion_key  = {"chrome.exe"       : ["C-l", "C-t"],
                           "msedge.exe"       : ["C-l", "C-t"],
                           "firefox.exe"      : ["C-l", "C-t"],
                           # "Code.exe"         : ["C-S-b", "C-S-f", "C-S-p", "C-S-n", "C-S-a", "C-S-e"],
                           "OUTLOOK.EXE"      : ["C-k"], # complete of address
                          }

# 左右どちらの Ctrlキーを使うかを指定する（"L": 左、"R": 右）
# fc.side_of_ctrl_key = "R"

# Escキーを Metaキーとして使うかどうかを指定する（True: 使う、False: 使わない）
# （True（Metaキーとして使う）に設定されている場合、ESC の二回押下で ESC が入力されます）
fc.use_esc_as_meta = True

#---------------------------------------------------------------------------------------------------
#
# IME をトグルで切り替えるキーを指定する（複数指定可）
fc.toggle_input_method_key = [
    "A-S-Space",
    "A-C-Space",
    "W-Space",
    "W-(127)",
]

# IME を切り替えるキーの組み合わせ（disable、enable の順）を指定する（複数指定可）
# （toggle_input_method_key のキー設定より優先します）
fc.set_input_method_key = []

## 日本語キーボードを利用している場合、<無変換> キーで英数入力、<変換> キーで日本語入力となる
#fc.set_input_method_key += [["(29)", "(28)"]]

## LAlt の単押しで英数入力、RAlt の単押しで日本語入力となる
## （JetBrains 製の IDE でこの設定を利用するためには、ツールボタンをオンにする必要があるようです。
##   設定は、View -> Appearance -> Tool Window Bars を有効にしてください。）
# fc.set_input_method_key += [["O-LAlt", "O-RAlt"]]

## C-j や C-j C-j で 英数入力となる（toggle_input_method_key の設定と併せ、C-j C-o で日本語入力となる）
# fc.set_input_method_key += [["C-j", None]]

## C-j で英数入力、C-o で日本語入力となる（toggle_input_method_key の設定より優先）
# fc.set_input_method_key += [["C-j", "C-o"]]

# Emacs日本語入力モードを利用する際に、IME のショートカットを置き換えるキーの組み合わせ
# （置き換え先、置き換え元）を指定する
# （Microsoft IME で「ことえり」のキーバインドを利用するための設定例です。Google日本語入力で
#   「ことえり」のキー設定になっている場合には不要ですが、設定を行っても問題はありません。）
fc.emacs_ime_mode_key = []
fc.emacs_ime_mode_key += [["C-s", "Left"],      # 文節を縮める
                          ["C-d", "Right"],     # 文節を伸ばす
                          ["C-j", "F6"],          # ひらがなに変換
                          ["C-k", "F7"],          # 全角カタカナに変換
                          ["C-l", "F9"],          # 全角英数に表示切替
                          ["C-Semicolon", "F8"]]  # 半角に変換
if is_japanese_keyboard:
    fc.emacs_ime_mode_key += [["C-Colon", "F10"]] # 半角英数に表示切替
else:
    fc.emacs_ime_mode_key += [["C-Quote", "F10"]] # 半角英数に表示切替

## IME の「単語登録」プログラムを起動するキーを指定する
fc.word_register_key = None

if is_japanese_keyboard:
    keymap.replaceKey("(28)", "Space")
    keymap.replaceKey("(29)", "Space")
    keymap.replaceKey("(242)", "Space")
    keymap.replaceKey("Apps", "RAlt")

#---------------------------------------------------------------------------------------------------

# VSCode の Terminal内 で ４つのキー（Ctrl+k、Ctrl+r、Ctrl+s、Ctrl+y）のダイレクト入力機能を使うか
# どうかを指定する（True: 使う、False: 使わない）
# fc.use_vscode_terminal_key_direct_input = True

# アプリケーションキーとして利用するキーを指定する
# （修飾キーに Alt は使えないようです）
# fc.application_key = "O-RCtrl"
# fc.application_key = "W-m"

# [section-base-2] ---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# VSCode で Extension のインストールが必要な機能は、個人設定ファイルで設定する

if 0:
    # VSCode に vscode-dired Extension をインストールしてお使いください
    # （Ctrl+x f に設定されているキーバインドは、Ctrl+x（Cut）の機能とバッティングするので、削除して
    #   ください（Open Keyboard Shortcuts コマンドで削除可能です）)

    def dired(func=dired):
        if checkWindow("Code.exe", "Chrome_WidgetWin_1"): # VSCode
            # VSCode Command : Open dired buffer
            vscodeExecuteCommand("Op-di-bu")
        else:
            func()

    define_key(keymap_emacs, "Ctl-x d", reset_search(reset_undo(reset_counter(reset_mark(dired)))))

if 0:
    # VSCode に Center Editor Window Extension をインストールしてお使いください

    def recenter(func=recenter):
        if checkWindow("Code.exe", "Chrome_WidgetWin_1"): # VSCode
            # VSCode Command : Center Editor Window
            self_insert_command("C-l")()
        else:
            func()

    define_key(keymap_emacs, "C-l", reset_search(reset_undo(reset_counter(recenter))))

if 0:
    # VSCode に Search in Current File Extension をインストールしてお使いください
    # （アクティビティバーの SEARCH アイコンをパネルのバーにドラッグで持っていくと、検索結果が
    #   パネルに表示されるようになり、使いやすくなります）

    def occur():
        if checkWindow("Code.exe", "Chrome_WidgetWin_1"): # VSCode
            # VSCode Command : Search in Current File
            vscodeExecuteCommand("Se-in-Cu-Fi")

    define_key(keymap_emacs, "Ctl-x C-o", reset_search(reset_undo(reset_counter(reset_mark(occur)))))
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Everything プログラムを起動するキーを指定する

if 0:
    # Everything を起動するキーを指定する
    everything_key = "C-A-v"

    # Everything プログラムを指定する
    everything_name = r"C:\Program Files\Everything\everything.exe"

    def everything():
        keymap.ShellExecuteCommand(None, everything_name, "", "")()

    define_key(keymap_global, everything_key, everything)

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
if fc.use_usjp_hack:
    keymap_usjp = keymap.defineWindowKeymap()

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

## 「IME の切り替え」のキー設定 & US->JP hack
if fc.use_usjp_hack:
    keymap.replaceKey("(221)", "(220)") # \|
    keymap.replaceKey("(192)", "(219)") # [ {
    keymap.replaceKey("(219)", "(221)") # ] }
    for m in (keymap_emacs, keymap_ime, keymap_usjp, keymap_ctrlm):
            define_key(m, "(243)", self_insert_command("S-(192)"))   # `
            define_key(m, "(244)", self_insert_command("S-(192)"))   # `
            define_key(m, "S-(243)", self_insert_command("S-(222)")) # ~
            define_key(m, "S-(244)", self_insert_command("S-(222)")) # ~
            define_key(m, "S-(50)", self_insert_command("(192)"))    # @
            define_key(m, "S-(54)", self_insert_command("(222)"))    # ^
            define_key(m, "S-(55)", self_insert_command("S-(54)"))   # &
            define_key(m, "S-(56)", self_insert_command("S-(186)"))  # *
            define_key(m, "S-(57)", self_insert_command("S-(56)"))   # (
            define_key(m, "S-(48)", self_insert_command("S-(57)"))   # )
            define_key(m, "S-(189)", self_insert_command("S-(226)")) # _
            define_key(m, "(222)", self_insert_command("S-(189)"))   # =
            define_key(m, "S-(222)", self_insert_command("S-(187)")) # +
            define_key(m, "S-(187)", self_insert_command("(186)"))   # :
            define_key(m, "(186)", self_insert_command("S-(55)"))    # '
            define_key(m, "S-(186)", self_insert_command("S-(50)"))  # "
else:
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

# Emacs の shell-command-on-region の機能をサポートする
# fc.Linux_tool = "WSL"
# fc.Linux_tool = "MSYS2"
# fc.Linux_tool = "Cygwin"
# fc.Linux_tool = "BusyBox"
# fc.MSYS2_path = r"C:\msys64"
# fc.Cygwin_path = r"C:\cygwin64"
# exec(readConfigExtension(r"shell_command_on_region\config.py"), dict(globals(), **locals()))

# C-Enter に F2（編集モード移行）を割り当てる
# exec(readConfigExtension(r"edit_mode\config.py"), dict(globals(), **locals()))

# Emacs の場合、IME 切り替え用のキーを C-\ に置き換える
# exec(readConfigExtension(r"real_emacs\config.py"), dict(globals(), **locals()))

# 英語キーボード設定をした OS 上で、日本語キーボードを利用する場合の切り替えを行う
# exec(readConfigExtension(r"change_keyboard\config.py"), dict(globals(), **locals()))
