import os

from sevdesk import Client, Unset
from sevdesk.accounting import AccountingCategories


def test_categories():
    token = os.environ["SEVDESKTOKEN"]
    client = Client(base_url="https://my.sevdesk.de/api/v1", token=token)

    categories = AccountingCategories.get(client)
    item = categories.find("path.to.invalid")
    assert isinstance(item, Unset)

    item = categories.find("Steuer.bezahlte Umsatzsteuer")
    assert item.id == 3

    item = categories.find("Umsätze.Einnahmen / Erlöse / Verkäufe")
    assert item.id == 26
