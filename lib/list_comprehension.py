def return_evens(num_list):
    pass
    even_numbers = []  
    for num in num_list:  
        if num % 2 == 0: 
            even_numbers.append(num)  
    return even_numbers 


   

        

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]
    pass