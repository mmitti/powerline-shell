def add_root_segment(powerline):
    import os
    if os.getenv('USER') == 'root':
        root_tmp = '#'
    else:
        root_tmp = '$'
    root_indicators = {
        'bash': ' \\'+root_tmp+' ',
        'zsh': ' \\'+root_tmp+' ',
        'bare': ' '+root_tmp+' ',
    }
    bg = Color.CMD_PASSED_BG
    fg = Color.CMD_PASSED_FG
    if powerline.args.prev_error != 0:
        fg = Color.CMD_FAILED_FG
        bg = Color.CMD_FAILED_BG
    powerline.append(root_indicators[powerline.args.shell], fg, bg)
