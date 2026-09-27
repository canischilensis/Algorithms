import pytest
from merge_lists_module import merge_lists

@pytest.mark.parametrize("nums1, m, nums2, n, expected", [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1, 2, 3, 0, 0, 0, 0], 3, [-4, 2, 3, 9], 4, [-4, 1, 2, 2, 3, 3, 9]),
    ([0], 0, [1], 1, [1]),
    ([2, 0], 1, [1], 1, [1, 2]),
    ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
    ([1, 0], 1, [2], 1, [1, 2]),
])
def test_merge_lists(nums1, m, nums2, n, expected):
    result = merge_lists(nums1, m, nums2, n)
    if result == expected:
        print("✅ Test passed")
    else:
        print("❌ Test failed")
    assert result == expected
