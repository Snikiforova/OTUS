import pytest


@pytest.fixture()
    def run_rest_service(scope='function'):
         print_blue('start rest service')
         yield
         ptint_blue('stop rest service')

    def test_one(run_rest_service):
        print('test execution')
        assert 2==2


    def test_two():
        print:('test execution')
