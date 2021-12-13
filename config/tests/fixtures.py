from _pytest.main import Session
import pytest
from django.core.management import call_command
import os 

@pytest.fixture
def create_admin_user(django_user_model):
    return django_user_model.objects.create_superuser(
        "admin",
        "admin@admin.com",
        "admin"
    )

@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    '''
        load data to database 
    '''
    log_id_data_file = os.path.abspath(os.curdir) + "/ecomm_apps/Dashboard/fixtures/" 
    with django_db_blocker.unblock():
        
        call_command("loaddata", log_id_data_file+"db_admin_fixtures.json")
