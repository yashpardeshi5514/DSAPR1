class TF:
    def __init__(self, value):
        self.value = value
        self.link = None

class Telephone:
    def __init__(self):
        self.HT = [None] * 10

    def fn_hash(self, value):
        return value % 10

    def insert_element(self, value):
        hash_val = self.fn_hash(value)
        new_node = TF(value)

        if self.HT[hash_val] is None:
            self.HT[hash_val] = new_node
        else:
            temp = self.HT[hash_val]
            while temp.link is not None:
                temp = temp.link
            temp.link = new_node

    def print_table(self):
        for i in range(10):
            print(f"a[{i}]:", end="")
            temp = self.HT[i]
            while temp:
                print(f" -> {temp.value}", end="")
                temp = temp.link
            print()

    def search_data(self, value):
        hash_val = self.fn_hash(value)
        temp = self.HT[hash_val]
        while temp:
            if temp.value == value:
                print(f"\nElement found at {hash_val}: {temp.value}")
                return
            temp = temp.link
        print("\nNo element found at key")

    def delete_element(self, value):
        hash_val = self.fn_hash(value)
        temp = self.HT[hash_val]
        if not temp:
            print("Element not found")
            return

        if temp.value == value:
            self.HT[hash_val] = temp.link
            print("Contact deleted")
            return

        prev = temp
        temp = temp.link
        while temp:
            if temp.value == value:
                prev.link = temp.link
                print("Contact deleted")
                return
            prev = temp
            temp = temp.link
        print("Element not found")

# Main logic
def main():
    h = Telephone()
    while True:
        print("\nTelephone :\n1.Insert\n2.Display\n3.Search\n4.Delete\n5.Exit")
        ch = int(input("Select your choice: "))
        if ch == 1:
            data = int(input("Enter phone number to be inserted: "))
            h.insert_element(data)
        elif ch == 2:
            h.print_table()
        elif ch == 3:
            search = int(input("Enter number to be searched: "))
            h.search_data(search)
        elif ch == 4:
            delete = int(input("Enter number to be deleted: "))
            h.delete_element(delete)
        elif ch == 5:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
