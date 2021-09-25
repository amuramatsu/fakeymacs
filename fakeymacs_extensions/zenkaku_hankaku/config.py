﻿# -*- mode: python; coding: utf-8-with-signature-dos -*-

####################################################################################################
## 半角と全角の入力を間違えた際、入力モードの切り替えと入力文字の変換を行う（Emacs日本語入力モード用）
####################################################################################################

try:
    # 設定されているか？
    fc.zenkaku_hankaku_key
except:
    # 本機能を利用するためのキーを指定する
    fc.zenkaku_hankaku_key = "C-Enter"

if fc.use_emacs_ime_mode:

    def hankaku_henkan():
        # 半角英数字に変換し、確定する
        self_insert_command("F10", "Enter")()

        # IME を OFF にする
        ei_disable_input_method()

    def zenkaku_henkan():
        # Microsoft Excel の場合、セルの編集中（ウインドウのタイトル文字列が空）でなければ終了する
        if checkWindow("EXCEL.EXE", "EXCEL*", "?*"):
            return

        if fakeymacs.forward_direction is None:
            # カーソル位置を変えないように、カーソルの前の word を選択する
            backward_word()
            mark2(forward_word, True)()

        # リージョンをクリップボードに格納する
        copyRegion()
        delay()

        clipboard_text = getClipboardText()

        # 半角英数字か？（特殊文字は key への変換が難しいので対象外とする）
        if clipboard_text.encode('utf-8').isalnum():

            # 選択されているリージョンを削除し、IME を ON にする
            self_insert_command("Delete")()
            enable_input_method()

            # クリックボードに格納されている英数字を一文字ずつ key として入力する
            for key in clipboard_text:
                keymap.InputKeyCommand(key)()

            # Emacs日本語入力モードを ON にする
            enable_emacs_ime_mode()
        else:
            # リージョンを解除する
            resetRegion()

    define_key(keymap_ei,    fc.zenkaku_hankaku_key, hankaku_henkan)
    define_key(keymap_emacs, fc.zenkaku_hankaku_key, reset_undo(reset_counter(reset_mark(zenkaku_henkan))))