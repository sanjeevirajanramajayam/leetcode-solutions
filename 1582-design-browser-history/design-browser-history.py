class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.rear = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        newPage = ListNode(url)
        self.curr.next = newPage
        newPage.rear = self.curr
        self.curr = self.curr.next
        return self.curr.val

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.rear:
                self.curr = self.curr.rear
            else:
                break
        return self.curr.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
            else:
                break
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)