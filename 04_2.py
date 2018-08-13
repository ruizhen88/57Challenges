# 미해결
# 오류 문구

def input_a_word(message):
    isFinished = False

    while isFinished is False:
        noun = input(message)

        if noun :
            isFinished = True
        else:
            print("Please enter a word.")

    return noun


noun = input_a_word("Enter a noun: ")

verb = input_a_word("Enter a verb: ")

adj = input_a_word("Enter a adj: ")

adv = input_a_word("Enter a adv: ")


print("Do you {} your {} {} {}?".format(noun, verb, adj, adv))

