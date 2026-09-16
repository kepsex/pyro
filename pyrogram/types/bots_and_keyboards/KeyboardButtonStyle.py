class KeyboardButtonStyle(TLObject):
    __slots__ = ["bg_primary", "bg_danger", "bg_success", "icon"]
    
    ID = 0x4FDD3430
    QUALNAME = "types.KeyboardButtonStyle"
    
    def __init__(self, bg_primary=None, bg_danger=None, bg_success=None, icon=None):
        self.bg_primary = bg_primary   # flags.0 - Biru
        self.bg_danger = bg_danger     # flags.1 - Merah
        self.bg_success = bg_success   # flags.2 - Hijau
        self.icon = icon               # flags.3 - Custom emoji ID
