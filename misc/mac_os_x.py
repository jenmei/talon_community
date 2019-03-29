from talon.voice import Context, press, Key

ctx = Context("mac_os_x")
ctx.keymap(
    {
        "cut": Key("cmd-x"),
        "copy": Key("cmd-c"),
        "paste": Key("cmd-v"),
        "(next tab | goneck)": Key("cmd-shift-]"),
        "((last | previous | preev) tab | gopreev)": Key("cmd-shift-["),
        "undo": Key("cmd-z"),
        "redo": Key("cmd-shift-z"),
        "new tab": Key("cmd-t"),
        "close": Key("cmd-w"),
        "close all tabs": Key("cmd-shift-w"),
        "(view|pick) (emojis|symbols)": Key("ctrl-cmd-space"),
        "force quit": Key("cmd-option-esc"),
        "preferences": Key("cmd-,")
    }
)
