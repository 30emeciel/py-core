from core import rst

NEW_RESERVATION = "new_reservation_fr.txt"
ARRIVALS_AND_DEPARTURES = "arrivals_and_departures_fr.txt"


def generate_notification_message(template, data):
    tpl = rst.env.get_template(template)
    return tpl.render(data)
