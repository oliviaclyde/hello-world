testCase = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]



def FindIntersection(strArr):

  # code goes here
  
  # lists = map(lambda s: s.split(", "), strArr)

  firstList = strArr[0].split(", ")
  secondList = strArr[1].split(", ")
  
  newList = []

  for item in firstList:
    if item in secondList:
      newList.append(int(item))
  
  strArr = ','.join(map(str, newList))
    
  return strArr

# keep this function call here 
print(FindIntersection(testCase))