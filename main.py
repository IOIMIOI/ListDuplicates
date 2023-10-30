import unittest
import time

class Duplicate_remover:
    name = ""
    compl = ""

    def remove(self, lis):
        return None

    def test(self, n):
        time_start = time.time()
        result = self.remove(n)
        time_res = time.time() - time_start
        print(self.name+" Cложность: "+self.compl+"\nРезультат:" + str(
            result) + " Затрачено время:" + str(time_res)+"\n")
        return result

class Duplicate_remover_1(Duplicate_remover):
    name = "С помощью множеств. Set не может хранить в себе одинаковые значения."
    compl = "O(n)"

    def remove(self, l):
        temp = set()
        new_l = []
        for i in l:
            t = tuple(i.items())
            if t not in temp:
                temp.add(t)
                new_l.append(i)
        return new_l


class TestStringMethods(unittest.TestCase):
    list_to = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"},
               {"key2": "value2"}]
    list_need = [{'key1': 'value1'}, {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}, {}, {'key2': 'value2'}]

    def test_remover_1(self):
        remover = Duplicate_remover_1()
        self.assertEqual(remover.test(self.list_to), self.list_need)

def main():
    pass

if __name__ == '__main__':
    unittest.main()