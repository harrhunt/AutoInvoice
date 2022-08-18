import isodate
from datetime import timedelta, datetime, timezone
from clockipy import Clockify


if __name__ == "__main__":
    c = Clockify(
        '',
        '5d753ee8e7fad02673718096',
        '5d753ee8e7fad02673718093',
        '62dae98cb8caf72f9d5b788b'
    )
    today = datetime.now()
    te = c.get_time_entries({
        "project": "5f62625c791d0934305da553",
        "page-size": 4999,
        "start": isodate.datetime_isoformat(
            datetime(today.year, today.month, 1, tzinfo=timezone.utc),
            "%Y-%m-%dT%H:%M:%SZ"
        )
    })
    print(isodate.datetime_isoformat(
        datetime(today.year, today.month, 1, tzinfo=timezone.utc),
        "%Y-%m-%dT%H:%M:%SZ"
    ))
    td = timedelta(0)
    print(te)
    for t in te:
        td += isodate.parse_duration(t['timeInterval']['duration'])
    print((td.days * 24) + (td.seconds / 3600))
    # print(c.get_project_by_name('Precision Pumping'))
