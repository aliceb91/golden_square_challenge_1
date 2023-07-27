class GrammarStats:
    def __init__(self):
        self.history = []

    def check(self,text):
        """
        Paramaters:
            text: string
        Returns:
            bool: true if the text begins with a 
                  capital letter and ends with a sentence-ending punctuation mark, false otherwise.
        """
        if text == "" or not text[0].isupper() and text[-1] not in ".!?":
            self.history.append(False)
            return False
        if not text[0].isupper():
            self.history.append(False)
            return False
        if text[-1] not in ".!?":
            self.history.append(False)
            return False
        self.history.append(True)
        return True

    def percentage_good(self):
        """
        Returns:
            int: the percentage of texts checked so far that passed the check 
                 defined in the 'check' method. The number 55 represents 55%.
        """
        true_count = 0
        false_count = 0
        print(self.history)
        for entry in self.history:
            if entry == True:
                true_count += 1
            else:
                false_count += 1
        total_count = true_count + false_count
        percentage = round((100 / total_count) * true_count)
        print(true_count)
        print(false_count)
        print(total_count)
        print(percentage)
        return percentage