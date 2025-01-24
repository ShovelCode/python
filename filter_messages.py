def filter_messages(messages):
    filtered_messages = []
    word_counts = []

    for message in messages:
        words = message.split();
        non_bad = []
        counter = 0

        for word in words:
            if(word == "dang"):
                counter = counter + 1
            else:
                non_bad.append(word)

        good_message = " ".join(non_bad)

        filtered_messages.append(good_message)
        word_counts.append(counter)
        
    return filtered_messages, word_counts
