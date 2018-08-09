from itertools import groupby

foo = [
        {
            "date": 20180228,
            "id": 1,
            "resolved_ip_network": "公有云",
            "resolved_number": 36956,
            "success_rate": 1
        },
        {
            "date": 20180228,
            "id": 2,
            "resolved_ip_network": "腾讯云",
            "resolved_number": 7986,
            "success_rate": 1
        },
        {
            "date": 20180228,
            "id": 3,
            "resolved_ip_network": "阿里云",
            "resolved_number": 28654,
            "success_rate": 1
        },
        {
            "date": 20180227,
            "id": 4,
            "resolved_ip_network": "公有云",
            "resolved_number": 3024,
            "success_rate": 1
        },
        {
            "date": 20180227,
            "id": 5,
            "resolved_ip_network": "腾讯云",
            "resolved_number": 1454,
            "success_rate": 1
        },
        {
            "date": 20180227,
            "id": 6,
            "resolved_ip_network": "阿里云",
            "resolved_number": 5054,
            "success_rate": 1
        }
    ]

result = {}

for date, items in groupby(foo, lambda x: x['date']):
    result.setdefault('date', []).append(date)
    for item in items:
        result.setdefault(item['resolved_ip_network'], []).append(item['resolved_number'])

print(result)
