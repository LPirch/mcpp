def t1(root, sitter, lang, calls=None):
    def num_descendants(node):
        return 1 + sum(map(num_descendants, node.children))

    return {
        "t1": num_descendants(root)
    }


def t2(root, sitter, lang, calls=None):
    def height(node):
        if len(node.children) == 0:
            return 1
        return 1 + max(map(height, node.children))
    return {
        "t2": height(root)
    }


def t3(root, sitter, lang, calls=None):
    def get_child_nums(node):
        if len(node.children) == 0:
            return []
        return [len(node.children)] + sum(map(get_child_nums, node.children), start=[])
    child_nums = get_child_nums(root)
    return {
        "t3": sum(child_nums) / len(child_nums)
    }
