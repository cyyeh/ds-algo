//: [Previous](@previous)
let array = "hello".map { ($0, 1) }
print(array)
let dict = Dictionary("hello".map { ($0, 1) }, uniquingKeysWith: +)
print(dict)

// two sum
// 給出一個整型數組和一個目標值，判斷數組中是否有兩個數之和等於目標值
func twoSum(nums: [Int], _ target: Int) -> Bool {
    var set = Set<Int>()
    
    for num in nums {
        if set.contains(target - num) {
            return true
        }
        
        set.insert(num)
    }
    
    return false
}

// two sum
// 給定一個整型數組中且僅有兩個數之和等於目標值，求這兩個數在數組中的序號
func twoSum(nums: [Int], _ target: Int) -> [Int] {
    var dict = [Int: Int]()
    
    for (i, num) in nums.enumerated() {
        if let lastIndex = dict[target - num] {
            return [lastIndex, i]
        } else {
            dict[num] = i
        }
    }
    
    fatalError("no valid output")
}

// google面試題
// 給出一個字符串，要求將其按照單詞順序進行反轉
// the sky is blue -> blue is sky the
func revereString(string: String) -> String {
    return string.split(separator: " ").reversed().joined(separator: " ")
}

revereString(string: "the sky is blue")
//: [Next](@next)
