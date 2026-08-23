from address import Address
from mailing import Mailing

to_address = Address(163059, "Архангельск", "Кировская", 13, 4)
from_address = Address(188416, "Санкт-Петербург", "Рубинштейна", 3, 9)

mailing = Mailing(to_address, from_address, 452, "TRK8756934035")

print(f"""Отправление {mailing.track} из {mailing.from_address.index},
{mailing.from_address.city}, {mailing.from_address.street},
{mailing.from_address.house} - {mailing.from_address.apartment}
в {mailing.to_address.index}, {mailing.to_address.city},
{mailing.to_address.street},
{mailing.to_address.house} - {mailing.to_address.apartment}.
Стоимость {mailing.cost} рублей.""")
