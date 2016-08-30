
def add_username_segment(powerline):
    import os

    if powerline.args.shell == 'bash':
        host_prompt = '\\h '
    elif powerline.args.shell == 'zsh':
        host_prompt = '%m '
    else:
        import socket
        host_prompt = '%s ' % socket.gethostname().split('.')[0]

    if powerline.args.shell == 'bash':
        user_prompt = ' \\u'
    elif powerline.args.shell == 'zsh':
        user_prompt = ' %n'
    else:
        user_prompt = ' %s' % os.getenv('USER')

    if os.getenv('USER') == 'root':
        bgcolor = Color.USERNAME_ROOT_BG
    else:
        bgcolor = Color.USERNAME_BG

    powerline.append(user_prompt+'@'+host_prompt, Color.USERNAME_FG, bgcolor)
