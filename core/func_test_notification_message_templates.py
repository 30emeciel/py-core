from datetime import datetime, timezone

from box import Box

if __name__ == "__main__":
    from notification_message_templates import generate_notification_message, NEW_RESERVATION

    pax = Box({
        "name": "Pax name"
    })
    request = Box({
        "kind": "COLIVING",
        "arrival_date": datetime(2021, 2, 19, tzinfo=timezone.utc),
        "departure_date": datetime(2021, 3, 1, tzinfo=timezone.utc),
        "number_of_nights": 3,
    })
    data = {
        "pax": pax,
        "request": request,
    }
    txt = generate_notification_message(NEW_RESERVATION, data)
    print(txt)

    request = Box({
        "kind": "COWORKING",
        "arrival_date": datetime(2021, 2, 19, tzinfo=timezone.utc),
    })
    data = {
        "pax": pax,
        "request": request,
    }

    txt = generate_notification_message(NEW_RESERVATION, data)
    print(txt)
