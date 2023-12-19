from mcdreforged.api import command
from mcdreforged.api.types import PluginServerInterface

import os
import json

from .callbacks import *
from .cfg import *

# 初始化
def on_load(server:PluginServerInterface,old):
    check_file()
    reg_command(server=server)


# 注册指令
def reg_command(server :PluginServerInterface):
    b = command.SimpleCommandBuilder()
    b.command("!!pdb back <player> <slot>",callback=callbacks.data_backer)
    b.command("!!pdb list",callback=callbacks.list_slots)
    b.command("!!pdb del <slot>",callback=callbacks.del_slot)
    b.command("!!pdb make",callback=callbacks.save_backup)
    b.command("!!pdb help")

    b.arg("player",command.Text)
    b.arg("slot",command.Text)
    b.register(server=server)
    return

# 检查配置文件
def check_file():
    if os.path.exists( cfg.get_cfg_name() )==False:
        cfg_file = open( cfg.get_cfg_name(), "w" )
        json.dump( cfg.default_cfg, cfg_file,sort_keys=False, indent=4, separators=(',', ':') )
        cfg_file.close()

    with open(cfg.get_cfg_name(),"r") as cfg_file:
        cfg.global_cfg = json.load(cfg_file)

    if os.path.exists(cfg.get_des_path())==False:
        os.mkdir(cfg.get_des_path())