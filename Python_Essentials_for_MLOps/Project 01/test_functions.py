
def test_clean_title_1():
  input_title = "Hello, 123 World!"
  expected_result = "Hello 123 World"

  result = clean_title(input_title)
  assert result == expected_result

def test_clean_title_2():
  input_title = "ABCD1234"
  expected_result = "ABCD1234"

  result = clean_title(input_title)
  assert result == expected_result

def test_clean_title_3():
  input_title = ""
  expected_result = ""

  result = clean_title(input_title)
  assert result == expected_result
