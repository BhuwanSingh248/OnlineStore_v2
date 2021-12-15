from _pytest.main import Session
import pytest
from django.core.management import base, call_command
import os


@pytest.fixture
def create_admin_user(django_user_model):
    return django_user_model.objects.create_superuser(
        "admin", "admin@admin.com", "admin"
    )


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    load data to database
    """
    base_path = os.getcwd()
    log_id_data_file = base_path + "/ecomm_apps/Dashboard/fixtures/"
    category_data_file = base_path + "/ecomm_apps/Inventory/fixtures/"

    with django_db_blocker.unblock():

        call_command("loaddata", log_id_data_file + "db_admin_fixtures.json")
        call_command("loaddata", category_data_file + "db_category_fixtures.json")
