//
//  Queue.swift
//  DataStructures
//
//  Created by ChihYu Yeh on 2019/3/4.
//

protocol Queue {
    associatedtype Element
    
    mutating func enqueue(_ element: Element)
    mutating func dequeue() -> Element?
    var isEmpty: Bool { get }
    var peak: Element? { get }
}

// implement Queue using array
struct QueueArray<T>: Queue {
    private var array: [T] = []
    
    var isEmpty: Bool {
        return array.isEmpty
    }
    
    var peak: T? {
        return array.first
    }
    
    mutating func enqueue(_ element: T) {
        array.append(element)
    }
    
    @discardableResult
    mutating func dequeue() -> T? {
        return isEmpty ? nil : array.removeFirst()
    }
}

// implement Queue using two stacks
struct QueueStack<T>: Queue {
    private var dequeueStack: [T] = []
    private var enqueueStack: [T] = []
    
    var isEmpty: Bool {
        return dequeueStack.isEmpty && enqueueStack.isEmpty
    }
    
    var peak: T? {
        if dequeueStack.isEmpty {
            return enqueueStack.first
        } else {
            return dequeueStack.last
        }
    }
    
    mutating func enqueue(_ element: T) {
        enqueueStack.append(element)
    }
    
    @discardableResult
    mutating func dequeue() -> T? {
        if dequeueStack.isEmpty {
            dequeueStack = enqueueStack.reversed()
            enqueueStack.removeAll()
        }
        return dequeueStack.popLast()
    }
}
