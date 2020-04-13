/*
 Array
 */

// Array Structure Reference: https://developer.apple.com/documentation/swift/array
// ContiguousArray: https://developer.apple.com/documentation/swift/contiguousarray
// ArraySlice: https://developer.apple.com/documentation/swift/arrayslice
// Array Design: https://github.com/apple/swift/blob/master/docs/Arrays.rst

/*
 Linked List
 */

class Node<Element> {
    var value: Element
    var next: Node<Element>?
    
    init(value: Element) {
        self.value = value
    }
}

class LinkedList<Element> {
    var head: Node<Element>?
    
    init(head: Node<Element>?) {
        self.head = head
    }
    
    func append(_ node: Node<Element>) {
        guard head != nil else {
            head = node
            return
        }
        
        var current = head
        while let _ = current?.next {
            current = current?.next
        }
        current?.next = node
    }
    
    func getNode(atPosition position: Int) -> Node<Element>? {
        guard position > 0 else {
            return nil
        }
        
        var counter = 1
        var current = head
        
        while current != nil && counter <= position {
            if counter == position {
                return current
            }
            
            current = current?.next
            counter += 1
        }
        
        return nil
    }
    
    func insertNode(_ node: Node<Element>, at position: Int) {
        guard position > 0 else {
            return
        }
        
        var counter = 1
        var current = head
        
        if position > 1 {
            while current != nil && counter < position {
                if counter == position - 1 {
                    node.next = current?.next
                    current?.next = node
                    break
                }
                
                current = current?.next
                counter += 1
            }
        } else if position == 1 {
            node.next = head
            head = node
        }
    }
    
    func deleteNode(withValue value: Element) {
        var current = head
        var previous: Node<Element>?
        
        while current?.value != value && current?.next != nil {
            previous = current
            current = current?.next
        }
    }
}


//: [Next](@next)
