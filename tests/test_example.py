import pytest
@pytest.fixture()
def run_rest_service():
     print('start rest service')
     yield
     print('stop rest service')

def test_one(run_rest_service):
     print('Test execution')
     assert 1 == 1


def test_two(run_rest_service):
     print('Test execution')
