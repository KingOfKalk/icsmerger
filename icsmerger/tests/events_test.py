from icsmerger import merge
from icsmerger.tests.helpers import make_ics


def test_get_events_and_create_calendar():
    events = merge.get_events(make_ics(("1", "One"), ("2", "Two")))
    calendar = merge.create_calendar(events)
    assert sorted(e.name for e in calendar.events) == ["One", "Two"]
    assert "SUMMARY:One" in calendar.serialize()
