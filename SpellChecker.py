class SpellChecker:
    def __init__(self , data):
        # the most suitable data structure for the dictionary is "set" as every word appear only once 
        # and not to include repeated words.
        self.dictionary = set(data)
        self.sortedList = sorted(self.dictionary)  # sort the set in lexicographically order and save it into list.
        print("for storing data,  time copmlexity: O(n)         Space complexity: O(n)")

    def spellCheck(self , input_word):
        # here we check if the input word is in set of words.
        if input_word in self.dictionary:
            print(f"Word {input_word} is already in dictionary.")
            return input_word           # then we return the word if it was in dictionary.
        
        else:
            self.dictionary.add(input_word)             # add the input word to set to know its place.
            self.sortedList = sorted(self.dictionary)   # update the sorted list.
            ind = self.sortedList.index(input_word)     # get the ndex of the word.
            nearset = []
            if ind == len(self.sortedList) - 1:         # when the word is the last we get the 4 words before as nearset ones.
                nearset.append(self.sortedList[-5:ind])
            elif ind == len(self.sortedList) - 2:       # when the word is before the last we get the 3 words before  and 1 after  as nearset ones.
                nearset.append(self.sortedList[-5:ind])
                nearset.append(self.sortedList[ind+1])
            elif ind == 0:                              # when the word is the first we get the  4 words after as nearset ones.
                nearset = self.sortedList[ind+1:5]
            elif ind == 1:                              # when the word is after the second we get the 3 words after  and 1 before  as nearset ones.
                nearset.append(self.sortedList[ind-1])
                nearset.append(self.sortedList[ind+1:5])
            else:
                nearset.append( self.sortedList[ind-2:ind])         # here we get the 2 words before 
                nearset.append(self.sortedList[ind+1:ind+3])        # and 2 after  as nearset ones.

            self.near4 = nearset
            self.dictionary.remove(input_word)              # here we remove the word as we previously insert it. 
            self.sortedList = sorted(self.dictionary)       # update the sorted list.
            print(f"the nearset 4 are: {self.near4}")       # print the results
            print("for getting nearset 4 words operation ,  time copmlexity: O(n)         Space complexity: O(n)")
            return self.near4                               # return the nearset 4 words.
        



                

        
    def addToDict(self , input_word):
         # here we check if the input word is in set of words.
        if input_word in self.dictionary:
            print(f"Word {input_word} is already in dictionary.")
        else:
            # then add the word to dictionary according to lexicographic order.
            self.dictionary.add(input_word)                         # add the input word to set.
            self.sortedList = sorted(self.dictionary)               # update the sorted list.
            print(f"Word {input_word} is added to the dictionary")  # print the results
        print("for addinf to dictionary operation,  time copmlexity: O(n)         Space complexity: O(n)")

    
import codecs
def main():

    content = []
    with codecs.open("dictionary.txt", 'r', encoding='utf-8' , errors='ignore') as fdata:
        content.append(fdata.readlines())
    
    data = content[0]
    data2 = [ data[i][:-1] for i in range(len(data)) if i != len(data) -1 ]
   

    c = SpellChecker(data2)
    print(c.sortedList[:5])

    c.addToDict("aab")
    c.addToDict("aab")
    print(c.sortedList[:5])

    c.spellCheck("aab")
    near = c.spellCheck("aac")







if __name__ == "__main__":
    main()