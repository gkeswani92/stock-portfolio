import humanreadable as hr
import time


def get_time_since_post(created_at: int):
    time_difference = int(time.time()) - created_at
    if time_difference < 60:
        return (
            f"{hr.Time(str(time_difference), default_unit=hr.Time.Unit.SECOND).seconds:.0f} "
            f"seconds ago"
        )
    elif time_difference < 60 * 60:
        return (
            f"{hr.Time(str(time_difference), default_unit=hr.Time.Unit.SECOND).minutes:.0f} "
            f"minutes ago"
        )
    elif time_difference < 60 * 60 * 24:
        return (
            f"{hr.Time(str(time_difference), default_unit=hr.Time.Unit.SECOND).hours:.0f} "
            f"hours ago"
        )
    else:
        return (
            f"{hr.Time(str(time_difference), default_unit=hr.Time.Unit.SECOND).days:.0f} "
            f"days ago"
        )
