import allure,pytest
class Test_01:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是第一个测试方法")
    def test_001(self):
        allure.attach("test_001", "这是test001的描述！")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是第二个测试方法")
    def test_002(self):
        allure.attach("test_002", "这是test002的描述！")
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是第三个测试方法")
    def test_003(self):
        allure.attach("test_003", "这是test003的描述！")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是第四个测试方法")
    def test_004(self):
        allure.attach("test_004", "这是test004的描述！")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是第五个测试方法")
    def test_005(self):
        allure.attach("test_005", "这是test005的描述！")
        assert 0