# return True if the two binary trees rooted and a and b are equal in value and structure
# return False otherwise
def compare(a, b):
    if a and b:
        if a.val == b.val:
            return compare(a.left,b.left) and compare(a.right,b.right)
        else:
            return False
    if not a and not b:
        return True
    else:
        return False
