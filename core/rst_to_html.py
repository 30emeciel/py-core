from docutils.core import publish_string
settings_overrides = {

}


def to_html(rst):
    h = publish_string(source=rst, writer_name='html5', settings_overrides=settings_overrides)
    return h.decode()
