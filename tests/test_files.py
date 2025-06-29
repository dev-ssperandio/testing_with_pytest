import os
from jformat.files import is_done

class TestIsDone:

    def setup_method(self, method):
        self.tmp_file = "./tmp/test_file"

    def teardown_method(self, method):
        if os.path.exists(self.tmp_file):
            os.remove(self.tmp_file)

    def write_tmp_file(self, content):
        with open(self.tmp_file, "w") as _f:
            _f.write(content)

    def test_yes(self):
        self.write_tmp_file("yes")
        assert is_done(self.tmp_file) is True

    def test_no(self):
        self.write_tmp_file("no")
        assert is_done(self.tmp_file) is False
        