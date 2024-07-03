# -*- coding: utf_8 -*-

from keyhac_clipboard import *
from keyhac_main import keymap
import types
import functools

#==============================================================================
# メソッド置換
#==============================================================================
def replacemethod(target_class):
    def _replacemethod(new_method):
        original = getattr(target_class, new_method.__name__)
        @functools.wraps(original)
        def replaced_method(*args, **kwds):
            return new_method(original, *args, **kwds)
        setattr(
            target_class,
            new_method.__name__,
            replaced_method
        )
        return new_method
    return _replacemethod

#==============================================================================
# cblister_ClipboardHistory._hook_onClipboardChangedへのパッチ
#==============================================================================
@replacemethod(cblister_ClipboardHistory)
def _hook_onClipboardChanged(original, self):
    def onClipboardChanged():
        seq = ckit.getClipboardSequenceNumber()
        if self.seq_number != seq:
            self._push(ckit.getClipboardText())
            self.seq_number = seq
    self.window.delayedCall(onClipboardChanged, 100)

#==============================================================================
# 置き換えた_hook_onClipboardChangedに入れ替える
#==============================================================================
keymap.clipboard_history.enableHook(True)
