//:## 1. Two Sum
/*
https://leetcode.com/problems/two-sum/
 
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
  var numsDictionary = [Int:Int]()
  
  for (index, num) in nums.enumerated() {
    if numsDictionary[num] == nil {
      numsDictionary[num] = index
    }
    
    if let value = numsDictionary[target - num], value != index {
      return [value, index]
    }
  }
  
  return []
}
//:## 2. Add Two Numbers
/*
https://leetcode.com/problems/add-two-numbers/
 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
 */

public class ListNode {
  public var val: Int
  public var next: ListNode?
  public init(_ val: Int) {
    self.val = val
    self.next = nil
  }
}

func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
  return addLists(l1,l2,0)
}

func addLists(_ l1: ListNode?, _ l2: ListNode?, _ carry: Int) -> ListNode? {
  switch (l1,l2,carry) {
  case (.none, .none, 0): return l1
  case (.none,.none,_): return ListNode(carry);
  case (.some(let l),.none,_), (.none,.some(let l),_):
    let sum = l.val+carry
    let res = ListNode(sum%10)
    res.next = addLists(l.next,.none,sum/10)
    return res
  case (.some(let l1),.some(let l2),_):
    let sum = l1.val+l2.val+carry
    let res = ListNode(sum%10)
    res.next = addLists(l1.next,l2.next,sum/10)
    return res
  }
}

//:## 344. Reverse String
/*
 https://leetcode.com/problems/reverse-string/
 Write a function that reverses a string. The input string is given as an array of characters char[].
 
 Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
 
 You may assume all the characters consist of printable ascii characters.
 
 Example 1:
 
 Input: ["h","e","l","l","o"]
 Output: ["o","l","l","e","h"]
 Example 2:
 
 Input: ["H","a","n","n","a","h"]
 Output: ["h","a","n","n","a","H"]
 */

func reverseString(_ s: inout [Character]) {
  let length = s.count
  
  if length < 2 {
    return
  }
  
  let mid = length / 2 - 1
  
  for i in 0...mid {
    (s[i], s[length - i - 1]) = (s[length - i - 1], s[i])
  }
}

//:## 136. Single Number
/*
 https://leetcode.com/problems/single-number/
 Given a non-empty array of integers, every element appears twice except for one. Find that single one.
 
 Note:
 
 Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 
 Example 1:
 
 Input: [2,2,1]
 Output: 1
 Example 2:
 
 Input: [4,1,2,1,2]
 Output: 4
 */

func singleNumber(_ nums: [Int]) -> Int {
  var hashSet: Set<Int> = []
  
  for num in nums {
    if hashSet.contains(num) {
      hashSet.remove(num)
    } else {
      hashSet.insert(num)
    }
  }
  
  return hashSet.removeFirst()
}
