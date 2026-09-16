from io import BytesIO
from pyrogram.raw.core.primitives import Int, Long, Bool
from pyrogram.raw.core import TLObject
from typing import Optional, Any

class KeyboardButtonStyle(TLObject):
    """Constructor of :obj:`~pyrogram.raw.base.KeyboardButtonStyle`."""
    
    __slots__ = ["bg_primary", "bg_danger", "bg_success", "icon"]
    
    ID = 0x4FDD3430
    QUALNAME = "types.KeyboardButtonStyle"
    
    def __init__(
        self,
        *,
        bg_primary: Optional[bool] = None,
        bg_danger: Optional[bool] = None,
        bg_success: Optional[bool] = None,
        icon: Optional[int] = None
    ) -> None:
        self.bg_primary = bg_primary  # flags.0?true
        self.bg_danger = bg_danger    # flags.1?true
        self.bg_success = bg_success  # flags.2?true
        self.icon = icon              # flags.3?long
    
    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonStyle":
        flags = Int.read(b)
        return KeyboardButtonStyle(
            bg_primary=True if flags & (1 << 0) else False,
            bg_danger=True if flags & (1 << 1) else False,
            bg_success=True if flags & (1 << 2) else False,
            icon=Long.read(b) if flags & (1 << 3) else None
        )
    
    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        
        flags = 0
        if self.bg_primary: flags |= (1 << 0)
        if self.bg_danger: flags |= (1 << 1)
        if self.bg_success: flags |= (1 << 2)
        if self.icon: flags |= (1 << 3)
        
        b.write(Int(flags))
        
        if self.icon:
            b.write(Long(self.icon))
        
        return b.getvalue()
