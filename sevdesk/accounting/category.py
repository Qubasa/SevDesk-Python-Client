from __future__ import annotations

from collections import defaultdict
from typing import List, Union

import attrs

from .. import UNSET, Client, Unset
from ..client.api.accounting_type import get_accounting_types
from ..client.models import GetAccountingTypesResponse200ObjectsItem
from ..common import SevDesk


@attrs.define()
class AccountingType:
    id: int
    "Account-Type id"
    name: str
    "Account-Type name"
    translation_code: Union[Unset, str]
    "Tranlation Code"
    accounting_system_number: Union[Unset, int]
    "Accounting System Number"
    _model: attrs.field()
    "Internaly caching SevDesk Model"

    @classmethod
    def _from_model(
        cls, model: GetAccountingTypesResponse200ObjectsItem
    ) -> AccountingType:
        return cls(
            id=int(model.id),
            name=model.name,
            translation_code=str(model.translation_code)
            if model.translation_code
            else UNSET,
            accounting_system_number=int(model.accounting_system_number.number)
            if model.accounting_system_number
            else UNSET,
            model=model,
        )

    @staticmethod
    def _get(client: Client) -> List[AccountingType]:
        response = get_accounting_types.sync_detailed(
            client=client,
            embed="parent,accountingSystemNumber,isFavorite",
            limit=9999,
            use_client_accounting_chart=True,
        )

        SevDesk.raise_for_status(response, "querying accounting types")

        types = []

        model: GetAccountingTypesResponse200ObjectsItem
        for model in response.parsed.objects:
            types.append(AccountingType._from_model(model))

        return types

    @staticmethod
    def _get_by_id(client: Client, id: int) -> Union[None, AccountingType]:
        types = AccountingType._get(client)

        for accounting_type in types:
            if int(accounting_type.id) == int(id):
                return accounting_type

        return None


@attrs.define()
class AccountingCategories:
    _map: Union[Unset, defaultdict(dict)] = attrs.field(
        on_setattr=attrs.setters.frozen, default=UNSET
    )

    def find(self, path):
        """
        Get an accounting type by a . separated path using the
        category and accounting type names
        """
        keys = path.split(".")

        if not keys:
            return UNSET

        item = self._map

        for key in keys:
            item = item.get(key, UNSET)

            if isinstance(item, Unset):
                break

        return item

    @classmethod
    def get(cls, client: Client):
        temp = defaultdict(dict)
        unused = list()

        for t in AccountingType._get(client):
            if t._model.parent:
                temp[t._model.parent.name.strip()][t.name.strip()] = t
            else:
                unused.append(t)

        # Ensure all accounting types are mapped to a category
        for t in unused:
            if t.name not in temp:
                temp[t.name.strip()] = t

        return cls(map=temp)
