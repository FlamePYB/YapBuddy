from path_pkg import NormalFile


def test_normal_file_with_relative_path():
    file = NormalFile(r"..\test\resources\doc.txt", "RELATIVE")
    assert file.content == "this is a test file to be read"


def test_normal_file_with_absolute_path():
    file = NormalFile(
        r"C:\Users\machr\projects\YapBuddy\test\resources\doc.txt", "ABSOLUTE"
    )
    assert file.content == "this is a test file to be read"
