class StreamItem:
    def __init__(self, title):
        self.title = title

    def display(self):
        print(f"Stream: {self.title}")

class Upload(StreamItem):
    def __init__(self, title, file):
        super().__init__(title)
        self.file = file

    def display(self):
        print(f"Upload: {self.title} - File: {self.file}")

class Announce(StreamItem):
    def __init__(self, title, message):
        super().__init__(title)
        self.message = message

    def display(self):
        print(f"Announcement: {self.title} - Message: {self.message}")


class Submit(StreamItem):
    def __init__(self, title, assignment):
        super().__init__(title)
        self.assignment = assignment

    def display(self):
        print(f"Submission: {self.title} - Assignment: {self.assignment}")

class Stream:
    MAX_ITEMS = 100

    def __init__(self):
        self.items = []
        self.size = 0

    def add_item(self, item):
        if self.size < Stream.MAX_ITEMS:
            self.items.append(item)
            self.size += 1
        else:
            print("Stream is full. Cannot add more items.")

    def display_stream(self):
        for item in self.items:
            item.display()


def main():
    stream = Stream()

    upload = Upload("File Upload", "document.txt")
    stream.add_item(upload)

    add_announce = input("Add announcement? (yes/no): ").lower()
    if add_announce == "yes":
        announce = Announce("Important Announcement", "Meeting at 2 PM")
        stream.add_item(announce)
    else:
        stream.add_item(Announce("No Announcement Added", ""))

    stream.add_item(Submit("Assignment Submission", "Homework"))

    stream.display_stream()


if __name__ == "__main__":
    main()
