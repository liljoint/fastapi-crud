from test.test_main import setup, teardown

def pytest_sessionstart(session):
    setup()
    
def pytest_sessionfinish(session):
    teardown()