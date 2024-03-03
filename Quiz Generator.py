import random

capitals = {
    'Andhra Pradesh': 'Hyderabad',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata',
    'Andaman and Nicobar Islands': 'Port Blair',
    'Chandigarh': 'Chandigarh',
    'Dadra and Nagar Haveli and Daman and Diu': 'Daman',
    'Lakshadweep': 'Kavaratti',
    'Delhi': 'New Delhi',
    'Puducherry': 'Puducherry'
}

for quizNum in range(35):
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt','w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for quesNum in range(34):
        correct_ans = capitals[states[quesNum]]
        wrong_ans = list(capitals.values())
        del wrong_ans[wrong_ans.index(correct_ans)]
        wrong_ans = random.sample(wrong_ans,3)
        answer_opt = wrong_ans + [correct_ans]
        random.shuffle(answer_opt)
        
        quizFile.write(f'{quesNum + 1}. What is the capital of {states[quesNum]}?\n')

        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. {answer_opt[i]}\n")
        quizFile.write('\n')

        answerKeyFile.write(f"{quesNum + 1}. {'ABCD'[answer_opt.index(correct_ans)]}\n")
    
    quizFile.close()
    answerKeyFile.close()
