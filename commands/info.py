import command_system
from common_func import keyword_gen

def help(keyword=''):
    message = ''
    for command in command_system.command_list:
        message += '{} - {}\n'.format(command.keys[0].upper(),
                                      command.description.lower())
    return message, ''

help_command = command_system.Command()
help_command.keys = keyword_gen('помощь')
help_command.aliases = keyword_gen('помоги', 'help', 'хелп', 'pomosh')
help_command.description = 'Покажу список команд и их описание'
help_command.process = help

def all_commands(keyword=''):
    message = ''
    for command in command_system.command_list:
        # все чётные комманды - это транслит на нечётные
        message += '{}\n'.format(command.keys[0].upper())
        for i in range(0, len(command.aliases), 2):
            message += '{}, '.format(command.aliases[i])
        message = message[:-1] + '.\n'
    return message, ''

all_commands_command = command_system.Command()
all_commands_command.keys = keyword_gen('команды')
all_commands_command.aliases = keyword_gen('все команды', 'список команд')
all_commands_command.description = 'Покажу все команды и их псевдонимы'
all_commands_command.process = all_commands