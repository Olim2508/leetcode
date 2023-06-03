from main import length_of_longest_substring


def test_length_of_longest_substring():
    s = "abcabcbb"
    assert length_of_longest_substring(s) == 3
    s = "bbbbb"
    assert length_of_longest_substring(s) == 1
    s = "pwwkew"
    assert length_of_longest_substring(s) == 3
    s = ""
    assert length_of_longest_substring(s) == 0
    s = " "
    assert length_of_longest_substring(s) == 1
    s = "au"
    assert length_of_longest_substring(s) == 2
