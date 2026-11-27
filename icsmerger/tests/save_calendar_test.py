from icsmerger import merge


def test_save_writes_utf8_without_newline_translation(tmp_path):
    out = tmp_path / "out.ics"
    text = "SUMMARY:Müller\r\nEND:VCALENDAR\r\n"
    merge.save_calendar(text, str(out))
    assert out.read_bytes() == text.encode("utf-8")
