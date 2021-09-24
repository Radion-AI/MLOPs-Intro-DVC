import test_outer as t

def test_is_datazip_present():
    assert t.is_datazip_present() == False

def test_is_model_present():
    assert t.is_model_present() == False

def test_check_model_accuracy():
    assert t.check_model_accuracy() == True
