import time
import math
from datetime import datetime, timedelta

def snapSchedule(minimumMinutes: int = 30, snapMinutes: tuple[int, int] = (0, 30)) -> dict:
    '''Powerful snap scheduler (will update this docstring later)'''
    now = datetime.now()
    minimum = now + timedelta(minutes=minimumMinutes)
    snapMinutes = sorted(snapMinutes)

    for snap in snapMinutes:
        if minimum.minute < snap:
            scheduled = minimum.replace(minute=snap, second=0, microsecond=0)
            break
    else:
        scheduled = (minimum.replace(minute=0, second=0, microsecond=0)
                     + timedelta(hours=1))

    return {
        'now': now,
        'minimum': minimum,
        'scheduled': scheduled,
        'formatted': scheduled.strftime('%I:%M %p')
    }
