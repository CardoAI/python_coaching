from uuid import uuid4

import pytest

from session2_testing.domain import User
from session2_testing.exceptions import OrganizationAccessError


def test_cannot_create_without_required_fields():
    """
    Test that the class cannot be created without the required fields.
    """
    with pytest.raises(TypeError):
        User()


def test_get_full_name_when_first_and_last_name_are_present():
    """
    Test that the full name is returned when first and last name are present.
    """
    first_name = 'John'
    last_name = 'Doe'
    user = User(
        username='test',
        idp_user_id=1,
        first_name=first_name,
        last_name=last_name,
    )

    assert user.get_full_name() == f'{first_name} {last_name}'


def test_get_full_name_when_first_name_is_not_present():
    """
    Test that the full name is returned when first name is not present.
    """
    last_name = 'Doe'
    user = User(
        username='test',
        idp_user_id=1,
        last_name=last_name,
    )

    assert user.get_full_name() == ' ' + last_name


def test_has_organization_when_organization_is_inside_the_list():
    """
    Test that the method returns True when the organization is inside the list.
    """
    organization_id = uuid4()
    user = User(username='test', idp_user_id=1, organizations=[{'id': organization_id}])
    user.check_organization_access(organization_id)


def test_has_organization_when_organization_is_not_inside_the_list():
    """
    Test that the method returns False when the organization is not inside the list.
    """
    organization_id = uuid4()
    user = User(username='test', idp_user_id=1, organizations=[{'id': uuid4()}])

    with pytest.raises(OrganizationAccessError):
        user.check_organization_access(organization_id)
