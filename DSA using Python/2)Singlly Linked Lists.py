class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        if self.start is None:
            return None
        else:
            return self.start

    def insertion_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insertion_at_last(self, data):
        n = Node(data)
        if self.is_empty() is not None:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, val):
        temp = self.start
        while temp is not None:
            if temp.item == val:
                return temp
            temp = temp.next
        return None

    def insertion_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    def delete_at_first(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_at_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_at_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def __iter__(self):
        return Iterator(self.start)


class Iterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# Testing code
sllobbj = SLL()
sllobbj.insertion_at_start(10)
sllobbj.insertion_at_last(80)
sllobbj.insertion_at_last(100)
sllobbj.insertion_after(sllobbj.search(10), 50)
sllobbj.print_list()
print("\nfor loop using class iterator")
for x in sllobbj:
    print(x, end=' ')
sllobbj.delete_at_item(50)
print("\ndelete at item")
sllobbj.print_list()
sllobbj.delete_at_last()
print("\ndelete at last")
sllobbj.print_list()
