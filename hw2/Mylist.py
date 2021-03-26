class Mylist(list):
    def get_min(self):
        min_elem = None
        for elem in self:
            if not min_elem or elem < min_elem:
                min_elem = elem

        return min_elem

    def get_max(self):
        max_elem = None
        for elem in self:
            if not max_elem or elem > max_elem:
                max_elem = elem

        return max_elem


if __name__ == '__main__':
    ls = [2, 9, 14, -1, -99, 107, 0, -94]
    lst = Mylist(ls)
    print(lst.get_min())
    print(lst.get_max())
