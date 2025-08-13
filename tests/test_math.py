import sys

def test_addition():
    asserts 2+2 == 4, "Math is borken!"

try:
    test_addition()
    print("✅ All tests passed!")
except AssertionError as e:
    print(f"❌ Test failed: {e}")
    sys.exit(1) #exit with code 1 -> pipeline will fail
