from talon.voice import Context, press, Key
ctx = Context("Bear", bundle="net.shinyfrog.bear")


ctx.keymap(
    {
        "(checkbox|to do)": Key("cmd-t"),
        "select line": [Key("cmd-left"), Key("shift-end")],
        "insert date": Key("cmd-shift-8"),
        "bold":Key("cmd-b"),
        "(italics|italic|italicize)":Key("cmd-i"),
        "(underline)":Key("cmd-u"),
        "strikethrough":Key("shift-cmd-e"),
        "link to": Key("cmd-k"),
        "pullquote": Key("shift-cmd-u"),
        "insert code": Key("option-cmd-c"),
        "code block": Key("ctrl-cmd-c"),
        "(bullet|list)":Key("cmd-l"),
        "(number|numbered list)": Key("cmd-shift-l")
    }
)

