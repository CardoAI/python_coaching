from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from session2_testing.exceptions import OrganizationAccessError


@dataclass
class User:
    username: str
    idp_user_id: int
    is_active: bool = True
    date_joined: datetime = field(default_factory=datetime.now)
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    last_login: datetime | None = None
    organizations: list[dict] = field(default_factory=list)

    def get_full_name(self) -> str:
        return f'{self.first_name or ""} {self.last_name or ""}'

    def get_short_name(self) -> str:
        return self.first_name or ""

    def _has_organization(self, organization_id: str | UUID) -> bool:
        if isinstance(organization_id, str):
            organization_id = UUID(organization_id)

        return any(organization['id'] == organization_id for organization in self.organizations)

    def check_organization_access(self, organization_id: str | UUID) -> None:
        if not self._has_organization(organization_id):
            raise OrganizationAccessError()
