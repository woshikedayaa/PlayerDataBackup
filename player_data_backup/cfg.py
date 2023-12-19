default_cfg = {
    # 备份槽位的数量
    "slot_count":"3",
    # 备份数据来源
    "from":"server/world/playerdata",
    # 备份到哪
    "to":"pdb_data",
    # 备份前要执行的指令 使用 "," 分开
    "before":"kick",
    # 备份后要执行的指令 使用 "," 分开
    "after":""
}

global_cfg = default_cfg

def get_des_path():
    return global_cfg.get("to")

def get_cfg_name():
    return "config/player_data_backup.json"

def get_slot_count():
    return global_cfg.get("slot_count")

def get_from():
    return global_cfg.get("from")

def get_before_command():
    return global_cfg.get("before")

def get_after_command():
    return global_cfg.get("after")