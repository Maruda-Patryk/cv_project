import datetime
import pytz

SEND_NOTIFICATION_TASK = [
    (
        [
            {
                'create_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
                'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
            },
            {
                'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
                'create_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc)
            }
        ],
        datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
        [
            {'username': 'Test', 'email': 'test@test.com'},
            {'username': 'Test1', 'email': 'test1@test.com'}
        ],
        True,
        ['test@test.com', 'test1@test.com'],
    ), (
        [
            {'create_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc)},
            {'create_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc)}
        ],
        datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc),
        [
            {'username': 'Test', 'email': 'test@test.com'},
            {'username': 'Test1', 'email': 'test1@test.com'}
        ],
        True,
        ['test@test.com', 'test1@test.com'],
    ), (
        [
            {'last_update_date': datetime.datetime(2021, 2, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc)},
            {'last_update_date': datetime.datetime(2021, 2, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc)}
        ],
        datetime.datetime(2021, 2, 1, 1, 0, 0, tzinfo=pytz.utc),
        [
            {'username': 'Test', 'email': 'test@test.com'},
            {'username': 'Test1', 'email': 'test1@test.com'}
        ],
        True,
        ['test@test.com', 'test1@test.com'],
    ), (
        [
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
        ],
        datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
        [
            {'username': 'Test', 'email': 'test@test.com'},
            {'username': 'Test1', 'email': 'test1@test.com'}
        ],
        True,
        ['test@test.com', 'test1@test.com'],
    ), (
        [
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
        ],
        datetime.datetime(2021, 3, 1, 0, 0, 0, tzinfo=pytz.utc),
        [
            {'username': 'Test', 'email': 'test@test.com'},
            {'username': 'Test1', 'email': 'test1@test.com'}
        ],
        False,
        ['test@test.com', 'test1@test.com'],
    ), (
        [
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
        ],
        datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
        [],
        False,
        ['test@test.com', 'test1@test.com'],
    ), (
        [
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
            {'last_update_date': datetime.datetime(2021, 1, 2, 1, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
        ],
        datetime.datetime(2021, 1, 2, 0, 0, 0, tzinfo=pytz.utc),
        [
            {'username': 'Test', 'email': 'test@test.com'},
            {'username': 'Test1', 'email': 'test1@test.com'}
        ],
        True,
        ['test@test.com', 'test1@test.com'],
    ), (
        [
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
            {'last_update_date': datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
             'create_date': datetime.datetime(2021, 1, 1, 1, 0, 0, tzinfo=pytz.utc)},
        ],
        datetime.datetime(2021, 1, 8, 1, 0, 0, tzinfo=pytz.utc),
        [
            {'username': 'Test', 'email': 'test@test.com'},
            {'username': 'Test1', 'email': 'test1@test.com'}
        ],
        False,
        ['test@test.com', 'test1@test.com'],
    ),
]
