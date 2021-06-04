import dotenv
import pytest


@pytest.fixture(autouse=True)
def setup():
    dotenv.load_dotenv()


def test_send_slack_message():
    import slack_message
    ss = slack_message.SlackSender()

    ss.send_slack_message("""\
test _ end@email.com markup with spaces_  2 _ not trimed and not email _ *bold*    :visage_souriant_avec_une_larme: :smiling_face_with_tear:
""")
