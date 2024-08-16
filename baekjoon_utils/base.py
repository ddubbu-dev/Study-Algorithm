def set_open(input_):
    class open:
        def __init__(self, x):
            self.read = lambda: input_

        def __iter__(self):
            return iter(input_.split("\n"))

    return open


def set_input(input_):
    return iter(input_.split("\n")).__next__


input = set_input("""TODO""")

# ================== 여기서부터 제출 ==================
